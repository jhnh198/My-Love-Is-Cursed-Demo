# My Love is Cursed by jhnh198 12/16/2021
# Chapter 1

# characters
define n = Character("Nozomi", color="FF0044")
define s = Character("Shin", color="2255AA")
define t = Character("Teacher", color="AABBCC")
define h = Character('Hachi', color="CCCC00")
define u = Character('Unknown', color="333333")
define a = Character('Amaya', color="FF0044")
define student = Character("Student")
define sen = Character('Ari', color="FF0044")
define am = Character('Amaya\'s Mother', color="222222")
define sm = Character('Shin\'s Mother', color="663377")

# game mechanic variables
$ numberOfDays = 0

# define BGM
    # "Characters Floating in the Setting Sun" By soundorbis
    # https://dova-s.jp/bgm/play5700.html

    # "Nagareboshi" 2 versions, By MoppySound
    # https://dova-s.jp/bgm/play2627.html
define background_music = ['audio/music/characters_floating_in_the_setting_sun.mp3',
'audio/music/nagareboshi.mp3',
'audio/music/nagareboshi_2.mp3']

# The game starts here.
label start:

    call PartOne from _call_PartOne

    scene
    return


label language_chooser:
scene black

menu:
    "{font=DejaVuSans.ttf}English{/font}":
        $ persistent.lang = "english"
    "{font=mikachan.ttf}русский{/font}":
        $ persistent.lang = "russian"

$ renpy.utter_restart()
