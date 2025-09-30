print(r"""
           (                 ,&&&.
            )                .,.&&
           (  (              \=__/
               )             ,'-'.
         (    (  ,,      _.__|/ /|
          ) /\ -((------((_|___/ |
        (  // | (`'      ((  `'--|
      _ -.;_/ \\--._      \\ \-._/.
     (_;-// | \ \-'.\    <_,\_\`--'|
     ( `.__ _  ___,')      <_,-'__,'
      `'(_ )_)(_)_)' ASCII art by jrei
""")
print("Echoes in the Forest: A choose your own adventure game.")
print("-- Made by Edro ;) --")

print("""
You’re alone. That was the point.

A weekend to unplug, to sit by the fire and forget the weight of your job, your phone, and the endless cycle of news. You chose this forest because no one comes here. That’s what the old ranger said anyway — his eyes hesitant, like he almost wanted to say more.

Now, it’s past midnight. The fire crackles lazily. Stars peek through the swaying trees above.

Then you hear it.

A voice. Far off. Human. Talking. But not to you.

It’s coming from deep within the forest. No lights. No footsteps. Just a voice — muttering, almost conversational. Too far to make out the words.

You lean forward. Your fire pops behind you.""")

choice_a = input("""
>>> What do you do?

>> 1: Call out to the voice.

>> 2: Douse your fire and stay quiet.

>> 3: Pack your stuff and leave now.

-> Your choice: """)

if choice_a == "1":
    print("""
You shout: “Hello? Who’s out there?”

The forest holds its breath.

Then the voice stops.

For a moment, there’s nothing. Silence. Then — closer now — it responds, mimicking your voice:

“Hello? Who’s out there?”

Chills run down your spine. You didn’t just hear an echo — it spoke like you.""")
    choice_b = input("""
>>> What do you do?
> 1: Pretend it’s someone playing a prank and demand they stop.
> 2: Get in your car and leave immediately.
-> Your choice: """)
    if choice_b == "1":
        print("""
You yell into the dark, forcing a shaky laugh.
“Okay — good one. Ha-ha. You got me. Come out and knock it off.”

At first, silence.

Then… it repeats your words. Slowly. Word for word.
But it stutters — like it’s trying to remember how a mouth works.

“O… kay… goooood… o-one. Ha. H-Ha. Yuh-you got… me.”

Your voice — but wrong. Wet. Crooked.
You hear something moving, dragging itself just out of view.

You realize, dimly, that you’ve wandered far off the glow of the campfire.

Then a new sound.

Breathing.

Close.

You turn in a panic — your flashlight catches something between the trees.
A figure, crouched low. Thin. Wrong. Its limbs are too long. Its head twitches, like it’s listening for a signal.

Your phone buzzes.

You glance down. A message.

It’s from you. A photo.

You open it.

It’s your campsite. Taken just now.
And in the photo, you’re standing at the edge of the trees — but you’re still holding the phone.

You look up.

Through the gaps in the trees, far behind you where the fire should be, something else is standing in your place at the campfire.""")
        choice_c = input("""
>>> What do you do?
> 1: Approach the thing at the fire.
> 2: Run — get to the car, don’t look back.
-> Your choice: """)
        if choice_c == "1":
            print("""
You step into the firelight, breath caught in your throat.

The figure turns — and it is no one. No face, no eyes, no voice. A shape built from shadows and bone, its limbs too long, its skin like bark peeled from a dead tree. There's no logic to how it moves — it shifts with a sound like cracking joints underwater.

It doesn’t speak. It doesn’t need to.

You take one more step.

Your vision dims, not from fear — but because the forest itself is fading. Or maybe you are. You feel your heartbeat slow, your thoughts stretch and blur.

The creature opens its mouth — wide, impossibly wide — and all you hear is the fire, your name, and everything you’ve ever regretted being said at once.

Then you’re gone.""")
        if choice_c == "2":
            print("""
You just run.

The fire dies behind you as you tear through the dark, flashlight swinging wildly in your grip. The voices follow — dozens of them, all broken, all whispering your name in tones you've never heard from a human throat.

Something moves through the trees beside you, always just out of view. Too fast. Too tall.

Your lungs burn. You stumble. Keep running.

Then — your car. Glinting in the dark like a lifeline. You dive in, slam the door, jam the keys in with trembling hands.

From the passenger side, just inches from your ear, a voice hisses:

“You forgot something.”

You don’t answer. You don’t look. You drive. Fast.

You don’t stop until you hit pavement. Until the trees are far behind you.      """)
    if choice_b == "2":
        print("""
You throw your gear together, half-packed, and bolt down the dark trail toward your car. The voices in the woods grow louder — layered, echoing your name in different tones. You don’t stop. You don’t look back.

Branches claw at your jacket. Something mimics your footsteps behind you — always just a half-step late. You spot your car. You sprint.

As you start the engine, a voice outside your window whispers, “Wait.” You don’t turn. You hit the gas.

You drive until the trees thin, until streetlights return. You never hear the voices again.

You survived. You left before the forest could take anything from you. Sometimes, the best choice is knowing when to run.""")

if choice_a == "2":
    print("""
You douse your fire, dive into your tent, and zip it shut with shaking hands, trying to quiet your breathing.

The forest outside goes still.

Too still.

You sit there in the dark, barely moving, clutching your flashlight without turning it on. The thin nylon walls press in around you. It feels smaller now — like the tent is shrinking.

You hear it again.

Footsteps. But not on the ground — around you, above you, like something is circling the tent without touching it.

Then... a sound like breathing.
Not yours. Not human.

It’s right outside.

You hold your breath.

The zipper twitches. Just once. Like a finger traced it from the outside.

You reach out to stop it — and that’s when you realize: you can see your breath inside the tent. The air is freezing.

Then everything goes quiet.

For a moment, you think it’s gone.

Then the wall of the tent pushes inward, a long, hand-shaped impression stretching toward your face from the outside. The fingers press through the fabric, impossibly slow. The tent doesn’t rip. It just lets it in.

You scream, but no one hears.

The tent never kept anything out. It only kept you in.""")

if choice_a == "3":
    print("""
You don’t wait. You throw your gear together, half-packed, and bolt down the dark trail toward your car. The voices in the woods grow louder — layered, echoing your name in different tones. You don’t stop. You don’t look back.

Branches claw at your jacket. Something mimics your footsteps behind you — always just a half-step late. You spot your car. You sprint.

As you start the engine, a voice outside your window whispers, “Wait.” You don’t turn. You hit the gas.

You drive until the trees thin, until streetlights return. You never hear the voices again.

You survived. You left before the forest could take anything from you. Sometimes, the best choice is knowing when to run.""")

