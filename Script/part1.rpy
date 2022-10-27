label PartOne:
    # story board
    call Intro from _call_Intro

    $ renpy.random.shuffle(background_music)
    $ renpy.music.queue(background_music, fadein=2)
    call FindNeko from _call_FindNeko
    call ArriveClass from _call_ArriveClass
    call MeetingNozomi from _call_MeetingNozomi
    call GoingHome from _call_GoingHome
    call MeetHachi from _call_MeetHachi
    call AmayaPast from _call_AmayaPast
    call AmayaWalk from _call_AmayaWalk
    call AfterAmayaStory from _call_AfterAmayaStory

    return

label Intro:
    # "Memories Are Far Away" by K'z Art Storage
    # https://dova-s.jp/bgm/play15756.html
    play music 'audio/music/memories_are_far_away.mp3' volume 0.3 fadeout 1.0 loop

    centered """What do I know about love?

    The thought of it...

    terrifies me...

    Another person to spend the rest of your life with

    Someone to be close to

    Love is supposed to be a wonderful thing

    I don't know what love is""" (what_color="#fff")

    stop music fadeout 1.0
    centered '...perfect love' (what_color="#fff")
    centered 'What is love really like?' (what_color="#fff")
    centered 'And why am I so afraid of it?' (what_color="#fff")

    scene black
    return

label FindNeko:
    show school_hallway_day
    'Shin is running late to school, again.'
    s 'What is this?'
    'There\'s a small, shiny gold object on the ground.'
    'Shin picks it up and looks around. There\'s no one else here.'
    'He picks it up and attaches the clip to his bag.'

    scene black
    return

label ArriveClass:
    show classroom_day with fade
    'Shin walks into class 15 minutes late.'
    t 'Late again, Harana-san. Come see me after class.'
    'The class laughs at Shin.'
    s 'Yes, sir.'
    'Shin trudges over to his desk.'
    t 'Please take out your History books and go to chapter...'
    'Nozomi sees the Golden Teruko on Shin\'s bag.'
    'Nozomi goes to her bag to get her book.'
    'A pit in her stomach forms as she sees it is not there.'
    n 'I must have dropped it... that looks too cute for Harana-kun to have...'
    return

label MeetingNozomi:
    show cafeteria_day with fade
    'Shin is eating lunch alone.'
    'May I sit with you?'
    'Shin looks up to the girl in front of him.'
    show nozomi_smile with fade
    'She brushes her hair dangling in front of her face,
    for it to fall back in front again.'
    'Her persistent smile fades for a single moment and then returns.'
    s 'Sure, I don\'t mind.'
    'The girl sits down with her meal.'
    n 'I\'m Nozomi Shirai! It\'s nice to meet you!'
    'She bounces with a slight nod and has a bright, cheerful smile.'
    n 'Maybe you already know me...'
    n 'I am in your class.'
    s 'It\'s nice to meet you Nozomi. My name is Shin Harana.'
    s 'I know you but I don\'t think we have actually met.'
    'Shin looks down and Nozomi cranes her head to look at his eyes.'
    'He doesn\'t look back for several moments and she looks away.'
    n 'Where did you get that Golden Teruko, Shin?'
    s 'Golden Teruko... what is that?'
    'Nozomi points to his bag at the small, round golden trinket.'
    s 'Oh this. I found it today on the ground in front of school.
    It looked nice so I didn\'t want to leave it to get stepped on.'
    n 'I had one too. I seem to have misplaced it today.'
    n 'Coincidentally, the same day you found one...'

    'Shin hands the Golden Teruko to Nozomi.'
    'Nozomi\'s eyes widen as she takes it gently with both hands.'
    n 'Oh no.'
    n 'It has some scratches on it. I just got it and it\'s already messed up...'
    'She trails off and then looks back to Shin.'
    n 'Thank you for finding it! I owe you!'

    s 'What is that thing?'
    n 'The Teruko? It\'s a character from a game, Neko Collector. Have you heard of it?'
    s 'It\'s been out for a while, right?'

    n 'The new game came out this last weekend! I love it. Do you play?'
    s 'I play some other games.'
    n 'Ah.'
    s 'Have you played Lizard Quest?'
    n 'Um? I haven\'t gotten around to that one. {i}eheh{/i}'

    'They eat their meal together in silence for a few moments.'
    'The murmur of the crowd and sounds of the room fill the air.'
    n 'Would... would it be okay if I took you for lunch sometime?'
    s '{i}She seems nice enough.{/i}'
    s 'Okay.'
    n 'Here is my LINE. Please reach out to me.'
    s 'I will. Thank you, Nozomi.'

    scene black
    return

