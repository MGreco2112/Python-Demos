#Age Classifier

#if the person is 1 year old or less, result is infant
#if person is > 1 year but < 13, result is child
#if person is >= 13 and < 20, result is teenager
#if person is >= 20, result is adult

#takes input from user, stores as integer
person = int(input("Enter your age: "))

#constants declared for maximum value of infant, minimum value for teenager, and minimum value for adult
INFANT_CLASSIFICATION = 1
TEENAGER_CLASSIFICATION = 13
ADULT_CLASSIFICATION = 20

#if elif else flow to identify range in which person falls into
if person <= INFANT_CLASSIFICATION:
    print("You are an infant")
elif person >= INFANT_CLASSIFICATION and person < TEENAGER_CLASSIFICATION:
    print("You are a child")
elif person >= TEENAGER_CLASSIFICATION and person < ADULT_CLASSIFICATION:
    print("You are a teenager")
else:
    print("You are an adult")