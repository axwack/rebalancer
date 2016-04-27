import psycopg2, datetime
import sys
from django.conf import settings
import os.path
from itertools import izip
import logging

# set up configurations
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rebalancer.settings")
FEED_FILES = os.path.realpath(os.path.dirname(__file__)) + "/loadfiles"

# Get an instance of a logger
logger = logging.getLogger('rebalancer_log')

print "In directory: " + FEED_FILES


def run(*args):
    con = None

    try:

        con = psycopg2.connect(database=settings.DATABASES['default']['NAME'],
                               user=settings.DATABASES['default']['USER'])
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

        print "args:" + str(args)

        i = iter(args)
        parameters = dict(izip(i, i))
        print "args : parameters %s " % parameters

        cur.execute('SELECT feed_cd, entity_to_run from equity_feeds where enable=TRUE')
        results = cur.fetchall()
        print ("Feeds enabled: %s" % str(results))
        f = iter(results)
        feeds = dict(*izip(f, f))

        FEED_FILE = FEED_FILES + "/" + parameters['file']

        for feed in feeds.keys():
            print "Doing feed ... %s" % feed

            if feed == 'SECURITY':
                print ("Truncating tables...")
                cur.execute("truncate table staging_equity_security")
                print "Loading " + feed + " ..."
                logger.info("[DoLoads.py] Loading " + feed + " ...")
                cur.execute("copy staging_equity_security from '" + FEED_FILE + "' DELIMITERS ',' CSV HEADER")
                print ("Rows Inserted to " + feed + ": %s  " % str(cur.rowcount))
                con.commit()
                update_security_sql = 'INSERT INTO equity_security ( "secId", "secName", "listExchCd", "baseCurrency", "mktPrice", "amtIssued", "amtOutstanding", "couponRate", "secType_id", "benchmarkSecurity", "comments", "countryOfRisk", "crossCurrencyCd", \
                             cusip, "divCurrency", "extSecId", isin, "issueState", "lastModifyBy_id", "locCurrencyCd", sedol, "shortName", "strikePrice", \
                              ticker, valoran, "issueCountry_id", "createDate", "lastModifyDate", "recordVersion", "RIC", "issueDate") \
                            select  "secId", "secName", "listExchCd", "baseCurrency", "mktPrice", "amtIssued", "amtOutstanding", "couponRate", "secType_id", "benchmarkSecurity", "comments", "countryOfRisk", "crossCurrencyCd", \
                              cusip, "divCurrency", "extSecId", isin, "issueState", "lastModifyBy_id", "locCurrencyCd", sedol, "shortName", "strikePrice", \
                              ticker, valoran, "issueCountry_id", "createDate", "lastModifyDate", "recordVersion", "RIC", "issueDate" \
                            from staging_equity_security ON CONFLICT(secid) DO \
                             UPDATE SET \
                              es1."secId" = ses."secId", \
                              es1."secName" = ses."secName",\
                              es1."listExchCd" = ses."listExchCd",\
                              es1."baseCurrency"= ses."baseCurrency",\
                              es1."mktPrice"= ses."mktPrice",\
                              es1."amtIssued"= ses."amtIssued",\
                              es1."amtOutstanding" = ses."amtOutstanding",\
                              es1."couponRate"= ses."couponRate",\
                              es1."secType_id"= ses."secType_id",\
                              es1."benchmarkSecurity"= ses."benchmarkSecurity",\
                              es1."comments"=ses.comments,\
                              es1."countryOfRisk"=ses."countryOfRisk",\
                              es1."crossCurrencyCd" = ses."crossCurrencyCd",\
                              es1."cusip" = ses.cusip,\
                              es1."divCurrency"= ses."divCurrency",\
                              es1."extSecId"= ses."extSecId",\
                              es1."isin"= ses.isin,\
                              es1."issueState"=ses."issueState",\
                              es1."lastModifyBy_id"=ses."lastModifyBy_id",\
                              es1."locCurrencyCd"=ses."locCurrencyCd",\
                              es1."sedol"=ses.sedol,\
                              es1."shortName"=ses."shortName",\
                              es1."strikePrice"=ses."strikePrice",\
                              es1."ticker"=ses.ticker,\
                              es1."valoran"=ses.valoran,\
                              es1."issueCountry_id"=ses."issueCountry_id",\
                              es1."createDate"=ses."createDate",\
                              es1."lastModifyDate"=ses."lastModifyDate",\
                              es1."recordVersion"=ses.recordVersion,\
                              es1."RIC" = ses.RIC,\
                              es1."issueDate" = ses.issueDate \
                            from equity_security as es1 \
                            inner join staging_equity_security ses \
                            on ses.secId=es1.secId'

                print 'UPDATE SECURITY SQL: % s' % update_security_sql

                cur.execute(update_security_sql)

            if feed == 'PRICES':
                cur.execute("truncate table staging_eodsecdata_secprices")
                cur.execute("copy staging_eodsecdata_secprices from '" + FEED_FILE + "' DELIMITERS ',' CSV HEADER")
                con.commit()

            logger.info("[DoLoads.py] Securities loaded into Staging: %s ", str(cur.rowcount))
            print "Getting current feeds...."

        cur.execute(
            "INSERT INTO equity_" + feed + " select symbol, close from staging_eodsecdata_secmaster ON CONFLICT (ticker) DO UPDATE SET mktPrice = close; ")





    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)


    finally:

        if con:
            con.close()