label GoingHome:
    show school_hallway_day
    show nozomi_smile
    'Nozomi approaches Shin at the end of the day.'
    n 'Thanks again for finding my Teruko. I was really upset when
     I realized it was missing.'
    s 'No problem. I wasn\'t trying to do anything special.'
    'Nozomi chuckles to herself and walks away.'
    hide nozomi_smile with dissolve

    show livingroom_night with fade
    s 'I\'m home...'
    'There\'s no answer.'
    'Shin kicks off his shoes and they hit the wall with a loud bang.'
    'It didn\'t leave a noticable mark this time.'
    s 'Mom and dad must be working late again.'
    'Shin heats up a cup of instant ramen for dinner and heads to his room.'

    show bedroom_evening with fade
    'Shin lays on the bed and stares at the ceiling.'
    'He pulls out his phone and stares at Nozomi\'s profile.'

    s 'She is pretty...'
    'He looks at the message button and freezes up.'
    s 'What do I say?'
    'He turns off his phone and puts it down next to him.'
    s 'I\'m going to bed.'

    scene black
    return

label MeetHachi:
    show street_summer_day
    'The next day, Shin is walking home after school.'
    'A bee flies up to him. It dances around and hovers towards his face.
    It seems to be staring into his eyes.'
    u 'Reach out to the girl.'
    'Shin scans the area. He sees no one around.'
    'He is reluctant to move to avoid agitating the bee.'
    'The bee continues to look at him for several moments.'
    u 'It is the bee that is talking to you. Follow me, for I am the bee.'
    'The bee flies around the corner of a small shed in a nearby park.'
    s 'I don\'t have time for this... why am I following a bee?'

    show hachi_frown
    'Instead of a bee behind the shed, there is a blonde woman dressed formally.'
    h 'My name is Hachi. You may not understand this, but...'
    h '...you have a curse.'
    s 'A curse? I don\'t believe in that.'
    h 'I understand how this may sound bizarre, foolish even, but consider this:'
    h 'Would you believe a bee has ever turned into a woman before?'
    s 'I... um, no.'
    h 'Until you break it, no one will fall in love with you.
    As soon as you start to develop feelings for another person, they will be
    driven away. You will make them hate you for it.'
    h 'There\'s no way around this.'
    h 'I would never ask anything unfair of you or solely for my own benefit.
    You won\'t own me anything. If you decide you do not want my help, I will
    leave you in peace.'
    s 'How did this happen then? Why do you know about it unless you have
    something to do with it?'
    'Hachi looks away and her eyes narrow a bit.'
    h 'How bold to blame another for thine own misfortune...'
    'She faces Shin again.'
    h 'I am a benevolent bee, only wishing to help humans.'
    h 'You want to know who caused this curse?'
    'Hachi raises her arm slowly and points at Shin.'
    h 'This comes from breaking the heart of a lover.
    You mistreated them.'
    s 'I don\'t know what I could have done. No one has ever loved me.'
    h 'Everyone is loved by someone, even if they don\'t know it. Even
    if one fully believes they don\'t deserve love. Even if one has commited to
    being unloved.'
    s 'I don\'t know. It just seems like every time I like someone, they never
    like me.'
    s 'The last girl I tried to date... she stopped talking to
    me.'
    h 'What happened?'
    s 'It just... we talked less and less. I would try to start a conversation
    and eventually she stopped responding.'
    h 'Did you argue?'
    s 'Not that I can think of. Everything seemed fine and then
    I never heard back from her. She says hi sometimes but any time
    I ask her if she wants to get together she is busy.'
    h 'Tell me about anyone else you think it could be before her.'

    return

