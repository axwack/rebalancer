# I also get the error if I define the validator here
def validate_tgtWeights(value):
    if value == '':
        raise ValidationError(u'%s cannot be left blank' % value)
