###
class switch(object):
    value = None

    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == switch.value for arg in args))



#########
imagesSelector_1_2_3_4 = 2
showResultsOnOnePicture = True
showResultsOnDifferentPictures = True

while switch(imagesSelector_1_2_3_4):
    if case(1):
        print("Using: img01-before1.png / img01-after1.png")
        NameOfImageBefore = 'img01-before1.png'
        NameOfImageAfter = 'img01-after1.png'
        break
    if case(1, 4, 9):
        print("Using: tc300302....png / tc300302...after.png")
        NameOfImageBefore = 'tc300302_p000_s003_Satellite_Mode_Zoom_5km_DLS_STATE_4.png'
        NameOfImageAfter = 'tc300302_p000_s003_Satellite_Mode_Zoom_5km_DLS_STATE_4-after.png'
        break
    if case(2):
        print("Using: img02-2-before.png / img02-2-after.png")
        NameOfImageBefore = 'img02-2-before.png'
        NameOfImageAfter = 'img02-2-after.png'
    if case(2, 3, 5, 7):
        print("n is a prime number.")
        break
    if case(2):
        print("Using: img03-before.png / img03-after.png")
        NameOfImageBefore = 'img03-before.png'
        NameOfImageAfter = 'img03-after.png'
        break
    print("Using default choice 2: img02-2-before.png / img02-2-after.png")
    NameOfImageBefore = 'img02-2-before.png'
    NameOfImageAfter = 'img02-2-after.png'
    break


print("Before {} After {}", NameOfImageBefore, NameOfImageAfter)