label AmayaPast:
    'Shin thinks for a while.'
    s 'The only girl who comes to mind is Amaya.'
    h 'Who is Amaya?'
    s 'She was a girl I grew up with. She moved away.'
    h 'Tell me about her.'

    show school_hallway_day with fade
    show amaya_smile

    'Three years ago...'
    'Shin and Amaya are walking back to class.
    Shin is looking off, in a daydream. Her attention is on him.'
    'Amaya wears a small tattered rope bracelet. A friendship
    bracelet that she made for Shin and herself. She has worn it every day
    since then.'
    a 'You took your bracelet off again, didn\'t you?'
    s 'Hmm? Oh... I forgot it.'
    a 'Will you walk home with me today?'
    s 'We walk home together every day. I live right next to you.'
    a 'You could be busy though.'
    s 'I\'m not busy today. I\'m always free.'
    a 'But you could be and so that\'s why I asked.'
    s 'It\'s time to go back inside.'
    'Amaya blushes and looks away as they walk together.'
    'Before they get to the door, Amaya reaches for Shin\'s hand.'
    s 'What are you doing?'
    'He pulls away and they continue to walk to class in silence.'

    show classroom_day with fade
    show amaya_smile
    'They sit down in their seats next to each other.'
    'Shin starts to go through his bag and get his things.'
    a 'What\'s wrong, Shin?'
    'Amaya reaches for Shin\'s hand again.'
    s 'Don\'t do that. People will make fun of us.'
    a 'So what if they do? I don\'t care what everyone else thinks.'
    s 'Will you stop?'
    a 'No.'
    'At this point some of the other students are looking at them.'
    'The class is growing a little quieter but they are talking still.'
    s 'You never listen to anyone! Your dad yells at you so loud I can hear it
    next door. Why don\'t you just do what people tell you to do?!'
    'Everyone heard that. The class erupts in murmurs.'

    show amaya_frown
    stop music
    a 'W-why...?'
    a 'What made you want to say that?'
    'Amaya is trembling and tears are flowing down her cheeks onto the floor.'
    'She runs out of the classroom, sobbing and covering her face.'
    hide amaya_frown with fade
    student 'That was really mean.'
    'Another student goes after her.'
    t 'Come with me, Shin.'
    'The teacher takes Shin to the Principal\'s office.'

    $ renpy.random.shuffle(background_music)
    $ renpy.music.queue(background_music, fadein=2)

    scene black
    show street_summer_day with fade
    show hachi_frown

    s 'I got scolded, but not for telling the secret.
    They told me it was a good thing that I said something.
    I should have gone to the teachers or my parents, instead of screaming
    it at her in class.'
    s 'I didn\'t see Amaya at school for several days.'
    s 'I didn\'t really care that she was gone.'
    s 'I tried to see her. It wasn\'t that I wanted to see her,
    but I felt like it was an obligation.'
    s 'I was supposed to go check on her. So I did.'

    scene black
    show street_summer_evening with fade
    'Shin approaches Amaya\'s house.'
    'A heavy cloud hangs over it. Shin can feel it emanating from the place.'
    'Shin knocks on the door.'
    'The door creaks open slightly.'
    am 'Amaya isn\'t home right now.'
    'The door closes before Shin can answer.'

    scene black
    show street_summer_evening with fade
    'The next day, Shin goes to Amaya\'s house and knocks again.'
    'After several moments the door opens a little.'
    am 'Amaya is busy.'
    'The door closes a little more forcefully today.'

    'The next day...'
    'Shin knocks and waits for 2 minutes.'
    '{w} {w=3.0}'
    'No one answers.'

    scene black
    return

