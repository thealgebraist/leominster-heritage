TRACKS = [
 dict(id='Dc1uBZahhts',slug='01_flaunching',title='Flaunching',duration=15.813,
 transcript=[('0.0–1.5','Flaunching, flaunching!'),('1.7–3.0',"What's around your pot?"),('3.2–3.8','A flaunching!'),('3.8–5.3','Soaping nicely, keeping it dry.'),('5.3–7.7',"Flaunching 'round your pot, up in the sky."),('9.6–10.8','A flaunching!'),('10.8–15.8','No further intelligible words recovered; musical/video tail.')],
 pronunciation=[('Flaunching','FLAWN-ching','Two syllables; strong first syllable. FLAWN versus a rounder FLON vowel remains unverified.'),("What's around your pot?",'wots uh-ROUND yuh POT','Light connecting words; punch POT.'),('A flaunching','uh FLAWN-ching','The little opening uh is a pickup, not the word air.'),('Soaping nicely, keeping it dry','SOH-ping NYSS-lee, KEE-ping it DRY','Both main ASR passes hear “soaping”. It may be intentional wordplay or a lyric different from the expected building term; do not silently replace it with “sloping”.'),("Flaunching round your pot, up in the sky",'FLAWN-ching round yuh POT, up in thuh SKY','Short syllables leading to a held or accented SKY.')],
 issues=['Whisper full, short-chunk and targeted passes agree on “soaping nicely”; the separated-vocal model also returned “soaping”. The sampled frames do not provide a readable caption for this word. Since “sloping” is only a contextual architectural guess, the source transcript and Suno lyric use the better audio-supported “soaping”, with the potential pun/error noted.','The article before the last flaunching is less clear than the captioned earlier “A flaunching”.'],
 recipe='A very short hook–question–answer jingle. Begin with two accented repetitions, put the question on a compact speech-like phrase, hit the answer, accelerate the explanatory line, and leave a short gap before the final answer. Keep the hook more memorable than the backing.',
 lyrics='''[Short rhythmic hook]
Flaunching, flaunching!
What's around your pot?
A flaunching!
[Quick rhythmic line]
Soaping nicely, keeping it dry
Flaunching round your pot, up in the sky
[Brief instrumental gap]
A flaunching!
[Short ending]'''),
 dict(id='Dc8axxYIC3k',slug='02_guttae',title='Guttae / Good Day',duration=22.29,
 transcript=[('0.0–5.9','Guttae! … Guttae! … Guttae!'),('5.9–10.5','Rapid chopped two-syllable hook, heard as “Guttae/Gootay” or repeated “good day” by different Whisper passes; exact words and count unresolved.'),('10.5–11.3','Good day!'),('11.4–12.1','Guttae!'),('12.2–13.3','Too many guttae!'),('14.0–18.3','Guttae! Guttae! Guttae! Guttae! [approximately four further calls]'),('18.3–22.3','Ending / title-card tail; no further reliable lyric recovered.')],
 pronunciation=[('Guttae','GUH-tay / guh-TAY','Whisper and the separated-vocal model (“gotay”) support a final AY sound, not eye. Exact first vowel and stress vary/are unresolved; preserve the good-day pun.'),('Good day','guh-DAY','Two short syllables, matching the rhythm and sound of guttae.'),('Too many guttae','too MEN-ee GUH-tay','Speed through too many, land on the two-syllable architectural word.')],
 issues=['The chopped middle has clear repeated two-syllable calls but uncertain wording: full/short Whisper variants render them as Gootay/Guttae, while the targeted pass hears repeated “good day”. The good-day/guttae homophone makes this difficult to settle from ASR; exact count and whether the phrase alternates remain unresolved. The Suno version chooses repeated Guttae for a compact motif, not a claimed exact transcript.','“Good Day” is directly visible at about 10.5 seconds. The sound is interpreted as close to “guttae”, so spelling alone cannot identify every occurrence.'],
 recipe='A two-syllable vocal motif treated as the main rhythmic instrument. Start with widely separated calls, compress into a short stuttered cluster, interrupt with the near-homophone “good day”, then use “too many” as a spoken pickup and repeat the hook. Preserve the gaps; do not turn the tiny text into a long verse.',
 lyrics='''[Spaced rhythmic calls]
Guttae!
Guttae!
Guttae!
[Quick chopped chant]
Guttae, guttae, guttae, guttae
Guttae, guttae
[Spoken interjection]
Good day!
[Chant]
Guttae!
Too many guttae!
Guttae!
Guttae!
Guttae!
Guttae!
[Short instrumental ending]'''),
 dict(id='DcRZB_PBFkr',slug='03_corbel_bargeboard',title='Corbel / Bargeboard / Architectural Features',duration=38.011,
 transcript=[('0.0–3.5','Corbel, corbel, corbel, corbel / Bargeboard, bargeboard.'),('3.6–7.0','Corbel, corbel, corbel, corbel / Bargeboard, bargeboard.'),('7.1–10.7','Mullion repeated [approximately four calls].'),('10.7–14.5','Brace repeated [rapid calls; exact count unresolved].'),('14.6–16.3','Quatrefoil, quatrefoil.'),('16.4–18.1','Quoin repeated [exact count unresolved].'),('18.2–19.7','String course, string course.'),('19.8–26.0','Buttress repeated [caption remains visible through about 26s; exact spoken-call count uncertain].'),('26.0–28.5','Corbel, corbel, corbel, corbel / Bargeboard, bargeboard.'),('28.5–30.1','Mullion, mullion.'),('30.1–32.0','Brace, brace.'),('32.0–33.0','Finial!'),('33.0–38.0','Musical/end-card tail; no further reliable words recovered.')],
 pronunciation=[('Corbel','KOR-buhl','Two compact syllables; four evenly spaced calls.'),('Bargeboard','BAHJ-bawd','Two strong word components; broad British non-rhotic rendition is a suggested performance choice.'),('Mullion','MUL-yun','Compress to two sung syllables, rather than mull-ee-on.'),('Brace','BRAYSS','One syllable, crisp BR onset; useful for repeated percussive hits.'),('Quatrefoil','KAT-er-foyl','Recognizer approximations “cutterfoil” support three syllables; first vowel is not narrowly verified.'),('Quoin','KOYN','One syllable, like coin, not kwoyn.'),('String course','STRING kawss','Two beats/syllabic attacks; clipped STRING and a longer COURSE.'),('Buttress','BUT-riss','Two syllables; emphatic first, weaker second.'),('Finial','FIN-ee-ul','Three syllables ending the sequence as a punchline; caption corrects ASR “video”.')],
 issues=['The captions establish the sequence of specialist nouns that the full recognizer omitted. Repetition counts in the middle remain approximate. The caption “Buttress” stays visible from about 20 to 26 seconds; the number of spoken repetitions cannot be read from one sustained caption.','The four initial corbels are supported by the short-chunk pass; the full pass incorrectly inserted a fifth.'],
 recipe='A catalogue chant built out of short repeated cells. Contrast fast COR-bel pulses with slower BARGe-board responses, move through the other nouns as new rhythmic motifs, then reprise the opening and end with an isolated three-syllable FIN-ee-ul. Use stop/start spaces and short punctuating fills rather than long melodic lines.',
 lyrics='''[Rhythmic chant]
Corbel, corbel, corbel, corbel
Bargeboard, bargeboard
Corbel, corbel, corbel, corbel
Bargeboard, bargeboard
[New repeated motif]
Mullion, mullion, mullion, mullion
Brace, brace, brace, brace
Brace, brace, brace, brace
Quatrefoil, quatrefoil
Quoin, quoin, quoin, quoin
String course, string course
[Longer accented calls]
Buttress!
Buttress!
Buttress!
[Reprise]
Corbel, corbel, corbel, corbel
Bargeboard, bargeboard
Mullion, mullion
Brace, brace
[Final exclamation]
Finial!
[Short ending]'''),
 dict(id='DcYTYvMBSMn',slug='04_columns',title='Columns / Classical Orders',duration=53.615,
 transcript=[('0.0–7.0','Column, column, Doric column / Tuscan, Tuscan. [twice]'),('7.0–12.8','Ah—Corinthian / Ionic, Ionic.'),('12.8–19.7','Pilaster, pilaster, Doric pilaster / Capital, capital. [twice]'),('19.7–25.3','Ah—Palladio / Ionic, Ionic.'),('25.3–32.8','Fluted, fluted, Doric column / Tuscan, Tuscan. [twice]'),('32.8–37.8','Ah—Corinthian / Ionic, Ionic.'),('37.8–44.5','Capital, capital, Corinthian / Shaft, shaft. [twice]'),('44.5–49.2','Ah—Composite / Palladio!'),('49.2–53.6','Musical/end-card tail.')],
 pronunciation=[('Column','KOL-um','Two syllables; the written n is silent.'),('Doric column','DOR-ik KOL-um','Four syllables in a compact rhythmic unit.'),('Tuscan','TUS-kun','Two clipped syllables.'),('Corinthian','kuh-RIN-thee-un','Strong RIN, then two light syllables; can compress the ending toward th-yun at speed.'),('Ionic','eye-ON-ik','Three syllables, central stress.'),('Pilaster','pih-LAS-tuh','Stress LAS; do not substitute “I lost a”, an ASR error.'),('Capital','KAP-ih-tuhl','Three quick syllables, strong KAP.'),('Palladio','puh-LAH-dee-oh','Four syllables, strong LAH and a rounded held final OH.'),('Fluted','FLOO-tid','Two syllables; long OO.'),('Shaft','SHAHFT','One long open vowel for a suggested British rendition; the source vowel is not narrowly verified.'),('Composite','kum-POZ-it','Three syllables, central stress, not COM-poh-site.'),('Ah','AAAH','Open sustained vowel before the longer architectural name.')],
 issues=['Specialist spellings are supported by the captions; ASR variants “biloster”, “dory”, and “I love you” have been corrected to the captioned terms.','Timings are approximate section boundaries; rapid sung syllables need not align exactly with the animated captions.'],
 recipe='Four catalogue blocks using the same compact rhythmic template. Two brisk list phrases are followed by a broader held “Ah” and a more melodic long name. Reuse the rhythmic cell for column/pilaster/fluted/capital, with short Tuscan or shaft answers. Keep the long vowels at the end of each block distinct from the clipped list delivery.',
 lyrics='''[Rhythmic verse]
Column, column, Doric column
Tuscan, Tuscan
Column, column, Doric column
Tuscan, Tuscan
[Held melodic exclamation]
Ah, Corinthian
Ionic, Ionic
[Rhythmic verse]
Pilaster, pilaster, Doric pilaster
Capital, capital
Pilaster, pilaster, Doric pilaster
Capital, capital
[Held melodic exclamation]
Ah, Palladio
Ionic, Ionic
[Rhythmic verse]
Fluted, fluted, Doric column
Tuscan, Tuscan
Fluted, fluted, Doric column
Tuscan, Tuscan
[Held melodic exclamation]
Ah, Corinthian
Ionic, Ionic
[Rhythmic verse]
Capital, capital, Corinthian
Shaft, shaft
Capital, capital, Corinthian
Shaft, shaft
[Held final exclamation]
Ah, composite
Palladio!
[Short ending]'''),
 dict(id='DcbYsWLhhdZ',slug='05_doors',title='Doors',duration=64.691,
 transcript=[('0.0–6.3','Door repeated [approximately seven calls].'),('6.3–7.6','Green door, red door.'),('7.6–10.6','Door repeated; exact count unresolved.'),('10.6–11.2','Cat flap [likely; supported by two ASR passes and partial OCR at 11s].'),('11.2–12.4','Blue door, black door.'),('12.4–14.2','Door repeated.'),('14.2–16.4','Back door, front door / Big door, small door.'),('16.4–18.0','Door repeated; two overlapping Whisper chunks hear a possible “trap door” near the end, but the word is not caption-confirmed.'),('18.0–18.9','Old door, new door.'),('18.9–20.3','Door repeated.'),('20.3–23.5','Stable door / Cellar door!'),('23.5–28.8','Ah! / hold on? / [Hodor?] / intervening vocal passage; the exact wording is unresolved.'),('28.8–31.9','Door, panel door [caption also says panelled], plank door.'),('31.9–35.2','Door, door, studded door, arched door.'),('35.2–40.0',"Door, door, secret door / Where? / Behind the door."),('40.0–42.9','Door repeated [approximately six calls].'),('42.9–45.9','Green door, red door, blue door / Cat flap!'),('46.0–50.3','Door, door, door / And one more…'),('51.5–59.3','Dumbledore! [caption splits it as Dumble / Door; held/effected passage follows]'),('59.4–61.3','Door!'),('61.3–64.7','End-card/music tail.')],
 pronunciation=[('Door','DAW','One syllable with a long rounded vowel; avoid adding a separate duh-or syllable.'),('Green / red / blue / black door','GREEN DAW / RED DAW / BLOO DAW / BLAK DAW','Make the colour a pickup or accented first word, then repeat the identical door sound.'),('Back / front / big / small door','BAK DAW / FRUNT DAW / BIG DAW / SMAWL DAW','Crisp adjective; consistent long DAW.'),('Trap door','TRAP DAW','Two sharply articulated syllables; transcript status is tentative because only Whisper chunk passes suggest “trap”.'),('Old / new / stable / cellar door','OHLD DAW / NYOO DAW / STAY-buhl DAW / SEL-uh DAW','Stable and cellar are two syllables each.'),('Panel / plank / studded / arched door','PAN-uhl DAW / PLANK DAW / STUD-id DAW / AHCHT DAW','The source audio recognizer supports panel while captions use both panel and panelled.'),('Secret door; Where? Behind the door','SEE-krit DAW; WAIR? bih-HYND thuh DAW','Use a separate spoken questioning voice for Where if recreating the comic dialogue.'),('Cat flap','KAT FLAP','Two abrupt syllables; not “cut flop”.'),('And one more','und WUN MAW','Build anticipation by delaying the answer.'),('Dumbledore / Dumble-door','DUM-buhl-DAW','Three syllables; same long DAW as every other door. Preserve the pun.'),('Hodor?','HOH-daw?','Tentative identification only; a separate low spoken interjection is a reconstruction option, not confirmed text.')],
 issues=['The original full ASR pass looped on “door” for 29 seconds and is unusable in that section. Short chunks plus captions recover the list, but do not establish every repetition count.','The passage around 24–28 seconds is not reliably transcribed. Both Whisper and the separated-vocal model return “hold on”; “Hodor” is a contextual alternative, not a recovered fact. The second model also reports an initial Ah vocalization. The paste-ready version keeps an Ah/hold-on spoken break, marking the wording as uncertain rather than replacing the vocal with an instrumental break.','An early “cat flap” at about 10.6 seconds is likely: two independent ASR passes agree, and OCR partially reads “Cat Fla…” on the sampled 11-second frame. Exact onset and the surrounding repetition count remain uncertain. The later cat flap is also supported by audio recognition and a caption.','Two overlapping Whisper chunk passes suggest “trap door” shortly after “small door”, but captions show repeated Door labels and do not confirm trap. The Suno lyric includes the tentative phrase to preserve this plausible spoken line; verify by listening before treating it as established.','Repeated door counts in the recreation version are rhythmic choices, not claimed exact counts.'],
 recipe='A one-word ostinato with adjective substitutions. Keep the same door vowel, pitch cell, and rhythm through most of the piece, then use pauses and character-like spoken interruptions for the puns. Broaden stable/cellar door, break briefly, resume the list, ask “Where?”, and build a delayed Dumbledore payoff before the final single door.',
 lyrics='''[Repeated rhythmic hook]
Door, door, door, door
Door, door, door
Green door, red door
Door, door, door, door
Cat flap!
Blue door, black door
Door, door, door
Back door, front door
Big door, small door
[Possible phrase; verify against source]
Trap door
Door, door, door
Old door, new door
Door, door, door
[Longer calls]
Stable door
Cellar door!
[Brief spoken break; wording uncertain]
Ah! Hold on!
Door, panel door, plank door
Door, door, studded door, arched door
Door, door, secret door
[Spoken question]
Where?
[Spoken answer]
Behind the door!
[Rhythmic hook]
Door, door, door, door, door, door
Green door, red door, blue door
[Sharp spoken interjection]
Cat flap!
[Chant]
Door, door, door
[Spoken buildup]
And one more...
[Pause, final exclamation]
Dumbledore!
[Musical tail]
Door!
[End]'''),
 dict(id='DcqWhZtBIEI',slug='06_windows',title='Windows',duration=67.013,
 transcript=[('0.0–6.9','Window repeated [four principal calls, with possible extra chopped repetitions].'),('7.0–10.9','Mullion, muntin, meeting rail, transom.'),('10.9–14.8',"Window, window, what have you got? / Mullion in the middle, glazing in the lot."),('14.8–19.4','Casement! / Is that a casement? / Yes, a casement!'),('19.4–21.3','Open it out, shut it again.'),('21.4–24.9','Stay, fastener, hinge, pane.'),('24.9–28.4','Rail, stile, glazing bar / Rail, stile, glazing bar.'),('28.4–30.5','Sash goes up, sash comes down.'),('30.5–35.7',"Sash cord! / Where's it gone? / In the box. / Obviously."),('35.7–38.6','Window repeated [exact count unresolved].'),('38.7–42.2','Fanlight, sidelight, oriel [possibly followed by “too”; unresolved].'),('42.2–48.6','Bay window, bow window / What does it do? / Lets in light. / Very good.'),('49.7–55.0','Casement! / Is that a casement? / Yes, a casement!'),('56.9–60.4','Mullion, muntin, transom, pane.'),('60.4–64.4','Open the window / Shut it again.'),('64.4–67.0','Musical/end-card tail.')],
 pronunciation=[('Window','WIN-doh','Two syllables, strong WIN; same motif whenever it returns.'),('Mullion / muntin','MUL-yun / MUN-tin','Both two syllables; distinguish L-y from NT.'),('Meeting rail / transom','MEE-ting RAYL / TRAN-zum','Strong first word beats; transom is two syllables.'),('What have you got?','wot-uv-yuh GOT','Compress unstressed syllables before GOT.'),('Mullion in the middle, glazing in the lot','MUL-yun in thuh MID-ul, GLAY-zing in thuh LOT','Quick syllabic delivery with MID and LOT accented.'),('Casement','KAYSS-munt','Two syllables; KAYSS remains clear in the question and answer.'),('Stay / fastener / hinge / pane','STAY / FAS-uh-nuh / HINJ / PAYN','Fastener has a silent t; keep the listed objects separate.'),('Rail / stile / glazing bar','RAYL / STYL / GLAY-zing BAH','Stile sounds like style; glazing begins GL, not BL.'),('Sash cord','SASH KAWD','Two strongly accented words, not sash gone or sashcorn.'),("Where's it gone? In the box. Obviously.",'WAIRZ it GON? in thuh BOKS. OB-vee-us-lee.','Treat as a brief spoken dialogue with small gaps.'),('Fanlight / sidelight / oriel','FAN-lyt / SYD-lyt / OR-ee-ul','Two, two, then three syllables; the possible following too remains uncertain.'),('Bay window / bow window','BAY WIN-doh / BOH WIN-doh','Bow rhymes with go, not cow.'),('Lets in light. Very good.','LETS in LYT. VEH-ree GUD.','Dry spoken answer then approving response; not “lesson lie”.')],
 issues=['“Oriel” is caption-confirmed. Whisper alternatives include too/through; one second model returns “oriel too”, while the caption sequence is not clear enough to settle a following word. The Suno version tentatively uses “too”.','The exact window repeat count after “obviously” is uncertain. The copy-ready pattern uses four calls.','Architectural spellings were corrected using captions: glazing, stile, pane, sash cord, muntin, fastener.'],
 recipe='Alternate compact sung catalogue phrases with a miniature spoken question-and-answer routine. Use the two-syllable window as a recurring melodic/rhythmic anchor. Give casement a short call, a questioning rise in “Is that a casement?”, then a conclusive answer; those contours are suggested reconstruction directions, not a note transcription. Run the lists quickly, leave space around obviously and very good, and finish with two contrasting commands.',
 lyrics='''[Rhythmic hook]
Window, window, window, window!
[Quick list]
Mullion, muntin, meeting rail, transom
Window, window, what have you got?
Mullion in the middle, glazing in the lot
[Call and response]
Casement!
Is that a casement?
Yes, a casement!
Open it out, shut it again
[Rhythmic list]
Stay, fastener, hinge, pane
Rail, stile, glazing bar
Rail, stile, glazing bar
Sash goes up, sash comes down
[Spoken exchange]
Sash cord!
Where's it gone?
In the box
Obviously
[Hook]
Window, window, window, window!
[Rhythmic list]
Fanlight, sidelight, oriel too
Bay window, bow window
[Spoken exchange]
What does it do?
Lets in light
Very good
[Call and response]
Casement!
Is that a casement?
Yes, a casement!
[Closing list]
Mullion, muntin, transom, pane
Open the window
Shut it again!
[Short ending]'''),
 dict(id='DcvxvGDhSeb',slug='07_echinus_entasis',title='Echinus / Entasis',duration=22.477,
 transcript=[('0.0–3.8','Echinus, entasis / Echinus, entasis.'),('3.8–6.5','A bulbous end / A gently swelling shaft.'),('6.8–9.2','Echinus, entasis.'),('9.2–11.8','A bulbous end / A gently swelling shaft.'),('12.2–14.8','A gently swelling shaft.'),('16.0–18.7','A gently swelling / swirling shaft [word unresolved; captions and one targeted pass support swelling, another chunk hears swirling].'),('18.7–22.5','Musical/end-card tail.')],
 pronunciation=[('Echinus','ek-EYE-nuhs (UK) / ih-KY-nuhs (US)','Three syllables, middle stress. Cambridge lists these regional pronunciations. The UK form is a reasonable target for this British architectural context, but the recording vowel is not clear enough here to confirm which form was sung; the audio model’s “etchinoss” is not accepted as standard.'),('Entasis','EN-tuh-sis','Three syllables, first stress; consistent with the dictionary IPA /ˈɛntəsɪs/. Whisper supports the spelling, while the audio model’s “and tossiss” is a recognition error, not a pronunciation guide.'),('A bulbous end','uh BUL-bus END','Three stressed/unstressed word units; keep END as a distinct noun, not just “and”.'),('A gently swelling shaft','uh JENT-lee SWEL-ing SHAHFT','Six syllables; compact gently/swelling, lengthen the final shaft.')],
 issues=['The caption explicitly supplies “A Bulbous End”. ASR merges this with the next line as “a bulbous and a gently…”. The corrected transcript follows the captioned noun phrase.','Near 16–19 seconds, captions say “A Gently Swelling Shaft”; one targeted recognizer hears “swelling”, while another chunk hears “swirling”. The word is marked uncertain in the source transcript; the Suno lyric uses the caption-supported “swelling”.','Phonetic guidance for echinus and entasis is a broad pronunciation target, not a measured phoneme transcript.'],
 recipe='Pair two three-syllable technical terms as a repeating melodic cell. Answer with two descriptive phrases, the second longer and ending in the punchline shaft. Repeat that final phrase twice with space between repetitions, allowing its last vowel to carry the ending. Avoid adding new verses.',
 lyrics='''[Paired rhythmic motif]
Echinus, entasis
Echinus, entasis
[Answering phrase]
A bulbous end
A gently swelling shaft
[Repeat motif]
Echinus, entasis
A bulbous end
A gently swelling shaft
[Refrain]
A gently swelling shaft
[Brief pause, final refrain]
A gently swelling shaft
[Short ending]'''),
 dict(id='DdLxzBIoJ8F',slug='08_hall_house',title='Hall House',duration=49.967,
 transcript=[('0.0–4.1','Hall house, hall house / Have you visited a hall house?'),('4.1–7.3',"Front door, back door / Let's see your cross passage."),('7.4–10.3','Hall house, hall house.'),('11.0–14.5','Open hall, nice and wide / Service end, at the side.'),('14.5–18.1',"Upper end, lower end / Show me where your screens have been."),('18.1–19.9','Hall house, hall house.'),('20.0–23.2','Smoke-blackened all the way / Big old hearth, what can I say?'),('23.4–25.1','Inserted floor, oh behave!'),('25.8–28.7','Hall house, hall house.'),('28.7–32.8','Front door, back door / Straight through the cross passage.'),('32.8–34.4','Hall house, hall house.'),('34.4–38.1','Nice big frame, plenty of bays / Service end, seen better days.'),('38.1–41.0','Solar upstairs / Very private.'),('41.0–43.9','Hall house, hall house.'),('44.2–46.9','Have you visited a hall house?'),('46.9–48.65','Short audio tail; the audio stream ends at approximately 48.65s.'),('48.65–49.97','Video-only tail; no source audio stream remains.')],
 pronunciation=[('Hall house','HAWL HOWSS','Two strong syllables; hall and house have different vowels. Clearly articulate the H of house.'),('Have you visited a hall house?','hav-yuh VIZ-it-id uh HAWL HOWSS','Quick unstressed lead-in; three syllables in visited, then the two-word hook.'),('Front door, back door','FRUNT DAW, BAK DAW','Four deliberate word attacks.'),("Let's see your cross passage",'lets SEE yuh KROSS PAS-ij','Cross passage has three syllables; avoid swallowing the final ij.'),('Open hall, nice and wide','OH-pun HAWL, NYSS un WYD','Rhyming phrase end on wide.'),('Service end, at the side','SUR-vis END, at thuh SYD','Two syllables in service; side matches wide.'),('Upper end, lower end','UP-uh END, LOH-uh END','Parallel rhythmic cells.'),('Show me where your screens have been','SHOH mee WAIR yuh SKREENZ hav BIN','Screens is one syllable. Bin/been vowel is a broad suggested rendition, not established exact vowel.'),('Smoke-blackened all the way','SMOHK BLAK-und awl thuh WAY','Blackened is two syllables, not “black and”.'),('Big old hearth, what can I say?','BIG ohld HAHth, wot kun eye SAY','Hearth has the heart vowel in the suggested British rendition, not the earth vowel.'),('Inserted floor, oh behave','in-SUR-tid FLAW, oh bih-HAYV','Emphasise the comic oh behave as its own aside.'),('Nice big frame, plenty of bays','NYSS big FRAYM, PLEN-tee uv BAYZ','Keep the frame/bays stresses clear.'),('Service end, seen better days','SUR-vis END, SEEN BET-uh DAYZ','Rhymes days with bays.'),('Solar upstairs, very private','SOH-luh up-STAIRZ, VEH-ree PRY-vit','Solar is the room name, two syllables; private two syllables.')],
 issues=['“Service end, seen better days” is supported by repeated audio recognition and the visible “Seen Better Days” caption; punctuation is editorial.','The audio stream lasts 48.645 seconds although the video lasts 49.967 seconds; the final 1.32 seconds are not missing transcription. A short ASR chunk mishears hall house as whorehouse. The persistent caption and other audio passes establish hall house.'],
 recipe='A recurring two-word refrain interleaved with short rhyming descriptive couplets. Keep the narrative syllabic and brisk; broaden the two strong beats of hall house. Let oh behave and very private become spoken comic asides. Repeat the opening question at the end, rather than adding a conventional new chorus.',
 lyrics='''[Hook]
Hall house, hall house
Have you visited a hall house?
Front door, back door
Let's see your cross passage
Hall house, hall house
[Verse]
Open hall, nice and wide
Service end, at the side
Upper end, lower end
Show me where your screens have been
[Hook]
Hall house, hall house
[Verse]
Smoke-blackened all the way
Big old hearth, what can I say?
Inserted floor
[Spoken aside]
Oh behave!
[Hook]
Hall house, hall house
Front door, back door
Straight through the cross passage
Hall house, hall house
[Verse]
Nice big frame, plenty of bays
Service end, seen better days
Solar upstairs
[Spoken aside]
Very private
[Final hook]
Hall house, hall house
Have you visited a hall house?
[Short ending]'''),
 dict(id='DdZlT3TIx3q',slug='09_door_knockers',title='Door Knockers',duration=37.7,
 transcript=[('0.0–1.8','K.K. Knockers!'),('2.1–4.9','Big knockers, small knockers, long knockers too.'),('4.9–8.6','Funny little knockers staring back at you.'),('8.6–12.1','Brass knockers, iron knockers, some as big as your head.'),('12.1–14.8','On the door, I said.'),('15.8–19.2','Polish your knockers, give them a shine.'),('19.2–22.7','Show me your knockers, I’ll show you mine.'),('22.7–23.6','Knock, knock!'),('24.2–25.2','Who’s there?'),('25.4–26.5','Door furniture.'),('26.5–27.4','Behave!'),('27.4–35.9','Musical tail; no further intelligible words recovered.')],
 pronunciation=[('K.K.','KAY-kay','Two letter names, brisk pickup before Knockers.'),('Knockers','NOK-uhz','Two syllables, first stress; keep the final r non-rhotic for the apparent British-style delivery, though the singer’s accent is not independently established.'),('Big / small / long knockers','BIG / SMAWL / LONG NOK-uhz','Three parallel, strongly accented list items; keep each adjective distinct.'),('Funny little knockers, staring back at you','FUN-ee LIT-ul NOK-uhz, STAIR-ing BAK at YOO','Quick unstressed middle syllables; land on YOU.'),('Brass / iron knockers','BRASS / EYE-urn NOK-uhz','Iron is two syllables in the suggested rendition; separate the paired material names.'),('Some as big as your head, on the door I said','sum uz BIG uz yuh HED, on thuh DAW eye SED','Maintain the head/said rhyme across the phrase break.'),('Polish your knockers, give them a shine','POH-lish yuh NOK-uhz, giv thum uh SHYN','Polish is the verb with first-syllable stress; let shine carry the rhyme.'),('Show me your knockers, I’ll show you mine','SHOH mee yuh NOK-uhz, ayl SHOH yuh MYN','Parallel show me / I’ll show you phrasing; emphasize the final mine.'),('Knock, knock! Who’s there?','NOK NOK! HOOZ thair?','Switch to a short spoken knock-knock exchange.'),('Door furniture. Behave!','DAW FUR-ni-chuh. bih-HAYV!','Dry spoken punchline followed by a sharp admonishing response.')],
 issues=['Whisper large-v3-turbo and the independently run Vosk small English model agree on the long verse and knock-knock exchange despite Vosk substitutions. Sampled on-screen captions directly support K.K., Knockers, Funny Little Knockers, Big Knockers, Small Knockers, Long Knockers, Iron Knockers, Show me your Knockers, Who’s There?, Door Furniture and Behave. Caption OCR is noisy and does not settle every syllable; “On the door, I said” is primarily audio-recognizer evidence.','The opening is captioned “K.K.” followed by “Knockers”; punctuation as “K.K. Knockers!” is editorial.','The video stream lasts 37.7 seconds, but its AAC audio ends at about 35.9 seconds; the final visual tail has no source audio.'],
 recipe='Deliver the main text as a cheeky, briskly rhymed comic verse, with each adjective list snapping to the beat. Keep the K.K. pickup short, make “head / said” and “shine / mine” the phrase-ending rhymes, then break into a spoken knock-knock call and response. Drop the register for “Door furniture” and finish with a separate emphatic “Behave!” before the instrumental tail.',
 lyrics='''[Quick spoken pickup]
K.K. Knockers!
[Bouncy rhythmic verse]
Big knockers, small knockers, long knockers too
Funny little knockers staring back at you
Brass knockers, iron knockers, some as big as your head
On the door, I said
[Rhyming couplet]
Polish your knockers, give them a shine
Show me your knockers, I’ll show you mine
[Spoken knock-knock exchange]
Knock, knock!
Who’s there?
Door furniture
[Spoken punchline]
Behave!
[Instrumental tail]''')
]

ASSET_STEMS = {
    'Dc1uBZahhts': 'flaunching',
    'Dc8axxYIC3k': 'guttae-good-day',
    'DcRZB_PBFkr': 'bargeboard',
    'DcYTYvMBSMn': 'columns-classical-orders',
    'DcbYsWLhhdZ': 'doors',
    'DcqWhZtBIEI': 'windows',
    'DcvxvGDhSeb': 'echinus-entasis',
    'DdLxzBIoJ8F': 'hall-house',
    'DdZlT3TIx3q': 'door-knockers',
}

def asset_stem(source_id):
    """Return the stable, content-based basename for one source-video ID."""
    return ASSET_STEMS.get(source_id, source_id)