label AmayaWalk:
    stop music
    show bedroom_evening

    'Shin is in his room.'
    sm 'Shin. Amaya is here for you.'
    'He goes to see her at the doorway.'

    show livingroom_night with fade
    show amaya_frown
    a 'Come with me.'
    scene black
    play music 'audio/music/memories_are_far_away.mp3' volume 0.5 fadeout 1.0 loop

    show street_summer_evening with fade
    show amaya_frown
    'Amaya walks slowly with her head down.'
    a 'I\'m moving.'
    s 'Where are you going?'
    a 'Numata, it\'s really far away.'
    s 'Maybe there is something nice out there to see?'
    'Amaya looks up at him with a blank stare.'
    a 'It is just... I don\'t want to go.'
    s 'Will you come back?'
    'Amaya looks over at Shin\'s wrist.'
    a 'You aren\'t wearing your bracelet.'
    s 'Wearing my... '
    'He looks down to his wrist.'
    a 'The friendship bracelet I made for you. Like this?'
    'She raises her arm up to show hers.'
    s 'The guys at school always make fun of me when I wear it.'
    a 'You\'re with me. No one else is here. You could just hide it under your
    sleeve or something!'
    a 'You could make an effort...'
    s 'I forgot. I\'m sorry.'
    a 'Are you really my friend?'
    s 'Yeah.'
    'Amaya sniffles.'

    'Neither of them say anything for several minutes. Shin is looking away
    from Amaya. She is staring at the ground. She is still and unmoving.'

    'Shin is shifting about in his place. He meanders towards something like it
    might be appealing. Something to distract himself while he gets through
    this.'

    'All he can feel is the buzzing in his mind that makes him aware of her
    uncomfortable presence.'

    'All I want to do is get through this.'

    stop music
    '{w} {w=3.0}'

    s 'At least it will be a change of pace?'
    a 'I don\'t care about what is out there!'
    'She steps up to him quickly. Shin takes a step back.'
    s 'I was just sayi-{nw}'
    a 'I want you! I don\'t care about anything else!
    Everyone hates me, but I thought... I thought that you were my friend.'
    s 'I am your friend. I helped you. Now everyone knows what was going on
    so it won\'t happen anymore, will it?'
    'Amaya wraps her arms around Shin and holds him in place. He can\'t move
    his arms to return the embrace.'
    a 'Don\'t say anything. Just let me hold you for a moment.'
    '{w}Amaya is shaking with her head buried in his chest. She is pulling down
    as her knees start to tremble. Shin doesn\'t hold her but stands trying
    to keep his own balance.{w=6.0}'
    a 'I... you\'re the smartest fool I know.'
    a '{w}I wish you could see how stupid it was!{w=6.0}'
    a 'My mom and me are going to lose everything.'
    a 'Things are messed up. We can\'t stay where we are.
    We have to move for safety. It\'s what the police say we have to do, just to
    be sure.'
    'Shin swallows hard as the realization that things are much worse than
    he gave himself credit for.'
    a 'Don\'t you know how I feel? Don\'t you care?'
    s 'Yeah.'
    a 'Why did you say that in front of everyone?!'
    'Amaya pounds on his chest and backs up. Her hands are still balled into
    fists.'
    s 'I\'m sorry that you fe-{nw}'
    'Amaya punches Shin across the cheek.'
    s 'Ow...'
    'It stings. He looks down and sees a few drops of blood coming from his
    mouth.'

    hide amaya_frown with dissolve
    '{w}He can taste the salt and feels tears forming in his eyes. His vision is
    a bit blurrier for a moment while Amaya storms off, away from him.{w=6.0}'

    s 'I know I should follow her, but my feet and my body won\'t move.'
    s 'I am stuck to this spot.'
    s 'I can\'t do anything.'
    s '''Doing nothing is the easier way out.
    Instead of the broken thoughts I can only piece together.
    I can only guess of whatever might come if I tried to go after her.'''
    s 'I can\'t follow my only friend.'
    s 'Someone I am losing right now, in front of me.'
    s 'Do I care?'
    s 'Is there some sliver of compassion I have buried?'
    s 'I can\'t find it.'

    scene black
    centered 'She wanted comfort and I had none for her.' (what_color="fff")
    return

label AfterAmayaStory:
    show street_summer_day with fade
    show hachi_frown
    h 'It sounds like she was in love with you.'
    s 'How do you know?'
    h 'She wanted to be around you.'
    s 'I didn\'t want her around.'
    h 'Are you glad she isn\'t around anymore?'
    'Shin was ready to respond, as if he knew what Hachi would say,
    as if he knew exactly the right answer to give before the question was even
    asked.'
    'As the words sink in he stops. The pause tells more than
    if they were spoken. The explanation would ruin whatever merit they had.'
    s 'I didn\'t realize that getting what I wanted would hurt that much.'
    s 'I believe in you, Hachi. I think there is something special about you.
    Will you help me?'
    h 'I will.'
    s 'What should I do?'
    h 'I want you to test the curse. I want you to see what happens when someone
    falls in love with you, or you them.'
    s 'How do I do that?'
    h 'Develop feelings of love.'
    s 'But how?'
    h 'Sometimes things just happen on their own.'
    s 'It\'s odd when you put it that way. I know that it is obvious why you say it,
    because it is true. And at the same time, it feels so unhelpful.'
    s 'I don\'t know why it feels like something I cannot do,
    but everyone else seems to be able to.'
    h 'It doesn\'t mean you can\'t do it, even if you think you can\'t or don\'t
     want to.'
    h 'Try talking to the girl, Nozomi, first.'
    s 'I will try.'

    scene black
    centered 'End of Demo '(what_color="fff")
    stop music

    return
