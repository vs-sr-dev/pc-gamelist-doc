# pc-gamelist-doc

**Index of the PC and portable-C game documentation** — one repository per
title. This family has no shared platform checklist: a DOS game from 1987 and a
PhyreEngine remaster from 2018 have almost nothing in common except the machine
they end up on, which is exactly why the index is per platform and not per
engine.

Two strands run through it. The first is format archaeology from the DOS and
early-Windows era — containers, sprite codecs, map formats and the editor work
files that shipped by accident.
The second is modern remasters and PC ports, where the interesting layer is the
older console the build is still pretending to be. A third opened with *Allods
Online*: a **live client of a live service**, delivered over BitTorrent rather
than pressed, which is the first object here that could be checked against a
cryptographic descriptor instead of being taken at its word — and the first
whose byte total changed while it was being measured. No repository here
contains game assets or executables — only measurements and the code to
reproduce them.

## The titles

Listed in the order they were documented. The **Saga** column is filled in where
the title belongs to a series that may one day earn its own index; it is empty
where it does not. Several of them — the *Final Fantasy* rows, and *Mana* — point
at a Square Enix cluster large enough to deserve its own repo, and *FINAL
FANTASY VIII* is the one that says why the column is worth being strict about:
its cell is filled **on the title**, because the two objects it would have to
share bytes with are not on the machine that measured it, and the row says so
rather than letting a series name pass for a measurement.
**HeroQuest** is one of the sagas of two here, and its other half is on a
different machine entirely: *HeroQuest II: Legacy of Sorasil* sits in the CD32 list as
[cd32-heroquest2-doc](https://github.com/vs-sr-dev/cd32-heroquest2-doc). Two
titles across two families is not yet an index of its own.
**Baron Baldric** is another of them, and the mirror image of that
arrangement: both halves are on this machine and in this list, *Baron Baldric:
A Grave Adventure* and its sequel *Mystic Towers*. Its Saga cell was empty
until the sequel arrived, because a saga of one is not a saga; two titles in
one family is a column entry and still not an index of its own. What the two
have in common turns out to be a protagonist, a Borland runtime and three
asset files — different studio, different publisher, different engine, and a
different machine underneath.

Some entries **are not games**, and they are in the list on purpose. *Viaggio
al centro del Mondo* is the data session of an 883 CD Extra: put the disc in a
stereo and it plays an album, put it in a computer and it
opens a Macromedia Director program with a slot machine inside it. The slot
machine is 2.7 % of the data track and the rest is a hypertext menu, nineteen
QuickTime movies and an installer for a 3D avatar chat world. An index that
admits its edge cases is more useful than one that hides them, and the What-it-is
cell of every such row says plainly that it is not a game — because leaving them
out would lose facts like an Italian record label shipping an Activeworlds
client in every copy of an album in 1999.

*Blood & Lace* and *Zero Comico* are the first pair of *games* here to share an
**engine**, and their Saga cells are deliberately **empty**. Both are GMM
Entertainment, both running `japotek3d.dll`, seven months apart — and
they have no characters, setting or fiction in common, which is what the Saga
column is for. The Studio column already carries the link that exists. What
the two discs say about each other is a great deal, and it is said in prose,
in [pc-bloodandlace-doc chapter
11](https://github.com/vs-sr-dev/pc-bloodandlace-doc/blob/master/docs/11-two-discs-one-engine-seven-months.md),
which is the first side-by-side comparison in this family: the engine *lost*
237,568 bytes of code between them, and three claims in the older repository
are corrected by the newer one.

**Two counts, and they do not agree, on purpose.** The table counts titles
reachable from here; the write-ups section counts the ones documented in this
family. A title whose primary index is elsewhere gets a row and no write-up —
*Tales of Berseria*, whose format belongs to
[tales-gamelist-doc](https://github.com/vs-sr-dev/tales-gamelist-doc) rather
than to the platform — and every such crosslink widens the gap by one. Neither
number is written into the prose above, because a count written down is a count
that goes stale: both are re-derived by command when they are wanted. Making
them agree would either claim a write-up that does not exist here, or hide a
title that is on this platform.

**Mega Man** is the saga that shows what the Saga column is actually for. Its
cell was deliberately empty when *Mega Man* (PC/DOS, 1990) was the only half of
it here, with the reason written out: *Mega Man* is an enormous series, this is
a licensed title written from scratch for the PC with
Robot Masters and stages the NES game does not have, and **the column is filled
only when another object in this collection shares bytes with it**. A saga of
one is not a saga and a licence is not a saga either.

The other object arrived later. *Mega Man 3: The Robots are Revolting*
(PC/DOS, 1992) is the same studio, the same programmer and the same platform
twenty-one months later, and the two programs share **1,855 bytes** in runs of
32 or more — 98 of them the options display list, 32 of them both palette
tables, the rest EGA blitter code — measured with the threshold named before the
comparison was run. So both cells are filled now, on that measurement and on
nothing else. **There is still no PC *Mega Man 2*:** the first DOS game is
called *Mega Man* and the second is called *Mega Man 3*.

*Grande Fratello Il Gioco* is a further Italian disc and is **not** a third
member of that pair: different studio, different city, two years later, and —
measured file by file by content hash — **not one byte in common** with either
of them. The only thing it shares with them is somebody else's: `fmod.dll`, in
two different versions. Discs from one country are not a national school, and
the comparison chapter says so; what it does
say is that the differences are almost all differences of *year* rather than
of place, and that the third disc, by arriving with its subchannel, was able
to correct the other two rather than merely be compared with them.

*Lucignolo Il Videogioco* is the Italian disc that could first be set against a
genuine like-for-like — two tie-ins to Mediaset television programmes, four
years apart. It closes the question rather than extending it: **not one file on
it is byte-identical to any file on *Zero Comico*, *Blood & Lace* or *Grande
Fratello*, and the set of filenames common to the four is empty.** `fmod.dll`,
the one thing the first three shared, does not survive; this game uses Audiere.
Four discs and three studios are no more a national school than three were, and
the useful result is the negative one: the only crossing anywhere in the four is
between the two discs that share a studio.

**The Saga column's rule was rewritten when the second Resident Evil arrived,
and the reason is measured rather than editorial.** The rule until then, as
*Mega Man* established it and CLIC 02/97 refined it, was **shared bytes**: a cell
fills when another object in this collection shares bytes with this one, a saga
of one is not a saga, and a licence is not a saga. That rule was invented before
the index held a genuine pair of one series, and the first genuine pair broke it.
*Resident Evil* (1997) and *Resident Evil 2* (1999) — same studio, same
publisher, same engine, two years apart — share **12 files and 352,267 bytes**,
and every one of the twelve is a Microsoft DirectX driver or licence. The same
discs share **221 files and 10,537,993 bytes** with *FINAL FANTASY VIII*. By
shared bytes, Resident Evil 2 is **thirty times** more closely related to a
Squaresoft role-playing game than to its own predecessor, and all 222 of its
crossings are Microsoft's. A rule whose honest output is *Resident Evil 2 belongs
to the Final Fantasy saga* is measuring the wrong thing.

So the column now reads: **a Saga cell names the video-game series the title
belongs to, and is filled once a second member of that series has been measured
in this collection.** The second half is the old *Mega Man* criterion, unchanged
— a saga of one is still not a saga, and no cell fills from outside knowledge of
what exists in the world. What is dropped is the byte criterion, which keeps the
job it does well: it is the **crossings** measurement, and "222 files, 10,539,308
bytes, all of them Microsoft's" is exactly the right sentence for it. Kinship
between two releases of one codebase is measurable too, and it was measured: the
two Resident Evils share seven structural traits — the PlayStation TIM
identifier, the `.RDT`/`.EMD`/`.ESP` extensions, one `CORE00.ESP` each in the
engine's data directory, the `RC####` background naming scheme, no version
resource on any of the studio's binaries, and a nine-hour Tokyo offset on the
studio's build stamps — and Final Fantasy VIII shares **none** of the seven. The
argument is in [pc-residentevil2-doc chapter 13](https://github.com/vs-sr-dev/pc-residentevil2-doc/blob/master/docs/13-the-crossings-and-the-saga.md).
Both Resident Evil cells were filled in the commit that added the second one;
*Mega Man*'s two and *Harry Potter*'s three already satisfied the new rule under
the old one.

*Tesla Effect: A Tex Murphy Adventure* is the largest object in this family, and
arrived four orders of magnitude above the one measured before it — 17.5
gigabytes against 392,593 bytes. **Its Saga cell is empty, and the reason is
the rule and not an oversight.** It is the sixth and last *Tex Murphy*, of six
that began in 1989; the column is famous-title-proof and fills only once a second
member of the series has been measured here, and today there is no other *Tex
Murphy* here. The one thing this object contains that points at its own series is
a video file called `meanstreets_newspaperarticle.bk2`, naming the 1989 game the
series began with — and **a reference is not a shared byte.** When the rest of
the series is measured, the cell fills itself, on a measurement, exactly as
*Mega Man*'s did after a session of standing empty.

*Deadly Premonition: The Director's Cut* is the second cell to be left empty
under the rewritten rule, and it is a harder test than Tesla Effect's, because
this object **names its own franchise in its own bytes**: `DP.exe` carries the
string `Deadly Premonition: The Director's Cut - ACCESS GAMES INC. All Rights
Reserved.`, and its archive carries a project code name, `mmv01`, that a sequel
might well share. There is a sequel — *Deadly Premonition 2: A Blessing in
Disguise*, 2020 — and it is not in this collection, so **the cell is empty**. A
name in a string is not a second member, and the rule fills on a measurement or
not at all. Twice now it has said yes, for the two Resident Evils, and twice no.

It is also the first entry here whose subject is a **live installation on
somebody's disk** rather than a disc, an image or a folder of files, and the
first with personal data in it. Two fields of its Steam manifest belong to the
person who owns the copy and are redacted in the repository; the game's own
runtime log, written on that machine, is neither copied nor quoted. The
distinction the document draws is worth carrying: a name found *in the object* —
`masonj`, `courtneyj`, `steve w` — is a measurement, and a name belonging to the
person who installed it is not.

*The Legend of Heroes: Trails in the Sky* is the **third** cell left empty under
the rewritten rule, and it is the hardest of the three, because this object does
not merely name its series — it is **numbered** by it. `ED6` is the prefix on
every file Nihon Falcom wrote here, `dll\copyrights.txt` opens with
`Legend of Heroes VI: SORA NO KISEKI`, and the version resource of `ed6_win.exe`
reads `日本ファルコム 英雄伝説 空の軌跡`. The object says *six* four different
ways, and *Eiyuu Densetsu* runs to more than a dozen entries with an internal
trilogy beginning at this one. **No second member of that series has been
measured in this collection, so the cell is empty.** A number in the title is not
a second member measured, and the rule fills on a measurement or not at all.
Three times now it has said no.


| Title | Year | Studio | Saga | What it is |
|---|---|---|---|---|
| [**Prince of Qin**](https://github.com/vs-sr-dev/pc-princeofqin-doc) | 2002 | Object Software |  | The Chinese action RPG and Object Software's "EasyRPG" engine |
| [**Meridian 59**](https://github.com/vs-sr-dev/pc-meridian59-doc) | 1996 | Archetype Interactive |  | One of the first graphical MMORPGs, and 30 years of operational strata |
| [**Forgotten Realms: Dungeon Hack**](https://github.com/vs-sr-dev/pc-dungeonhack-doc) | 1993 | DreamForge / SSI | Forgotten Realms | The AESOP/16 engine |
| [**Wacky Wheels**](https://github.com/vs-sr-dev/pc-wackywheels-doc) | 1994 | Apogee |  | Its fixed-point pseudo-3D floor renderer |
| [**Battle Bugs**](https://github.com/vs-sr-dev/pc-battlebugs-doc) | 1994 | Sierra / Epyx |  | 800x600 in 16 planar colours, one asset set serving both modes, and a per-bitplane column-major image codec |
| [**Corridor 7: Alien Invasion**](https://github.com/vs-sr-dev/pc-corridor7-doc) | 1994 | Capstone / IntraCorp |  | A licensed Wolfenstein 3-D taken to 256 colours, shipping its levels in TED5's editor work file |
| [**H.U.R.L. / Slob Zone 3D**](https://github.com/vs-sr-dev/pc-hurl-doc) | 1995 | Deep River Publishing |  | Lary Myers' ACK-3D, with levels shipped as commented ASCII naming 661 of the game's 684 bitmaps |
| [**Might & Magic: Secret of the Inner Sanctum**](https://github.com/vs-sr-dev/pc-mm-doc) | 1987 | New World Computing | Might & Magic | The first of the series |
| [**Sargon V: World Class Chess**](https://github.com/vs-sr-dev/pc-sargon5-doc) | 1991 | Mediagenic | Sargon | Five files with four different extensions turn out to be one container, whose LZW packs least-significant bit first |
| [**Nitemare-3D: A House of Horrors**](https://github.com/vs-sr-dev/pc-nitemare3d-doc) | 1994 | David P. Gray |  | A one-man 256-colour shooter that owes nothing to Wolfenstein: every format is Gray's own and none of it is compressed |
| [**GRANDIA HD Remaster**](https://github.com/vs-sr-dev/pc-grandiahd-doc) | 2019 | GungHo | Grandia | The PSX GPU/SPU/CD libraries reimplemented on D3D11/XAudio2 |
| [**Secret of Mana (PC remake)**](https://github.com/vs-sr-dev/pc-secretofmana-doc) | 2018 | Square Enix | Mana | A PhyreEngine title |
| [**FINAL FANTASY V (PC)**](https://github.com/vs-sr-dev/pc-ff5-doc) | 2015 | Square Enix | Final Fantasy | The mobile-port fingerprints in the build |
| [**FINAL FANTASY TYPE-0 HD**](https://github.com/vs-sr-dev/pc-fftype0-doc) | 2015 | Square Enix / HexaDrive | Final Fantasy | PSP heritage and the HexaDrive render layer |
| [**Infinite Undiscovery**](https://github.com/vs-sr-dev/pc-infiniteundiscovery) | 2008 | tri-Ace |  | The ASKA engine, which turns up again twelve years later under *Tales of Crestoria* |
| [**Tales of Berseria**](https://github.com/vs-sr-dev/pc-talesofberseria-doc) | 2017 | Bandai Namco Studios | Tales | Container format and obfuscation. **Crosslink** — its primary index is [tales-gamelist-doc](https://github.com/vs-sr-dev/tales-gamelist-doc), because the format is the saga's, not the platform's |
| [**HeroQuest**](https://github.com/vs-sr-dev/pc-heroquest-doc) | 1991–92 | Gremlin Graphics | HeroQuest | The board game on three floppies: the whole 26 × 19 board rebuilt from twenty-four quest files, accents remapped onto the lower-case ASCII row, and one 1980 timestamp in eighty-four files |
| [**Baron Baldric: A Grave Adventure**](https://github.com/vs-sr-dev/pc-baronbaldric-doc) | 1992–93 | CTV-Link / Manaccom | Baron Baldric | A house container with no directory at all, the Turbo Pascal linker map that shipped inside it by accident, and thirteen timestamps forty-eight years in the future |
| [**Mystic Towers**](https://github.com/vs-sr-dev/pc-mystictowers-doc) | 1994 | Animation FX / Apogee | Baron Baldric | The Baldric sequel, and an Amiga game underneath: AMOS memory and sprite banks shipped whole inside the DOS container, ten of them source art the game cannot display |
| [**Zero Comico**](https://github.com/vs-sr-dev/pc-zerocomico-doc) | 2001 | GMM Entertainment / Medusa Games |  | An Italian TV tie-in that is 69.49 % Indeo video for thirteen minutes of it, two in-house containers wrapping a 1989 LZHUF stream, and an engine still carrying the cancelled game it was written for |
| [**Blood & Lace**](https://github.com/vs-sr-dev/pc-bloodandlace-doc) | 2001 | GMM Entertainment |  | The game that engine was built for, seven months earlier: a signed licence notice from its author inside `japotek3d.dll`, and 237,568 bytes of code the later disc no longer has |
| [**Grande Fratello Il Gioco**](https://github.com/vs-sr-dev/pc-grandefratello-doc) | 2003 | Trecision |  | The official Big Brother tie-in, and the first disc here dumped with its subchannel: 43 wrong bits in 12 MB of Q prove the read, and 2,934 files come out of one cabinet |
| [**Lucignolo Il Videogioco**](https://github.com/vs-sr-dev/pc-lucignolo-doc) | 2007–08 | 7Th Sense s.r.l. |  | An eight-file DVD of which one file is 96.79 %, whose copy protection is a six-byte file containing the word `codice`, and whose sector padding echoes the data 65,536 bytes earlier |
| [**Viaggio al centro del Mondo** (883 CD Extra)](https://github.com/vs-sr-dev/pc-883d-doc) | 1999 | Moltimedia |  | **Not a game** — the multimedia session of a music CD Extra: a slot-machine minigame that is 2.7 % of the data track, and an installer for an Activeworlds chat world |
| [**1000 Miglia**](https://github.com/vs-sr-dev/pc-1000miglia-doc) | 1991–92 | Simulmondo — *the material itself names no studio (`Simulmondo` occurs 0 times in 1,588,227 bytes), and that remains true of this folder. The attribution is no longer external to the collection: the **Simulman V** row below measures a second Simulmondo object that names the company in full, and the two share one byte-identical executable* | | The Brescia–Rome–Brescia road race, whose sixteen route filenames are a graph — one closed circuit through fifteen towns with Bologna visited twice — and 37.93 % of it is unreadable PowerPacker |
| [**Harry Potter and the Philosopher's Stone**](https://github.com/vs-sr-dev/pc-harrypotter1-doc) | 2001 | KnowWonder / Electronic Arts *(the game's own credits name no studio, only "PC Team"; `KnowWonder` appears once in 540 files, as a Windows domain inside a developer's path, and on the printed case)* | Harry Potter | The first object here measured from the disc itself: a table hidden in the 344 bytes ISO 9660 requires to be zero, naming both edges of a 9,280-sector unreadable region a binary search cannot find |
| [**Harry Potter and the Goblet of Fire**](https://github.com/vs-sr-dev/pc-harrypotter4-doc) | 2005 | Electronic Arts *(publisher; the disc names no development studio at all — it names RenderWare, RealCore 6.27.01, RealGraph 6 and Havok, and one Perforce path, `d:\P4\Eauk\HPGoF\`)* | Harry Potter | A DVD that is 93.98 % one file, and whose 126 unallocated gaps are not gaps: they hold a complete second filesystem, UDF File Entries agreeing with ISO 9660 on all 1,659 files |
| [**Harry Potter and the Order of the Phoenix**](https://github.com/vs-sr-dev/pc-harrypotter5-doc) | 2007 | Electronic Arts *(publisher; the disc names no development studio as a company, but `hp.exe`'s Authenticode certificate reads `O=Electronic Arts, OU=UK Studio, L=Guildford, ST=Surrey, C=GB` and eleven source paths sit under `z:\phoenix\code`)* | Harry Potter | A pressed DVD assembled with a desktop ISO editor, whose primary namespace is not ISO 9660 — zero `;1` version suffixes and 1,185 lower-case names, which is exactly why it carries no Joliet |
| [**Age of Wonders II: The Wizard's Throne**](https://github.com/vs-sr-dev/pc-ageofwonders2-doc) | 2002 | Triumph Studios *(the disc names it in `AoW2.~ex`'s version resource and four times in a plaintext credits block; the publisher, Gathering of Developers, holds the copyright in the English readme)* |  | The first disc here whose unallocated space is the subject: 23.91 % of it belongs to no file, and 143,595,520 bytes of that are reproduced from two integers |
| [**Il cane di terracotta**](https://github.com/vs-sr-dev/pc-canediterracotta-doc) | 2000 | IM*MEDIA (software), Sellerio (publisher) |  | **Not a game** — an interactive cartoon from Camilleri's novel, and the first hybrid here: 2,374 files on the Windows side, 2,401 on the HFS one, and 2,372 of the shared 2,373 begin on the same sector |
| [**CLIC 11**](https://github.com/vs-sr-dev/pc-clic11-doc) | 1997 | CLIC *(the magazine; the disc names its own maker in the volume identifier `CLIC_11` and in no other field — `publisher`, `data preparer` and `copyright file` are empty on both descriptors, and `Clic95.exe`'s `CompanyName` reads `Macromedia, Inc.`, which is the engine's vendor and not the disc's)* |  | **Not a game, and not a work** — the CD bound into an Italian magazine: eleven separately-assembled bodies of software spanning 1,636 days, of which the magazine itself made 3.37 % |
| [**Tubular Worlds**](https://github.com/vs-sr-dev/pc-tubularworlds-doc) | 1993–94 *(the file mtimes, 1993-10-11 to 1994-05-31; there is no descriptor here to separate the date of the product from the date of this copy, and the last file is a player's high score)* | *(none — the object names **nineteen people** in `PART2.EXE`'s credits and no organisation anywhere; the only copyright string in 3,432,758 bytes is Clarion Software's, and it belongs to the compiler of an 8 KB DOS version check)* |  | The first object here that is not a medium — a downloaded folder of 107 files, no volume descriptor and no lead-out — whose whole game is drawn from a 64-byte 8×8 tile recovered from arithmetic |
| [**Mega Man**](https://github.com/vs-sr-dev/pc-megaman-doc) | 1990 *(28 of the 29 files carry mtimes from 1990-09-30 to 1990-11-29 and the executable is the last of them; the 29th is a BBS descriptor written 2011-01-22. As with the other loose-file object in this list there is no descriptor, no version field and nothing to separate the date of the product from the date of this copy — except that here the executable's own filename table names every data file the folder holds)* | *(none as a company — the object credits a **person**: `CREDITS.STA`, rendered, gives **design, graphics, programming and sound to Stephen Rozner** and the concept to **Capcom**, and `LOGO.STA` carries `© 1990 CAPCOM CO.,LTD.` — all of it drawn as pixels, none of it as text. The publisher, **Hi-Tech Expressions, Inc.**, is named by exactly one file, the `file_id.diz` added in 2011, and by nothing in the 28 files of 1990)* | Mega Man | Not the NES game but a licensed DOS original, whose executable holds under a third of its code: the other 71 % lives in five per-stage 8086 modules that far-return to it |
| [**Mega Man 3: The Robots are Revolting**](https://github.com/vs-sr-dev/pc-megaman3-doc) | 1992 *(64 of the 64 files carry DOS mtimes from 1992-07-18 to 1992-08-02, and this is the first object in this list whose year is also **drawn into it**: `LOGO.STA`, rendered, carries `© 1992 CAPCOM CO.,LTD.` and `™ and © 1992 CAPCOM, USA, INC.`. The container disagrees and says **2008-06-23**, which is the date of the archiving and of nothing else — one ZIP record in 65)* | **Rozner Labs**, and for once the object says so — but in pixels, not in text: `ROZLABS.STA` renders as a circuit board reading `A` / `ROZNER` / `LABS` (spelled on four seven-segment displays) / `PRODUCTION`, `HITECHLO.STA` renders as the **Hi Tech Expressions** logo over the word `PRESENTS`, and `CREDITS.STA` gives **design, programming and sound to Stephen Rozner** and **graphics to William Rozner**, with the concept to **Capcom**. None of those six words exists as ASCII anywhere in the 55,456 bytes of unpacked executable | Mega Man | The second Mega Man on PC is called the third, because there was never a second: one twelve-bit LZW codec for all four families, and 1,855 bytes shared with its sibling |
| [**Tesla Effect: A Tex Murphy Adventure**](https://github.com/vs-sr-dev/pc-teslaeffect-doc) | 2014 *(and the first object in this list whose **filesystem dates nothing**: Steam rewrote all 4,769 mtimes into one six-minute window on the day this copy was downloaded, so the year comes only from inside file contents — the five script workbooks were created 2013-11-20T17:42:33Z and last saved between 2014-04-14 and 2014-05-09, and the studio's own code carries a linker stamp of **2014-06-11T21:55:36Z**. The `.exe` is stamped 2014-01-08 and dates the **engine**, not the game)* | **`BigFinishGames`**, and the object says so in exactly two places, neither of them a credit: as Unity's `companyName` in `mainData`, and inside `/Documents/BigFinishGames/TeslaEffect/` in the assembly — **the only place in 17.5 GB where the studio names itself in text is the path your saved games go to**. `TeslaEffect.exe`'s version resource has no `CompanyName`, no `ProductName` and no copyright; `Assembly-CSharp.dll` has every field present and every one **empty**; and the only binary here that names its maker is **RAD Game Tools**, in the video codec. The credits are `MainCredits.bk2`, 271.1 seconds, and a document that counts bytes cannot read them |  | Fourteen and a half gigabytes of video with a program around it: 82.93 % of the bytes are 1,035 Bink 2 films, 5 h 33 m of running time summed from headers with zero frames decoded |
| [**Lands of Lore: The Throne of Chaos**](https://github.com/vs-sr-dev/pc-landsoflore-doc) | 1993/94 *(and the messiest this column has been, because the object carries **four dates and three of them are not the product's**. The game is 1993; this is the **CD revision**, and the disc names its own version in the one field built for it — `volume_id` = `LOL_V102`. Its 209 directory records date 1992-06-11 to 1994-08-16 — 1 file from 1992, 51 from 1993, 157 from 1994 — and the `DATA` directory record, which dates the mastering rather than the content, says **1994-10-14**. The ISO primary volume descriptor says **2011-09-13T11:39:37**, seventeen years late, and it is the only descriptor in this list with a field designed to date a product and a wrong value in it. Two storefront icons say 2017 and a web cache says 2019. And 62 of the 65 filesystem mtimes say the day this copy was installed, inside a **ten-second window**)* | **Westwood Studios**, and for the first time in this collection the object states its maker **in a field built for the purpose**: `publisher_id` of the volume descriptor reads `WESTWOOD STUDIOS`, with `preparer_id` naming the mastering software, `EASY-CD PRO INCAT SYSTEMS INC.`. It repeats it in `SETUP.EXE` (`Westwood Studios -- Lands of Lore`) and 38 times in `INSTALL.EXE` — and **zero times in `MAIN.EXE`**, the game itself. The only third-party copyright anywhere in the game layer is `Copyright (C) 1991,1992 Miles Design, Inc.`, in six `.ADV` sound drivers: as in 2014, the vendor whose name survives inside a shipped binary is the audio middleware. The credits are a member of an archive inside a disc image, and they name a different product coordinator in German than in English and French |  | A CD-ROM inside a file, an emulator that has never heard of it, and a shop wrapper around both: 94.17 % of the object is one ISO 9660 image, and 77.8 % of it is recorded speech |
| [**FINAL FANTASY VIII (PC)**](https://github.com/vs-sr-dev/pc-finalfantasy8-doc) | 1999-2000 *(and the column has to say which 1999: the game is a 1999 PlayStation title and **this is the port**, so the console's year is not this object's. The object dates itself, and for once the filesystem is alive rather than rewritten by an installer — 1997: 15 files, 1998: 1,363, 1999: 123, 2000: 31. The four movie archives are **1999-11-15, 11-16, 11-23 and 12-15**, one a week and out of order; the four two-byte disc markers are all **1999-11-17**; the `FIELD` triptychs of discs 1, 2 and 4 are **1999-12-21**; Eidos's launcher is **2000-01-05**; and then **2000-01-14** is four things at once — disc 3's `FIELD` triptych, every file of the InstallShield package, `FF8.exe`'s linker stamp at 20:48:19Z, and the two extra bytes that make disc 3's archive incompatible with disc 4's index. The readme is **2000-01-17**, the French disc's volume descriptor **2000-01-18**, and DirectX is **1998**)* | **Square**, and the object says so exactly **once**: `Software\Square Soft, Inc\Final Fantasy VIII\1.00`, a registry key, four times inside `FF8.exe` and once in the installer's index. Every field built to describe the *product* names the publisher instead — the disc's `publisher_id` is `Eidos Interactive`, so is `DATA.TAG`, so is `SETUP.INI` — and **`Eidos` appears zero times in the game's own executable**. It is the mirror of *Lands of Lore*, where the studio was in the descriptor and absent from `MAIN.EXE`. By bytes the split is not close: **Square 97.999 %, Eidos 0.045 %** — 1,373,299 bytes, being an autorun launcher, a bitmap, a readme and a 29-byte `AUTORUN.INF`. `preparer_id` on the French disc holds a common English personal name and `application_id` holds `BURNER 4`: the disc names its mastering tools twice and its author never | Final Fantasy *(filled **on the title**, and this row says so. The rule in this index is shared bytes, `crossmatch.py` is the tool for it, and **the comparison was not run**: neither `pc-ff5-doc` nor `pc-fftype0-doc` has its object on the machine this was measured on, so there was nothing to compare. Declared, not measured.* **It has been measured now.** *The session that added* Final Fantasy XI *ran it, in both directions and at two levels. `crossall.py` over 64 repositories: **2 crossings of that object's 61,184 file hashes**, one of them Microsoft's `MSVCR71.dll` and the other a four-byte file, and **neither of them this one**. Then `datmembers.py` hashed **1,718,526 chunks** of its `.DAT` so the question could be asked at member level, and `crossall.py` over those returned **0 crossings of 739,235 distinct members** — against every hash list in the collection, this object's 91,584 container leaves included. **Two Square PC games two years apart share a trademark, a publisher and one compiler version, and not one byte of content.** The Broken Sword rows in this table record 291 member crossings between 2003 and 2006; this pair records none. The cell stays filled, on the title, and is no longer an untested assertion)* | A game that is still a PlayStation, measured until the seams show: the console's own 3×3 fixed-point matrix on each of 51,750 frame records, and 31,737 absolute build paths |
| [**Plundered Hearts**](https://github.com/vs-sr-dev/pc-plunderedhearts-doc) | 1987 *(and for the first time in this column the year does **not** come from an mtime. Four of the five files say `1996-06-21T23:41:02Z` and the fifth says `2001-02-20T21:05:48Z`; **no filesystem clock in this object comes within eight and a half years of the product**. The year comes from the `serial` field at offset `0x12` of the story file's header — `870730`, six ASCII digits between two binary addresses, **30 July 1987** — and it is the only 1987 anywhere in the object, since a search for the string `1987` across all five files returns zero. The 1996 stamp is a repackaging that left no other trace, and the 2001 one is a 61-byte batch file somebody wrote to make the game run. A third event has no date at all: the story file carries a trailing `0x1A`, the DOS end-of-file marker, so at some point between 1987 and 1996 a binary went through a program that thought it was reading text)* | **the object never names it in ASCII.** `infocom` returns **0** across all 146,252 bytes, and so do `1987`, `plundered` and `briggs`. **Decoded, it is there four times**: three inline literals in the story file's compressed text read `Infocom interactive fiction` / `Copyright (c) 1987 by Infocom, Inc. All rights reserved.` / ` is a trademark of Infocom, Inc.` — 110 bytes, at `0x0793D`, `0x07982` and `0x079A4`, in five-bit characters no `grep` can see. **The author is named nowhere**, encoded or not: zero on the raw bytes and zero over 110,992 characters of decoded text. The interpreter calls itself only `IBM/MS-DOS 2.0 Interpreter Version N` and never says whose it is, so the layer table marks that row **inferred**. The only humans named as plain bytes anywhere in the object are **Tom Almy and Daniel Kegel**, and they wrote a shareware console driver that has nothing to do with the game |   | The smallest object in this collection, and the first that can be understood entirely: five files, 146,252 bytes, a Z-machine version 3 program and the 12,004-byte machine that runs it |
| [**Leather Goddesses of Phobos**](https://github.com/vs-sr-dev/pc-leathergoddessesofphobos-doc) | 1986 *(second row running whose year is not a clock, and the first time two adjacent rows are dated the same way. All **fourteen** files carry one identical mtime, `1996-12-24T22:32:00Z`, to the second — which is one copy operation recorded fourteen times, not fourteen observations, and the arithmetic matters because it is the third data point for the branch's FAT even-seconds question. The year comes from the `serial` field of the story file's header: `860730`, **30 July 1986** — the same day and month as the row above it and exactly one year earlier. The `release` field runs the other way, **59 here against 26 there**, which settles what it counts: not time and not titles, but revisions of one story file, so `(release, serial)` is a version and neither half is one alone. And the trailing `0x1A` is here too, one byte past a declared length, outside a checksum that still matches — **two out of two makes that a fact about how these copies were made and not about Infocom**, which is the first time this branch could tell those apart)* | **Infocom, and for the first time in plain ASCII.** The previous Infocom object returned **0** for a case-insensitive `infocom` across all five of its files and hid the name in five-bit characters no `grep` could see. Here the same search returns **8** — twice in `read.me`, twice in `readme.1st`, four times as `INFOCOM` in the installer's screen text and its `\INFOCOM` directory. **The difference is not about Infocom, it is about which files survived**: both objects hide the name in the story file and neither interpreter ever says whose it is, but this copy also kept a readme, an installer and a note from a stranger, and those are made of plain text by nature. Decoded, the story file says `Infocom interactive fiction -- a racy space-age spoof` and `Copyright (c) 1986 by Infocom, Inc. All rights reserved.` The author is named nowhere. The interpreter still calls itself only `IBM/MS-DOS 2.0 Interpreter Version N`, so that layer row is still marked **inferred** — though the inference now has a second leg, because the same 11,984 bytes load two different Infocom titles |   | The second Infocom object, and the first comparison this list could make on bytes: the two interpreters are 99.83 % identical and differ in twenty bytes, every one inside a filename |
| [**Sam & Max Hit the Road**](https://github.com/vs-sr-dev/pc-samandmaxhittheroad-doc) | 1993 *(the game, from `Copyright 1993 LucasArts Entertainment Company` in the menu program and from the 1993 mtimes of the bundled demo — and the first row in this column where the product's own version string and the filesystem clock **agree**. A script chunk inside the container reads `Sam & Max Hit the Road, Versione CD1.0, 05-01-95`, in Italian day-month-year, and the file holding it is stamped `1995-01-05T22:51:56Z`. Three dates, all true of different things: **1993** the game, **1994-06-29** the engine build, **1995-01-05** this edition's data — written that evening in a session whose two halves are 3 h 52 m 26 s apart, the speech file first and the container it is indexed from second, which is the order the data requires because the scripts point into the speech by absolute byte offset. The *Final Fantasy VIII* row asked exactly this question and answered it the same way: the year is the game's, the build is argued in this cell)* | **LucasArts** (engine, game and demo), **C.T.O. S.p.A.** (this edition) *(and the split is not the usual developer/publisher courtesy — it is measured. Twelve of the sixty-four files carry an Italian sentence and the distributor's two `README.TXT` are only two of them: so do the game container, the menu's resource archive, the boot-disk maker, three Sound Blaster drivers, the audio-setup layout file, and `REBEL.EXE`, the executable of a demo of **a different game**, whose sound-card configuration screens were translated. The object names nobody else: no translator, no dubbing studio, no voice actor. `README.TXT` closes with a street address, a support telephone number with opening hours and a fax, and **none of the three is transcribed in that repository, `notes/` included**)* |   | 227 MB of which 88.11 % is a human voice — a full Italian dub, 31 % of it unsubtitled — and a SCUMM container read from scratch without opening the famous free implementation |
| [**Allods Online**](https://github.com/vs-sr-dev/pc-allodsonline-doc) | 2009 *(the year the game shipped in Russia — and the first row in this column where **five candidate dates** had to be argued against each other, with the filesystem eliminated first. There are 281 distinct mtimes on **four days**, 254 of them the day of the download, and the oldest byte-timestamp in seventeen gigabytes belongs to a **Microsoft DLL** inside the launcher's browser. The *Tesla Effect* row said its filesystem dated nothing because Steam had rewritten every mtime into one window; this one is the same finding from the other side — the clock dates the **download**, 2026-09-01 07:59:58 to 08:06:25 UTC, 387 seconds for 17 GB. Inside the archives, **99.0590 % of 355,159 entries declare `2009-10-02 00:00:20`** and there are only **five distinct timestamps in the whole population** — it is a build constant, not a date, and the proof is `Bin/pack.loc`, stamped 2009 and containing the strings `2020 - "Русь" (Russia)` and `2023 (subscription servers) — Золотая Орда (RU)`. The real build event survives in **exactly two entries of 355,159**: `Version/DataPacksInfo.bin` and `Version/GameCenterInfo.bin`, `2026-08-13 17:48:28` and `:26`, two seconds apart, with the two `AOgame.exe` linked four hours earlier the same afternoon and the torrent cut twenty-seven minutes later. So: **2009** the game, **2026-08-13** this build, **2026-09-01** this copy — and the cell takes the game's year, as the *Final Fantasy VIII* row did and for the same reason. The *Meridian 59* row's thirty years of operational layers is the nearest precedent here and it is a live service too)* | **Astrum Nival / Mail.Ru, today MY.GAMES** *(and the object was asked before the cell was filled, as the *Plundered Hearts* row asks rather than assumes. Outside the archives, `MY.GAMES` occurs **1,624 times in 26 files** and `Nival` **16 times in 5** — a hundred to one for the operator over the developer. The full lineage is legible in four `CompanyName` fields in one directory: **Nival Interactive** on the modding tools, **Nival Online** on `protect.dll` **5.70.009.0** whose product string still reads `Allods Online (for ALLODS_2 test)`, **ASTRUM LAB LLC** on `protect.dll` **6.02.2605.072** called `Allods Online New`, and **MY.GAMES B.V.** on nine images of `MY.GAMES Anti-Cheat 4.48.0`. Two generations of the same protection module ship at once. And the two files that matter most — `bin/AOgame.exe` and `bin_x64/AOgame.exe` — **declare no company at all**: 54 of the object's 108 PE images are anonymous, including the game)* |   | The first object here that could be *verified* rather than believed: 17 GB fetched over BitTorrent, 8,666 SHA-1 pieces and 871 manifest hashes checked, zero failures |
| [**CLIC 02/97**](https://github.com/vs-sr-dev/pc-clic0297-doc) | 1997, to the second — the primary volume descriptor says `1997-02-14 18:54:32.00 GMT+0` and writes it twice, identically. *(Which **issue** it is, is the harder half, and this is the first row where the object contradicts its own catalogue: the volume identifier is `CLIC`, with no number and no date, unlike CLIC 11's `CLIC_11`; the only directory naming an issue is `NUMERI/CLIC297/`, February 1997; and `/LEGGIMI.TXT` at the root opens **«Clic! Cd-rom di Marzo»** and then says it contains the February website. It is the **March** disc carrying **February** content, and it advertises an April trade fair. Called **02/97** here after the directory, and after this collection's habit of sorting on what the filesystem says, with the readme's disagreement recorded rather than resolved. The back-issue archive it carries is coded **4, 6, 7, 9, 10, 11, 12** and then `197`, `297` — and those codes are **months, not positions in a sequence**: the magazine cites its own back issues only by month name, five times (*«numero di ottobre»*, *«di maggio»*, *«di giugno»*…), `PAG/12CO003.HTM` names the October issue as a back number, and `PAG/11CO005.HTM` previews a release *«Il 15 novembre»* in the future tense. So 4–12 are April to December 1996 and the year was appended only when 1996 ran out. **There is no running issue count for `CLIC_11` to be the eleventh of**, which dates the other object in this index: a disc cut on 1997-10-20 is the **November 1997** issue, as this one cut on 14 February is the March one)* | **CLIC!**, published by **Mondadori Informatica S.p.A.**, CD-ROM produced by **GLAMM Interactive s.r.l.** of Milan — and the three are named in inverse proportion to what they made. `/CREDITS.HTM` is a published colophon crediting thirteen people, and **both names under *Produzione CD-ROM*** are GLAMM's. Counted as literal byte strings across all 2,818 files, the magazine names itself **1,649 times** (`Clic!` 1,104 + `CLIC` 545) and contributed **0.82 %** of the bytes; **Mondadori** appears 86 times; **Leader**, whose catalogue is 72.4342 % of the disc, appears **69**; **GLAMM**, who built the object, appears **fourteen**. Exactly one binary on the disc carries a `CompanyName` of `GLAMM Interactive` — `SETUPIE.EXE`, 16,896 bytes, PE32, COFF-stamped 1997-02-12 14:16:04 — and it is what `AUTORUN.INF` runs | CLIC — **and this is the first Saga cell in this index to fill on measured *process* rather than on shared payload, which is a change to how the rule is applied and is argued out in [chapter 14](https://github.com/vs-sr-dev/pc-clic0297-doc/blob/master/docs/14-against-clic11.md) rather than assumed.** The two CLIC discs share **1,792,592 bytes and none of it is theirs**: `QTINSTAL.EXE` (Apple) and `VBRUN300.DLL` (Microsoft), plus a third matching hash that is two empty files and is not a crossing. **Zero bytes of either magazine's own work appears on both.** Filling the cell on a QuickTime installer would put every hybrid in this collection in a saga with every other, so the rule's implicit clause is made explicit — *shared bytes must belong to the objects, not to a third party both licensed* — and by that reading the payload measurement is **zero**. What fills the cell instead is five independent fingerprints of one production line: the same mastering program in two versions (`TOAST … 1993-1995 MILES SOFTWARE ENGINEERING` / `TOAST 2.5 Partition` here against `TOAST … 1997 ADAPTEC` / `Toast 3.5.2 PPC HFS Optimizer` there), the same ISO+HFS hybrid with an Apple partition map at block 0, the same empty implementor fields, **99.0622 % even seconds against 99.11 %**, and **two unowned sectors, both zero**, on two discs of different sizes mastered by different versions of one program | **Not a game** — a magazine's cover disc whose ownership map is walked from two catalogues at once, because 96.79 % of a hybrid is owned twice; its padding is 16.5 MB of uncleared memory |
| [**Il Mio Computer 02/2006**](https://github.com/vs-sr-dev/pc-ilmiocomputer0206-doc) | 2006, and for once the argument is short because **the packaging prints it**: `FEBBRAIO 2006` screen-printed on the disc face and repeated on the sleeve, against a primary volume descriptor reading `2006-01-04 16:46:00 GMT+01:00` — a February number cut on 4 January, the same relationship CLIC 02/97 had and the first time in this index it is **read rather than inferred**. *(The **issue number** is the interesting half and it is nowhere on the object: the volume identifier is `MICO02CD`, the sleeve says only the month, and no page prints a number. What dates it is the disc's own database of everything before it. `Micodb/` — which the briefing for that session read as an article archive and which is nothing of the kind — holds **684 records, one per program the magazine had published on a cover disc**, each naming its issue and month, and they run **113 (Dicembre 2004) to 128 (Gennaio 2006), sixteen consecutive numbers with no gaps** — thirteen a year, because a *Natale* issue sits between November and January. The next number is **129**, and it is derived, not printed. The same database says **102 of the 684 were *solo nel DVD***, which is why the sleeve has `CD` in a box in its corner)* | **Il Mio Computer**, published by **Future Media Italy S.p.A.** — and the attribution has two independent sources that agree, which the previous magazine row did not: the archive record names the publisher, and the disc carries three e-mail addresses on the `futuremediaitaly.it` domain. The full legal name appears **once** on the whole object, in the privacy notice at the foot of the questionnaire. Counted as literal strings over 810 text-shaped files, *Il Mio Computer* appears **696 times in 688 files** — but **686 of those are the masthead on the 685 database pages it copied in**, and in the front end a reader actually sees it names itself **nine times in two files**. It made **0.8111 %** of the bytes, 0.7509 % once ten Windows thumbnail caches and a Dreamweaver design note are taken out; CLIC 02/97, a different magazine from a different publisher nine years earlier, came out at 0.82 %. **It wrote no software at all**: `IERunner.exe`, the shell `autorun.inf` launches, is a Borland-built third-party utility — `Comments: TWebBrowser wrapper`, `LegalCopyright: (c) 2001-2002 Pavel Kilovatiy`, US-English translation, ISO record dated 2002 — which the session briefing had called the one thing the magazine produced |   | **Not a game** — a magazine disc with four games on it, and the first here whose physical sectors survived: 349,462 raw sectors, every EDC verified, and 12.93 % of the file is CD frame |
| [**Flight of the Amazon Queen**](https://github.com/vs-sr-dev/pc-flightoftheamazonqueen-doc) | **1995**, and the object carries **five** dates of which four are not the product's — the widest spread this column has had to argue since *Allods Online*, and unlike that one it is settled **inside the game data**. The credit roll exists **twice**: `DATA`, 5,172 bytes, reads `Copyright (c) **1994**, Interactive Binary Illusions`; `CREDIT1.CRD`, 1,540 bytes, is the same page with the same indents and reads `Copyright (c) **1995**`. Both ship on every copy. The 1994 roll credits a **Sound Engineer** and no recording infrastructure; the 1995 pair adds *Voice Recording Project Management*, *Executive Voice Producers*, two *Production Assistants* and a **Sound Mixer**, and corrects two people's names — `Will Jeffries` becomes `Will Jeffery`, `Mark Dearling` becomes `Mark Dearsley`. So the two years are not a contradiction: **1994 is the game and 1995 is the talkie**, and the same executable that indexes this file also indexes the 1994 floppy release at 22,677,657 bytes, one eighth the size, with the same rooms and no recordings. The cell takes the year of the object in hand, as the *Lands of Lore* row did with its 1993/94. *(The other three dates are in the object too and none is the product's: `Copyright (C) **1990** by Voyetra Technologies`, in a MIDI meta event inside `AQBANK.RL`, five years older than the game; `ScummVM 2.0.0 (Dec  9 **2017** 07:14:40)`, the interpreter's own `__DATE__`, and the only date the two largest binaries will give — both are GNU-linked with a COFF timestamp of zero, which is reproducibility refusing to answer; and **2018**-04-25 11:48:02 on all nine members of the shop's web cache. The filesystem says none of them: 41 of 45 mtimes fall inside **six seconds** of the morning this copy was installed, which is the *Lands of Lore* finding — 62 of 65 inside ten seconds — reproduced exactly. And the shortcut disagrees with the filesystem by precisely 7,200 seconds, because a Shell Link stores UTC)* | **Interactive Binary Illusions**, Brisbane — published by **Renegade, UK** — and the string was counted before the cell was filled, as this column now requires. `Interactive Binary Illusions` occurs **6 times in 190,787,021 bytes**, all six inside the three credit resources and nowhere else; `Renegade` 6 times, `Bitmap Brothers` twice, `John Passfield` 27, `Steve Stamatiadis` 23, `Tony Ball` 10. The studio is two people and the roll says which did what: story and design both, programming Passfield and Ball, graphics and animation Stamatiadis, script Passfield *(extra words by Steve)*. *(The credits also name the engine, which is why this row can do something the others cannot: **JASPAR Game Engine and other development systems — John Passfield**, and a separate line, **JASPAR PC Conversion — Tony Ball**. `.JAS` is JASPAR. That single line explains why a 1995 MS-DOS CD is indexed in **big-endian** and holds **375 AMOS memory banks** — AMOS being a BASIC for the Commodore Amiga — every one of them closing to the byte under a Motorola reading and to nonsense under an Intel one. The Amiga release came first, one person converted the engine, and nobody converted the data. Four PCX backgrounds are still **320 × 256**, which is a PAL Amiga screen)* |   | A talking adventure whose talking is 89.23 % of it and whose script is 0.33 %: one 190 MB file with no index of itself, described only by a table inside ScummVM twenty-two years later |
| [**Resident Evil**](https://github.com/vs-sr-dev/pc-residentevil-doc) | **1997**, and the object offers **five** dates of which four are not the product's. The primary volume descriptor reads `1997-08-22 12:13:04`, the newest file on the disc is `RESIDENTEVIL.EXE` at `1997-08-22 12:03:44` — and it is also the last file in extent order, at sector 312,222 — so the disc was closed on 22 August 1997 and the cell takes that year. *(The other four: the **game** this is a port of came out for the PlayStation in **1996**, and the executable still calls itself `bio1997` after the Japanese title while carrying the string `1997/3/21` in Japanese date order; the **oldest file** is `1995-07-10 21:09:00`, eight months before the PlayStation original shipped, and it is a Microsoft display driver for a Japanese PC, not a game asset — all 76 files dated 1995 are third-party; and the `.bin` file's own mtime says **1996-12-25 03:32:00**, which is **240 days before the volume it contains** and is therefore synthetic, the same impossibility `pecensus.py` tests binaries for, applied to an image and failing.)* **What makes this row different from every other one here is that the year is not the only thing the filesystem knows.** This is the first object in the collection whose directory records date the **work** rather than the copy: 1,102 distinct timestamps over **129 distinct days**, 1995-07-10 to 1997-08-22, proved two ways — the seconds field is even on **2,638 of 2,638** file records that are not exactly midnight, which is FAT and nothing else, while the 47 directory records written by the mastering program are even on **25 of 47**, which is chance; and four of the five root programs carry a recorded time exactly **nine hours** ahead of their own COFF linker stamp, to within fifteen seconds. Nine hours ahead of UTC is Japan. Every one of the 3,436 records declares a timezone byte of GMT+01:00, which is where the disc was mastered, and it is wrong about all of them | **Capcom Co., Ltd**, published in Europe by **Virgin Interactive Entertainment (Europe) Ltd** — and the strings were counted before the cell was filled. `Capcom` in any case occurs **21 times in 634,776,465 bytes** across seven files, `Virgin` **3 times**, and `Interactive Entertainment` **once**. Both attributions come from the same place: two lines of prose at the top of `README.TXT`. Everywhere else the name is a registry key, `Software\CAPCOM\RESIDENT EVIL`, in four of the five programs — and two of the three lower-case `virgin` hits are a path to `virgin.tim`, the publisher's logo screen. *(**Who did the port is not on the disc, and the silence is structural.** All five programs — `RESIDENTEVIL.EXE`, `LAUNCH.EXE`, `SETUP.EXE`, `UNINSTALL.EXE`, `CHECKER.EXE`, 2,163,200 bytes, one linker version, no Authenticode — carry **`VS_VERSIONINFO: ABSENT`**. Not one company name, not one product name, not one file version, on any binary the publisher wrote. The only path that leaks a machine at the company that made it is a single CodeView record, `E:` + `work` + `Unsetup` + `Release` + `Uninstall.pdb`, inside the uninstaller: **one leaked build path in 736,133,664 bytes**, against Final Fantasy VIII's 31,737. The mastering software names itself twice, in the two identification fields that are not blank — `GEAR VERSION 4.0 APRIL 1996` and `ELEKTROSON 1996`, both naming the company that wrote the burner — so the disc identifies its tool and neither of its authors)* | Resident Evil | A PlayStation game on a Windows CD: every recording of the world is in a PC format and every description of it is in the console's — 2,601 TIM textures and 828 TMD models inside a Win32 product |
| [**Resident Evil 2**](https://github.com/vs-sr-dev/pc-residentevil2-doc) | **1999**, the year both volumes were written — `1999-03-21`, an hour and two minutes apart — and the second of the two years in the readme's own copyright line, `CAPCOM CO.,LTD. 1998,1999`. *(Five other dates are on the discs and none is the product's: the PlayStation original is **1998**; the oldest file is **1996-10-20** and the newest **1999-02-01**; and the game executable is stamped **1999-02-16** on one disc and **1999-01-21** on the other, because they are two different builds of the same 1,001,984 bytes.)* | **CAPCOM**, published in Europe by **Virgin Interactive** — the readme's own two lines, and shorter than 1997's `Capcom Co., Ltd` and `Virgin Interactive Entertainment (Europe) Ltd`. *Who did the port is again not on the discs: all four of the studio's binaries carry `VS_VERSIONINFO: ABSENT`, which is nine of nine across two products and seven years* | Resident Evil | Two CDs of 1999 in Mode 2 sectors that use nothing Mode 2 exists for, of which more than half of each disc is the other — 42 minutes of Indeo 5 named `.BIN`, and five hours of four-bit speech |
| [**Deadly Premonition: The Director's Cut**](https://github.com/vs-sr-dev/pc-deadlypremonitiondc-doc) | **2013**, and this object offers **six** candidate years of which five are not the product's. The cell takes 2013 because that is when the two programs in this package were built: `DPLauncher.exe` is linked **2013-11-12 10:40:58** and `DP.exe` **2013-11-28 09:20:54**, and both stamps are the PE header's own. *(The other five: the game this is a director's cut of shipped on **Xbox 360 in 2010**, and the archive still carries a build path with `X360` in it; the **film** was encoded in **2007** and **2009** — four ASF creation dates run 2007-09-10 to 2007-10-12 and twenty-three run 2009-07-17 to 2009-10-23, three years before the console release; the mod in the folder dates itself **2013-12-03**, and it is not the game's; and the **GOG wrapper** is stamped **2015-01-05**, corroborated by five ZIP member dates in `webcache.zip`, which is when this package was made rather than when the game was.)* **What the filesystem says is nothing at all**, and this is the third and cleanest sample of that: **937 of 958 files carry an mtime inside 243 seconds** of the installation, and of the 930 files the publisher declares, exactly **two** carry a date that means anything — both of them GOG's. Every year above came from inside a file, out of four internal clocks: COFF timestamps, XACT `FILETIME`s, ASF creation dates and a ZIP member date | **Access Games Inc.**, published by **Marvelous Entertainment Inc.**, licensed to and published in the west by **Rising Star Games Ltd.**, distributed by GOG — and every one of those was counted over all 6,877,549,781 bytes before the cell was filled: `Access Games` **79 occurrences in 8 files**, `Marvelous` **73 in 7**, `Rising Star` **11 in 7**, `Ignition` **8 in 2**. They are in the **credit roll**, `credit.prm`, a 502,368-byte parameter table that exists **thirteen times** in this object — six on disk, one per language, and seven more inside the archive — names **seven companies** (`Digital Media Lab.,Inc.` x12, `Access Games Inc.` x6, `Marvelous Entertainment Inc.` x5, `aquablue.inc`, `Katalyst Lab Inc.`, `SPHEREFRAME CO., LTD`, `shaft Inc.`) and closes with a **2010** copyright line, three years before the binary that displays it. *(So this row can do what the two Resident Evil rows could not: the studio **is** in the bytes, in quantity — but not in any of the places built to hold it. `DP.exe` carries **no `VS_VERSIONINFO` at all**, which is nine Capcom binaries plus these two across three products and sixteen years; and `DPLauncher.exe` carries a complete one in which four fields were never edited: `CompanyName = TODO: <Company name>`, `FileDescription = TODO: <File description>`, `LegalCopyright = TODO: (c) <Company name>. All rights reserved.`, `ProductName = TODO: <Product name>`. That resource shipped to two storefronts. Neither of the studio's binaries is signed; the five certificates in the object belong to Microsoft, NVIDIA, Inno Setup and GOG. What **is** everywhere is the machine: `D:\programmer_PC\main\UPDATA/...` prefixes all 14,328 records of the game's archive, and four more Access Games roots — `e:`, `V:`, `Z:`, and `C:\nakai\Work\mmv01\NEW\X360\` — appear inside the members. And `DP.exe` still carries, six times in six languages, `Please insert Rainy Woods disc.` — **Rainy Woods** being what this game was called in 2007 before it was withdrawn and remade, which is also the year of the four oldest ASF creation dates in its film)* |   | A 6.88 GB install whose program is 0.157677 %: a third of it is an archive indexed by 14,328 paths off the developer's own disk, and the same 643 minutes of sound ship twice in two codecs |
| [**The Legend of Heroes: Trails in the Sky**](https://github.com/vs-sr-dev/pc-thelegendofheroes6-doc) | **2004**, and this is the hardest cell this index has had to argue: the object offers **twelve** dated strata and **not one of them is a filesystem timestamp** — 137 of its 141 files carry a single **78-second** window in 2026, and the four that do not belong to GOG. The cell takes 2004 because the object says so twice in its own words: `dll\copyrights.txt` opens `Legend of Heroes VI: SORA NO KISEKI` / `Copyright (c) 2004 Nihon Falcom Corporation. ALL RIGHTS RESERVED.`, and all four binaries carry `LegalCopyright = Copyright (C) 2004-2017 Nihon Falcom Corp.` It is corroborated by the largest single event in the object's own calendar: on **2004-06-10**, between 02:16:32 and 07:22:44 UTC, **3,852 of the archives' 12,821 members and 836,051,791 bytes** were written — six archives concurrently inside one nineteen-minute window, with timestamps that do **not** rise with offset, which means the packer copied the source files' own mtimes and that day is when the shipping copy was made rather than authored. *(The other eleven strata, none of which is the product's: the oldest sound effects are **1998**-09-08 and 1999, six years before the copyright line claims; 55 of the 58 Ogg were encoded by `Xiphophorus libVorbis I 20010615`, a **2001** beta of a library whose 1.0 was released in July 2002, and the other three by a **2002** build; **2010**-11-18/19 touches 360 members; **2013**-09-07 rebuilds 3,289 in one Saturday; **2014**-07-21 to **2015**-11-07 adds 1,942 DirectDraw textures; **2017**-04-22 rebuilds 961 members and a Visual Studio crash file is stamped 04:02:50 the same day; the ending film was composited **2017**-05-02 and the opening re-rendered **2018**-04-21, both in After Effects CC 2015 at **UTC−04:00**, in North America; `steam_api.dll` is linked **2021**-11-23; all four Falcom binaries are linked **2022**-09-22 within ten seconds of each other, from a directory the CodeView record names `20220922-configfix`; and the GOG package is stamped **2022**-11-23.)* **And the 12,821 internal timestamps settle a question this branch had carried for four sessions**: 95.80 % of them fall inside one fourteen-hour band, which is 09:00–22:59 in Tokyo read as honest UTC, and a weekday histogram over distinct days gives 68 working days against 7 weekend ones | **Nihon Falcom** — and for the first time in four sessions the studio's name is in the version resource, in Japanese, on **four binaries of four**, counted over all 2,654,569,986 bytes in three encodings before the cell was filled. `日本ファルコム` occurs **8 times, all UTF-16LE, all inside those four resources, two apiece** — because `ed6_win.exe` and `ed6_win_DX9.exe` each carry **two** `VS_VERSION_INFO` blocks, one Japanese (`日本ファルコム 英雄伝説 空の軌跡`) and one English (`Nihon Falcom Corporation` / `The Legend of Heroes: Trails in the Sky`), both stamped langid `0x0411`, which is Japanese. *(The two text files nobody had opened say the rest. `dll\copyrights.txt`, 2,335 bytes, credits exactly three parties — Nihon Falcom for the game, the Xiph.Org Foundation for Ogg Vorbis, and one individual for an SSE and 3DNow! patch to a Vorbis build called `wuvorbis.dll`, a file that is not in the object — and it does **not** mention XviD, whose `xvid.dll` and `xvid.ax` are 786,432 bytes here. `EULA.txt`, 57,718 bytes, is the GOG.com User Agreement and names GOG sp. z o.o. of Warsaw and nobody else. And the company that produced the English edition this package is built on is **absent from the bytes**: `XSEED` occurs **0 times** in 2,654,569,986, in ASCII, UTF-16LE and Shift-JIS alike, and so does `Carpe`. What the object does leak of its makers is one Windows domain login, serialised into a 3D mesh in `ED6_DT16.dat` on 2004-06-10 and shipped ever since, counted and not reproduced)* |   | A 2.65 GB install whose program is 0.3042 % and whose 65 % is an uncompressed archive of 12,821 self-dated members — 44.72 % recorded media, and the sound that decides it is inside the container |
| [**Broken Sword: The Sleeping Dragon**](https://github.com/vs-sr-dev/pc-brokensword3-doc) | **2003**, and the object offers **five** candidate years of which four are not the product's. The cell takes 2003 because it is the only one that two independent things inside the executable agree on: `BSTSD.exe` carries the printable string `Core built at Nov 26 2003 06:12:12`, its engine's own build stamp, and the video middleware it ships and imports, `binkw32.dll`, is linked **2003-04-17 02:19:57**. Nothing in 1,724,710,597 bytes names a graphics API later than Direct3D 8 — `d3d9.dll` occurs **0 times** in ASCII, UTF-16LE and Shift-JIS alike — so between the engine's 2003 and the linker's 2007 the program did not move. *(The other four: **2007**, the COFF stamp of `BSTSD.exe`, 2007-08-25 13:35:17, and the month the manual was typeset — QuarkXPress 7.02, distilled on a Macintosh, source file `2.0_BrokenSword_PC_mnl_UK.qxd`, `/CreationDate D:20071015114114+01'00'`; **2008**, the manual's `/ModDate`, 2008-12-12, which disagrees with its own XMP `ModifyDate` of 2007-10-24 by fourteen months; **2014**, the DOS date on the ZIP member inside `goggame-1207658708.hashdb`, and it is 2014-04-01 00:00:00, a placeholder rather than a moment; and **2026**, this copy.)* **What the filesystem says is nothing at all**, and this is the fifth and cleanest sample of that in this collection: **6,746 of 6,748 files carry one mtime inside an 85-second window**, and the two that do not are GOG's icons. Every year above came out of a file. And this object is the counter-example the branch was looking for on the other side of that question — the format that holds 47 % of it, RenderWare's stream chunk, spends **2,048 bytes of header per file and not one bit of it on a date** | **Revolution Software Limited**, published by **THQ**, on **RenderWare** of **Criterion Software** — and every name was counted over all 1,724,710,597 bytes in three encodings before the cell was filled. `RenderWare` occurs **114 times**, `THQ` **158**, `Revolution` **10**, `Criterion` **3**. Inside `BSTSD.exe` alone the ratio is starker: `RenderWare` 112, `Revolution` 4, `Criterion` 1, **`THQ` none** — and the 112 are not a credit, they are 110 source paths reading `RenderWare/RW36Active/rwsdk/...` left in the objects by an unexpanded version-control keyword, so the engine outnames the author by accident. *(**The studio is not in any of the places built to hold it.** `BSTSD.exe` carries `VS_VERSIONINFO: ABSENT` — no `CompanyName`, no `ProductName`, no copyright line — which is now eleven binaries across four products and sixteen years; it is unsigned, and the object's only certificate belongs to **GOG Sp. z o.o.** of Warsaw, on an Inno Setup uninstaller stub built 2018-08-20 and signed 2019-10-14 that is **byte-identical to the one in Trails in the Sky**. What the object does say about its makers, it says in prose: `Readme.txt`'s 781-line credits section names five organisations — Revolution Software Limited, **Sumo Digital Ltd**, Six by Nine Limited, Babel Media Limited and THQ — and a `Localisation` section with French, German, Italian and Spanish translation houses, directors and voice casts, for a build that ships **one** language. Three absolute paths of a Revolution machine survive in the bytes, six occurrences in six files, and `buildpaths.py` can see only one of them: the richest, `\\Server2\Sword3` and `BS3\Demo2\Data\Susarro2\Graphics\objects\case_corner\textures\black.bmp`, is not drive-rooted where it sits, and the executable's own PDB path, `l:\BS3\BS3PC\Master\BS3PC.pdb`, is rejected by the tool's vowel filter at ten per cent against a fifteen per cent threshold)* | **Broken Sword**. Empty when this row was published; filled by the session that measured *The Angel of Death*, the second member of the series in this collection. **291 archive members are byte-identical between the two games** — 87.83 % of the fourth game's bitmaps, 99.07 % of its PNG, 100 % of its animation event maps — and no sound, film or geometry | A 1.72 GB install with two manifests that count it three ways, whose program is 0.1012 % — 47 % is 6,721 RenderWare audio streams, eleven hours of four-bit speech against nine minutes of film |
| [**Broken Sword: The Angel of Death**](https://github.com/vs-sr-dev/pc-brokensword4-doc) | **2006**, and the object offers **six** candidate years, of which the cell takes the earliest that is the *work* rather than the packaging. The criterion is stated before the verdict: the year of a game is the year its content was made, not the year somebody relinked it for a shop. And this is the first object in the collection whose content dates itself: **1,967 of its 1,987 compiled scenes carry an ASCII timestamp at byte 200 of their own header**, `HH MM SS DD MM YYYY`, and they span **100 distinct days from 2006-04-20 09:24:55 to 2006-08-14 12:07:50**, with a weekday histogram, a lunch hour and a 9.35 % weekend. Four DLLs and two `.ini` agree: `mss64.dll` 2006-06-07, the two Bink libraries 2006-06-23 six seconds apart, `mss32.dll` 2006-07-06, and comments inside `system\custom.ini` and `system\compat.ini` reading `18:49 22/07/2006` and `18:49 08/08/2006`. *(The other five: **2011**, the COFF stamp of `bs4pc.exe`, 2011-09-21 09:14:29, and the manual's `/ModDate` of 2011-10-13, twenty-two days apart — a relink, not a rewrite; **2017**, `d3d9.dll`, linker 11.00, COFF 2017-10-04, a Direct3D proxy carrying `mhookcxx` that GOG's own manifest declares as the first of its twenty-one game entries; **2018**, the Inno Setup uninstaller and the DOS date on the ZIP member inside the 207-byte hash database; **2019**, `support.ico`; and **2026**, this copy, which is 29 of 31 files inside one minute.)* **The filesystem again says nothing**, sixth sample running — and this is the counter-example the branch had been looking for, because the format holding 58.39 % of the object spends 312 bytes of header per member and **twenty of them on a date** | **Revolution Software**, developed with **Sumo Digital Ltd**, published by **THQ**, on the in-house **Emmersion** engine — every name counted over all 2,668,075,144 bytes in two independent encodings before the cell was filled. `Emmersion` occurs **3,449 times in ASCII and 2 in UTF-16**; **`Immersion`, the spelling the literature uses, occurs 0 times in either**. The engine team is named in the object's own `credits.txt`, between *Additional Programming* and *Engine Programmers*: **Sumo Digital Advanced Technologies group**. `THQ` 397, `Revolution` 36, `Sumo` 14, `Sumo Digital` 4. *(**And the lighting technology the literature calls *Amex* is called `amBX`.** `Amex` and `AMEX` occur **0 times** in 2.67 GB; `amBX` and its five other casings occur **1,073 times in ASCII and 5 in UTF-16**, there is a 4,186,664-byte video member called `mov_ambx.bik`, the executable carries **220 distinct `amBX_` asset and effect identifiers** in an embedded XML table, and the single occurrence of `Philips` in the whole object is the credits line `Thanks To: Philips amBX`. It is Philips' ambient-experience system, and the object contradicts the encyclopedia 1,073 to 0.* **The studio is not in the place built to hold it**: `bs4pc.exe` has a complete version resource with `FileDescription`, `ProductName`, `InternalName`, `OriginalFilename` and `LegalCopyright` — and **no `CompanyName` key at all**, while five other binaries in the folder have one. Its `FileVersion` and `ProductVersion` both read `dont_change_` followed by twenty-six `X`, a build-script placeholder that shipped; its binary versions are `0.0.0.0` and `1.0.0.1`, which disagree with each other and with everything else. And the assets name people the credits do not: **23 distinct author fields across 1,970 of 1,987 compiled scenes**, counted and not published)* | **Broken Sword**, and this row is why the cell above it is no longer empty. The rule is symmetric and had never before been able to be: the *Sleeping Dragon* row, published the day before, was updated in the same commit | A 2.67 GB install of 31 files, three of which are 99.38 % — and 58.39 % is compiled 3D scenes that date themselves to the second |
| [**Broken Sword 5: The Serpent's Curse**](https://github.com/vs-sr-dev/pc-brokensword5-doc) | **2014**, and this is the first row in this index whose year is **not in the object at all**. Every date the 6,608,639,638 bytes contain belongs to the packaging or to a library: four COFF stamps, 2009-06-03 (`OpenAL32.dll`, signed by Creative Labs), 2018-08-20 (GOG's Inno Setup uninstaller), 2022-04-28 (`SDL2.dll`) and 2022-06-06 09:04:23 (`BS5.exe`); the DOS date on the ZIP member inside the 279-byte hash database, 2022-06-06 10:09:08, **sixty-five minutes after the link**; and the mtimes, 31 files of 33 inside a five-minute window on 2026-09-02 with GOG's two icons at 2017-09-28 and 2019-08-26. `2013` and `2014` were searched for as strings and as dates and the object does not carry either. The cell takes **2014**, the completed release, over 2013, the first episode, over 2022, a relink, over 2026, this copy — and says openly that the number came from outside. *(**And the format is why.** The two container formats hold 99.8996 % of the object between them, and neither has room for a date: a `VT7A` record is sixteen bytes fully occupied by key, offset, uncompressed size and stored size, an `AUFS` record is twelve bytes fully occupied by id, offset and size. Seventh sample of the filesystem that dates nothing, and the first in which the archive format **cannot** date its members rather than merely declining to — which makes the previous game's twenty ASCII bytes of timestamp per scene the exception in this branch, measured now across three formats by one studio rather than two.)* | **Revolution Software**, self-published after Kickstarter — and the object **does not name its engine**, which is the finding this session exists for. `Virtual Theatre`, the name universally attributed to it, occurs **0 times** in all 6,608,639,638 bytes in both independent encodings; so does `VirtualTheatre`, `Theatre` and `Theater`. That alone proves nothing, because the object is 98.44 % above entropy 7.5 and **`George` occurs 0 times too** — so the containers were opened: `general.vt7a` holds 5,012 zlib members inflating to 12,663,529 bytes of XML and string tables, in which `george` occurs **22,475 times**, `Kickstarter` **83**, `Revolution` 35 more — and `Virtual Theatre` **still zero**. *(**The engine is twelve open-source libraries and no middleware at all.** `legal.txt` lists SDL, zlib, TinyXML, libogg, libvorbis, libtheora, libtheoraplayer, the OpenGL Extension Wrangler Library, libwebp, openal-soft-1.15.1, Opus and opusfile, every one corroborated by a structure in the bytes — 6,933 zlib members, 287,931 Ogg pages, twelve `\x80theora` headers, 3,138 decoded WebP, 56,162 `OpusHead`. Against RenderWare in 2003 and Bink plus Miles in 2006, the third media stack costs **nothing**. `GLEW` itself occurs 0 times: `legal.txt` writes the library's full name and the acronym is applied from outside, exactly like `Virtual Theatre`. And `BS5.exe` carries **no version resource at all** — third executable of three by this studio and the second with none, PE checksum 0, unsigned; the only certificates in the installation belong to **Creative Labs Inc** and **GOG Sp. z o.o.** of Warsaw. A build path from a tree that is not Revolution's, `F:\Megabot\Backspace\ThirdParty\theoraplayer-1.1.0\`, sits inside the executable beside four from `F:\Revolution\BS5\`.)* | **Broken Sword**, third cell, and the first time this index has had three members of one series measured with the same tools. The two above it were true as written and were not touched. `crossmembers.py`, extended this session from two sides to N, hashes 109,667 members across the three objects: **291 crossings between 2003 and 2006, and zero between 2014 and either** — eight years, a complete change of media stack, and not one shared digest | A 6.6 GB install of 33 files whose program is 0.0333 % — 76 % is the same artwork at two resolutions, and the engine's name is nowhere in it |
| [**FINAL FANTASY XI (PC, Steam)**](https://github.com/vs-sr-dev/pc-finalfantasy11-doc) | **2002**, and this is the first row in this index where the year of the work and the year of the bytes are twenty-three years apart. The criterion is declared before the verdict: **the year the work was released, not the year these bytes were written** — and for once the object confirms it from the inside, because `FFXiVersions.dll` carries COFF **2002-09-17 13:07:47** and a `CompanyName` reading `SQAURE CO., LTD.`, which is *pre-merger Square with the U and the A the wrong way round*, a typo that has been shipping for twenty-three years and is still registered by `regsvr32` at install time. The other three candidates are all defensible and all wrong for this cell: **2003**, the Western PC release; **2025**, the newest COFF stamp (`FFXiMain.dll`, 2025-12-04 01:27:14) and the installation itself; and **2026**, this copy. *(**And this is the eighth sample of the filesystem-that-dates-nothing question, and the first where the answer is that it dates plenty.** Ten distinct mtime days, not one: **2025-10-26 is 61,492 files and 92.9 % of the object** — the install — then four patch waves, 11-04 (4,164 files, 1.2 GB), 11-11 (46), 12-04 (7) and 12-11 (383, 244 MB), every one of them dominated by `ROM`, the 2002 layer, which is the layer that keeps changing. And then the last three dated days — 12-13, 12-16 and 12-27 — contain **not one byte of the product**: they are 97 files of one player's saved state, macros, logs and mail spool. The object's own timeline separates the product from the person without being asked to. Against that, sixteen distinct COFF days spanning **23 years 2 months 17 days**, an order of magnitude wider than anything else in this collection, and exactly one file where the two clocks describe the same event: `FFXiMain.dll`, linked 2025-12-04, written to this disk 2025-12-11, seven days of patch cycle visible end to end.)* | **Square Enix**, and the object spells it four ways. `SQUARE ENIX CO., LTD.` on 26 of the 27 binaries that carry a `CompanyName`; **`SQAURE CO., LTD.`** on the twenty-seventh; `SQUARE` and not Square Enix inside the original install path `C:\Program Files\PlayOnline\SQUARE\FINAL FANTASY XI`, still compiled into `FFXi.dll` in 2025 because moving it would break every installation in the world; and **`SquareSoft` zero times in 15,150,034,054 bytes** — every name counted with `strcount.py` in two independent encodings before the cell was filled. *(**The engine has no name to be absent, which is a different thing from an absent name.** This is the fourth engine chapter in this collection and the first where nothing was licensed: `RenderWare` 0, `Criterion` 0, `Havok` 0, `Bink` 0, `Miles Sound System` 0, `Vorbis` 0, `EmotionEngine` 0, `OpenGL` 0, `DirectShow` 0, with positive controls firing throughout (`Direct3D` 14, `d3d8` 39+1, `Moogle` 2,915). The only two library names in the whole object are `zlib` (18) and `libpng` (21). `FFXiMain.dll` is **2,896,464 bytes = 0.0191 % of the disk**, linked with **Visual C++ 6.0 on 2025-12-04**, and imports **12 DLLs and 294 functions** of which eleven DLLs are shipped with Windows; the twelfth is `d3d8.dll` and it imports **exactly one function, `Direct3DCreate8`**. No C runtime — statically linked. No D3DX: `D3DXCreate` occurs 0 times. **A 1998 compiler emitting one call into a 2000 graphics API, three months before this was measured**, beside a 2003 Unicode shim for Windows 98 shipped twice, is what twenty-three years of continuous operation costs, and it is legible in the import table.)* | **Final Fantasy**, second cell — and this row exists to close the question the row above it left open. *Final Fantasy VIII*'s cell says it was **filled on the title** and that the byte comparison the index's rule asks for **was not run**, because the other objects were not on the machine. Both are on this machine now, both measured with the same tools. `crossall.py` over 64 repositories: **2 crossings of 61,184 file hashes**, one of them Microsoft's `MSVCR71.dll` and the other a four-byte file. `datmembers.py` then hashed **1,718,526 `.DAT` chunks** so the comparison could be made at member level, and `crossall.py` over those: **0 crossings of 739,235 distinct members.** Against the Broken Sword rows in the same index — 291 member crossings between 2003 and 2006 — two Square PC games eight years apart share a trademark, a publisher and one compiler version, and **not one byte of content**. The cell stays filled, on the title, and is no longer an untested assertion; *Final Fantasy VIII*'s row is updated in the same commit | A 15.15 GB Steam install of a live service, half of which is on somebody else's machines: 73 % is one nameless file type, nine indexes that never overlap, and a checksum that turned out to be MD5 |
| [**Simulman V**](https://github.com/vs-sr-dev/pc-simulman5-doc) | **1993**, and this is the first row in this index whose year the object states **in pixels**. Four clocks disagree and none of them is the filesystem: all **120 files carry one identical mtime**, `1996-12-24 23:32:00`, a single second three years and three months after the fact; `TNC.NFO`, which is not the product, says `Release Date: 09/20/93` twice; `SMAN5/COD/PLAYER.EXE` carries `COPYRIGHT (C) 1992, 93, 94`, which is a range and belongs to a tool rather than to the game; and the **string `1996` occurs zero times inside the bytes** while `1993` occurs once, in the file that is not the product. What settles it is the title card: `SMAN5/BNK/INTRO00.ANI` decodes to a 320x200 screen reading `SIMULMAN`, `(C) FRANCESCO CARLA' 1993` and `(C) SIMULMONDO 1993` — **drawn as run-length-encoded artwork, where no string search can reach it**. The criterion is stated before the verdict: the product's own statement about itself, over a statement about the product, over the filesystem. *(Ninth sample of the filesystem-that-dates-nothing question and the sharpest: *Broken Sword 3* gave a window of 85 seconds, *Final Fantasy XI* ten distinct days, and this one gives **zero**. It is the signature of a copy made with a tool that stamped every file as it wrote it, on Christmas Eve 1996, of material already three years old — and the anachronism runs backwards for the first time in this index: **the product is older than its container**.)* | **Simulmondo S.r.l.**, of Bologna, and **the object says so itself**, which is why the *1000 Miglia* row above had to be revisited. `SIMULMONDO` occurs **3 times** — twice in `PLAYER.EXE`, once in the release note — and one of those is the full corporate line `@COPYRIGHT (C) 1992, 93, 94  SIMULMONDO S.r.l. BOLOGNA (ITALY)`, with two engineers credited by initial and surname immediately above it. Every grapheme was counted in both cases before the cell was filled: **`Simulmondo` occurs 0 times and `SIMULMONDO` 3; `Bologna` 0 and `BOLOGNA` 1** — the same words, and searching one case only would have produced the opposite row with a straight face. *(**There is no engine name to be absent, and two compilers built what there is.** `SIMULMAN.EXE` and `SIMULMCR.EXE` carry `Portions Copyright (c) 1983,90 Borland` — the Turbo Pascal 6.0 runtime, the same string as six of nine executables in *1000 Miglia* — while `PLAYER.EXE` and `NEWMIDIL.EXE` carry `Borland C++ - Copyright 1991 Borland Intl.`; `Borland` occurs 6 times and **`Turbo Pascal` zero**, so the name that identifies the toolchain is absent and the runtime's own error-message table proves it. The split is not Pascal-is-the-game: **the Pascal knows the filenames and the C knows the file formats.** `PLAYER.EXE` is a script interpreter that documents its own command line in Italian — fourteen buffers, `dev = device musicale (0=PCspeaker,1=adlib,2=soundblaster)` — and carries a cooperative scheduler calling itself `High Performance Kernel Multitask`, while `NEWMIDIL.EXE` still holds its linker symbol table in clear: `ADLIB.C`, `MIDIINT.C`, `MIDIPLAY.C`, `SndSAttDecay`, `carrierSlot`, `Meta_Event`.)* | *(empty, and deliberately)* — ***Simulman*** was a **five-part newsstand serial** and this is part five; the other four are not in this collection and are not measurable from this one, so the rule this index adopted holds and the cell stays empty until a second member is **measured**. *1000 Miglia* is the same studio and not the same series. The object mentions the serial exactly once and not as a word: **the `5` in the directory name `SMAN5`**, repeated 369 times inside the scripts. `edicola`, `episodio`, `puntata` and `Simulman 5` all occur zero times. *(**And one file crosses to the row above.** `NEWMIDIL.EXE`, 26,137 bytes, sha1 `cc4bf11d45eac6800d2739b2c341490981d1f1fa`, is **byte-identical** to *1000 Miglia*'s `MIDI3DRV.EXE` — same driver, different name, a year apart, and the only pair of files anywhere in the two objects that even match by length. `crossall.py` reports **0 crossings against 65 repositories and 41,500 hash tokens** and is wrong in the only way that matters, because `pc-1000miglia-doc` records no SHA-1 anywhere: a tool that finds nothing is not a tool that says zero. The two games also share the `.PAL` format, and it can be dated — the header grew from **two bytes to five** between them, proved by `2 + 3*(last+1)` and `5 + 3*(last+1)` closing exactly on 15 files at three different palette sizes.)* | A 2 MB folder with **not one compressed block in 557**, in which 58.35 % is a format with no magic number that opens to 156 pictures of 156, the dialogue is XOR'd with a key stored in its own first byte, and **0.0000 % was recorded** |

## The write-ups

Each entry below is the write-up that used to sit in the
*Game and engine documentation* table of the [profile
README](https://github.com/vs-sr-dev), moved here **verbatim**. Nothing was
rewritten or summarised in the move: same prose, same numbers, same links. The
only change is that a `\|` written to escape a pipe inside a table cell is now
a plain `|`, because these are no longer table cells.

### [Prince of Qin](https://github.com/vs-sr-dev/pc-princeofqin-doc)

*Prince of Qin* (秦殇, 2002) and Object Software's "EasyRPG" engine

### [Meridian 59](https://github.com/vs-sr-dev/pc-meridian59-doc)

*Meridian 59* (1996), one of the first graphical MMORPGs — and 30 years of operational strata

### [Forgotten Realms: Dungeon Hack](https://github.com/vs-sr-dev/pc-dungeonhack-doc)

*Forgotten Realms: Dungeon Hack* (1993) and the AESOP/16 engine

### [Wacky Wheels](https://github.com/vs-sr-dev/pc-wackywheels-doc)

*Wacky Wheels* (Apogee, 1994) and its fixed-point pseudo-3D floor renderer

### [Battle Bugs](https://github.com/vs-sr-dev/pc-battlebugs-doc)

*Battle Bugs* (Sierra/Epyx, 1994) — 800×600 in 16 planar colours, one asset set serving both modes, and a per-bitplane column-major image codec

### [Corridor 7: Alien Invasion](https://github.com/vs-sr-dev/pc-corridor7-doc)

*Corridor 7: Alien Invasion* (Capstone / IntraCorp, 1994) — a licensed **Wolfenstein 3-D** taken to 256 colours, shipping its levels in TED5's `TED5v1.0` **editor work file** with the map directory linked into the EXE. The MUSE tags date the whole soundtrack to the day, and ten credit sprites hang along a corridor on level 1

### [H.U.R.L. / Slob Zone 3D](https://github.com/vs-sr-dev/pc-hurl-doc)

*H.U.R.L.* / *Slob Zone 3D* (Deep River Publishing, 1995) on Lary Myers' **ACK-3D**. Levels ship as commented ASCII naming 661 of the game's 684 bitmaps by their original artist file names, and every projectile sits in a sealed room off the edge of the map because the engine allocates nothing at run time. The retail build still holds a level-select switch and an objective system never enabled

### [Might & Magic: Secret of the Inner Sanctum](https://github.com/vs-sr-dev/pc-mm-doc)

*Might & Magic: Secret of the Inner Sanctum* (1987)

### [Sargon V: World Class Chess](https://github.com/vs-sr-dev/pc-sargon5-doc)

*Sargon V: World Class Chess* (Mediagenic, 1991) — five files with four different extensions turn out to be **one container**, whose LZW packs **least-significant bit first**. One 8-bit asset set drives all four displays, the tutorial lessons are 258-node decision trees whose authoring sources shipped by mistake, and the About box hides a hamster

### [Nitemare-3D: A House of Horrors](https://github.com/vs-sr-dev/pc-nitemare3d-doc)

*Nitemare-3D: A House of Horrors* (David P. Gray, 1994) — a one-man 256-colour shooter that owes **nothing** to Wolfenstein: every format is Gray's own and none of it is compressed, because the engine demand-pages its art through a three-tier RAM/XMS/disk cache. An artist's placeholder shipped in the retail data as a wall reading *"See file TILES007.PCX"*

### [GRANDIA HD Remaster](https://github.com/vs-sr-dev/pc-grandiahd-doc)

*GRANDIA HD Remaster* — the PSX GPU/SPU/CD libraries reimplemented on D3D11/XAudio2

### [Secret of Mana (PC remake)](https://github.com/vs-sr-dev/pc-secretofmana-doc)

*Secret of Mana* (2018 PC remake), a PhyreEngine title

### [FINAL FANTASY V (PC)](https://github.com/vs-sr-dev/pc-ff5-doc)

*FINAL FANTASY V* (2015 PC) and the mobile-port fingerprints in the build

### [FINAL FANTASY TYPE-0 HD](https://github.com/vs-sr-dev/pc-fftype0-doc)

*FINAL FANTASY TYPE-0 HD* — PSP heritage and the HexaDrive render layer

### [Infinite Undiscovery](https://github.com/vs-sr-dev/pc-infiniteundiscovery)

*Infinite Undiscovery* (tri-Ace, Xbox 360) and the ASKA engine

### [HeroQuest](https://github.com/vs-sr-dev/pc-heroquest-doc)

*HeroQuest* (Gremlin Graphics, 1991–92) — the licensed board game on three DOS floppies, documented from somebody's installed directory zipped up in 2008. All three executables are **EXEPACK**-packed by the same linker flag and only one of them, `QUEST.EXE`, carries a **1980-01-06 19:48:46** timestamp, which exonerates the packer and hands the CD32 checklist's long-standing "sixth epoch" question its first DOS sample. The twenty-four quest files each open with a 26 × 19 byte grid, and because every square is either zero or one fixed region id, the union of all twenty-four **reconstructs the entire board**: 42 regions, 494 squares, zero unassigned, one square where the quests disagree. Accented letters are remapped onto the **lower-case ASCII row** — `a` = Ä, `e` = È, `n` = Ñ, `u` = Ü — because the 87-glyph font has no lower case to displace, which is a different answer from the CD32 sequel's `( ) * +` and for a reason visible in the two fonts. The interface is in five languages and the quest prose is in English only. The copyright notice is **plain text** here and pixels-only on CD32, so that finding was never a house policy; Imagitec supplied the audio to both games and is credited on screen here and hidden in a linked binary there. And the tempting 1.945 ratio between all the VGA and all the EGA art collapses to **1.123** once the ten VGA-only intro pictures are excluded — the number was measuring the intro, not the colour depth

### [Baron Baldric: A Grave Adventure](https://github.com/vs-sr-dev/pc-baronbaldric-doc)

*Baron Baldric: A Grave Adventure* (CTV-Link / Manaccom, 1992–93) — an Australian DOS platformer surviving as somebody's installed `C:\BARON` directory: thirteen files, 2,036,866 bytes, and **every single date forty-eight years in the future**. Twelve files are stamped 2040–41 and one is stamped 2050, all of them legal values in the seven-bit MS-DOS year field; subtracting 48 puts the build at **1992-11-29 → 1993-02-07**, and the number is pinned not by the dates but by two strings — a Borland runtime copyright reading `1983,92`, which forbids anything earlier, and the game's own banner reading `(ver 1.0  Nov 1992)`. The lone 2050 outlier looked like noise and turned out to be **the only file that can distinguish an addition from a stuck bit**, because 12 and 13 share no bits with 48 and 22 does. The three `.BNK` containers have **no directory whatsoever**: a five-byte `-ID-` marker precedes every member and the chain *is* the index, which makes the walk self-proving — eighty-eight members, three walks, all three landing exactly on the file length. Inside one of them sits `BALDRIC.MAP`, which is not a level but **the Turbo Pascal linker's own map file, packed into the shipping game by a build script that globbed for `*.MAP`**: it names seven `.PAS` sources, 178 public symbols and the entire global state (`ENERGY`, `LIVES`, `FLINTS`, `TREASURE`, `LIGHTREMAINING`), and because Pascal lays globals out consecutively, the gap between one symbol and the next yields **thirty animations with their frame counts** — `AWALKL` 8, `ADIE` 8, and `AFART`, `APICKNOSE` and `ASCRATCHBALLS` for the idle loop. Its `LEV` variable is 3,516 bytes and every level file is 3,520 with a four-byte header; its `DIGITS` is 640 and `DIGIT.FNT` is 640. It also describes a build **half the size of the one that shipped**, twenty-six days earlier. Nothing is packed, the 4,096-byte launcher sets `e_maxalloc == e_minalloc` so it can `EXEC` the game (which is what the underscore in `_BALDRIC.EXE` is for), the 165-frame sprite codec encodes against a **256-byte row pitch unrelated to the frames' declared widths**, ten of the eleven levels ship a compiled 8086 trigger table whose 255 case labels all fall inside the 3,500-cell grid, and one audio member turns out to be **twelve complete Creative VOC files concatenated head to tail**. Two extension collisions are closed by measurement (`.BNK` is not an AdLib bank, `.HSC` is not an HSC-Tracker module) — and the eleven members that genuinely hold FM music open with a magic, `AmBk`, that remains unidentified

> *Added after the fact, because the write-ups above are otherwise reproduced
> verbatim and this one ends on a claim that is no longer true:* `AmBk` **has
> since been identified** as the AMOS memory-bank magic, from the sequel below.
> See [pc-mystictowers-doc, docs/07](https://github.com/vs-sr-dev/pc-mystictowers-doc/blob/main/docs/07-the-amiga-inside.md).

### [Mystic Towers](https://github.com/vs-sr-dev/pc-mystictowers-doc)

*Mystic Towers* (Animation FX / Apogee, 1994) — *A Baron Baldric Adventure*,
and the sequel turns out to share a protagonist, a Borland runtime and three
asset files with its predecessor and **nothing else at all**. Forty-six members
of its single 3.4 MB container open with `AmBk` and ten with `AmSp`: these are
**AMOS memory banks and AMOS sprite banks**, and all fifty-six parse to
completion — 46 of 46 once the top bit of the length long is read as AMOS's
chip-memory flag and the length is counted from offset 12, and 10 of 10 sprite
banks closing on their frame chain plus a 64-byte palette. Every one of the 231
frames is five bitplanes deep and a whole number of **16-pixel words** wide,
the palettes are 32 entries of Amiga `$0RGB` with no bit above bit 11, the
eight music members are ProTracker `M.K.` modules and 90 of 93 digitised
samples are **signed**. The credits, XOR'd with 0x55 inside a container member,
say it in words: *Amiga Programming — Steve Hovelroud / PC conversion — Darren
Baker*. That identifies the `AmBk` magic
[pc-baronbaldric-doc](https://github.com/vs-sr-dev/pc-baronbaldric-doc) left
unidentified, and answers its question about why a little-endian shop wrote
big-endian words — here the seam is visible **inside single structs**: the AMOS
sprite header and the DOS one are the same five fields in opposite byte orders
for the same artwork, and a sound entry carries a big-endian sample rate four
bytes in front of a little-endian length. Ten AMOS sprite banks shipped in the
retail data **by accident**, 170,520 bytes and 231 frames the DOS game cannot
open, nine of the ten matching their converted twin's frame count exactly — the
same class of mistake as the linker map that shipped inside the previous game,
ten times larger and at a different studio. Elsewhere: the ZIP's seven
identical 1996 timestamps are a **TorrentZip constant**, proved by recomputing
`CRC32` of the archive's own 448-byte central directory and getting the
`3E1FE61E` in the comment; the only surviving real date is the ISO 9660 volume
descriptor's **1994-07-26 11:03:34**, under which the mastering tool had
already flattened all 307 file records to one second; the disc labelled as the
game's CD edition is a **German CDV Software shareware compilation**, 60 % of
it two promotional slideshows, and the "installed" folder beside it is a
byte-identical copy of one directory off it; `MT-HELP.EXE` has **no MZ header
at all**, so it is a `.COM` image that turns out to be an Apogee help text run
through TXT2COM and then PKLITE; and the predecessor's sprite codec's signature
256-byte row pitch holds on **0 of 2,002** frames here, because this codec
restarts at every scanline


### [Zero Comico](https://github.com/vs-sr-dev/pc-zerocomico-doc)

*Zero Comico* (GMM Entertainment / Medusa Games, 2001) — an Italian
television tie-in for the comedy trio Aldo, Giovanni e Giacomo, documented
twice: from a 506,378,240-byte **WinISO image made in 2003** and from the
**pressed CD**. All 2,862 files hash identically between them and **every one
of the 2,862 recorded timestamps differs**, because the converter discarded
660 real dates and wrote eleven values, three of which are not dates at all
(month 230, day 0, hour 192) — so the image's `WinISO software` publisher,
its 2003 creation date, its ISO 9660 violations and its **four duplicate
paths** are artefacts of the copy, while the original reads
`NERO___BURNING_ROM`, `2001-10-08 15:00:00` at **GMT+2**, and is conformant.
The real dates then agree with the PE linker timestamps **to within one
second** and date the build to the afternoon of 28 September 2001, on which
**2,191 of 2,862 files** were re-exported. **69.49 % of the disc is thirteen
minutes and forty-nine seconds of video**: seven Indeo 5 files at 320×240
averaging 3,370 kbit/s, six of them encoded with *every frame a keyframe* —
9,539 video chunks and 9,539 keyframe flags in `intro.avi` alone — and the
seventh, encoded four days later at 23:08, with sixteen in 1,206. The seven
are **2.86 times the size of the entire game**, and 7.22 % of the disc is
uncompressed PCM inside them on a CD that also ships 558 MP3s and an MP3
decoder. 2,188 files sit inside two in-house containers, `JFX1` and `JGF5`,
both wrapping an **LZHUF** stream — Okumura 1989, LZSS under an *adaptive*
Huffman coder, which is why 503 documented attempts against it failed — and
all 2,188 decode to their exact declared length, turning 72.8 MB into
**214.4 MB**. Nothing on the disc is what its extension says: the 1,433
`.tga` are not Targa (**0 of 1,433** pass the header arithmetic, they are
32-bit `JGF5`, 96.4 % power-of-two), the 25 `.flc` are not FLIC, and the 82
`.bsp` are plain CRLF text holding a verified **two-dimensional** BSP over
the walkable floor — the preorder walk closes on all 80, N internal nodes and
exactly N+1 nulls, over 1,948 convex cells and a 53,518-arc pathfinding graph
with **exactly one node per room-outline vertex**. The engine is not this
game's: `Lucifer 3D Interface`, source headers from **1998-08-20**, four
hard-coded paths including `d:\motore\japotek3d.dll`, a DirectPlay lobby,
twelve directional hit-reaction slots, `obj_spada`, `combat.mp3` and the
title string **`Silver Raven On-line`** — and the three protagonists joke,
across three chapters, that the studio never made them a fighting animation,
which the executable's own symbol table confirms. The retail executable's
version resource reads `Playable Demo`, version **`0.8.0.0`**,
`OriginalFilename: game_engine.exe`, `Copyright © 1999 GMM Entertainment
S.r.l.`, naming a developer that appears nowhere on the packaging or in the
readme. Elsewhere: **400 lines of the shipped scripts are 56-byte runs of
`0xCD`**, the Microsoft C runtime's *debug-build* fill for uninitialised
heap, and they are all 400 of the game's `sound:` lines, none of them valid;
3.2 MB of English MSI transform ships registered and unreachable because
`EnableLangDlg=N`; twenty-three script files are signed
`//Puzzle Files Created by Game Editor by PietruZ&DariuZ`, the only place on
the disc where a person who made this game is named; and the 49,163
characters of dialogue hold Monkey Island's **insult sword-fighting** with 65
hand-written lines across five opponents, a plumber whose **surname is
Mario** and whose brother Gigi lives upstairs, and Pac-Man introducing
himself under his 1980 Japanese trade name, **`Puck Man`**

### [Blood & Lace](https://github.com/vs-sr-dev/pc-bloodandlace-doc)

*Blood & Lace* (GMM Entertainment, Tortona, mastered 2 March 2001) — the
game the Zero Comico engine was **built for**, seven months earlier, and the
title whose `JGF5` files were reported as holding "LZH-compressed data",
which is the tip that opened that disc. A 519,358,464-byte image with
`NERO - BURNING ROM` in its application identifier, `BLOODLACEMASTER` as its
volume label, and — unlike its sibling — **no retail disc in the session to
check it against**, which is stated in every chapter that depends on
filesystem metadata. Its 215 unclaimed sectors account for themselves
exactly: two root directory records, **56 zero-length `.bsp` files** (24.7 %
of its floor plans, 41 of them camera maps, against two of 82 on the other
disc), and 157 zero sectors at the end of which **155 sit inside the declared
volume**, the same 155 as on Zero Comico's pressed disc — which that repository
read as a Nero signature and which the *Grande Fratello* disc has since taken
apart: **150 of the 155 are the Red Book post-gap**, present after every burned
data track whoever built the image, and only five belong to the image. **Two thirds of the disc has one
date**: 4,624 of 6,918 files stamped 30 December 2000 between 04:47 and 04:53,
after `japotek3d.dll` linked at 04:44:31 and `blood&lace.exe` at 04:45:20 —
the whole product assembled in nine minutes at a quarter to five in the
morning, while the executable's version resource claims, in Italian and with
an exclamation mark, `Compilata il 6 dicembre 2000 alle 6 del mattino!`, which
is twenty-four days wrong. Eight shipped `SpeechTracer` dumps carry the
compiler's `__DATE__` of the build that wrote them, so the disc records
**nine builds over six weeks** from a binary with one timestamp of its own,
three of them after 9 p.m. The engine DLL contains **3,576 bytes of signed
Italian**: a licence notice in the first person stating that `japotek3d.dll`
was developed entirely by **Dario Pelella of Genoa** from **1996**, licensed
per compiled version to Giunti Multimedia Entertainment of Tortona, dated
*29 dicembre 2000* — four hours and forty-four minutes before its own COFF
timestamp, both correct if you have not been to bed — plus a four-person team
credit that gives `PietruZ&DariuZ` their surnames, and greetings to
**JapoTek, a demo group since 1993**, which is where every `J` in `JFX1`,
`JGF5` and `japotek3d` comes from. **None of that block survives into Zero
Comico's copy of the same DLL.** Nor does a third of the code: `.text` is
704,512 bytes here against 466,944 there, so **237,568 bytes and 31 C++
translation units were removed**, including a named software rasteriser,
`JapoTek SimPlus`, with 8-bit and 32-bit back ends — and the 262,144-byte
difference in file size is five section alignments summing coincidentally to
2^18. `Silver Raven On-line`, the cancelled project fossilised in the 2001
binary, is **absent** here on four independent measures, so it was linked in
*after* this game rather than carried since 1999. The combat that Zero
Comico's characters joke about never having is **real**: 32 sword animation
sets, 26 collision-sensor files declaring 99 hit zones, 76 combat sounds
named *attacco* / *subita* / *morte*, five weapons wired to the inventory and
a heartbeat that speeds up as energy drops. 4,622 of 4,622 LZHUF containers
decode to their exact declared length, turning 209.8 MB into **389.6 MB**;
the 2,824 `.tga` are 32-bit `JGF5` again, 96.8 % power-of-two, and their
channel order turns out to be **BGRA** — five textures named `*pelle`, skin,
are blue as RGBA, and the other disc's own `azzurro.tga` is orange. The nine
Indeo films are **640×480**, four times the sibling's pixels, at **0.0663
bytes per pixel against 0.1961**, and seven of the nine use interframe
prediction properly; there are **85 minutes 30 seconds of recorded speech**
against six, and — on both discs, across 2,598 files — not one MP3 tag of any
kind. The model format finally parses: record type `0xF044` is a group with a
`u32` length at `+4`, which closes the walk on **1,029 of 1,030 files here
and 526 of 526 on Zero Comico**, up from 520, and still yields no vertex
count, because 675 distinct `0xF003` body lengths with a gcd of 1 is not a
stride. And `char.esc`, which the older repository called a one-letter typo,
is **108 files, fifteen of them called `char.esc`** — an earlier name for the
same format, renamed to `.isc` during this game's production, with the
diagnostic string left behind. Also on the master: `Stanzarossa`, a 538 KB
test level that is one four-point square room with 62 characters and all five
weapons in it; a directory named `SUPERFLUI` holding more speech than the
chapter above it kept; a script called `Copia di char.isc`; and a licence
that asks for **ten pounds sterling** to replace a defective CD


---

### [Grande Fratello Il Gioco](https://github.com/vs-sr-dev/pc-grandefratello-doc)

*Grande Fratello Il Gioco* (Trecision S.p.A., Genoa, mastered 20 February
2003) — the official PC game of the Italian *Big Brother*, made under licence
from **Endemol Italia** and covering the show's first three editions. It is
the **smallest disc in this list and the first that arrived as a CloneCD set
rather than an image**, which is the whole difference: the `.ccd` brings a
table of contents and the `.sub` brings 12,017,088 bytes of subchannel, so for
the first time here something can be said about a disc *as a disc*. The dump
is somebody else's, made 69 days after the disc, and its 69-byte cue sheet
still reads `FILE "fifa2.img" BINARY` — a rip of a football game's sheet,
reused and never edited, which is why every figure in that repository says
whose numbers they are on the first page. **125,178 sectors close three ways**
(× 2,352 = the image, × 96 = the subchannel, = the lead-out in the TOC, which
also declares the disc CD-ROM XA); all of them are Mode 2, 125,176 Form 1 and
**two Form 2**, with zero bad sync, zero bad headers and **zero EDC failures**.
The subchannel is the opposite: **125,136 of 125,178 Q entries are
byte-identical to the entry the TOC predicts, 42 differ, and 41 of those by
exactly one bit** — 43 wrong bits in 12,017,088, a rate of 3.578 × 10⁻⁶.
A byte-perfect main channel and a damaged subchannel from the same read is
precisely what 276 bytes of Reed–Solomon per sector against 16 bits of CRC
looks like, and it is the proof that the dump is a physical read rather than a
synthesis — **the session predicted the subchannel would be too clean to prove
anything, and nine of its ten subchannel predictions are wrong for that one
reason.** The same layer settles a question standing across two repositories:
the P channel flags pause on **exactly 150 blocks**, so **150 of the 155
trailing zero sectors that all three Italian discs share are the Red Book
post-gap** and only five are anybody's convention. The volume says `GF` three
times, `TRECISION` twice, and **`ABELLONDI`** in the data preparer field —
the first time a person's name has turned up in that field here, and he is
credited twice in the game. All twenty files carry **one** timestamp, 37
minutes after the volume that contains them, and stacking every clock on the
disc puts compile, master and burn inside **84 minutes of one Thursday
morning**. **62.02 % of the disc is nine MPEG-1 program streams** whose GOP
time codes are not zero-based: they span **17 hours 29 minutes of one
continuous recording** of which 1.13 % was kept, and two of the nine are
**frame-adjacent** — television, cut from a house feed, with nine buttons in
the menu to match. Each carries **two** 384 kbit/s Layer II audio tracks, and
the second alone is 13.39 % of the CD. The game is **20.76 %** of its own
disc and the redistributables are **17.21 %**: four DirectX 8.1 packages in
two languages and two Windows flavours, plus a `setup.exe` hiding three more
cabinets and 38 files nobody sees. Inside `Data1.cab` are **2,934 files in one
flat heap**, whose 194 directories exist only in the MSI — read out with a
from-scratch OLE2 and Windows Installer reader — and the game itself is **one
749,568-byte executable with no version resource**, importing one function
from Direct3D 8 and twenty-two from FMOD. It contains a complete tokenised
scripting language whose reserved words include **`AZIONE`, `IMPREVISTO`,
`PROB` and `GUINAME`**, and a simulation in the clear: five rooms, four turns
a day, empathy on five named levels, public approval, a tolerance meter, a
malus for repeated actions, secrets with a gravity field, jealousy, and 26
named actions from `raccogli le uova` to `fai sesso`. The cast is **34
records** — name, texture folder, surname, birthplace, residence, star sign,
occupation, distinguishing marks — of which **four carry an edition tag,
`1a`, `2a` and `3a`, because two housemates share a first name across
seasons**: the disc is forced to write down which three editions it covers,
and it does. The 2,212 textures are Truevision Targa **XORed by the low byte
of each file's own length** — a key the file carries in its own size, because
a Targa's ID-length byte is always zero — and `tga.py`, written for another
studio's game two sessions earlier and listed as inapplicable, reads all of
them one XOR later. Also on the disc: **Ogg Vorbis 1.0 release candidate 3**
in a 2003 retail box, 155 one-second WAVE files and **no recorded speech at
all**, a Visual SourceSafe status file installed onto the buyer's hard drive
whose 82 records match the 82 files beside it, a mirrored copy of **Radio
101's FM frequency pages** scraped with Teleport Pro and given a Start Menu
shortcut, a second build of the game carried only to supply an icon, a
telephone number that is an email address, four untranslated InstallShield
placeholders, and — in the video player, in English, in an Italian product —
`Press the 'Arrow' keys to move the ball.` The session was briefed to ask how
much of the disc is a PlayStation port; the executable's credits answer it the
other way, naming **`conversione per playstation a cura di`** with no
reciprocal PC credit, and there is not one Sony toolchain string, asset magic
or sector alignment anywhere on the disc.

### [Lucignolo Il Videogioco](https://github.com/vs-sr-dev/pc-lucignolo-doc)

*Lucignolo Il Videogioco* (7Th Sense s.r.l., content finished 22 November
2007, published 30 January 2008) is the tie-in to a late-night Italia 1 magazine programme and the fourth
Italian disc in this list. It arrives as a **cooked ISO with no pressed
original behind it**, and the volume says who made the image and nobody else:
application identifier `WWW.BURN4FREE.COM`, volume label `DISC 13 291107`,
publisher and data preparer blank. Every volume-level figure in that
repository therefore describes a stranger's home re-master, which is a
regression from the previous disc's CloneCD dump and is on its first page
rather than in a footnote. **Eight files, of which one is 96.7857 %** of a
1.11 GB disc.

The copy protection is the headline and it is a measurement rather than a
joke: `Installer\Installer.spf` is **six bytes containing the ASCII word
`codice`**, and the game's executable holds `LUCIGNOLO CD CHECK`,
`%c:\Installer\Installer.spf`, three Italian *insert the DVD* messages and
the literal `codice` — which is the entire disc check, and the word occurs
exactly twice in everything extracted. The second finding closes a question
three other discs left open in a different form: **the padding after every one
of the eight files, and the sector past the declared volume, is a byte-exact
copy of the data 65,536 bytes earlier in the image**, eight files out of eight,
bounded exactly by the padding and not one byte further. The image is 17,010
whole 64 KiB buffers, which is the whole explanation — and it says nothing
about the 155-sector tail on the other three, which stays open for a third
session because Burn4Free is not the program that wrote them.

The third finding settles a time zone by subtraction instead of inference. The
ISO declares GMT+0 in its volume descriptor and UTC+1 in its directory records
for the same instant; Inno Setup records 2,440 source timestamps in local time
and sets a flag saying so; the game's PE COFF header is UTC by definition.
**Inno minus COFF is 59 minutes 59 seconds** — one hour of zone and one
second of link-to-close lag — which makes the directory records truthful, the
descriptor's zero an unfilled default, and the installer's build time
computable at 54 minutes 10 seconds. The note sent back to
`pc-grandefratello-doc` is that its InstallShield timezone inference is sound
and does not generalise: three programs wrote timestamps into this one image
and used three conventions.

Inside, both executables are **Inno Setup 5.2.1** from the same compiler, and
`setup.exe` has no payload at all — its header block begins where its data
area begins, and the four areas sum to the file size exactly. The 1.03 GB one
is a single solid LZMA chunk holding **2,440 files, 1,411,108,085 bytes**, a
ratio of 1.3083×, which open out to a **2.14 GB tree of which 51.028 % is DDS
texture**. The engine is **OGRE 1.2.4 "Dagon"** with Newton, CEGUI, Cg, DevIL
and Audiere, and it names itself because the developers shipped a 475-line
`Ogre.log` from a laptop with an ATI Mobility Radeon X1600 — along with
`ogre.cfg`, `Crash.log`, `OgrePlatform.dll.backup` and a `resources.cfg` still
carrying `D:/VGData`. OGRE was built from source in **one twenty-minute run on
12 November 2006**. CEGUI ships, 2,281,472 bytes, and appears in neither the
import table, nor `Plugins.cfg`, nor the log, nor the strings; the entire
customisation of the middleware stack is **one bitmap and two dialog templates**
in the configuration DLL, with the original next to it. The eight video files
are **6 minutes 37.5 seconds of Cinepak** — a 1991 codec — at 512 × 512, with
uncompressed PCM that is 22.041 % of their bytes: the later Mediaset tie-in has
**56 % as much television in it** as *Grande Fratello* had, on a disc four and a
third times the size. Nothing is hidden anywhere: 1,609 images with 1,609
correct magic numbers, `.sgi` and `.ssd` that are XML, a `levels.db` that is
flat text, 1,387 written lines of dialogue across 353 chains and 69 speakers of
which 81.3 % are voiced, 102 minutes 29 seconds of Ogg Vorbis, and a 49-verb
scripting language in 1,002 XML steps. The whole of it is run by a **492,032-byte
executable, one part in 4,340 of the tree it manages**, and no file on the disc
outside `credits.avi` names a publisher, a distributor or a broadcaster.

The Year cell straddles because the disc and the world disagree: **every clock
on the image is 2007** — the newest file is 29 November, the newest file inside
the installer 21 November — while the stated publication date is 30 January
2008. Nothing in the image distinguishes a pre-release burn from an ordinary
two-month gap between gold and shelf, and the repository says so rather than
choosing. The publisher (2lite) and distributor (Halifax) are external
knowledge and appear nowhere in the 2,440 installed files.


### [Viaggio al centro del Mondo — the 883 "Grazie mille" CD Extra](https://github.com/vs-sr-dev/pc-883d-doc)

*Viaggio al centro del Mondo* (Moltimedia, October 1999) — **the one entry in
this index that is not a game, and it says so in its own What-it-is cell.** It
is the data session of a CD Extra: session one is ten audio tracks of the 883
album *Grazie mille*, session two is a Macromedia Director 7 program. The disc
names itself twice, in two files written 44 minutes apart by two different
machines, and the name it gives is **not the album's** — it is track 6's. There
is a game inside: a slot machine that unlocks the songs, which is `SLOT.DXR`,
6,053,234 bytes, **2.723 % of the data track**. The other 97.277 % is a menu,
nineteen QuickTime movies, five spherical panoramas, eleven Flash banners, two
web browsers, two copies of QuickTime, and a network client for a 3D chat world.

**The material is a regression on every disc before it**: not an image but a
copied folder, 142 files and 222,271,591 bytes, with no volume descriptor, no
directory records, no extent map, no padding, no unclaimed sectors and **no
audio session**. Twenty of the thirty inherited tools do not apply and each is
listed with its verdict. Two things came back that should not have.

**The first is twenty-four raw CD sectors.** Three of the four files in
`PICTURES/` are `RIFF/CDXA` containers, which hold Mode 2 Form 2 sectors
*complete* — 2,352 bytes each, sync pattern and absolute MSF address included.
Seven sectors, then fourteen, then three: **LBA 204,602 to 204,625,
contiguous, ascending, in file order**, every sync correct and every 8-byte XA
subheader present twice and identical. It is the only physical geometry that
survived the copy, and because MSF 45:30:02 is 45½ minutes into the disc it
puts a ceiling on the audio session that is not there. Inside them are three
MPEG-1 stills of the album sleeve at 176×144, 352×288 and 704×576 — a clean
1:2:4 ladder, 25 fps, PAL geometry, muxed at exactly CD audio's 1,411,200
bit/s — beside a fourth file that is an 800×600 JPEG carrying Apple's
`AppleMark` comment.

**The second is that the filesystem mtimes survived, and lie.** Read at face
value they describe a product authored in September 1998 and finished in
September 1999, with a year of nothing between. They are wrong, and the proof
is a subtraction: eighty-nine files carry a second timestamp inside themselves
— PE COFF, QuickTime `mvhd`, MS-CAB file tables — and **seven of them disagree
with their own mtime by exactly one year and by nothing else**. The month
agrees, the day agrees, the hour, minute and second agree once the +2:00 CEST
correction is applied that works on the thirteen control files. `BRANDING.CAB`
settles it: the Internet Explorer branding cabinet that Tiscali's IEAK run
produced was **built 1999-09-21 09:37:36 UTC** and carries an mtime of
1998-09-21 **11:37:38** — two seconds later, one tick of FAT granularity, one
year early. Eleven binaries have an mtime that precedes their own link
timestamp, which is impossible; forty-nine of fifty-one cabinets contain files
dated after their own mtime; and the product in that directory is Internet
Explorer **5**, which the disc states itself (`pver=5.0`) and which did not
exist in September 1998. **One workstation in the build chain had its system
year set to 1998 while the year was 1999**, and the corrected calendar puts the
entire authored production between **18 September and 4 October 1999** —
seventeen days. There was no September 1998.

**The Director container had never been opened by this family of repositories**,
and it cost four bugs, all the same bug. The `XFIR` byte-swap applies to the
chunk *framing* only — the four-character tags and the lengths inside `imap`
and `mmap` — while **every chunk body stays big-endian**. Breaking that never
crashes; it yields plausible positive integers. `Lnam` reported 17,152 names
(`0x4300`, which is 67). `Lscr` reported 65,535 handlers per script, because
offset 0x30 is `factoryNameID` and an ordinary script stores −1 there — the
tool printed **5,767,080 handlers across 88 scripts** without complaint. `CASt`
reported cast type 16,777,216 (`0x01000000`, which is 1, bitmap). `STXT`
reported a text length of 301,989,888 for the eighteen characters `INSTALLA
QUICKTIME`. Each was fixed by finding a falsifier rather than a better guess:
`literalsOffset + 8 × count == literalsDataOffset` holds on 88 of 88 scripts,
and the number of type-1 cast members equals the number of `BITD` chunks
exactly on all five containers — 158, 230, 42, 42 and 1 — as sounds equal
`sndS` and palettes equal `CLUT`. A fifth error was not a parser bug at all:
the first census counted `mmap` entry 0, the outer container whose declared
length is the whole file, and so halved every share it printed.

What the containers hold is small and Italian. **216 handlers, 744 names and
6,184 bytes of string literal for the entire product**, against 14.9 MB of
bitmaps in the menu movie alone — `menuDir7.dxr` is **97.45 % `BITD`**, and its
106 scripts are 0.19 % of it. Three-quarters of its memory map is `free` or
`junk`, the fossil record of an incremental save. The `VWFI` movie-info chunk
names the studio in a field nobody clears: `Alessandro ciao - Moltimedia`,
`Emanuele Belloni`, and the authoring machine's own path, `E:\883\CD\dati\`.
It also names **`Eric Blanpied - Apple Computer`** as the *creator* of two of
the movies, because both were started from Apple's QuickTime VR Director sample
and the field was inherited along with sixty `QTVR…` handler names, six
`Test…`/`Sample…` pairs and a complete English diagnostic dialog referring the
user to a section called 'Display' that does not exist on this disc. **The
Italian menu of an 883 CD-ROM is descended from an Apple demo file, and the
provenance is still in it.**

**The slot machine writes twenty-one characters to a text file.** The Lingo
names are `RitornoLeva`, `percentualeLeva`, `proceduraVittoria`,
`DefinisciVincite`, `gLampeggio`, `culoRand`, `bloccaPalliniIntervista` and
`gCanzone0` through `gCanzone9`; the FileIO vocabulary is `initFilePreferenze`,
`getOSDirectory`, `createFile`, `writeString`, `decodevinti`. The file is
**`pref883CD.txt`**, in the operating system's own directory — which is the
only choice that works from a CD — and its content is `X`, two digits, six
digits and ten digits, shipping as three separate literals (`11`, `111111`,
`1111111111`) with an all-zero default and an all-one target. Ten is the
songs. **The program contains no music at all**: it drives the album's *other
session* through `CDPRO.X32`, a commercial Xtra from **Penworks Corporation**
at version 0.1.0.0, with `playTrack`, `TrackTimeElapsed`, `NumTracks` and
`Eject`. That is why the readme insists on a multi-session drive, and why the
word `karaoke` is in the name table and there is no karaoke file.

**And the reason this entry is in the index at all is a directory name.**
`dati/install/883d.exe` is a 16-bit New Executable on a CD mastered in October
1999 — module `VISESTUB`, **MindVision Installer VISE**, 2.66 % code and
98.28 % payload — and it installs the **Activeworlds** browser: `AWORLD.EXE`,
`Aworld.ini`, eleven `.awm` language files (one of them called **`Copy of
Italiano.awm`**), `TELEGRAM.DAT`, `TELEPORT.TXT`, `CONTACTS.TXT`, and five DLLs
named `Rw…21` which are **RenderWare 2.1**. It ships the world's art cache
**already populated**, and Activeworlds names that cache after the world's
object-path server with the URL's slashes flattened to hyphens. Two other
entries in the same cache — `www.ccc.nottingham.ac.uk-pub-sat-images-d2m.awb`
and `194.121.52.190-video-grabs-cnn.awb`, neither of which has anything to do
with an Italian pop record — independently confirm the rule, and applying it to
the third gives **`http://vrml.moltimedia.it/aw`**, on the same domain as the
studio, with a property cache for a world called **`city`**. Inside: four
objects (`panel883.rwx`, `panelbustina.rwx`, `tv2bs.rwx`, `insegnatele.rwx`),
one avatar, one sky, four sounds including `comemai.wav`, and **twenty-nine
avatar animations of which fourteen have Italian names** — `balla`, `wave`,
`disperato`, `esultare` among them, which are precisely the four actions the
menu's Italian help text lists by name, written by different people in a
different format in a different file. **Thirty-nine art assets, out of a
world.** The client is here and it works; the server is not. `Tribumatta`, the
name 883D is said to have taken later, occurs **zero times** in 1,569,177
printable runs.

Three smaller things the measurements settled. **The disc ships four separate
3D technologies** and uses one and a half: Activeworlds on RenderWare,
RealVR (a 1996 Xtra with twenty-four Winsock imports it does not need, driving
five Photoshop-on-a-Mac panoramas that are all exactly 2000 × 1000), Apple's
QuickTime VR as inherited scaffolding, and — entirely by accident, inside the
Internet Explorer distribution — **Microsoft's VRML 2.0 Viewer**, 3.3 MB and
never touched. **Nothing on the disc names `VIDEO_01.mov` or `VIDEO_02.mov`**,
which are 55,648,873 bytes and 25.036 % of the data track; two scripts name
`video1.mov` and `video2.mov`, which are not there. And the `.mov` share of
53.293 % that makes this look like a video disc is mostly not video: **21.589 %
of the whole data track is lossless Apple Animation `rle` of the user
interface**, eleven files at 427 KB per second, and the six actual interviews
are 6.667 % and four minutes fifty-two seconds.

The Studio cell says **Moltimedia** because the disc says so three times inside
its binaries and never once in a document written for the buyer — `LEGGIMI.TXT`
names Microsoft, Apple and Tiscali and nobody else, and the record label is not
named anywhere on the disc at all. The Year cell says 1999 because the last
file written to the disc, the CD Extra directory itself, is stamped
**1999-10-04 21:13:54**; the studio's own present-day description says 883D
came about "in 2000", and the repository records the disagreement in a labelled
external-context section rather than resolving it in either direction. Whether
883D was among the first 3D avatar chat worlds is a census of everything else
that existed in 1999, and a folder cannot answer it — which is stated in the
README rather than left implied.

### [1000 Miglia](https://github.com/vs-sr-dev/pc-1000miglia-doc)

*1000 Miglia* (MS-DOS, 1991–92) — **124 files, 1,588,227 bytes, one flat
directory, no subfolders.** The sixth Italian object in this list and the first
that is not a disc at all: what survives is a directory as it sat on somebody's
hard disk, and the largest single finding is that **it is not the product**. The
game was finished on **1992-02-11 19:38:50**, when `MIGLIA.EXE` and `MM.OVR`
were written in the same second. Six files are newer, and three of them are not
the studio's: `LEGAL.NFO`, 659 bytes of United States Code boilerplate in
English written at **04:17 in the morning** on 23 March 1992; `MUSIC`, an Amiga
**ProTracker** module whose sample names read *"composed by morph of ***-dual
crew-***"* and give a phone number in **Dundee**; and `EXPLO.EXE`, run *first*
by `RUNME.BAT`, packed with a packer no signature matches, and carrying the
fragment ` intro by Hard C`…`ore.` at offset 0x48C inside its own compressed
stream. The last two files are eight months later still — `MM.CNF` at
1992-11-09 15:51:52 and `RUNME.BAT` sixteen minutes after it, one person
installing a game and typing a batch file. **This folder is one installation of
a March 1992 BBS distribution**, which is a third answer to a question that had
been asked as *floppy or CD*.

The provenance is measurable at the modern end too, and it is the first time
this collection can say so with a number. The original GamesNostalgia package
was supplied alongside the delivered folder: **124 of 124 files identical by
SHA-1 and 124 of 124 identical by mtime to the second, delta zero.** The eleven
wrapper files removed are all outside the game folder, and the briefing's claim
that they are all from 2019 except one is wrong in a way worth recording — two
are from March 2015, because they are the SDL runtime of the DOSBox 0.74-3
build. And `7z l` cannot be quoted for dates: its listing applies today's UTC
offset to every entry while extraction applies the per-date one, so **31 files
list identically and 104 list an hour late**, split at the last Sunday of
October 1991.

**The sixteen filenames are the title of the game.** Sixty-four of the 124 files
are sixteen groups of four — `ANRI`, `BLRO`, `BOFI`, `BOPA`, `BSPR`, `FISI`,
`FLVE`, `GUTL`, `PAFL`, `PRBO`, `RIBO`, `ROSP`, `SIBL`, `SPGU`, `TLAN`, `VEBS` —
each with a `.CT4`, a `.POS`, a `0.PTS` and a `2.PTS`. Read two letters at a
time they are pairs of city codes; the set of first halves equals the set of
second halves and has fifteen members; and the sixteen directed edges form
**exactly one closed circuit**, with `BO` the only node of degree two:
`BS→PR→BO→FI→SI→BL→RO→SP→GU→TL→AN→RI→BO→PA→FL→VE→BS`. Brescia, Parma,
Bologna, Firenze, Siena, Bolsena, Roma, Spoleto, Gubbio, Tolentino, Ancona,
Rimini, Bologna again, Padova, **Feltre**, Verona, Brescia — confirmed word for
word by sixteen Pascal strings at `MIGLIA.EXE+0xB001`. Bologna is named twice
because the route passes it going out and coming back, which is precisely why
the legs are named by their two ends instead of by a destination.

Three of the four size columns are one integer times a record size, and **the
division has two answers**: `CT4 = 64n`, `POS = 386n`, `PTS0 = 122n + 18` with
`n` in {44, 49, 54, 59, 68}, and an exactly-half rival `32n` / `193n` /
`61n + 18` that fits the arithmetic equally well. Opening a file kills it in one
line: a `.POS` record is a two-byte header followed by **64 (x, y, z) `int16`
triples**, and 193 − 2 is not divisible by six. The sixteen `n` values sum to
**892** and are drawn from five sizes, so the route was not modelled leg by leg;
it was modelled out of five lengths and each leg was given one. The fourth file
of each group has no formula because it holds variable blocks — the roadside
scenery, capped at sixteen objects per road segment, and the rank correlation
between leg length and scenery weight is 0.87.

**37.93 % of the folder is an Amiga compressor with the bits the wrong way
round.** The seven `.FL` files are containers: a fixed 128-slot directory of
`[u32 offset][int8 type][u24 length]`, where the type byte is **signed** —
positive means stored, negative means packed, and the magnitude is the format
(1 = raw image, 2 = RLE image, 3 = MIDI). 235 of the 328 members carry the
signature `PP20`, which is **PowerPacker 2.0**, an Amiga compressor, in a DOS
game in 1992 — and the count of `PP20` strings found by a scan that knows
nothing about the directory is 235 exactly. The textbook PP20 depacker fails on
every one of them on the first match. What found the fix was an oracle rather
than a structural test: a packed member of `MUSICHE.FL` had to be a MIDI file,
a MIDI file has to end `ff 2f 00`, and what came out ended `ff f4 00` — and
**0xF4 is 0x2F with its bits reversed**. These streams assemble a multi-bit
field with the first bit read as the *most* significant, which is the 68000
order; the C depacker everyone copies uses the other one. One line changed, and
all 328 members read: **1,245,538 bytes out of 602,478.** Inside them: 206 raw
images, 104 RLE images, and **eighteen MIDI files**, which are the game's entire
soundtrack in 18,072 bytes.

The rest is Borland. Six of the nine executables carry `Portions Copyright (c)
1983,90 Borland` — **Turbo Pascal 6.0**, a 1990 compiler in a 1992 game — and
`MM.OVR` is a Borland overlay whose `FBOV` header declares 105,071 bytes and
closes on 105,079 exactly. The overlay is **more than twice the size of the
program that loads it** and `MIGLIA.EXE` calls into it through 32 `INT 3Fh`
stubs. `MIDI3DRV.EXE` is Borland C++ 1991 with its symbol table intact
(`ADLIB.C`, `AdLib_Specific`) and 12,345 bytes of instrument data appended past
the end of its MZ image. And the briefing's claim that `CHELINGU.EXE` carries
the Borland Pascal `MZP` marker is wrong for an arithmetic reason: `e_cblp` is
the file length modulo 512, `CHELINGU.EXE` is 4,176 bytes, 4,176 mod 512 is 80,
and 80 is `P`. **There is no `MZP` in this folder**, and the one file with a
`P` that matters, `MIGLIA.EXE`, has 0xD0.

Everything the game declares about the race lives in 4,917 bytes — 0.31 % of
the folder, half of what its fourteen palettes weigh. Ten built-in scores
(Nuvolari and Guidotti at 7,500, down to Taruffi and Pellegrini at 250), 35
cars with cylinder counts, top speeds and displacements matched to a 35-entry
name array at `MIGLIA.EXE+0x0A732`, 77 driver pairings with six ability numbers
each, and the sixteen route polylines drawn on a 256×256 map of Italy. No two
of the four tables share a record stride — 27, 33, 14, 101 — so the dialect is
not a format; it is one language feature reused. **That feature leaves a
fingerprint.** Turbo Pascal does not clear a fixed-length string past its
length, so `Nuvolari` is followed by `rco`, which is the end of `Castelbarco`,
and `Minoja` by `chini`, which is the end of `Borzacchini`. The same habit shows
up in three other places: the first directory slot of all seven containers has
one stale length byte, `TRATTI.COR` writes fifty map points per leg where no
leg exceeds **thirty-nine** and all sixteen blocks are byte-identical from index
39 onward, and five bytes of 8086 (`pop di; pop si; sub ax,ax; push ax`) are
stuck to the end of `MONTI.IMV`. Every closure test in the repository passed —
and underneath every one of them is the same decision not to tidy what nobody
was going to read.

Two smaller results. **`Simulmondo` occurs zero times in 1,588,227 bytes**, and
so does every name the game is credited to; the Studio cell says so rather than
importing the attribution. And the overlay contains the sentence *"Programma non
installato, usare INSTALL per l'installazione"* — while no `INSTALL` exists in
this folder, and five Turbo Pascal utilities (`CHELINGU`, *which language*;
`GUARDA65`, holding the string `SOUND-DRIVER-AD-LIB`; `NUMPARAM`; `SPAZIO`;
`WRITEAT`) sit here with nothing calling them. **The product contained at least
one file this copy does not, and the program says so itself.** Against the seven
other trees `discdiff.py` returns zero over 15,238 files, as it has five times
before — but the comparison *by form* does not return zero for the first time:
Turbo Pascal 6.0 is shared with *Baron Baldric*, and PKLITE, an IFF `FORM` and a
ProTracker `M.K.` module are all shared with *Mystic Towers*. Three unrelated
DOS games reaching into the same small box of tools, and only this one reaching
as far as an Amiga compressor.

### [Harry Potter and the Philosopher's Stone](https://github.com/vs-sr-dev/pc-harrypotter1-doc)

*Harry Potter e la Pietra Filosofale* (Windows, Electronic Arts, October 2001) —
**540 files, 577,088,559 bytes, 292,173 sectors, Unreal Engine 1, SafeDisc
2.40.010.** The seventh object in this list and the first that is not a copy:
the retail disc, in a drive, readable as many times as needed. That inverts the
provenance chapter every previous entry opened with, and it makes three
measurements possible that no image and no file tree could support.

The first is arithmetic. The lead-out sits at LBA **292,323** and the volume
declares **292,173**; the difference is **150 exactly**, and four independent
sources — the ISO descriptor, the mounted filesystem, `IOCTL_CDROM_READ_TOC` and
`IOCTL_DISK_GET_LENGTH_INFO` — split two against two across that gap. Three
earlier discs in this collection carried a tail of **155**; those five extra
sectors were never on a disc, and the question closes here.

The second is a place nobody had looked. This disc has **two primary volume
descriptors**, at sectors 16 and 17, and they are not identical: **344 of 2,048
bytes differ**, every one of them inside the application-use and reserved fields
that ECMA-119 requires to be zero. Sector 17 is clean. Sector 16 carries a run
of twelve 32-bit integers of which **six are exact boundaries of this disc** —
the LBA of `00000001.TMP`, the end of the unallocated hole, the extent of
`00000002.TMP`, and both edges of a region that no filesystem describes at all.
The copy protection wrote a map of itself into the descriptor and left a clean
shadow next to it.

The third is the region those numbers describe, and it is where the session made
its largest mistake. A binary search with cold seeks put the first unreadable
sector at **755**, confirmed three times, stable. It is wrong. An inherited tool
run only to check whether it still applied died on sector **818** instead —
which was one of the integers in the descriptor that nothing had explained.
Fifteen sequential reads from eight starting points then had exactly one
solution: **the drive fetches 64 sectors per request and fails the whole request
if any of them is bad**, so the lowest failing cold seek is 818 − 63 = 755. The
true region is **818 to 10,097, 9,280 sectors, 19,005,440 bytes**, both ends of
it written on the disc by whoever made it unreadable, and the near edge is
invisible to any instrument that only probes one sector at a time.

Inside the 10,000 sectors the layout reserves, 720 read: 745,472 bytes of
high-entropy content that no directory record claims, arranged as nine blocks
of **one sector stored ten times over** at a stride of forty, then a 265-sector
run that stops of its own accord seven sectors before the damage begins.

The content is Epic's format and this studio's decisions. All **249 packages**
parse and five of six oracles pass on every one; the sixth fails eight times and
each failure is a finding, including the two largest files on the disc —
`HPSounds.u`, 29.7 MB of sound effects, and `HPModels.u`, 17 MB of meshes and
textures — wearing Unreal's extension for *code*. The package version field is
Epic's, but its **distribution is this build's**: seven distinct values sorting
the 249 files into layers by when anyone last touched them, from six stock
texture packages fifteen format revisions behind the game down to the 208 built
in the fortnight before the master. The 91 music packages contain **no tracker
module at all** — every one is MPEG-2 Layer II — and of 87 distinct streams,
three of the four duplicate pairs are one cue shipped twice under two spellings
of an apostrophe.

The narrative is measured twice and agrees with itself. `ChangeLevel` strings
inside the map packages give **31 maps in one line**, from `Lev_Tut1` to
`Snapes_Office` to `startup`, with the nine Quidditch maps reachable from code
and nothing else. `System/Dobby.int` — a localisation file for a module that is
not on the disc, named after a character who is not in this book — turns out to
hold a numbering of the same maps, and the two sources agree at **30 of 30 with
zero contradictions**, including the one place the filenames lie: `Lev2_Fire2`
is played before `Lev2_fire1`, and the two stems differ in the case of one
letter.

Twenty-five language tags across fifteen axes and **not one language on all
fifteen**: four dialogue tracks, five menu-art sets, three readmes with no
English among them, five help files in languages the game does not speak, and
one Hungarian texture pack that exists on exactly one axis and in no numbered
directory. `autorun.cfg` settles what the disc is in five lines —
`NumLanguages=3`, Italian, Spanish and standard Portuguese, `English=0` — and
the index behind `System/0`, `1`, `2` is written on the disc four times over as
Windows locale identifiers in sort order, with the three `Default.ini` copies
differing **in three bytes**: `Language=spa`, `ita`, `por`.

**89.09 % of the file bytes were written for this disc**, against 33 % on the
883 CD Extra and 0 % on 1000 Miglia — because by 2001 the licensed engine was
4.25 % of the object and DirectX alone was bigger than all of it. `discdiff.py`
against the eight previously measured trees returns **zero over 16,434 files**,
the seventh zero in seven sessions, including against the DirectX
redistributable that was the first concrete reason in this collection to expect
otherwise.

And the studio's name survives inside the software exactly once, in 540 files:
not in the 6,779-byte credits roll that names a hundred and eighty people and
attributes the work to *"PC Team"*, but at offset 0x25B5C of `System/HPModels.u`,
in a 3ds Max exporter comment recording where it found a bitmap —
`C:\Documents and Settings\dhunt.KNOWWONDER\Desktop\Dhunt\work\Harry Potter` —
attached to the texture of the Golden Snitch.

### [Harry Potter and the Goblet of Fire](https://github.com/vs-sr-dev/pc-harrypotter4-doc)

*Harry Potter e il Calice di Fuoco* (Windows, Electronic Arts, October 2005) —
**1,659 files, 1,369,393,885 bytes, 671,664 sectors, RenderWare on EA's RealCore
6.27.01, SafeDisc 4.50.000.** The second Harry Potter disc in this index and the
second object measured in a drive rather than from a copy. It is also the most
opaque thing here: **93.98 % of it is a single file**, `0compressed.zip`, and
the other 6.02 % is an installer, a technical-support booklet in ten languages,
and a copy protection.

So the session measured the 6 %, and the 6 % turned out to contain a second
filesystem nobody had asked about.

`isodev.py` reports 126 unallocated gaps totalling 2,096 sectors, **79 of them
exactly 20 sectors long**, and a counter shows one appearing after every twenty
files in layout order — 71 times out of 79 at exactly twenty. Reading them
instead of assuming they were empty found descriptor tag `05 01`: a **UDF File
Entry**. The disc carries ISO 9660, Joliet *and* a complete **UDF 1.02**
filesystem, and 1,740 of the 2,096 "unclaimed" sectors are its metadata — one
sector per file, emitted in batches of twenty. Both filesystems describe 1,659
files in 40 folders totalling 1,369,393,885 bytes and agree on every total. The
genuinely spare space on this DVD is 92 sectors.

The second finding is one sector long. The DVD's physical format information,
the drive's `READ CAPACITY(10)`, the Windows device length and the ISO
descriptor all say **671,664** sectors; the mounted volume and every `ReadFile`
say **671,663**. Windows mounts the UDF, whose partition ends one sector early —
and at LBA 671,663, outside that partition, sits the closing **Anchor Volume
Descriptor Pointer** that UDF requires to be at the last recorded sector.
Reading it needed `IOCTL_SCSI_PASS_THROUGH_DIRECT` and a raw `READ(10)`, which
four earlier repositories in this family had carried as an open question and
never attempted. The sector above it returns ILLEGAL REQUEST, and the disc ends
exactly where the physical format information said.

The protection names itself twice. `DIAG.EXE` carries SafeDisc's `BoG_` marker
at file offset **0xFD4** — the same offset as on the 2001 disc — with the
version triple at `+0x20` reading **4.50.000**, against that disc's 2.40.010.
And the primary volume descriptor carries a 267-byte payload beginning exactly
256 bytes into the application-use field, in the same place the 2001 disc put
its own: there, twelve integers of which six were that disc's boundaries; here,
ten of the twelve are zero and the two that survive are **`4` and `50`**.
Meanwhile `00000001.TMP` is 10,001 sectors of high-entropy data whose eight
16-sector blocks fall on **absolute DVD ECC-block boundaries, 18 of 19 run
edges** — placed first and written second — while the 2001 disc's equivalent was
a 10,000-sector hole that could not be read at all.

Nobody signs the disc except the company that cut it. `KnowWonder` appears zero
times in either ASCII or UTF-16; no development studio appears anywhere; the ISO
publisher, application and copyright fields are empty. `*GEAR UDF` appears in
the implementation-identifier field of **every one of the 1,699 File Entries** —
1,717 occurrences in all. What the game executable does name is its middleware:
`RenderWare::AttrHandler::Packet`, `Havok::hkPoolMemory`, and compiler paths to
`C:\packages\realcore\6.27.01\source\file\cmn\big_vfs.cpp` — the virtual
filesystem that reads the four EA `BIGF` archives inside the zip. The only human
being named on the disc is in a Visual Studio home-directory path inside a
support utility, which is the same accident that gave the 2001 disc its studio.

The whole master was assembled in **fourteen minutes and thirty-seven seconds**
on 18 October 2005, from the first `.big` at 20:43:26 to the volume descriptor
at 20:56:09 — and the ISO and UDF filesystems, written by the same program in
the same pass, disagree about the timezone of every file by exactly one hour.
`autorun.cfg` settles what the edition is in one line, `NumLanguages=5`, with
English switched off in both of its variants; the disc names 27 language codes
across ten separate lists, four of which appear on all ten. `discdiff.py`
against the eight previously measured trees returns **zero over 17,553 files**,
the eighth zero in eight sessions.

And the file the previous disc shares a name and a length with — `00000002.TMP`,
317,440 bytes on both — is **73.99 % different**. That comparison needed no
second drive: the 2001 session published enough about its copy (entropy
−0.0000, one byte value in 256) to reconstruct it exactly, which is the one
thing in that repository that can still be compared against anything.

### [Harry Potter and the Order of the Phoenix](https://github.com/vs-sr-dev/pc-harrypotter5-doc)

*Harry Potter e l'Ordine della Fenice* (Windows, Electronic Arts, June 2007) —
**1,187 files, 3,740,991,488 bytes, 1,826,656 sectors, RenderWare on EA's
RealCore 6.27.01, SecuROM.** The third Harry Potter disc in this index, and the
first where the person handing it over expects a sequel and the disc disagrees
in three seconds.

The box is a sequel: same two logos, same case, the actors updated to the fifth
film. The disc is a different object. Where the 2005 DVD says
`GEAR CD/DVD PREMASTERING` and `*GEAR UDF` 1,717 times, this one says `Win32`
and `UltraISO V8.5 CD & DVD Creator, (c) 2006 EZB Systems, Inc.`, with
`*EZB UltraISO` in each of its 1,213 UDF File Entries and nine volume
structures. It is nonetheless a **pressed** disc — `layer type 1` is embossed,
the profile is `0x0010 DVD-ROM`, one track, no session border. An industrially
replicated DVD whose filesystem carries the name of a desktop ISO editor. Who
ran it, and why, is not on the disc, and the repository does not guess.

What the editor did to the layout is measurable, and it is six things. The
sharpest is that **this disc's ISO 9660 is not ISO 9660**: of 1,187 file records
in the *primary* descriptor, **zero** carry the `;1` version suffix the standard
requires, 1,185 contain lower-case letters, 67 contain spaces and 747 have stems
longer than eight characters, the longest running to 52. Joliet exists to carry
names a primary descriptor is not allowed to hold; this primary holds them
anyway, so there is **no supplementary descriptor at all**. The 2005 disc has
three namespaces and this one has two. Everything else runs the same way: 1,213
UDF File Entries in **one contiguous run** where GEAR wrote them twenty at a
time down the length of the volume; **three** gaps of three distinct sizes where
GEAR left 126, seventy-nine of them identical; a partition ending on the last
sector instead of one before it, so Windows sees the whole disc. Reading all
1,521 unclaimed sectors names 1,317 of them, and the genuinely spare space on
this DVD is **204 sectors**.

`toc.py` reports the lead-out at LBA **1,151,849** on a volume of 1,826,656 — a
lead-out 674,807 sectors *before* the end of the disc. It is not a fact about
the disc. `READ TOC` returns each address as three one-byte fields, the largest
expressible value is `255:59:74`, and `(255 × 60 + 59) × 75 + 74 − 150` is
1,151,849 exactly. The tool that proves it carries no disc's constants at all:
fed the two siblings' volume sizes it reproduces **both of their published MSF
values** — `64:59:48` and `149:17:39` — from the definition alone, and then says
this volume would need M = 405.

The protection changed vendor and stopped identifying itself. There is no
`DIAG.EXE`, no `00000001.TMP`, no `BoG_` marker and no occurrence of
`Macrovision` in either encoding. `hp.exe` has **nine** PE sections, not the
five a first reading found: `.text .rdata .data .rsrc` and then **`ars`, `est`,
`artem`, `celare`** and `.securom`. The four added names are the four words of
*ars est celare artem* — "the art is to conceal the art" — with the last two
swapped, which is what the bytes say and is left as it is. `ars` is 5,920,096
bytes at entropy **8.000** marked writable *and* executable; `celare` is a
statically linked **zlib 1.2.2**, Mark Adler's copyright string intact; the
entry point is inside `est`. A sweep of all 10,329,160 bytes finds **no version
string in any shape** — against SafeDisc's 2.40.010 and 4.50.000, both of which
sat at a fixed offset in a file that announced itself.

What the wrapper did **not** eat is the debug directory, because a packed
executable still has to load. Relocated into `.securom`, twenty-eight bytes:
`z:\phoenix\code\release_pc\game\built\pc\hp_unity_f.pdb`. Eleven more source
paths name `eauk_renderframework`, `eauk_shadercore`, `seedrt` and
`realcore\6.27.01` — **the same point release as the 2005 disc**, in the same
three source files, under a different root. And `hp.exe` is Authenticode-signed
to `C=GB, ST=Surrey, L=Guildford, O=Electronic Arts, OU=UK Studio`. Two
structures written by two unrelated tools naming the same organisation is the
strongest provenance result this family has produced; the 2001 disc named its
studio once by accident and the 2005 disc named nobody. `KnowWonder` is still
zero, and so is every actor's surname — the two hits for `Watson` are both
`_invoke_watson`, in Microsoft's C runtime.

Then the streak. `discdiff.py` had printed zero on eight discs running, most
recently over 17,553 files. It ends here, and it ends on nothing glamorous:
**500 files on this disc are byte-identical to files on the 2005 disc**, 40
distinct contents, 32,311,885 bytes — of which 97.8 % is **five DirectX
cabinets** Microsoft did not touch between the two dates, and the rest is the
technical-support booklet's furniture and four RoboHelp build logs that crossed
twenty months untouched. **Not one of the 524 HTML pages matched.** The booklet
is regenerated; only its chrome is copied.

The 2001 disc went back into the drive during the session and its 540 files were
hashed for the first time, closing the family's oldest open item — and the hole
that repository measured, 9,280 unreadable sectors, turns out to touch no file
at all. It shares **zero** files with either DVD. Four years, a change of
medium, a change of engine and a change of studio transmit nothing; twenty
months and the same building transmit forty distinct contents. Three points,
with two consecutive products missing between the first and the second, and — as
the repository says in its own first chapter — that is two differences that
agree, not a series.

Smaller things that are still measurements. Forty controller maps named both as
DirectInput GUIDs and as English device names, whose **twelve content groups
pair the two schemes** and thereby prove, from this disc alone, which half of
the GUID is the vendor. `Localization.ini`, UTF-16LE, twenty-four language codes
in each of five sections — and a commented-out block still carrying **FIFA 2004,
FIFA 2005 and Madden 2005** patch URLs, which is what a publisher-wide template
looks like from the inside. Two ZIP archives with no ZIP64 locator, the first at
**97.55 % of 2³¹** with no remaining member small enough to fit, which is the
whole reason there are two rather than one. Forty-three signed Microsoft
cabinets, each with a bare PKCS#7 appended and **no** `WIN_CERTIFICATE`
header — an eight-byte difference from a PE, and the reason the reader written
for them called all forty-three unrecognisable on its first run.

### [Age of Wonders II: The Wizard's Throne](https://github.com/vs-sr-dev/pc-ageofwonders2-doc)

*Age of Wonders II: The Wizard's Throne*, PC CD-ROM, June 2002. Volume `AOW2`,
335,261 sectors, 686,614,528 bytes, **thirty-six files in thirteen folders** —
one twentieth of the file count of the disc measured before it, and the first
title in this list that is not a tie-in of anything.

**The subject is the space no file claims.** 80,163 sectors, **23.91 % of the
volume**, in four gaps. The largest is 70,125 sectors sitting between the last
file and the root directory, and it is not filler in the sense that word usually
means: every sector of it is an arithmetic progression modulo 256, and the whole
region is one formula.

```
    byte[i] of the sector at LBA  =  ((LBA + 82) * (i + 77)) mod 256
```

Checked against **all 2,048 bytes of 70,115 of the 70,125 sectors** — 143,595,520
bytes, 99.9857 %. The ten that do not match are the last ten before the root
directory and they are zeros. The formula was written as a prediction, derived
from five eight-byte samples, before the region was read; it agreed with 69,842
of 69,842 sectors on the first pass. The sectors that come out all-zero are not
an exception to it: they are the sectors where `LBA ≡ 174 (mod 256)`, the step is
zero, and the pattern degenerates.

**The other gap contains damage, and the disc knows where it is.** Like the 2001
*Philosopher's Stone* CD, this one has two primary volume descriptors where
ISO 9660 expects one, identical in every defined field and differing in **305
bytes** the standard requires to be zero. Four little-endian integers sit inside
those bytes. Two are ordinary layout — the LBA of a protection file, the end of a
gap. The other two are **807** and **10,265**, and they are the first and the
last physically unreadable sector on the medium: `key 3 MEDIUM ERROR, asc 11
ascq 00`, with 806, 808, 10,264 and 10,266 all reading in the same pass. Neither
number is a boundary of the filesystem; the only way to find them from outside is
to ask the drive one sector at a time and wait seven seconds for each refusal.
The damage is not a contiguous region, as it was on the 2001 disc — it is
**isolated single sectors**, sampled at 6.17 % of a 9,476-sector region.

Getting there cost four hours and produced a result about the *reading* before
any about the disc. The inherited full-pass tool reads 1,024 sectors at a time;
this drive refuses anything over **707** through the volume device and over **32**
through SCSI pass-through, and refuses the first kind by timing out for 8.7
seconds. A full pass would have taken about **ten hours on an undamaged disc**.
Worse, a multi-sector read fails whenever *any* sector inside it is bad, so a
32-sector scan reports thirty-two dead sectors where there is one. And a drive
that has absorbed some sixty unrecoverable errors starts failing on sectors it
read correctly minutes earlier — which this session discovered by concluding,
reproducibly and wrongly, that 143 MB of perfectly good padding was unreadable.
Opening and closing the tray fixed it. Every damage figure in the repository
comes from a run with known-good control sectors interleaved.

**A Delphi game.** `AoW2.~ex` and `aow2Installer.exe` both begin `MZP`, both
declare linker 2.25, and both carry COFF timestamp `0x2A425E19` — 1992-06-19
22:22:17, which is not a date but the constant Borland's linker writes into
everything. The executable has sections named `CODE`, `DATA` and `BSS`, no Rich
header, and imports `Vcl50.bpl` and `Vclx50.bpl`; the only build paths that
survive anywhere end in `.pas`, under `d:\aow2\engine\`. The eleven ZIP archives
that are 92.07 % of the disc are ZIPs because the installer was built around
**VCLZip**, a Delphi component whose unregistered-version nag string ships in the
retail installer.

SafeDisc **2.60.052**, with `BoG_` at **0x3D4** rather than the 0xFD4 of the two
Harry Potter discs — and the wrapper is not opaque. It encrypts one section of
eight and leaves `.rsrc` alone, so the disc names, in plaintext and with offsets,
**Triumph Studios**, **PopTop Software**, **Take Two** in five offices, **Miles
Sound System**, **Bink Video** and — in the Italian readme and licence —
**Cidiverte**. `Gathering of Developers, Inc.` holds the copyright in the English
readme and is thanked in the credits for its *ex*-Dallas staff, in the same
binary, in June 2002. Every claim on the case lid, confirmed from the software:
the first time that has happened in this list.

Two more measurements worth the space. The two files with the strangest names on
the disc, `00000000.016` and `00000000.256`, are **bitmaps** — the same 640 × 480
protection dialog at 16 and at 256 colours, and the file names are the palette
sizes. Decoded and compared, **not one pixel of 307,200 is the same colour in
both**, because the two quantisations share exactly one palette entry of sixteen.
And there are **seven** language folders, four of them completely empty, against
six languages in an undocumented `MLD` dictionary that this repository wrote a
reader for — a dictionary in which Spanish does not appear, though the disc ships
a Spanish licence for a Spanish build it does not contain.

**And the collection's first crossing between two publishers.** Two of the
thirty-six files are byte-identical to files on the 2001 *Philosopher's Stone*
disc: `cfgmgr32.dll` and `setupapi.dll`, 383,248 bytes, the only two of nine
DirectX files whose sizes agree to the byte and the only two Microsoft linked in
**1997**. Zero against the 2005 and 2007 DVDs and zero against eight trees on
disk — 19,314 other file records. The eight-disc run of zeros that ended twenty
months and one building apart now has a second exception, and this one crosses
two companies. It is a measurement about Microsoft, not about either game.

The **Saga** cell is deliberately empty. *Age of Wonders* is a series and this
list holds one of it; the rule this collection has applied twice — to Harry
Potter until the fourth disc arrived, and to Baron Baldric until *Mystic Towers*
did — is that a saga of one is not a saga. The cell fills in when a second Age of
Wonders disc is measured, and not before.

### [Il cane di terracotta](https://github.com/vs-sr-dev/pc-canediterracotta-doc)

*Il cane di terracotta* (November 2000) — **the second entry in this index that
is not a game**, after *Viaggio al centro del Mondo*, and the two are close
relatives: both Italian, both Macromedia Director, both either side of 2000. It
is an interactive cartoon of Andrea Camilleri's Montalbano novel, and it is the
**first hybrid disc in this family** — the first whose answer to "how many files
are on it" depends on which operating system you ask.

Windows mounts the ISO 9660 volume and reports **2,374 files in four folders**.
The HFS volume that lives on the same sectors reports **2,401 in eleven**. The
briefing that opened the session called that a difference of 27 files and 6
folders; counted consistently it is **28 files the PC cannot see, 1 the Mac
cannot see, and 7 folders**, because the HFS header excludes the root and the
ISO count includes it. Nothing inherited into this collection reads HFS, so the
partition map, the Master Directory Block and the catalog B-tree were read from
the structures up, addressed and never scanned.

**The two catalogues describe one disc, not two.** 2,372 of the 2,373 shared
paths begin on **exactly the same sector**, and the reason is one line of the
volume header: the HFS allocation block is 10,240 bytes — five sectors — and the
first one lands on **LBA 1610 = 5 × 322**. Every file therefore sits on a
multiple of five, and the padding after each one follows
`gap = (-ceil(size/2048)) mod 5` at **100.0000 % over 2,370 files, with no free
parameters**. The ISO volume was not built beside the Macintosh one; it was built
over it, on a grid that already existed.

**One file breaks it, and breaks it four ways.** `Data/Varie.cst` is `XFIR` at
LBA 1,558 and `RIFX` at LBA 110,175 — two addresses 108,617 sectors apart, two
lengths ten bytes apart, two timestamps 3 m 45 s apart, and the two byte orders
of a Motorola and an Intel processor. It is the **only Intel-order container
among 139**, and those ten bytes are the only quantity that does not cancel when
the two filesystems' totals are reconciled. The disc's other off-grid file is
`Installa.exe`, and the pair of them are exactly the two files the Macintosh
volume does not place.

**What Windows cannot see is the whole Macintosh half**: a Director projector
with the movie welded into its tail, five `.dxr`, two `.cst`, ten PowerPC Xtras —
three of which name Shockwave Audio, so the audio format is identified by the
decoder the disc ships rather than by a file extension — plus four files whose
*names* ISO 9660 cannot express, because they end in a carriage return. Under it
all sits the debris of the machine that built it: the Finder's desktop database,
an AppleShare index, an empty SimpleText document called *Copiami sull'Hard
Disk* whose entire content is its own name, and **a Norton AntiVirus 6.0 scan
cache** that somebody's Mac left in the folder and Toast pressed onto the disc.

**And there is a Windows machine in it.** Every one of the 517 Shockwave Audio
files carries a few hundred bytes of uninitialised memory in its header. Read
little-endian, the address `0xBFF713EE` appears in **510 of the 517** and three
neighbours in 509 each — 39 distinct values in the 64 KB window where Windows 95
and 98 map `KERNEL32.DLL`, **enriched 1,423 times over chance**. The disc is
Macintosh in its filesystem, its partition map, its byte order, its build paths
and its executable format; its three hours of audio were encoded somewhere else,
and each file leaks the same four stack frames of the machine that did it.

Those three hours are the other arithmetic. The sales blurb promised "over 40
minutes of original music"; the measurement is **3 h 00 m 45 s** by sample count
and 3 h 02 m 05 s by file size, two calculations from disjoint header fields
agreeing to 0.74 %. It promised fifteen games and the disc has **fourteen**,
numbered `Gio01` to `Gio15` with a hole at fourteen that occurs in no byte of the
medium. And it promised a Vigatese dictionary of over 750 entries, which cannot
be counted at all: **the entire text content of this disc is 1,620 bytes in 46
chunks, and every one of them is a number** — the games' clocks, and empty
save-name boxes. `Camilleri`, `Vigàta`, `perché` and `città` each occur **zero**
times across seven encodings. The words were set in Photoshop and shipped as
pixels, 397 MB of them.

**The Saga cell is deliberately empty.** *Il cane di terracotta* belongs to one of
the longest series in Italian fiction, but this list measures **software**, and
of Montalbano software there is exactly one. The rule this collection has applied
three times — to Harry Potter until the fourth disc, to Baron Baldric until
*Mystic Towers*, and to *Age of Wonders II* which is still waiting — is that a
saga of one is not a saga.

**The Studio cell names two parties because the disc does.** `Installa.exe`
carries `CompanyName` `IM*MEDIA`; the volume label is `SELLERIO`, which is the
publisher of the novel and the first time in this collection that the name on the
box and the name in the descriptor are the same name. They are different things
and the cell keeps them apart. The Year is **2000** from the ISO descriptor
(2000-11-25), which is the date the object in hand was made; the HFS volume is
five days older and the one executable was linked in April.

It is also the first disc of this family with **no protection at all**, and the
first whose `application use` and `reserved` descriptor fields are genuinely
zero after four discs that all carried something there. And it shares **nothing**
with anything else here: 0 files in common over **19,458 records**, four
published hash lists and nine working trees — including against `pc-883d-doc`,
which shares a vendor with it and not one component, because Macromedia's runtime
is PowerPC code on one disc and Win32 PE on the other.

### [CLIC 11](https://github.com/vs-sr-dev/pc-clic11-doc)
**The twelfth disc measured here and the first that is not an opera.** Eleven of
the previous twelve were monographic — one game, one cartoon, one CD Extra — and
every instrument in this collection was built on that assumption: `discdiff`
looks for files shared *between* discs, `clocks` looks for clocks that *ought* to
agree, `whose` looks for *the* producer. On a magazine's cover disc all three
assumptions are false by construction, and the useful question inverts: not *is
this coherent* but **how heterogeneous is it, and does the layering read from
the bytes**.

It does. `CLIC_11` on the ISO side, `CLIC! 11` on the HFS side — the magazine's
exclamation mark survives only because ISO 9660 cannot spell it and HFS can —
mastered by **Toast 3.5.2** on 20 October 1997 at 15:57:10 GMT and closed
thirty-seven seconds later. Eleven bodies of work, four and a half years apart at
the extremes: a **rolling demo of Microsoft Encarta 98** (33.76 %), the whole of
the 1996 Mondadori adventure **Wolfgang il cyberlupo** (33.99 %), a
Hewlett-Packard promotional website about Italian football (14.67 %), **Internet
Explorer 4.0 build 1712** in 121 signed cabinets (10.27 %), FrontPage 98, a
FileMaker Pro 3 database of the magazine's reviews, an LCSI MicroWorlds demo, and
the magazine's own Director browser in two platform builds. **What the editorial
staff made is 3.37 % of their own disc.**

**The file count is a property of the walker, and this is the disc that proves
it.** Windows shows 857 files. The ISO 9660 volume holds **875 directory
records**: eighteen of them carry **File Flags bit 2, the Associated-File flag of
ECMA-119 §9.1.6**, which means "this record describes a file associated with the
next record of the same name" and which Toast uses for the **Macintosh resource
fork**. The Windows CDFS driver implements that bit by not showing you the
record. Every one of the eighteen lengths matches, to the byte, the `rsrc_len`
the HFS catalogue records for the same file — two structures written by two
halves of one program in 1997, agreeing on eighteen numbers. Three of the
eighteen have a data fork of **zero bytes** and 528,413 bytes of 68000 machine
code in the fork: Macromedia's Shockwave Audio Xtras for Macs without a PowerPC,
which on the PC side are three empty files with meaningless 8.3 names. Add the 23
files that exist only in the HFS catalogue — a Macintosh Internet Explorer
installer, a FileMaker runtime, an application whose entire content is a 1.4 MB
resource fork, and the Finder's own desktop database — and **26,607,777 bytes of
this disc, 4.02 %, cannot be read by any Windows machine**, including the one
that made the copy this work started from.

**Two sectors out of 322,926 belong to nobody.** Building an ownership array over
the whole volume and letting five claimants write into it — ISO metadata, ISO
extents, the Apple partition map, HFS volume structures, HFS forks — leaves
**4,096 bytes unclaimed, both sectors zero**, between the last ISO file and the
start of the Apple partition. **46.7 % of the disc is claimed by both catalogues
at once**, which is what a hybrid *is*, and no sector is claimed twice by two
records of the same catalogue. The HFS lattice comes out closed: allocation
blocks of 6,144 bytes = exactly three sectors, first block at LBA 159,494, so
`LBA(n) = 159494 + 3n` with **both constants read out of the Master Directory
Block and neither fitted**. Under that formula every one of the **385 forks
present in both catalogues resolves to the same LBA — 385 comparisons, zero
disagreements**: the disc was built in one pass and nothing on it was written
twice. Two of the three sectors that first came out unclaimed were bugs in the
tool; the third was the **HFS alternate Master Directory Block**, sitting in the
very last sector of the volume and announcing itself with `BD` and the volume
name. The last sector of this disc is a backup copy of its own name.

**Ninety-nine point one one per cent of the directory records have an even
seconds field.** MS-DOS packs a file time into sixteen bits and leaves seconds in
units of two; HFS does not, and ISO 9660 has a whole byte for them. So a disc
mastered on a Macintosh, by a Macintosh program, into a filesystem that could
have recorded odd seconds, has **891 of 899 records on the FAT grid** — because
the material arrived from PCs and Toast copied the timestamps rather than
restamping them. The eight exceptions are the whole counter-example and they are
legible one by one: **three files, all of them among the eighteen with a resource
fork**, and two directories made on the mastering Mac in the last two days.
Alongside it, 18.02 % of records land on `:00` seconds against 1.67 % by chance
and 13.13 % on an exact hour against 0.0278 % — twenty-two files in the Internet
Explorer folder share the timestamp `1997-09-14 05:00:00` **to the second**, and
one cabinet among them, `DXDDEX.CAB`, contains members dated three and a half
days *later*, which is impossible by copying and proves all twenty-two synthetic
from a single file.

**The difference between two clocks turns out to be a place.** Every directory
record on the disc carries a GMT offset of zero and a COFF `TimeDateStamp` is UTC
by definition, so for files recorded on the same day they were linked the
difference between the two is the **time zone of the machine that did the
linking**. Seven LEADTOOLS DLLs come out at **+4.00 h** in October 1996 and four
MicroWorlds DLLs at **+5.00 h** in January and February 1997 — North American
Eastern Time, with its daylight saving, recovered from an Italian magazine's
cover disc in a field that was never meant to record a zone. Getting there
required fixing a tool that had read the same clock through the Windows
filesystem and reported eleven files as *written before they were linked*: an
error that was hiding a finding.

**And the eight-disc run of zero shared files ends properly.** The tenth session
in this family formulated the rule — *two discs share files only where they share
a third party's component* — and the two discs after it had almost no
third-party components to test it with. This one is made of little else. Against
**21,870 records**, five published hash lists and nine working trees, there are
**two crossings and both are Microsoft redistributables**: `DXMINI.CAB`, 339,279
bytes of DirectX mini-installer, and a 22-byte `FILELIST.DAT`, both identical to
files on *Viaggio al centro del Mondo* a year later. Not one JPEG, not one
Director movie, not one HTML page crossed. The same mechanism fires *inside* the
disc too: the MS-Setup loader that installs Video for Windows 1.1 for the Encarta
demo is byte-for-byte the loader that installs Win32s 1.30c for the magazine's
database, 24,624 bytes, recorded 1993-11-18 in one folder and 1996-04-27 in the
other.

Three smaller things worth the sentence. The 171 underscore-suffixed files are
not one format but **two Microsoft compressors — 98 SZDD, all of them in one
folder, and 72 KWAJ, all of them in another, with zero overlap**, which is the
sharpest stratigraphic separation on the disc and was invisible until a tool that
read them all as SZDD reported containers that had *grown* under compression. The
magazine's `.clc` database is a **FileMaker Pro 3** file — `FMP3`/`NFIN` on the
Mac side, six Claris `CompanyName`s on the PC side — whose Windows copy contains
**680 accented Italian letters, every one of them MacRoman and not one Latin-1**,
so the PC users got the Macintosh file; and 1,408 bytes of its free space are
filled with *All work and no play makes Jack a dull boy*, which is what FileMaker
writes into unused blocks. And the root of the disc is somebody else's: eight of
its nine entries are the **1996 Wolfgang CD-ROM's root, copied whole**, including
an `AUTORUN.EXE` with no `AUTORUN.INF` to start it — so the program designed to
autorun does not, and the browser that should have does not either.

**The Saga cell is deliberately empty, and this is the first object where the
rule and the intuition pull apart.** A magazine *is* a series; issue 11 implies
issues 1 to 10. But the rule this collection has now applied five times — to
Harry Potter until the fourth disc, to Baron Baldric until *Mystic Towers*, to
*Age of Wonders II* which is still waiting, and to *Il cane di terracotta* — is
that **a saga of one is not a saga**, and of CLIC there is exactly one disc here.
If CLIC 12 ever arrives the cell fills then, and the fact that a periodical
*obviously* has siblings is precisely the intuition the rule exists to resist.

**The Studio cell names the magazine and the write-up has to say why**, because
this is the first disc here where "who made it" and "whose code is in it" give
different answers and both are defensible. A byte census attributes 32.14 % of
the disc to **Macromedia**, which is true — every Director movie carries
Macromedia's copyright — and useless, because Macromedia did not make Wolfgang.
Turning on the weakest evidence grade attributes **186 MB of a 1996 Italian
adventure game to Microsoft** because one Microsoft-linked helper DLL sits in the
game's data folder, which is why that grade is off by default. The disc names its
own maker in the volume identifier and in **no other field**: publisher, data
preparer, copyright file, abstract and bibliographic are all empty on both
descriptors, and `Clic95.exe`'s `CompanyName` reads `Macromedia, Inc.` because it
is a Director 6 projector — with the *same COFF timestamp*, `1997-05-10
22:42:39`, as the Encarta demo's executable, since both are built on one stub.

The **Year is 1997** from the descriptor, and the cell needs the caveat that
**fifty-seven of the disc's files are from 1993**: the date of a disc is not the
date of its contents, and this is the first object in this list where that
distinction carries a third of the bytes. Leftovers come to **3,813,223 bytes,
0.5766 %** — the largest share this collection has measured, and composed
differently from the last: not a virus scanner's cache and leaked memory, which
are traces of a *machine*, but duplicates and superseded originals, which are
traces of an *assembly*. Chief among them, 1.8 MB of a 1996 game's discarded
working files, saved as `.OLD` beside the versions that replaced them and
pressed onto two CD-ROMs anyway.

### [Tubular Worlds](https://github.com/vs-sr-dev/pc-tubularworlds-doc)
**The thirteenth object measured here and the first that is not a medium.** The
twelve before it were discs, and every one of them carried a notary: an ISO 9660
primary volume descriptor states when the volume was built, by what program, how
many sectors it holds and where they stop. It is a field, in a fixed place, that
a mastering program wrote once and that nothing since had a reason to touch.

This is a **downloaded folder**: 107 files, 3,432,758 bytes, eight directories on
an NTFS volume. There is no such field, and there is no analogue of one. So the
first question is not what is inside it but **what it is**, and the answer has to
be built from the bytes.

**It came out of a DOS-era archive, and three columns prove it.** All eight
directories carry today's date and all 107 files carry 1993 or 1994 — the split
the person who handed it over predicted, with zero exceptions in either
direction, and the eight directories were made inside **1.547 seconds**. Then:
**every one of the 107 file times has an even seconds field.** MS-DOS stores a
file time in units of two seconds and the ZIP local header inherited that field
unchanged, so a timestamp off a 1994 FAT filesystem *cannot* carry an odd second.
107 of 107. **Every one has a zero sub-second field**, because a DOS-derived time
has nothing to put in NTFS's 100-nanosecond units. And **not one file has a
creation time at or before its modification time**: each was created here at
09:36:33 and then stamped 1994 — born older than it is, which is impossible for a
file actually written on this volume and is exactly what an extractor does.

**The boundary had to be rebuilt from the inside, and it closes.** A 1994 game
does not store 107 filenames; it stores **stencils** — `TEDIT/MAP/MAP00.DAT`,
whose two digit positions are overwritten in place before the open, which in real
mode costs two `MOV`s and no stack. Five such tables sit in `PART2.EXE`, one per
scene, and every path in them uses forward slashes, which DOS has accepted since
version 2.0 and almost nobody used. Matching literals, stencils and assembled
names against the tree: **106 of 107 files are reachable, and the 107th is
`TUBWORLD.BAT`**, the four-line batch file the player types. 3,432,724 bytes of
3,432,758. There is no dead file here, nothing forgotten and nothing dropped in
later — which on eleven previous objects was the side that always paid.

**The whole game is drawn from a 64-byte tile, and the arithmetic found it before
the picture did.** `TEDIT/CHAR` is 55.54 % of the object and eight of its files
are exactly 172,368 bytes, which factors as 2⁴·3⁴·7·19 and is therefore not a
width times a height. Two observations open it: seven of the fifteen banks are
**exact multiples of 64 once 768 bytes come off the end** — 768 being 256 palette
entries of three bytes, none above 0x3F, which is the VGA DAC's six-bit ceiling —
and the tile indices across all twenty-one maps form the **dense range 0..2639,
2,640 distinct values, every gap exactly 1**. That caps a tile at 65 bytes, which
forces 64, which is 8×8 at one byte per pixel in VGA mode 13h. Rendered,
`MAP9A.DAT` and `MAP9D.DAT` — two files nothing in the executables names — read
**GET READY** and **GAME OVER**.

**A closed form that holds thirty-five times, and the two that break it break
together.** `size = w·h·k + 4` on every `MAP` and `OBJ` file, with the map and the
object grid of each level declaring the same width and height sixteen times out
of sixteen. Level 3 breaks it in both files with the identical four bytes
`a9 00 30 00`. The obvious reading — the header is corrupt, the real width is
200, since (19,204−4)/(48·2) = 200.000 — is **wrong**, and proving it wrong took
three measurements: the autocorrelation of the payload's zero map peaks sharply
at lag **169** (0.9811) and sits at chance at 200 (0.6466); rendered at 169 the
level is a coherent picture and at 200 it is a diagonal shear; and the content
stops at exactly row 47, the last row the header declares, dropping from fifty
non-zero cells to seven at row 48. **The header is right and the file is 1,488
cells too long**, in both members of the pair — 4,464 bytes of buffer nobody
trimmed.

**The loading screens are Amiga-format pictures that never saw an Amiga.**
`LG01.DAT` and `LG02.DAT` are IFF ILBM, 640×480 in four bitplanes, ByteRun1, and
both decode to **exactly 153,600 bytes** consuming their input to the last byte.
They hold six chunk types, not the four the game's parser names — and three of
the extra ones, `DPPS`, sixteen `CRNG` and `TINY`, are **Deluxe Paint's**
signature, which is how the paint program gets named in a document where nothing
says it in words. The palette settles the platform: every byte of both `CMAP`
chunks is 0 or congruent to **3 modulo 4**, which is a six-bit value widened by
`(v<<2)|3` — the **VGA DAC**, not the Amiga's four bits per gun widened by 17.
And 640×480 in four planes is not an Amiga mode at all; it is IBM VGA **mode
12h**, which `PART1.EXE` sets sixteen bytes before it draws.

**A German keyboard, in a lookup table nobody wrote to be read.** Fifty-eight
bytes compiled into both game programs, indexed by IBM scancode from zero — `1`
at 0x02, `Q` at 0x10, `A` at 0x1E, `M` at 0x32, and a space at 0x39, which is the
space bar. The nationality is forced by two positions in opposite directions:
**`Z` at 0x15 and `Y` at 0x2C**, which a US layout has the other way round.
Nineteen people are named in the end credits, `mueller` and `guedelhoefer` with
their umlauts spelled out because the font has forty glyphs and none of them is
`ü`; **no company is named anywhere**. And at `PART2.EXE`+0x18d25, alone in
eighty-six bytes of zeros, in capital letters the game's font cannot draw, there
is `TODAY IS HER BIRTHDAY`.

**The compiler is not recoverable, and that is a measurement rather than a gap.**
`PART1.EXE` and `PART2.EXE` carry no toolchain banner, no runtime library string,
no error table and no floating-point message; they have **2 and 10 relocations**
where a compiled 115 KB program has hundreds, entry points sixteen bytes into the
image, and prologues that push every register in order. The absence is real, not
a broken search: `Borland C++ - Copyright` is found five times in
[pc-mystictowers-doc](https://github.com/vs-sr-dev/pc-mystictowers-doc) and once
in [pc-1000miglia-doc](https://github.com/vs-sr-dev/pc-1000miglia-doc) by the
same needle. What the two programs *do* share is **834 bytes of code**, longest
run 368 bytes, containing `MOV AH,48h / INT 21h` and `MOV AH,49h / INT 21h` — the
DOS allocate-and-free pair behind their shared message `ERROR: Memory allocation
failed!`. Against `CHECKMS.EXE`, whose TopSpeed/Clarion runtime makes it a
different chain entirely, the same measurement returns **0.00 %**. That negative
control matters: the first version of the tool, before it skipped runs of zero,
scored 48.9 % on it.

**Fifty-five bytes belong to a person.** `HOF.DAT` is dated 1994-05-31, four and
a half months after the January mass and six weeks after the last program, and it
is five records of eleven bytes — three characters of name, six ASCII digits of
score, a NUL, and a level. All five differ from the table compiled into
`PART2.EXE`; the scores are ten to fifty times the defaults they replaced; two
entries share `093750` to the digit, which is what happens when somebody plays
until they match a number on the screen; and one name is three spaces. This is
not the game as it shipped — it is **one person's copy of it**. The shipped
defaults are worth a line of their own: read in order and reversed, the five
names `loo ocs ien ino rez` spell `zeronineiscoool`.

**Zero of 23,631, and the number is defended rather than announced.** Eight
published hash lists and ten working trees, and not one file crosses. The single
third-party candidate is `CHECKMS.EXE`, 8,154 bytes of TopSpeed/Clarion runtime
wrapped around a check that refuses to run on MS-DOS 1.x — in 1994, nine years
after DOS 3.0 — and `TopSpeed RTL (C) Clarion Software Corporation` appears in
exactly **one of eleven trees searched**, this one. The tenth session's rule
survives with its prediction intact.

**And this is the first object in this list small enough to finish.** Twelve
600 MB discs could not honestly publish *how much of this do we know*; at 3.4 MB
it can be checked, and the tiers were defined before they were counted:
**85.447 % structured** — inside a region whose extent a verified rule produces —
**74.383 % decoded**, and **0.161 % residue**, bytes known to be unread. The
14.392 % that is neither is `.SHP` and `.ZMP` exactly, the two formats that do not
state their own length: the sprites are VGA mode-X planar and fourteen of them
render correctly, the music has event streams with monotonic timestamps, and
neither carries a size table anywhere. Leftovers come to **9,043 bytes, 0.263 %**
— the lowest rate this collection has measured, and a direct refutation of the
briefing's headline guess that a directory called `TEDIT` would turn out to be a
development tool's droppings. It is 78.96 % of the object, it holds every map and
every tile bank, and the game opens all four of its subdirectories by name.

### [Mega Man](https://github.com/vs-sr-dev/pc-megaman-doc)
**The second object in this list that is not a medium, and the first that had to
be *rendered* before it would say who made it.** *Tubular Worlds* was a folder of
107 files with no volume descriptor; this is a folder of **29 files and 346,995
bytes** with the same absence and a worse provenance — the only file that names a
publisher is a 184-byte BBS descriptor written on **2011-01-22**, twenty years
after the game, describing a `.zip` that is not here.

**And it is the most judged object this collection has opened.** *Mega Man* for
DOS is routinely listed among the worst conversions ever published. That is a
fact about its reception, it was true before this repository existed, and the
useful consequence of it is that **nobody ever opened the files**: the only
modding reference that carries a page for this game marks every one of its
formats *not editable* and documents none of them. Thirty-five years of
commentary, zero hex editors.

**The executable is nine tenths air, and the framing everyone repeats is
backwards.** `MM.EXE` is 20,349 bytes, EXEPACK'd, and unpacks to **exactly
211,712 bytes with zero packed input left over** — a written unpacker, verified
against `dest_len` before anything was read out of it, with the relocation table
located by trying every offset in the 685-byte stub and keeping the one where
sixteen length-prefixed groups close **exactly** on `exepack_size`. There is one
such offset and it holds 176 fixups. But **91.8 % of the expanded image is
zero**: content occupies two regions and comes to **17,415 bytes**. So the
ten-to-one is a fact about a linker's BSS, not about density — and the real
finding is the other way round: `.BIN` turns out not to be data at all but
**five separately built, position-independent 8086 modules**, one per stage,
42,449 bytes of them, that far-return to the resident core. **Seventy-one per
cent of this game's code is not in its executable.** The check that proves they
are modules rather than blobs: every `cs:[imm16]` reference in all five files
lands inside its own file — **2,318 of 2,318**.

**One codec, and one byte in it that a stock decoder gets wrong in silence.**
Maps, tiles, sprite banks and screens all go through the same run-length coder,
and it is PackBits with a single deliberate difference: **`0x80` is a run of 129,
not the reserved no-op Apple documented in 1984.** Decode this game with a stock
routine and the four fixed screens come out perfect while every stage map is
short by a few hundred bytes and still looks structured. It was caught by
arithmetic, not by eye: `SECUR.SCN`'s opening tokens must sum to the width in its
own header, and `129 + 55 + 16 = 200` while `71` is nothing.

**Two planar layouts in one game, and the wrong guess about either produces a
picture.** Backgrounds are four EGA bitplanes interleaved **one row at a time**;
sprites are **five** planes interleaved **every byte**, mask first. Read the
background as chunky and the credits screen decodes into three vertical bands of
legible-looking noise; read it plane-major and it becomes four bands of
text-shaped noise. Read the sprite mask as the last of the five instead of the
first and all 305 frames come out the right shape in the wrong colours — a white
Mega Man instead of a blue one, with no length check anywhere to complain. **A
wrong planar guess does not look like static.**

**Every format closes, and each closes on a number it did not have to.** `.SCN`
is `13 + width·height` bytes with the stage's own name at offset 4, exact on 5 of
5 with the input consumed to the byte. `.BLK` is 41,984 = **328 records of 128
bytes**, identical on all five stages despite compressed lengths spanning three
to one — and a map can address only **0..215** of those 328, the rest being the
heads-up display and, above record 320, **1,024 bytes the compressor itself flags
as not-tiles** by being the only region it does not encode one tile at a time.
`.FRM` is 305 per-frame records chained head to tail, **eight files, eight chains
ending exactly on EOF**. `.STA` is 30,720 = **320 × 192**, and its encoder is so
strictly row-aligned that all 192 row boundaries in all four files land on a
token boundary: **768 of 768**.

**The two shared blocks the briefing found turn out to be the same fact.** The
1,227 bytes common to all five stage sprite banks are **thirteen whole frames** —
the buster shot, the pickups, the explosion, the life icon — and the divergence
at offset 1,229 is frame 13's width byte in every one of the five. The 234 bytes
common to all five stage code modules are **13 × 18**: the hit boxes of those same
thirteen frames, in a table that holds exactly `18 × frames` bytes where `frames`
is the count in the matching `.FRM`, on all five, with neither file storing the
other's number.

**The screen is sixteen pixels wider than the screen, and two unrelated numbers
say so.** The sprite blitter's destination row pitch is an immediate: `mov bx,
2Ah` — 42 bytes, where 320 pixels is 40. The buffers the CGA and Tandy paths ask
DOS for are `mov bx, 888h` — 34,944 bytes, which is `(42 × 4) × 208`. A **336 ×
208** page for a **320 × 192** display: sixteen pixels of horizontal margin and
sixteen rows of vertical, which is what you build to scroll an EGA by moving the
CRTC start address instead of redrawing. One number out of a blitter, one out of
a DOS call, and they agree.

**The game has no text.** Twenty-two printable literals in the entire unpacked
executable — the options menu and a table of twelve filenames — and **no
copyright, no build path, no runtime signature and no compiler banner of any
kind**, which for a 1990 MS-DOS executable is itself a finding. Three of the menu
strings the briefing quoted turned out not to be strings: `CGA-`, `EGA2` and
`VGA7` are `CGA`, `EGA` and `VGA` followed by the **column byte of the next
record** in a display list of `[column][row][length][text]`. The menu offers four
graphics adapters and the program contains three initialisations; `VGA` resolves
to the EGA path, and there is no write to the VGA DAC anywhere in the image.

**So the only attribution in 346,995 bytes had to be decompressed,
un-interleaved, palette-corrected and looked at.** `CREDITS.STA`, rendered, gives
the concept to **Capcom** and **design, graphics, programming and sound to
Stephen Rozner** — four disciplines, one name — with two people thanked.
`LOGO.STA` carries `© 1990 CAPCOM CO.,LTD.`. Hi-Tech Expressions appears nowhere
in the object.

**And the copy protection is not a password system.** `PASS.FRM` renders `FIND
THE PICTURE IN THE MANUAL AND TYPE IN THE NAME`, holds twelve creatures and the
letters A–Z, and the **twelve accepted answers** sit in the executable in a
private alphabet that turns out to be **the glyph's own frame index minus
thirteen** — `0x00` a space, `0x01` a hyphen, `0x02` an `A`. Twelve pictures,
twelve names, index for index: `BATVIRE`, `FROGBOT`, `SEWER RAT`, `PIRANHA`,
`EEL-ECTRIC`, `RAPTORBOT`, `INSECTOBOT`, `SPYDROBORG`, `SENTRY BEE`, `DRILL
PRESS`, `ARMY ANT`, `ASSEMBLER`. The single `0x01` in the whole table is the
hyphen in `EEL-ECTRIC`, and it is the byte that proves the alphabet.

**The clocks hold a tool changing in the middle of an evening.** Four
`.SCN`/`.BLK` pairs were written on 1990-09-30 in three minutes and ten seconds,
and `DYNA`'s pair 26 days later. But the compressed streams group them
differently from the calendar: `SECUR.BLK` and `DYNA.BLK` emit runs of 129 and
the other three cap at 128 — so the compressor changed in the two-and-a-half
minute gap before `SECUR` was exported, and `DYNA` went through the new one four
weeks on. Then `PASS.FRM` twelve seconds after `CREDITS.STA` on a Sunday night,
and **24 days 8 hours** of nothing but the executable.

**Leftovers: 34,308 bytes, 9.89 %**, and half of it is **152 tiles that were
drawn and never placed in any level** — 55 of them in Wily's fortress. No
duplicate files, no orphaned data, no development artefacts, no dead strings, no
audio of any kind: the only sound hardware the code touches is the PC speaker,
and there is no Tandy sound chip access in an executable that sets a Tandy video
mode. Forty-four predictions were written before the executable was unpacked and
scored at **65.9 %**, the lowest here — with eight of the losses traced to a
single sentence about pixel packing that the predictions file had already
isolated, named and told the scoring to charge once.

### [Mega Man 3: The Robots are Revolting](https://github.com/vs-sr-dev/pc-megaman3-doc)
**The first object in this collection with a sibling already measured to the
byte, and the first whose Saga cell was filled by a command rather than by a
name.** *Mega Man* (PC/DOS, 1990) left that cell deliberately empty with the
rule written out beside it — *filled only when another object here shares
**bytes** with it* — and this is the other object: same studio, same
programmer, same platform, twenty-one months later. The threshold was named
before the comparison was run, 32 bytes, and both layers were compared, raw and
decoded, because two different compressors would otherwise have reported
"nothing shared" for a reason that has nothing to do with the objects.
**1,855 bytes of the 1992 program appear verbatim in the 1990 program**, the
longest run 234 bytes, including 98 bytes of the options display list and the 32
bytes of both palette tables. No data file of either game shares anything with
the other but runs of flat colour.

**And the sibling was a trap in exactly one place.** The prediction file put one
inference above all others and argued it from the menu being byte-identical, the
`Masking:` option still being there, and one art set still feeding three
adapters: *the pixel is the 1990 pixel, four EGA planes, four bits.* It is one
byte per pixel, chunky, sixteen colours out of the 256 a byte can hold — and the
options menu, which is the same 98 bytes, has **dropped the VGA entry** the 1990
game had, so the one adapter that could display a chunky byte is the one this
game no longer supports. Every tile is converted to planes at load time, 256
times per bank, by a routine whose address the `Graphics Card:` setting
switches. The lesson, written into the scoring chapter because it is the only
one the session was really for: *an inheritance visible in the interface is not
evidence about the representation.*

**One codec, four families, and it is LZW.** Twelve bits a code, most
significant bit first, no clear code, no width growth, dictionary frozen at
0xFFE. Sixty-three of sixty-three compressed files decode and stop on the 0xFFF
end code with 8 or 12 bits of byte padding left and never more — and the same
format is in the executable at 0xb280, with the bit reader at 0xb20a shifting a
32-bit accumulator right by twenty to take the top twelve. The 1990 game's
PackBits reader, run first and unmodified, **over-consumes**: 2,926 bytes read
out of a 2,866-byte file. And the freeze is not academic. Every `.ZBL` fills its
4,095 dictionary entries between 19 KB and 30 KB into a 74 KB output and codes
the remaining 45–55 KB frozen, which is why `.ZBL` is the only family the
archive's own DEFLATE can still halve — and why the region past the tiles
**expands** by a third.

**A stage stopped being a program.** The 1990 game shipped five compiled 8086
modules holding 71 % of its code; there is no `.BIN` family here. The executable
grew from 17,415 bytes of content to 32,838 and **collapsed to one segment** —
24 relocations against 176, `mov ax,cs / mov ds,ax` at the entry — and what the
overlays carried became data: **366 sixteen-byte object records** at the end of
the seven `.ZSC` files, and a four-word collision box on each of **326** frame
records. Forty-three `.VFR` banks named for what they draw, one file per object,
against eight per-stage banks in 1990. A one-byte map cell now meets exactly 256
tiles, where 1990 shipped 328 slots for the same one-byte index.

**It answers three of its sibling's ten open questions, and it does it with the
loader.** The `.ZBL` loader reads three regions with three explicit constants —
256 tiles of 256 bytes, 256 records of 32, then 1,024 bytes to `0d8a:0000` — and
the `Animation:` pass then indexes those last 1,024 by tile number every frame.
So the 1,024-byte trailer that ends every 1990 `.BLK` and that document could not
identify is **four 256-byte per-tile tables**, three of them read and one of them
slop; split the 1990 trailer the same way and the same four shapes are there.
`Animation:` itself is bit 2 of a flag byte at 0x593c, tested at exactly three
sites, one in each adapter driver, each guarding a per-frame redraw of every
visible tile whose attribute byte has either of two bits set. And the *volume
descriptor of a folder* turns out to be the executable's own filename table: 49
full names and 7 padded stems, accounting for all 63 data files, **no name
unfulfilled and no file unnamed**.

**The clocks are inverted.** In 1990 the data froze and the executable came
**24 days 8 hours** later, a month of work on code alone that nothing in the
folder could identify. Here the last data file is `Logo.sta` at 15:43:58 and
`Mm.exe` is at 16:05:34 — **21 minutes 36 seconds**, a link and not a build.
Thirty-eight `.vfr` came out of one tool run in 16 minutes 44 seconds in
alphabetical order; eleven `.zbl`/`.zsc` in under four minutes that evening; and
`Foilrig.zsc` sits alone seven hours earlier, the only stage in the object whose
two halves were not written within twenty seconds of each other.

**Leftovers: 118,293 decoded bytes costing 16,509 as shipped, 4.21 %** — against
9.89 % in 1990 — after a draft of that chapter said 26.51 % and was wrong,
because it modelled the tile bank as 288 flat slots from arithmetic that divides
perfectly instead of from the loader that does not. Twenty-three bytes in the
whole object hold a colour index above fifteen that a sixteen-entry palette
cannot express. **Fifty-three predictions scored at 70.8 %**, method 7 of 7 —
and of the three clauses marked as inherited from the sibling, two hit and the
third was the one that cost four others.

### [Tesla Effect: A Tex Murphy Adventure](https://github.com/vs-sr-dev/pc-teslaeffect-doc)

*Tesla Effect: A Tex Murphy Adventure* (PC/Windows, 2014) — **17,519,466,565
bytes in 4,769 files, of which 82.93 % is filmed video and 0.0090 % is the code
the studio wrote**, and the largest object in this collection by a factor of
44,600 over the one measured before it. The total closes three ways — `du -sb`,
the sum of 4,769 `stat` calls, and the distributor's own `SizeOnDisk` — which
makes this the first object here with an **external, dated, versioned volume
descriptor**, and the third different answer this branch has had to the question
*what is the volume descriptor of a folder*. It is also the first with **personal
data in it**: two fields of the Steam manifest belong to the person who owns the
installation and are redacted everywhere.

**1,035 Bink 2 headers, censused entirely, no frame decoded**: all 1,035 parse,
all 1,035 declared lengths match `stat`, **all 1,035 are 2048 × 1024** (a
power-of-two texture, not a picture), 1,028 run at 23.976 fps, every one declares
exactly one audio track, and the sum is **20,014.286 seconds — five hours,
thirty-three minutes, thirty-four point three seconds**. 4,570 distinct SHA-1s
for 4,769 files: **1,330,831,607 bytes already exist elsewhere**, 99.994 % of it
video, because the branching story is stored as a directory tree — a scene
reachable from six routes is written six times, while the subtitle file that goes
over it is written once.

The script is **five Excel 2003 workbooks**, shipped with their document
properties intact: `Author James`, `LastAuthor masonj` on English and Spanish and
`courtneyj` on the other three, all five **created in the same second**, English
and Spanish saved in the same second — and **the English one printed on
2014-04-24 at 20:59:23 UTC**, the only record of a piece of paper anywhere in
17.5 gigabytes. The sibling object's closure test closed exactly, 56 names for 63
files; **this one fails in both directions**, 294 of 3,262 requested string IDs
with no English text and at least 3,250 of 6,535 English keys named by nothing
visible, because the join is a function that concatenates a directory, a file
stem and an extension and nothing in the build ever checked it. English turns out
to have the **fewest** keys of the five languages: the famous 1,223-row gap is
1,404 blank rows where its section headings were cleared, and the translators
kept theirs — instruction rows included. A `???` left in a retail English line was
patched four different ways by five people; the Italian translator **invented a
name**.

**101 drive-lettered build paths in the executable, from five vendors, and none
from the studio** — against zero of any kind in the 1992 object — while
`Assembly-CSharp.dll` has zero, every version field empty, and 59 of its 882
types from Unity's tutorial, a bought FPS kit and iTween. Of its 5,002 string
literals, **65 are a line of script and 319 are keys**: the code holds the names
of text, not text. And **16.86 % of the object was not opened**, said so in its
own chapter — the one probe into it turned up 48,821,155 further duplicated bytes
that a per-file hash census structurally cannot see, which makes every leftover
figure in the document a floor. Fifty-six predictions and two named inferences
scored at **81.6 %**; the largest miss was the running time, wrong by 50 %,
because it trusted a sample of five files out of 1,035.

### [Lands of Lore: The Throne of Chaos](https://github.com/vs-sr-dev/pc-landsoflore-doc)

*Lands of Lore: The Throne of Chaos* (Westwood Studios, PC/DOS, the 1994 CD
revision) — **325,758,928 bytes in 65 files, of which 94.17 % is a single file
and that file is a CD**. It is the first object in this collection that is
openly the work of **three separate groups of people twenty years apart** — the
game from 1992-1994, DOSBox from the 2000s, a GOG wrapper from 2011 — so every
figure in the document names the layer it belongs to, because a 2011 date in the
root of an ISO is not Westwood's mistake and a 1992 timestamp on a 9 KB library
is not GOG's achievement.

`GAME.DAT` is an ISO 9660 image and the branch's **fourth answer** to *what is
the volume descriptor of a folder* — the first time the object has actually been
a disc. It has the field the other three lacked, `publisher_id` reading
`WESTWOOD STUDIOS`, and **it has that field's neighbour filled in wrong**:
created and modified both say **2011-09-13T11:39:37**, seventeen years after the
209 files inside. The evidence for what happened is a byte nobody looks at. The
seventh byte of a directory record is the GMT offset in quarter-hours;
**224 of the 226 records carry 0 and the two that say 2011 carry 8**, which is
Central European Summer Time. The root directory's 34-byte record exists **four
times in the image and all four disagree** — `1970-01-01T01:00:00` in the
descriptor, which is `localtime(0)` written by something that had no date;
`2011-09-13T11:39:37` twice in the root's own extent; and all seven date bytes
zero in `DATA`'s parent entry, 104 bytes from a record that says 1994. Three
code paths, three answers, one directory. Whatever produced this file in 2011
did not lay it out: the extent order runs backwards against the directory order
eight times, two archives are stranded in a hole between two language
directories, the root's own files sit at the far end of the disc in no order at
all, and there is **no padding and not one gap**.

**The sector map closes exactly** — 149,753 file + 8 directory + 2 path table +
16 system area + 2 descriptors = 149,781, zero sectors owned by nobody and zero
owned by two things, where the CLIC 11 disc left two unaccounted out of 322,926.
And for the first time in eight sessions the branch's Macintosh question is
carried forward with a **measurement** attached instead of a shrug: the
32,768-byte system area contains one distinct byte value and it is zero, there
is no Apple partition map, no `BD` signature, no El Torito and exactly two
`CD001`.

**77.815 % of the object is a recorded human performance** — 5,508 Creative
Voice Files, **8-bit unsigned PCM, mono, and not compressed at all**, at
22,222.22 Hz, because a VOC block states its rate as a one-byte time constant
and 22,050 is a number this format cannot express. **3 h 12 m 11.50 s**, summed
from declared block lengths with zero samples decoded, and then confirmed the
only way it can be: all 5,508 decoded to PCM and written as WAV, largest
disagreement with the header census **0.000000000 s**, and two of the results
played and correct. Of those, 4,912 are lines of dialogue in thirty `.TLK`
files, with a **median length of 1.907 seconds and none longer than 6.566** —
lines, not narration — addressed by bare coordinate, so that **no word appears
in any of 4,912 names**. Twenty-one years after this, *Tesla Effect* would be
82.93 % filmed video and store it as file names the code holds; the shape is the
same and the reasons are not, which is a chapter of its own.

A `.TLK` turns out to be a `.PAK`: **162 archives of 162 close to the byte**,
7,209 members, every name 8.3 and upper case, none holding a path separator —
and the terminator is **nine bytes rather than five**, all 132 `.PAK`
disagreeing with the documented reading by exactly four zero bytes, which is a
format rather than a bug. Format80 and Format40 were then implemented from
scratch, because censusing a format is not decoding it: **265 of 265 `.CPS`
decompress to exactly the 64,000 bytes they declare** and **529 of 529 `.WSA`
offset tables land on the end of their file**, both checked by extracting
identifying pictures and looking at them; **236 of 236 `.SHP` containers close**
in two variants told apart by a closure test rather than a guess, and **2,191 of
7,299 sprite frames come out**, which is stated as the boundary rather than
smoothed over. **89.66 % of the object has been through a decoder written in the
repository and come out agreeing with its own headers.**

The duplication is the answer to a question the previous object could not
answer. The game is here **three times** — installed loose, as files inside the
image, and again inside `WESTWOOD.001`, a fourth container format whose 22
`[length][data]` records close to the byte and whose first record is a text
table of contents naming Westwood's own build tree, `\projects\lol_cd\project\run\`,
the only source tree on the disc and four paths the inherited scanner did not
match. **28.670 % of the CD is content the CD already carries elsewhere**, and
128,461,128 bytes across all 7,504 leaves of the object — against the **64,230
bytes** a file-level SHA-1 census reports, wrong by a factor of two thousand.
That closes Q3 of `pc-teslaeffect-doc`, on an object that did not ask it, and
the object that did stays unanswered.

Of 32 loose Westwood files, **31 exist inside the image and one does not**:
`LANDS.CFG`, ten bytes, the only part of the game layer this installation
produced. A translation of the game costs **142,617 bytes — 0.739 %** of the
language trees, since 368 of 377 archive members are byte-identical in English,
French and German, and 133,011 of the 142,617 are pictures repainted because
they have words in them; the actual text is 9,606 bytes. `MAIN.EXE` and
`MAINW.EXE` differ by 4,272 bytes and **69.18 % of one is byte-identical to the
other**, found by a tool inherited unmodified from the 1992 object; neither is
compressed and neither is a Windows binary. **The oldest byte on the disc is not
Westwood's**: `WESTWOOD.DLL`, 1992-06-11, is a Borland C++ 1991 *Meter Custom
Control Library* — a progress bar.

The run this branch has been building continues: **absolute paths in the shipped
executables are 0 in 1990, 0 in 1992, 0 here, 0 in `DOSBox.exe` compiled by
volunteers in 2010, and 101 from five vendors in 2014.** GOG's
`goggame-*.hashdb` is **the first descriptor in this collection that can be
wrong** — 35 records of 1,056 bytes, 1,024 of name and 32 of MD5, all 35
verifying — and what it covers is the finding: the 33 files of the game, the
manual and the icon, and not the emulator, not the installer, not itself.
Leftovers total **502,100 bytes, 0.1541 %**, the cleanest object measured here,
and **99.96 % of them belong to the two groups who did not make the game**;
Westwood's entire share is a **187-byte text-editor session** left in the French
directory in December 1993, with its search buffers empty and its cursor
position recorded. **Sixty-one predictions plus three named inferences scored at
77.3 %** — method 88.9 %, content 75.5 % — and seven of the thirteen misses are
one error wearing different clothes: assuming that things which resemble each
other were made the same way.

### [FINAL FANTASY VIII (PC)](https://github.com/vs-sr-dev/pc-finalfantasy8-doc)

*Final Fantasy VIII*, the 1999–2000 Windows conversion, Italian edition
published by Eidos — **1,533 files and 3,046,644,782 bytes** across four game
discs, an installation disc and a raw image of the **French** fourth disc. It is
the first object in this collection that is **openly a port**, and the port is
visible in the shape of the files long before it is visible in the code.

**The inversion first, because it fixes every denominator after it.**
**1,466 of the 1,533 files are Microsoft's DirectX 6.1 redistributable and they
weigh 1.744 %. Twenty files are the game and they weigh 81 %.** Opening
`DATA1.CAB` — 510 MB of InstallShield's container holding Square's content —
moves half a gigabyte into the right column, and the honest split is **Square
97.999 %**, Microsoft 1.744, InstallShield 0.164, **Eidos 0.045**, Yamaha 0.035,
RAD Game Tools 0.013. The company on the box wrote 1,373,299 bytes.

**Five container formats, read from scratch, each closing on a census.** The
`FIELD` triptych is 2,703 twelve-byte index records — field order *(size,
offset, method)*, established because **offset is the only monotone field across
2,703 records** — against 2,703 CRLF-terminated absolute paths: **2,703 = 2,703
in both directions, 2,703 of 2,703 members decompressing to their declared size,
gap 0, overlap 0.** And then the shape nobody expects: the 2,703 names are **901
stems, each carrying all three of `.fi`, `.fl` and `.fs`**, laid out as three
parallel blocks of 901 on 901 of 901 stems, so the archive is an archive of
archives and its real leaves are **14,692 files two levels down**, where the
closure holds again. The four `.PAK` are 104 `F8P` blocks holding **208 Bink
Video files**, and `8·blocks + camera records + movies = file size` with
**unaccounted 0 on all five archives**. The InstallShield 5 cabinet holds 139
files, 139 MD5 digests, and **139 of 139 verify**.

**The most useful thing in the document is a decoder that was wrong while
passing every test.** The LZS reader was first written reading the ring buffer
at `offset + 1`, and under it all 2,703 members decompressed to exactly their
declared sizes with zero gap and zero overlap. The lengths come from the control
bits and are right either way; only the bytes are wrong. It was caught because
one member is a path table and came out as
`C:\ff8\Data\ia\iFIELD\mapdta\ibc` instead of
`C:\ff8\Data\ita\FIELD\mapdata\bc`. **A length-exact closure test does not prove
a decoder correct.** The same session then made the same mistake in a different
place: a constant rotation over the game's text produced fluent, idiomatic
Italian and was **wrong about every letter**, because the character table holds
two alphabets and the rotation mapped the lower-case range onto ASCII capitals.

**The port, measured.** 51,750 camera records of 44 bytes, each a 3×3 rotation
matrix in the PlayStation's fixed point where 1.0 is 4096 — 14,977 of 15,997 on
disc 1 have all three rows of unit length — plus padding and an `int32`
translation: the console's own `MATRIX` structure, one per frame. `FF8.exe`
carries **797 absolute build paths, 178 distinct**, of which 554 name a graphics
library at `C:\lib\` containing `tim.cpp`, `rsd.cpp` and `psx.cpp` beside
Direct3D, OpenGL **and** a software rasteriser, and eight name
**`C:\FF8\Common\psx2ssi\`** — the porting layer named after the machine it
converts. Ninety more name `x:\jppc\`, the Japanese build tree, inside the
Italian executable. The branch's absolute-path series becomes
**0 · 0 · 0 · 0 · 101 · 31,737**, and this object's are all the studio's own.
The menu says `NUOVO GIOCO` and `CONTINUA` and nothing else; the only `Esci` in
the game is between `Compra` and `Vendi` in a shop; and a few hundred bytes away
sits **`Non aprire il coperchio della console`**, beside the memory-card and
PocketStation vocabulary and a DualShock vibration table.

**The thesis of the last two documents breaks here.** 2014 was 82.93 % filmed
and 1994 was 77.81 % recorded; this object is **46.4384 %** recorded-or-rendered,
and almost none of it is a person — the film was rendered, not shot, and the
**soundtrack is not a recording at all**. 91 DirectMusic segments totalling
4,942,458 bytes and one 8,262,054-byte instrument set — **0.5577 % of the
object's distinct content** — with six pieces re-orchestrated for Yamaha XG and
a Yamaha S-YXG update on the disc, because the performance happens on the
buyer's machine. **Five minutes and forty-eight seconds of choir is the only
human being in three gigabytes.**

**Two dates decide the object.** On **1999-12-21** the `FIELD` triptych was built
and pressed onto discs 1, 2 and 4. On **2000-01-14** it was rebuilt, `FF8.exe`
was linked at 20:48:19Z, and the entire installer was made — and the rebuild
changed **exactly one leaf of 14,692**: a field script called `rgcock3.jsm`, in
which 171 of 2,676 opcode words differ and **all 171 are the same opcode with a
different literal**. That rebuild reached the installer and disc 3 and nowhere
else. The file that was missing from the worn fourth disc could therefore be
replaced from disc 1 or disc 2 and **not** from disc 3: disc 4's index closes
against disc 1's data to the byte and reads a length of 2,522,370,823 against
disc 3's. The proof is in the document beside the copy.

**And the leftovers are the best three hundredths of a per cent in the
collection.** Inside the shipping archive, pressed onto four CDs and packed into
the installer, sit four `.cnf` build scripts listing 2,724 source paths on
`x:\itcd\` — and **four `.bak` backups of those same scripts still pointing at
`x:\jpcd\`**, the Japanese CD tree. Somebody opened a build script, replaced
`jpcd` with `itcd`, saved, and the packing tool swept the editor's undo file in
with everything else. Beside them: four generated `.c` files, four Shift-JIS
`.h` headers dated `'98.8.7`, a `maplist.dir` of **982 Unix paths under
`/1a/proj/master/jppc/`**, a developer's debug configuration, and — on the
French disc only — `FIELD2.FS`, 5,301,008 bytes, dated 1999-11-02, **which is a
RIFF WAVE file**.

Seventy-two predictions were written before a container was opened and scored at
**72.92 %**; the sharpest was that `FIELD.FL` would differ between the two
languages in *exactly* 8,109 bytes, guessed from a line count and a directory
name, and it does.

### [Plundered Hearts](https://github.com/vs-sr-dev/pc-plunderedhearts-doc)

*Plundered Hearts*, Infocom, 1987, the MS-DOS edition — **five files and
146,252 bytes**, which is 1 : 20,831 of the object documented before it. It is
the smallest thing in this collection and the first that can be understood
completely: a **Z-machine version 3** story file of 128,963 bytes, and beside it
the 12,004-byte virtual machine that runs it, at a ratio of **1 : 10.7433**.

**The unit is words, because bytes cannot say anything here.** There are **zero
bytes of sampled audio, image, video, font or palette** in the object, and
`sound_effect` is one of the fourteen opcodes the game never issues. The
branch's running thesis — 82.93 % of one object filmed, 77.81 % of another
recorded, 46.44 % of a third rendered — reaches **zero**, and every byte is
either language or the program that chooses which language to print. So:
**18,701 words**, 101,368 characters, 2,391 prose strings, decoded from all five
string populations and not sampled. **Eighty-three per cent of that text is
inline inside `print` instructions**, so finding it required a disassembler;
a tool that reads only the packed strings finds 16.7 % of the game and reports
it as all of it.

**The header is the eighth answer to this list's oldest open question, and the
oldest.** Sixty-four bytes, thirteen big-endian fields, **eight of which are
addresses and none of which is a length except the file's own**. It declares
128,962 bytes and a 16-bit sum of every byte from `0x40` to that length, and the
sum comes to **`0x406D`** — computed in Python, and computed again by the
interpreter's own six 8086 instructions at `0x1234`, which seek the file to
offset 64, read it back off the disk and accumulate a byte at a time into `DX`.
Content verification was not invented by digital storefronts, and the previous
document in this branch had already pushed it back to a 1999 installer; this one
pushes it back another twelve years, to two bytes. The file on disk is **128,963**
bytes. The surplus one is `0x1A`, a DOS end-of-file marker left by a text-mode
copy some time between 1987 and 1996 — and the descriptor is arranged so that a
copy with it and a copy without it verify identically, because **the one part of
the file the checksum cannot cover is the checksum**.

**The year does not come from a clock.** Four files carry `1996-06-21T23:41:02Z`
and the fifth `2001-02-20T21:05:48Z`; nothing in the filesystem comes within
eight and a half years of the product. The year is `870730`, six ASCII digits at
header offset `0x12`, and it is the only 1987 in the object — the string `1987`
returns zero across all five files. Both distinct timestamps have an **even
seconds field**, which is the first positive observation in three sessions for
this list's FAT-quantisation question, and the document immediately says that two
observations both landing even happens 25 % of the time anyway.

**The alphabet was derived from the data and then checked against a copy printed
inside the machine that uses it** — because the previous object lost two chapters
to a decoder that passed every test while being wrong about every letter, and
reading the answer off would have been the same mistake in a new form. Five
steps: the 96 abbreviation strings **tile `0x0040`–`0x01E2` with gap 0 and
overlap 0**, which no wrong reading of the escape codes produces; the two shift
codes split the character stream into three disjoint frequency profiles; the 816
dictionary entries are **strictly ascending**, and a monotone bijection between
two totally ordered 26-element sets is unique, so A0 is forced to `a`…`z` with
nothing left to choose; and the dictionary header carries its three input
separators as **raw ZSCII**, which appear as three single-character entries and
pin three slots of A2 with no assumption at all. **29 of the 78 slots are forced
by this story file, 10 by an ordering assumption it does not force, and 37 come
from the interpreter — and the two derivations agree 78 of 78.** The table saying
which is which is the point of the chapter.

**The compression is a table of 96 strings and it removes a ninth of the file.**
All 96 are used, **9,735 times**, with no duplicate and no placeholder, saving
**12,158 bytes — 9.4275 %** net of their own 610-byte cost, break-even at
expansion number 466. The most-used entry is not a word: it is **`, `**, 1,174
times, saving one z-character each time. And **nine of the 96 are this story** —
three forms of `Lafond`, three of `Jamison`, plus `Nicholas `, `Cookie ` and
`ballroom` — so the compression table of a 1987 text adventure turns out to be an
accurate summary of who the book is about. The two previous objects in this
branch measured duplication as a defect, at 20.449 % and 60.1834 %; this one
measures how much duplication somebody removed on purpose, in 1979, with no
dictionary, no window and no entropy coder.

**The closure test runs for the fourth time and fails in both directions, and
that is the right answer.** 816 dictionary entries of seven bytes, ending
**exactly** on `0x4E00`, the declared base of high memory. 619 of them occur in
the prose; **2,743 of 3,362 printed forms would be refused by the parser**. A
game that printed only what it could parse would be written in 619 words; this
one is written in 3,705. The test is run on **six-z-character encoded forms**
rather than on words, because `pistols` and `pistol` are one entry and a
word-level test would have reported a failure the machine does not have.

**And the map closes.** Nineteen regions over **128,963 bytes, 0 owned by nobody
and 0 owned by two** — the fourth time this branch has drawn one and the third
that closes exactly, and the hardest of the four, because a Z-machine header
gives eight starting addresses and no lengths, so every region's end has to come
from the start of the next thing. Three regions had to be found some other way.
The best is two bytes wide: 240 globals from `0x02A2` end at `0x0482` and the
object table begins at `0x0480`, so the file is ambiguous about who owns them —
and **the code references 239 of the 240 globals, and the one it never touches is
number 239**, precisely the one that collides. The second is 1,761 bytes that
nothing in the header points at, resolved by the 38 global variables whose
initial values tile it, two of which are the parser's text and parse buffers. The
third is the boundary between code and packed strings, found by measuring **how
far the routine sweep skips**: never more than **four bytes** inside real code,
and 708 immediately after `0x1CDAC`.

**614 routines, 13,856 instructions, 60 distinct opcodes** — against the **91
routines a sound reachability walk can find**, because the game calls its 183
action routines through the parser's tables with the address in a variable. One
instruction in four prints something; arithmetic is 215 in 13,856, one in
sixty-four. Three wrong versions of a single comparison in the routine-end rule
produced **14, 88 and 623 routines**, every one of them silently, with a
confident byte count and a percentage attached.

**Two things in the interpreter are about games that are not in the box.**
`LEATHER.SCR` is an eleven-byte filename in a sixty-five-byte buffer, loaded by
three instructions, reachable from the character-output path **and** from the
keyboard, guarded by `cmp al, 2` — the first object in this branch where a binary
asks for a file that does not exist. And `Unauthorized copy` is referenced once,
from a branch taken on the carry flag returned by a subroutine whose entire body
is **`F8 C3` — clear carry, return**, so the message can never appear. Whether
that was compiled or patched needs a second Infocom DOS interpreter to diff
against, and the document stops there and says exactly what would settle it.

**Absolute paths: 0 and 0, measured three ways.** The inherited scanner run
unmodified, both path shapes per file, and then a third pass **over the decoded
text** — a search no byte-level tool in this branch has ever been able to run,
and one that matters here because 88 % of the object is invisible to a regular
expression. The series becomes **0 · 0 · 0 · 0 · 101 · 31,737 · 0**, and the
honest reading is not that 1987 was more careful: there was **nothing to leak
from**. No PE debug directory, no `__FILE__`, no linker map, no metadata section
exists anywhere in either format.

**Leftovers are 602 bytes, 0.4116 %**, and they are the most legible in the
collection because every item can be pointed at exactly: six developer verbs
shipped in a retail product — `#comm`, `#rand`, `#reco`, `#unre`, `zzmgck`, and
**`$ve`**, which reaches the file's single `verify` instruction and makes the
interpreter re-read 128,898 bytes off the disk; two grammar blocks that no
dictionary word can reach; and **twenty dictionary nouns that no object property,
no code constant, no preposition record and no printed word points at** —
`gator`, `guinea`, `breeks`, `ruby`, `sirrah`, `plumed`. Things that were in this
game once, whose words outlived them.

Sixty-six predictions were written before a Z-string was decoded and scored at
**84.85 %** — method 91.67 %, content 83.33 %, the highest in the branch. The
prediction file had said in advance that anything above 85 % would mean the
briefing had given too much away, which is why the scoring chapter reads as a
complaint rather than a victory lap.

### [Leather Goddesses of Phobos](https://github.com/vs-sr-dev/pc-leathergoddessesofphobos-doc)

*Leather Goddesses of Phobos*, Infocom, 1986, the MS-DOS edition — **fourteen
files and 164,594 bytes**, and the second object of its kind in this list. That
is the whole reason it is interesting. Every previous entry here was measured
against a description; this one could be measured against **another object of
the same format, from the same studio, sitting on the same disk**, and so it is
the first time the list has been able to ask *how much of an engine is engine*
and get a number instead of an adjective.

*(The game is an adult comedy with a three-position explicitness switch. This
document measures the switch, the vocabulary and the prose the same way it
measures the checksum, which means it neither quotes them for effect nor omits
them.)*

**The interpreter is 99.83 % engine, and the twenty bytes prove it.**
`leather.com` and the 12,004-byte `.COM` shipped with *Plundered Hearts* differ
in exactly **twenty positions, in four runs of five, all four inside two
filenames** — `PLUNDERE.DAT` becomes `LEATHER.DAT` and `PLUNDERE.SAV` becomes
`LEATHER.SAV`. The virtual machine is not built per title. It is one binary with
a name patched into it at build time.

Two consequences follow immediately, and both close things the row above left
open. The subroutine whose entire body is `F8 C3` — *clear carry, return* — on
whose carry flag the only reference to `Unauthorized copy` branches, is
**identical in both files**. Two independent crackers do not produce the same
two bytes at the same offset in the same routine while leaving 11,984 others
untouched, so the copy check was **built that way** rather than patched. And
`LEATHER.SCR`, the filename the previous document found hard-coded in a binary
belonging to a different game, sits at offset `0x19CA` in **both** interpreters
and is **not** among the twenty differing bytes: one title's filename is
compiled into every title's machine.

The `cmp al, 2` that guards it is **CTRL-B**, and the file it opens is here.
`read.me` — 640 bytes of Infocom's own marketing — advertises a "Boss Key", and
`leather.scr` is what it produces: 1,408 bytes, **92.1165 % printable ASCII in
twenty-four lines**, a pastiche of a screen from **Cornerstone, Infocom's own
relational database**, with a menu reading `DEFINE SORT PRINT TOUCH VIEW ENTER
RE-ENTER FONDLE LUBRICATE` and a status bar reading `Previous Mode: Titillate
Files Viewed: 69`. **Neither story file emits character 2 as a constant**, so
the boss key is a feature of the machine that neither game running on it knows
it has.

**Above the interpreter the answer inverts, and the shape of the inversion is
the finding.** Two story files compiled by the same compiler a year apart share,
in runs of 32 bytes or more, **1,653 bytes — of which 933 are runs of zeros**,
leaving **720, or 0.5580 %**. Nothing survives as a byte string because every
address in each file is different. What survives is structure, and the
structures share at wildly different rates:

    interpreter, byte for byte    99.83 %
    abbreviation table            69.79 %      67 of 96 entries identical
    dictionary                    46.01 %      450 entries identical
    action table                   0.00 %      0 of 183 shared indices agree

Total sharing in the machine, partial sharing in the tables, and a **hard zero**
at the first structure whose contents are behaviour rather than English.
**The engine ends where the action table begins.**

And the middle of that column is the opposite of the obvious reading. The
compression table is *more* shared than the parser vocabulary — which looks
backwards, since verbs like `take` and `quit` belong to the machine and a
compression table is fitted to one book. The resolution is that an abbreviation
table's ceiling is not the story but the **language**: `the `, `, `, `of `, `. `
are the top of any English text ever written, so ninety-six slots are nearly all
spoken for before the author starts. A 978-word dictionary is four times larger,
its verbs are shared entirely, and most of the extra room is nouns — and nouns
are the game. **The shared fraction of a structure measures how much of it
English already decided.**

The twenty-nine private abbreviations say the same thing in prose. The other
title's are people — three forms of `Lafond`, three of `Jamison`, `Nicholas`,
`Cookie`, `ballroom`. This one's are places and directions — `Martian `,
`Venusian `, `canal`, `north`, `south`, `direction`, `leads `, `toward `. **Only
three of the ninety-six are this story, and not one is a person's name**, which
is also why this file's abbreviations save **7.6172 %** where the other's saved
9.4275 %: compression ratio in an Infocom game is a measurement of how
repetitive its prose is, and a comedy that visits thirty-nine places and names
its cast once repeats less than a romance set in one house.

**Two numbers were predicted before the file was opened and came out exact.**
The dictionary: `(0x5C64 − 0x41A6) / 7 = 978`, remainder 0 — **978 entries
ending precisely on the declared base of high memory**. And the gap between the
globals and static memory: 240 globals from `0x2087` end at `0x2267`, static
begins at `0x2CAC`, **2,629 bytes**, occupied by the tables forty globals point
into. The row above found its two most-contested bytes at that boundary; here
there is no collision at all, because the object table comes *first*.

**The best thing in the object is 506 bytes that nothing appeared to point at.**
Between the base of high memory and the first routine sit **31 count-prefixed
groups of (noun, adjective, routine) triples** — `dust`, `door front` and `bar`
for `Joe's Bar`, `crown royal` and `gown flowin` for another room — tiling the
span to the byte at `2 × 31 + 6 × 74 = 506`, and reached by **property 14 of 39
room objects**. It is ZIL's `PSEUDO` table: the nouns you can refer to in a room
that are not objects, at **6.8 bytes each** against roughly 33 for a real
object. The previous title has no such table and uses property 14 as a boolean.

**Finding it was the price of a correct word count**, and the failure is worth
recording because nothing raised. The inherited disassembler assumed code begins
at the base of high memory; here 506 bytes of scenery sit there first, so its
walk hit a 386-byte gap on its first iteration, returned a code region of **zero
bytes**, and every byte of the program was decoded as text: **37,245 words**
instead of 16,345, with self-consistent totals and percentages that summed. A
second wrong count followed at once — the code region ends on an odd byte,
packed strings live at even addresses, and starting one byte early turned 428
sentences into 2,287 fragments. Both were caught the same way: **every changed
tool was re-run against the previous object, where it had to reproduce that
document's published figures exactly**, and did. A tool that is right on one
file and absurd on another is broken on the second, not discovering something
about it — and that sentence could only be tested because a second object of the
same format was on the disk.

The corrected census: **16,345 words**, 2,631 prose strings, **83.73 % of them
inline inside `print` instructions**; **228 objects** — `(0x0ADC − 0x02D8) / 9`,
remainder 0 — with 0 cycles, 0 orphans, 0 bad pointers, 0 asymmetries and **27
roots**, which read as a plot summary because parent 0 means *nowhere* and the
`Super-Duper Anti-Leather Goddesses of Phobos Attack Machine` is in the game and
in no room; **762 routines, 13,762 instructions, 61 distinct opcodes**, of which
a sound reachability walk sees **101**, because the parser dispatches its 230
action routines through a table. **22.50 % of every instruction prints
something**; arithmetic is one in fifty-nine. The map closes exactly for the
fourth time running: **21 regions over 129,023 bytes, 0 owned by nobody, 0 owned
by two.**

**The explicitness switch is measured rather than mentioned.** It is **variable
243**, set by three dictionary verbs — `tame`, `sugges`, `lewd` — at actions
**3, 4 and 5, consecutive**. The first two routines are four instructions each.
The third is 192 bytes: it checks a remembered age, and if there is none it
issues one of the game's six `sread` instructions — the same opcode that reads
`take the lamp` — and asks `What is your age? >`. Under 18 is refused; over 120
gets `Bullpuckies. Tell the truth. >`; and if you come back with a different
number it prints `Liar! You said before that you were ` and the previous figure.
**45 of 762 routines mention the variable, holding 21.39 % of the inline text**
— an upper bound, since such a routine carries all three versions of its prose.
And **0 % of the dictionary is mode-specific**: a version-3 entry has three data
bytes and none of them is a mode field, so the parser accepts the same 978 words
at every setting. **The switch changes what the game prints and never what it
accepts.**

**The missing producer from the previous document is here.** `setup.exe`, 1,584
bytes, writes `setup.inf` through the **FCB** calls MS-DOS inherited from CP/M —
delete, create, set DTA, random write, close — which the inherited
cross-referencer printed as bare function numbers with `?` beside them until its
table was extended. That is the second time a tool in this branch has been blind
to half of an interface, and `?` is the dangerous output, because it looks like
having looked. The three bytes are `PJY` and are **byte-identical to the
previous object's `SETUP.INF`** — not a copy of it, but two people on two
continents of the 1990s pressing Enter twice at the same two defaults. The
interpreter reads them as `'P'−0x37−1 = 24` rows and `'J'−0xFA = 80` columns:
**twenty-five lines asked for and twenty-four kept, because the last row is the
status line** drawn at `ESC[25;01H`. The two odd offsets map each legal range
**exactly onto printable ASCII**, `0x20` to `0x7E` for the columns, so a binary
config file survives being read aloud or copied in text mode.

**And 11.5855 % of the object is an installer that deletes itself.** `af.exe` is
13,168 bytes of **Lattice C 2.00** whose whole job is to locate `ANSI.SYS` and
print one `device =` line; `scan.com` (114 bytes) upper-cases `\config.sys` and
looks for `ANSI`; `gamedir.com` (62 bytes) checks the FAT media descriptor for
`0xF8` before creating `\INFOCOM`; `yes.com` (93 bytes) turns a batch-file
prompt into an exit code, which is the only way a 1986 `.BAT` can ask a
question. All of it exists so that a handful of ANSI escapes work — and
`statline.bat` ends with `del af.exe` and five siblings. **One byte in ten of
this object was designed to be gone before anyone played, and it is still here,
which is how we know this is a master diskette that nobody ever installed.**

**Absolute paths: 0, 0 and 0** — the inherited scanner unmodified, both shapes
per file, and a third pass over the **decoded** text, which no byte-level tool
can run because nearly half the story file is five-bit characters. It is the
first time the zero needed an argument rather than a command, because `\INFOCOM`
is a rooted path of a single component. Ruled a **destination and not a leak**:
a path is a leak when it names somewhere the player has never been, and
`\INFOCOM` names somewhere the player is about to be.

**The thesis reaches zero a second time.** No audio, no image, no video, no
font, no palette, and `sound_effect` among the thirteen opcodes never issued.
The one thing in the object you look at rather than read is
`leather.scr`, and it is characters. **The only picture in two Infocom products
is drawn with the alphabet.**

**Leftovers are 655 bytes, 0.3979 %**, and the best of them is a verb. Five verb
blocks in the grammar are reachable by **no word in the 978-entry dictionary**,
and one of them carries **twelve grammar lines dispatching to ten distinct
action routines** — a complete, compiled, unspeakable verb. Beside it: 39 nouns
the parser accepts that name nothing the game prints or holds, six developer
verbs that appear in **both** titles and were therefore the build rather than an
oversight, and seven strings from inside the compiler's own parser — `PRSI`,
`PRSO`, `Preaction`, `Not Here` — sitting at the very front of the string pool.

**What the object asks for and does not contain is five things**: an instruction
manual, hint booklets, a mail-order form, a **scratch-and-sniff card the text
indexes by spot number**, and a **3-D comic book that is an object in the game
world**. And `readme.1st` — the only file here Infocom did not write, 863 bytes
by whoever put this disk on a bulletin board in 1996 — apologises for being
unable to post the last two. The two lists were made ten years and one direction
apart and they agree. That file is also a source of a kind new to this list: an
unverifiable claim by an unidentifiable person, found inside the object it
describes. It says the writer recalls no copy protection, and **two bytes of
8086 agree with it**, which is the first time here that a claim inside an object
and a fact in its bytes have converged. It ends with a handle, a bulletin-board
name and a telephone number, and **none of the three is transcribed in that
repository, `notes/` included**.

Sixty-six predictions were written before a Z-string was decoded and scored at
**81.8 %** — method 85.7 %, content 80.8 %. That is three points below the row
above, on a briefing that gave considerably more away, and it fell in the right
place: the losses are concentrated in the ten clauses about the comparison,
which is the one block nothing could help with. The most instructive of them
predicted that the dictionary would be more shared than the abbreviation table,
on reasoning that was careful and wrong — and being wrong produced the best
result in the document.

**The Saga cell is empty, and this is the row that owes an explanation**,
because the row above it left the cell empty for want of a second Infocom object
and stated that a second one *"would fill it in one command and on bytes"*. The
second one is here, and the bytes are measured: **11,984 of interpreter, 3 of
`setup.inf`, 720 of story file, 67 abbreviations, 450 dictionary entries.** By
the letter of the index's rule — fill it on measured shared bytes — the cell
could be filled today.

**It is left empty on purpose.** Those bytes measure a **machine**, not a
series. The two titles share an engine and a publisher and share no character,
no place, no premise, and **0 of 183 action numbers**. Infocom is a publisher;
the Saga column is for fiction that continues, not for a runtime that recurs,
and filling it with `Infocom` would redefine the column as *ships the same
interpreter* — which would eventually swallow every Z-machine title ever
pressed. If enough Infocom objects accumulate here they earn **their own index**,
keyed on the engine, which is the right home for a 99.83 % interpreter diff. The
Saga column is not.

This is the first row in this list where the index's rule and the index's
purpose gave different answers, and it records the disagreement instead of
resolving it quietly.


### [Sam & Max Hit the Road](https://github.com/vs-sr-dev/pc-samandmaxhittheroad-doc)

*Sam & Max Hit the Road* (LucasArts, 1993), the **Italian CD-ROM edition** — the
data track of a CD copied to a hard disk: **sixty-four files, 227,198,319
bytes**, of which **88.1126 % is one file** and that file is two and a half
hours of recorded speech. The game it belongs to — every room, script, drawing,
costume, palette, font and note of music — is 13,789,910 bytes, one fourteenth
of it. The index that finds them both is 9,080 bytes, one twenty-two-thousandth
of the speech.

It is the first object in this list for which a mature, free, famous
implementation of the format already exists, and **it was not used**: not read,
not quoted, not consulted to check a result. Everything below was derived from
the bytes, and where a structure could not be, it is declared not derived.

**The cipher is given away by a zero.** A big-endian length of 13.8 million has
a zero in its top byte, and a zero XORed with a single-byte key *is* the key.
`0x69`, and `3b 27 28 24` becomes `RNAM`. The chunk shape — tag, big-endian
length, header included — is fixed not by belief but by the fact that **no
other reading tiles**: a wrong header size lands the second chunk inside the
first one's payload and the walk dies within a few hundred bytes. So the walker
carries no list of container tags at all; it asks of every payload whether it
parses end to end as chunks with nothing left over. **11,423 chunks, 51 distinct
tags, and an ownership map that closes exactly** — 91,384 bytes of headers plus
13,698,526 of leaf payload, 0 owned by nobody, 0 owned by two.

`LECF` declares 13,789,910 on a file of 13,789,910: the tenth answer to this
list's oldest question. The same object then answers it another **108 times** —
94 music wrappers, 8 animation files, 4 Autodesk FLI/FLC, a loose MIDI control
file, and a nine-entry archive whose payload sizes plus its 425-byte directory
come to its file size exactly — in four formats from three vendors. And it
supplies the counter-example in the same directory: `'SOU '` declares **zero**
on a 200,190,289-byte file. The reading that survives all of that is that the
mechanism is a property of **era and medium**, not of a toolchain: on sequential
media, a container that does not declare its own length cannot be read.

**The 9,080-byte index resolves into the container 566 times out of 566.**
Record shapes were found by division and then tested: take each directory
entry's room byte, look it up in the container's own room table, add the 32-bit
offset, and check the tag that lands. 120 `SCRP`, 94 `SOUN`, 348 `COST`, 4
`CHAR`, zero wrong — and every one of those four counts matches the container
census taken independently. `MAXS` turns out to be fifteen 16-bit fields whose
**last six are the six directory counts, in order**, which is what identifies
it as the engine's limit table.

**The text was found by anchoring rather than scanning**, because a printable-run
scan over-generated by a factor of two and the previous session in this branch
lost a word count by 128 % to exactly that. Every spoken line carries a voice
cue whose second half is the fixed eight bytes `FF 0A 0A 00 FF 0A 00 00`;
searching for them gives 4,741 hits, and the byte before each takes exactly
three values. The introducers are therefore derived from the data, and the 58
candidates that are operands rather than opcodes are rejected and reported.
**26,297 words** in 4,960 script strings and 950 object names — and **746 of the
950 names are the developers' internal identifiers**, `lab-wall-gash`,
`max-non-ears`, shipped in the same array as the translated ones, while the
room-name table beside them was stripped to a single zero byte.

**Ten English strings survive out of 3,356**, and the interesting thing is not
the ratio but the census: three are a programmer's assertion, four are `OK`, one
is a song lyric, one is a proper name, and one is a line of dialogue that was
simply missed.

**The codepage is deduced from an absence.** Nothing in sixty-four files
declares it. The text uses eight bytes above 0x7F and CP437 and CP850 agree on
all eight, so the strings cannot decide. But Italian needs `È`; CP437 has none
and CP850 has one at 0xD4; and this translation writes **`E'` 284 times, and
only ever for `E`**, while 0xD4 occurs in no string and has no glyph in any of
the four fonts. An encoding that had the character would have used it. The fonts
confirm it from the other side: their occupied slots are exactly the CP437
accented block and nothing at any CP850-only or Latin-1 position — and font 2
repurposes CP437's box-drawing range as twenty-six slots holding a decorative
A–Z.

**The speech was censused, not sampled, and the control came first.** The disc
leaves a 46,689-byte Creative Voice File in the clear; the parser had to land on
its last byte and **recompute its check word** before it was allowed near
200,190,289. Then, in one pass: **3,381 recordings, all at 22,222 Hz, 8-bit
mono, 9,001.17 seconds = 150.02 minutes, 100.000000 % accounted**. The first
version of that walk stopped at the first unexpected byte and printed a
confident 94.2 %; making it resync loudly is what turned it into 100 % and found
an 18,998-byte leftover.

**And the script points at the speech.** Four `FF 0A` escapes inside a string
encode a 32-bit byte offset into the speech file. **3,369 distinct offsets,
extracted from an encrypted container, all 3,369 landing on the four characters
`VCTL` in a different 200 MB file — zero misses.** It is the strongest single
check in the document and it validates the string grammar and the container walk
at the same time.

**The speech is an Italian dub**, which the prediction file bet against. The
bytes argue for it — 31 % of voiced lines carry no subtitle at all, 174 of them
longer than two seconds, and the delivery rate against the Italian text is a
flat, natural 16.3 characters per second at a 0.9467 correlation — but they do
not settle it, and the document says so. Four recordings were then extracted by
their cue offsets and played: Italian voices, speaking the Italian sentences
those offsets belong to. That is testimony, labelled as testimony wherever it is
used, and it moves the answer to *how much of this disc was made in Italy* from
**6.5716 %** to **94.6842 %** — because the localisation is not two readme
files, it is twelve, including the boot-disk maker, three Sound Blaster drivers,
the setup layout file and the executable of a demo of a **different game**.

**The image codec was found by brute force and fixed by an off-by-one.**
`code % 10` is the bit width — the only value that makes the walk stop inside
the strip for 100 % of every code — and the grammars were located by running the
decoder with the delta field at one to six bits. Two things that byte counts
could not decide were decided separately: the one-bit delta is a persistent
direction rather than a sign, on 42 out-of-range pixels against 10,638; and fill
order came from continuity **across** strip boundaries, 93,980 matching edge
rows against 19,661. The finished decoder still dripped, and the diagnosis came
from a person looking at a rendered room — *«come righe di acqua che colano»* —
but the fix came from the closure test: `run` lands exactly on the strip end
2,097 times of 3,359, `run − 1` 3,330 times, and `run − 2` overruns 3,173. The
run count includes the pixel already written.

**85 backgrounds, 4,210 strips, 6,710,400 pixels, zero strips reading past their
own end, 4,172 ending on their own last byte** — and one check nobody bought:
nothing in the decoder constrains a colour index to stay inside `2^bpp`, and
**6,710,389 of 6,710,400 pixels do**.

**The missing box appears twice.** The menu program offers three demos and the
disc holds one; it offers four Red Book audio tracks and the object holds zero
bytes of them, because a copy of a data track cannot hold audio tracks. There
are 16,631 bytes of menu screen and player program *about* four soundtracks that
were never files. Neither absence is counted as a leftover and the percentages
are not adjusted, because a percentage of a thing with no bytes is not a number.

**Two LucasArts engines sit on this disc and the comparison is measured.** The
*Rebel Assault* demo's animation format is the same `[tag][big-endian length]`
shape with the **opposite inclusion rule**, and 99.94 % of it is named, weighed
and deliberately left closed. `REBEL.EXE` and `SAMNMAX.EXE` share **13,005
non-constant bytes**, longest run 993 — against **199** shared with the DOS
extender that is byte-identical in both directories, which is the tempting
explanation and the wrong one. They were not even built with the same compiler.
What they share is the studio's own code, and `SAMNMAX.EXE` shares nothing but
padding with its own data file.

**Absolute paths: 34 drive-lettered, 0 source-tree**, ending a run of four
objects at zero — and seven of the thirty-four are false positives inside 200 MB
of 8-bit PCM. The document keeps that fact rather than quietly dropping them,
because the same file returns **291** matches under a looser pattern, which is
the measured value of the guards the inherited scanner was given three objects
ago. Twenty-six of the remaining twenty-seven are the product instructing its
buyer; **one** is somebody's working directory, in the shell's resource archive.
Zero in 266,434 bytes of decoded Italian text.

**The even-seconds question finally has a population**: 60 distinct mtimes over
702 days, and the seconds field is even in **64 of 64** files across 25 distinct
even values, with no odd value anywhere.

**Leftovers are 597,992 bytes, 0.2632 %**, and the best of them is invisible to
a file census: the shell's archive contains a **third byte-identical copy of the
Italian readme**, so the disc carries it three times and `sha1sum` can see two.
Beside it sit 18,998 bytes inside the speech file that belong to no recording
and that nothing points at — statistically **16-bit big-endian PCM**, mean
absolute delta 395 against 21,864 read the other way, the Macintosh convention
sealed inside a DOS speech container in an object where every other sample is
8-bit unsigned. Fifteen recordings, 38.03 seconds, are never cited by any
script. The demo is **excluded** from the total, with an argument: the product's
own front end is built to launch it.

**What the document did not open is a number as well: 19,369,491 bytes,
8.5254 %** — 348 costume resources, which turned out to be 61 % of the
container, and the demo below its chunk headers.

**Seventy predictions and five named inferences, scored at 73.3 %** — method
93.3 %, content 68.3 %, the widest gap between those columns in the branch. The
method was eight sessions old and the content was one day old. The predictions
assumed a low sample rate, which propagated into the recording count and the
running time and lost three clauses with one mistake; and they bet that the
speech was English, which is the whole difference between an edition that is
6.57 % Italian and one that is 94.68 %.

**The Saga cell is empty**, and for the third row running the reason is worth
writing down. *Sam & Max* is a real series of fiction, unlike the publisher name
that tempted the two rows above — but the index fills that column on **measured
shared bytes**, and there is no second *Sam & Max* object here to measure
against. The only other LucasArts product on this disc is a *Rebel Assault*
demo, and what it shares is 13,005 bytes of C runtime and no character, no
place and no premise. Filling the cell on the title alone is what the *Final
Fantasy VIII* row did, and declared it was doing; this row has the same option
and declines it. A second SCUMM object would do for this row what the second
Infocom object did for the row above it: turn *how much of an engine is engine*
from an adjective into a number.


### [Allods Online](https://github.com/vs-sr-dev/pc-allodsonline-doc)

*Allods Online* (Astrum Nival / Mail.Ru, now MY.GAMES, 2009), client build
**13.505**, version `16.0.01.78.2`, localisation `eng_eu` — **1,186 files and
17,366,372,506 bytes** that never touched physical media. It was downloaded over
BitTorrent on 2026-09-01 in **387 seconds**, and what is described here is the
state of one directory at 10:30:48 UTC that morning.

It is the first object in this list that could be **verified** rather than
believed. Every previous one declared a length from inside a container and was
taken at its word, because there was nothing else to do. This one ships
**9,148 SHA-1 piece digests** across two torrent files and **871 MD5s** in a
signed internal manifest, and all of them were recomputed: **8,666 of 8,666,
482 of 482, 871 of 871 lengths, 871 of 871 hashes, zero failures**. The three
totals that describe it — 18,173,919,232 declared, 17,366,372,506 on disk,
17,031,242,813 downloaded — close into a single identity with a difference of
**zero**, once the 875 synthetic padding entries the descriptor counts and never
writes are taken out and the 311 files the download did not bring are put back.

It is also the first object in this list that **changed while it was being
described**. The measurement it started from said 17,366,370,830 bytes; the
census run nineteen minutes later said 1,676 more, all of it in files a running
launcher was still writing, and sixteen files could not be hashed at all because
that launcher held them open. A pressing does not do that.

Three findings are worth pulling out of the twenty chapters.

**The naming nearly hid the redundancy.** Ten and a half gigabytes — 60.8 % of
the object — are archives named `.Mini.` and `.HiRes.`, and a literal comparison
of their 273,916 entry names finds **zero in common**. The high-resolution
archives spell the same paths with an infix, `X.(Texture).hi.bin`. Remove it and
**71,587 names are shared**, with the high-resolution copy larger on 71,586 of
them at a ratio of **11.87**. The same shape appears again in the `_x86` /
`_x64` pair, and there the object gives up the reason itself: **612 of the
localisation's 264,463 strings differ between the two builds**, and every one of
the differences is a machine word written into the *text* as hexadecimal and
padded to the host pointer width.

**The worst error in the session was made against a coordinate, not a
filename.** The whole document is built to stop 350,470 descriptive file names
from being mistaken for measurements — the `.bin` taxonomy prints *n opened of
350,470* on the line of every class, and 4,029 were opened. But the map's block
directories, `Maps/<zone>/040_020/`, were divided by a bounding box in units of
one, and reported that the fullest zone in the game was **2.60 %** full. The
coordinates advance in steps of ten. Measured on the lattice the object actually
uses: **mean fill 90.01 %, and 239 of 306 zones exactly 100 %.** A wrong answer
that was thirty-five times too small, with a plausible story already attached to
it.

**And the Russian that survives an English build is mostly invisible.** Eighty-
five of 181,513 strings contain a Cyrillic character, and **forty-eight of the
eighty-five are Latin look-alikes** — `Сolonel of the Imperial Keepers`,
`Т92 Arty`, `Open 3х3 Combat Rating` — a Russian keyboard slipping mid-word, in
characters that render identically to the ones they replace. One tooltip lists
two rewards in consecutive lines, one using the Cyrillic `х` as a multiplication
sign and the next using the Latin `x`. The thirty-seven that are genuinely
Russian are the ones that could not be translated — server histories, a
transliteration table, an autocomplete index — plus exactly one dialogue box
that was missed. The real Russian is elsewhere: `ModdingDocuments.zip` holds
**3,031 HTML pages of Lua API reference and 3,031 of them are in Russian**,
180,365 words, shipped to every player of an English client.

Twenty chapters, eighteen tools, seventy predictions scored at **72.9 %**, and
one layer of 19,657,422 bytes that was counted and never read, because it
belongs to the person who downloaded the game rather than to the people who made
it.

### [CLIC 02/97](https://github.com/vs-sr-dev/pc-clic0297-doc)

The CD-ROM bound into the Italian magazine *CLIC!*, published by **Mondadori
Informatica S.p.A.** and produced by **GLAMM Interactive s.r.l.** of Milan,
mastered with Toast 2.5 on a Macintosh on **14 February 1997 at 18:54:32 GMT**.
509,257,728 bytes, sha1 `ee3c2b6f7e16a178d4dd9093cdfe44ae007efca9`, **2,818
files a PC can open**, and nine separately-assembled bodies of software that
have nothing to do with one another.

It is the second CLIC disc here and the **first object measured from an image
rather than from a drive**. That is a gift and a cost, and the repository opens
by saying which: no lead-out, no table of contents, no subchannel, and a
302-sector tail of zeros that is a property of whoever made the image rather
than of the disc. It also makes this the *less* well-provenanced of the two
CLIC objects — `pc-clic11-doc` was read from a physical disc in a drive — and
where the two disagree, the first-hand artefact is the better witness. Three questions inherited from CLIC 11 are closed as *not
applicable* on that ground rather than repeated.

**The measurement this object exists for is an ownership map walked from both
filesystems at once.** Every sector map inherited into this collection assigns
each sector to at most one owner, because every previous disc had one filesystem
that mattered. This one has two and **they describe the same bytes**: the ISO
record for `/CATAL.HTM;1` and the HFS record for `Clic!/catal.htm` point at the
same LBA and mean the same 1,135 bytes. So the honest structure is a map of
*how many* owners each sector has, and the answer is that **96.7861 % of the
disc is owned twice**. Walked from both catalogues the map runs contiguously
from LBA 0 to LBA 248,358 and sums to 248,359, the declared volume space,
leaving **two sectors belonging to nobody** — LBA 136 and 137, both all-zero,
in the gap the Apple partition map opens by starting the HFS volume at LBA
138.25. Both zero-byte files on the disc point their extent field at one of
them. CLIC 11 left two of 322,926, also zero.

The 7,846 sectors the ISO side alone cannot explain decompose to the last one,
and **86.90 % of them are a granularity artefact**: an HFS allocation block here
is 10,240 bytes and an ISO extent is 2,048, so a hybrid can satisfy both only by
starting every file on a five-sector grid — and **2,821 of 2,823 records do**,
the two exceptions being the zero-byte files, which is 100 % of everything
containing a byte. The HFS side closes to the block: 49,439 file blocks + 102
catalogue + 102 extents = **49,643 = `drNmAlBlks`**, with zero free.

**Then the padding turns out not to be padding.** Not one of the 6,763 sectors
between the two grids is zero. None repeats its own file's tail — 0 of 2,395,
which kills the obvious explanation. And of 39 probes taken from the middle of
padding regions and searched against the whole 509 MB image, 8 land inside
another file, 14 only inside other padding, and **17 appear nowhere at all**;
one holds a fax cover-sheet template that is on no file of this disc. The
inherited `slack.py`, measuring the tail of each file's last sector for entirely
different reasons, agrees: **2,820 of 2,821 files have a dirty last sector**.
About **16.5 megabytes of this object is the uncleared working memory of a
machine in Milan in February 1997**, pressed onto a newsstand magazine's cover
disc and counted rather than transcribed.

**The two catalogues differ by exactly five Finder objects and by no content.**
`Desktop DB` (40,960 bytes), `Desktop DF` (**zero bytes and seven allocation
blocks**), and the invisible folders `Desktop Folder`, `Temporary Items` and
`Trash`. There is no Macintosh payload here at all — which closes CLIC 11's
standing Q6 in the negative and *structurally*, since this hybrid is a Macintosh
**view** of a PC disc rather than the 26,607,777 bytes of Mac-only material the
other one shipped, and the three files that question nominated are simply not
present.

**Five HTML files carry a 670-byte resource fork, and what is in it is somebody's
cursor.** Creator code `R*ch`, one resource of type `BBSR`: BBEdit. Inside is a
window rectangle — 502 × 346, thirty pixels from the left edge — the font
`Monaco` at size 9, and an insertion point, byte 757 of 1,135 for `CATAL.HTM`.
They are not the tree's entry points, which was the guess; they are **the last
five files anybody touched**. `CATAL.HTM` carries the newest directory record on
the whole disc, 17:03:32, eight minutes before the HFS volume was closed and
1 h 42 m 55 s before the ISO descriptor was written — a window in which **zero**
records fall, because that gap is the mastering run and nothing was still being
edited.

Five clocks agree on one week, and one of them is an accident: **twelve
`WS_FTP.LOG` files survive**, 884 transfers, recording the disc downloading
itself off `www1.mondadori.com` between Monday 10 February at 12:05 and Tuesday
at 13:59 — back issues first, then the current issue's images, then the
editorial pages section by section, and last of all the two cover images for the
two demos. Tomb Raider's directory kept a **Watcom linker map** naming every
source file of the game and the build stamp `96/09/03 22:38:51`, because a
developer's own two-line patch script shipped beside it and copied it there.
`MAGDEMO/PICS/` kept a **Paint Shop Pro thumbnail cache** whose header names the
folder it was made for.

**72.4342 % of the disc is a mail-order shop's catalogue** — 221 products in
three dBase tables of fourteen fields, carrying both the retail price and **the
trade price**, 39,900–149,000 against 25,700–111,800 lire, a 33.76 % margin
published by accident in 1997 — and **58.77 % of the whole object is 26 video
trailers for other companies' games**. **Tomb Raider is 9.74 %**: all 16 of 16
retail level names, 2 of 4 cut scenes, no FMV and no music, and it is **the only
one of the 221 products whose `DEMO` field is set**. The catalogue occupying
three quarters of the disc advertises exactly one playable demonstration, and
that demonstration is two directories away.

**The magazine made 0.82 % of its own disc and names itself 1,649 times.** The
distributor whose catalogue is 72 % names itself 69 times; GLAMM, who built the
object, fourteen. Copy protection is none — twelve markers over 75 executables,
one hit, and the hit is `SETTEC` in the middle of the Italian word
*SETTECENTO*. Absolute paths number **1,281**, from four vendors' machines in
Derby, Bellevue and Milan, while the same tool's 248 "Macintosh-shaped" hits are
noise out of Cinepak data and are reported as a fact about the heuristic rather
than added to a total. Leftovers are **4,898,814 bytes, 1.0017 %**, and
**sixty-two predictions written before the image was opened score 75.81 %**,
with the likeliest miss flagged in advance and duly missed.

The **Saga** cell fills for the first time in five rows, and it fills on
something new. The two CLIC discs share 1,792,592 bytes and **none of it is
theirs** — an Apple installer and a Microsoft runtime — so the rule's implicit
clause is made explicit, *shared bytes must belong to the objects*, and by that
reading the payload measurement is **zero**. What fills the cell instead is five
independent fingerprints of one production line, including 99.0622 % even
seconds against 99.11 % and two unowned zero sectors on both discs. It is a
change to how the rule is applied and it is argued rather than assumed.

And 104 files of readers' letters and 24,440 bytes of small ads carry 45 e-mail
addresses and 73 telephone numbers, belonging in part to people who in February
1997 wrote to a magazine hoping to swap floppy disks. The ones belonging to
companies are quoted. The ones belonging to people are counted, and appear
nowhere in the repository.

---

### [Il Mio Computer 02/2006](https://github.com/vs-sr-dev/pc-ilmiocomputer0206-doc)

The CD-ROM bound into the Italian magazine *Il Mio Computer*, mastered with
**Nero Burning ROM on 4 January 2006 at 16:46:00 GMT+01:00**, and the first
object in this collection that arrived as **raw 2,352-byte sectors**. Every
previous CD here was a copied file tree, a cooked 2,048-byte image, or a disc in
a drive, and all three discard the same thing: the sync pattern, the address
header, the subheader and the error-correction fields. This one kept them, so
for the first time the framing could be censused rather than assumed —
**349,462 correct sync patterns, 349,462 addresses equal to LBA + 150, zero
Mode 2 Form 2 sectors, and 349,462 of 349,462 EDCs verifying**.

The frame costs **106,236,448 bytes, 12.9252 % of the file**, and 97,849,360 of
that is Reed-Solomon parity — thirteen times everything the magazine itself
wrote. It is a descriptor of a kind this index has not had before: it does not
say what the data is or how long it is, it describes **the data itself**. Its
designers' model of what could go wrong was a scratch, and against a scratch it
is overwhelming.

And on the one question the session actually needed answered — did the burner
write the 155 blank sectors at the end of the disc, or did the dumper? — all 106
million bytes of it are **silent**, because the EDC of an all-zero sector is
zero and the parity of an all-zero codeword is zero, so a synthesiser and a
burner produce identical bytes. What answered was a **four-byte integer at
offset 80 of sector 16**: the volume space reads 349,462, which is the whole
image, so Nero counted its own padding. Two descriptors, both exactly as good as
their models, and the expensive one could not answer what the cheap one did.

Three questions carried in from other repositories closed. **Q5 of CLIC 02/97**
— is dirty slack a property of Toast or of writing CDs? — closed in one command:
1,263,580 slack bytes on this disc, **100.0000 % zero, 0 of 1,422 files dirty**,
against 2,820 of 2,821 dirty and roughly 16.5 MB of somebody's uncleared memory
on the 1997 disc. It was Toast. **Q2 of CLIC 11** closed too. **Q1 of CLIC 11**
narrowed and stayed open, and the row says so: the 150 is shown to be the
medium's, but this disc is neither Toast nor a hybrid, so the disputed 2 is
still unattributed and the session briefing's claim that this was the missing
control does not hold.

What makes the object worth a row here rather than only a spec sheet is that it
**declares its own contents three times and the three disagree in a structured
way** — 34 bullets printed on the sleeve, 50 entries in its own HTML each with a
licence and an operating system, 45 product directories — and the disagreement
resolves exactly: the four numbers on the disc face are counts of directories,
`11 + 4 + 13 = 28`, and they account for all 45 with nothing left over. The face
counted the disc; the back listed the products.

The **Saga** cell is empty, and for the rule rather than for lack of trying.
This is the only issue of this magazine in the collection: nothing to share
payload with, and — unlike the two CLIC discs, whose cell filled last time on
*measured process* — nothing to share a process with either, since those are
Toast on a Macintosh and this is Nero on Windows, hybrid against Joliet, nine
years apart, with **zero shared bytes** across twenty hash lists. What the
object does have is a series, and it is internal: its own database records
sixteen consecutive issues, 113 to 128, which is what dates this one to
**numero 129** — a number printed nowhere on the disc or its packaging.

The row is in an index of games and **this is not a game**. Four freeware board
games weigh 1.2664 %, and the argument for the row is not that percentage: it is
that the publisher printed `4 GIOCHI` in a black box on the label as one of the
five things worth naming, and that the disc's own catalogue of the sixteen
issues before it types **131 of 684 published programs — 19.2 % — as `Gioco`**,
the third-largest of fourteen standing categories. This is not a software disc
that happens to have games on it. It is one month of a magazine that published a
hundred and thirty-one of them in sixteen issues, and this month it published
four. Both measurements are in the cell so that nobody has to take the label's
word for it.

Three e-mail addresses on the publisher's domain sit on this object, each
appearing exactly once. One is a subscriptions desk and is quoted. Two are named
individuals whose working addresses were pressed onto a cover disc so that
readers would write to them — and on this disc **the name and the address are
the same string**, so the colophon reading that would allow the names to be
reported cannot be separated from publishing two live-looking work addresses.
They are counted and appear nowhere in the repository, `notes/` included, and
the ten developer account names found inside third-party build paths are
counted the same way.


---

### [Flight of the Amazon Queen](https://github.com/vs-sr-dev/pc-flightoftheamazonqueen-doc)

An installed copy of the GOG edition of a 1995 Australian point-and-click
adventure: 45 files, 237,605,368 bytes, four bodies of software written by three
groups of people twenty-two years apart, and one file that is 80.2959 % of the
whole and **contains no index of itself**. `queen.1` has no header, no directory,
no terminator and not one byte anywhere in it that says where a resource begins
or ends. It is 7,671 things laid end to end in alphabetical order.

The table that describes it is not on the object. It is compiled into
`scummvm.exe` — a free program written by other people in 2017, which is also a
file of the object, which is also the tool this repository measured the object
with. That collision has not happened here before, and the practice adopted is
the narrow one: **read it, never run it, and say on every figure whose reading it
is.**

Inside that executable, announced by the four bytes `QTBL`, sixteen tables run
head to tail, each preceded by its own 16-bit big-endian record count, with a
sixteen-entry little-endian index elsewhere in the binary naming each release and
declaring its data file's size. Every one of the sixteen sums to its declared
size **to the byte**. Six of them describe `queen.1` with zero holes and zero
overlaps, and five of those six are the French, German, Italian, Spanish and
Hebrew editions of the same game — near-identical files made by the same people
for other markets. The prettiest wrong answer covers **99.9703 %** and leaves a
56,643-byte tail that looks exactly like the kind of reperto this family
collects; it is the German table, cut off at record 6,924 because record 6,925
would have run 20,935 bytes past the end of the English file and a bounds check
dropped it without saying so.

Arithmetic cannot separate them. Content can, and it is not subtle: a `.PCX`
begins with the byte `0A`, and on the right table **128 of 128** do while on
every other table in the executable **none** do. Chosen that way, the coverage
closes at **100.000000 %** with 0 holes, 0 overlaps, 0 duplicate names, first
byte 0 and last byte 190,787,021 — the most complete description of an object
this collection has measured, and it was reconstructed by strangers two decades
after the fact, because their model was bigger: they were not describing this
file, they were describing sixteen editions at once.

Nothing in the file is compressed — 0 of 2,911 blocks above 7.5 bits of entropy —
so for once there is no excuse and every format was opened. The **speech** is
6,749 resources and 170,238,763 bytes, **89.2297 %**, and its container was
derived rather than guessed: a block count recovered by requiring that offset
plus payload equal the resource size exactly, which it does for 6,749 of 6,749
with no ambiguities. That gives **4 h 16 m 13.662 s** at the engine's 11,025 Hz —
the one number in the repository that is imported rather than measured, said so
everywhere it is used, and checked against the game's own 27,575 words, which
puts the delivery at 107.6 words a minute and excludes both alternative rates.
**Twelve and three quarter per cent of that payload is the byte 128 exactly**:
thirty-two minutes and forty-four seconds of digital silence, pressed onto every
copy because the disc was cheaper than the labour of trimming it.

The briefing for the session offered a higher figure, 92.2725 %, on the grounds
that eighty-six `.SAM` resources "look like audio too". They are sprite banks.
All 281 frame banks — `.BBK`, `.ACT`, `.SAM` — parse as a frame count followed by
frames of width, height and two hotspots, and all 281 close with **residue zero**
over 5,266 frames. Six bytes of header are not a format.

Two fixed-size populations solved: 65 masks of exactly 8,000 bytes are a
**160 × 50 grid of 4 × 4 pixel cells** covering a room of up to 640 × 200, which
is provable from the population rather than the file — 40 of the 65 use exactly
80 columns, which is a 320-wide room, and 52 use exactly 38 rows, which is the
150-pixel play area above the panel. 63 ramps of exactly 24 bytes are eight RGB
triples of **signed** offsets, and the credits name them: *Dynalum System*.

The music is **259 Standard MIDI files** inside five index-plus-data containers,
one of them still carrying `Copyright (C) 1990 by Voyetra Technologies` in a text
meta event. It is 0.5701 % of the disc and contributes **nought seconds** of
recorded reality, which is the whole economics of a 1995 talkie in one line: a
minute of eight-bit mono voice costs about 664,000 bytes and a minute of
sequenced music costs a few hundred.

375 resources begin `AmBk`, the header of an **AMOS memory bank** — AMOS being a
BASIC for the Commodore Amiga. All 375 close to the byte under a big-endian
reading and to values in the billions under a little-endian one, and so does the
whole 7,671-record resource table. The credits explain it in two lines: *JASPAR
Game Engine — John Passfield* and *JASPAR PC Conversion — Tony Ball*. The DOS
release is a conversion of the **program**; the data stayed exactly where it was,
in 68000 word order, and thirty-one years later a storefront resold it that way.

The written work is 626,243 bytes, **0.328242 %**. `QUEEN.JAS` alone is 79,642 —
**one part in 2,395.56** — and `QUEEN2.JAS` is 35,840 bytes of plain ASCII holding
all 1,427 lines the game can display. The dialogue is 22,608 more words inside 73
AMOS banks. Two people wrote a short novella and twelve actors were hired to read
it; the reading takes 6,174 bytes per word. The chapter that argues *recorded work
or written work* lands on **written**, because deleting the 170 megabytes leaves a
game that runs with subtitles — the floppy release, at one eighth the size, is on
the same executable's index — while deleting the 79,642 bytes leaves nothing but a
stranger's voice in an empty room.

The leftovers are 4,014,943 bytes, 1.6898 %, and **98.23 % of them by mass belong
to the shop and the interpreter** — the *Lands of Lore* finding again. What the
game itself contributed is 71,066 bytes and it is the best of them: two **backup
files with their own entries in the resource table**, `X6.BAK` (a PCX, 15,077
bytes larger than the `X6.PCX` that shipped) and `C30C_131.BAK` (a recording, a
third the length of the `C30C_131.SB` that shipped), plus `DATA`, the 1994 credit
roll superseded by the 1995 one and still on every copy. `X6.BAK` is, by the
alphabetical sort, the **last resource in the file**: the final 63,834 bytes of a
190-megabyte commercial master are somebody's undo file.

The shop's descriptor covers **2 of 45 files — 4.4444 % by count and 82.2422 % by
bytes**, the lowest by count and the highest by mass this collection has seen, and
the two are exactly the files GOG did not make. `pc-landsoflore-doc` measured the
same structure at 35 of 65 and concluded that *what a descriptor covers is the
reperto*; this one covers the irreplaceable input and vouches for none of its own
output, including the 34-megabyte interpreter without which the input is unreadable.

The 1995 object contains **no personal data at all** — zero real e-mail addresses,
zero telephone numbers, zero absolute paths in 190,787,021 bytes, against 2,775,312
printable runs and 42 path-shaped strings that are all waveform. The 2026
installation contains three identifiers of the machine that made it: the install
path 25 times over four files, a volume label, and a NetBIOS name inside the
shortcut's tracker block. They are counted and never written, and a tool in the
repository reads all three out of the object and proves that none of them appears
in any committed file.

The **Saga** cell is empty, and for the rule rather than for lack of trying. This
is the only object of this studio in the collection; there are zero shared bytes
against 23 hash lists; and there is no shared process to fall back on either, in
the sense *CLIC 02/97* established and *Il Mio Computer 02/2006* applied — the
nearest specimen here, *Sam & Max Hit the Road*, shares a year, a genre and a
percentage (88.11 against 89.2297) and shares neither an engine, a toolchain, a
continent nor a byte. That two adventures built that far apart land within a point
of each other is the strongest evidence this index has that the recorded-reality
column is measuring **what storage cost in 1995**, and not what either game is.

### [Resident Evil](https://github.com/vs-sr-dev/pc-residentevil-doc)

The twenty-ninth object, the second in this branch to arrive as raw 2,352-byte
sectors, and the first whose filesystem tells the truth about when its contents
were made.

`Resident Evil (Europe).bin` is **736,133,664 bytes** and it is the disc, not a
copy of its files: **312,982 sectors of 2,352 with no remainder**, in **Mode 1**.
The inherited raw census could not read a byte of it, and the way it failed is
the useful kind. Pointed at the image unmodified, `rawcensus.py --validate`
reports that its vectorised CRC agrees with its own scalar reference on 64 of 64
sectors and agrees with the disc on **0 of 64** — arithmetic right, answer wrong,
which means the polynomial is fine and the bytes it is being fed are not. Mode 2
Form 1 computes its error-detection code over bytes 16..2071, deliberately
excluding the sync and the header; **Mode 1 computes it over bytes 0..2063,
starting at byte zero**. That is the whole difference, and a new tool was written
around it rather than the old one bent.

Censused whole, with nothing sampled: **312,982 correct sync patterns, 312,982
header addresses equal to LBA + 150 in BCD, mode byte 1 on 312,982, 312,982 of
312,982 EDCs verified, and both ECMA-130 Reed-Solomon parity blocks recomputed
and matched on 312,982 of 312,982.** Zero mismatches of any kind, and the eight
reserved bytes between the EDC and the ECC are zero in every sector. The parity
took two attempts and the mistake is worth keeping: **P is computed over the
2,064 bytes at offsets 12..2075 and Q over the 2,236 at 12..2247**, which is the
same data *plus the P parity that was just written*. Q protects P. Assuming
otherwise reads off the end of the array, and three assertions now sit under the
gather tables so the next person gets an index error rather than a plausible
wrong number.

Il Mio Computer 02/2006 spends **12.9252 %** of itself on its frame and so does
this. That looks like a coincidence between two discs and it is a fact about one
division: Mode 1 spends 12 + 4 + 4 + 8 + 276 non-payload bytes and Mode 2 Form 1
spends 12 + 4 + 8 + 4 + 276, the two layouts disagree about what those bytes are
and agree exactly on how many, and 304 ÷ 2352 = 0.129251700680… Any disc in
either mode gives the same figure. What *is* about this disc is the other
division: 86,383,032 bytes of Reed-Solomon, **13.6084 % of the 634,776,465 bytes
of files** — for every eight bytes of Resident Evil, roughly one byte whose only
job is to survive a scratch.

**The dates are the reason this object is not like the other twenty-eight.**

Every previous session concluded that a filesystem dates the copy. This one
concludes the opposite and has to demonstrate it, because the safe conclusion is
safe for a reason. There are **1,102 distinct timestamps over 129 distinct days**,
1995-07-10 to 1997-08-22 — a burn writes one, and even a sloppy burn writes a
handful.

Two tests, and the second has a control group inside the same volume. ISO 9660
gives the seconds field a whole byte and can record an odd second; FAT stores
time in two-second units and cannot. The seconds are even on 3,436 of 3,436 file
records — which is worth less than it looks, because **798 of them read exactly
`00:00:00`** and zero is even for free. On the denominator that carries
information the answer is **2,638 of 2,638**. And the 47 *directory* records,
written by the mastering program on the day of the burn, in the same field of the
same volume, are even on **25 of 47**, which is chance. Two populations, one
volume, one field.

The second test needs no filesystem at all. A PE carries a COFF timestamp that
the format defines as UTC; the ISO record carries a wall-clock reading with no
zone attached; subtract them and the difference is a place. Twenty-six DirectX
files come out at **+7:00**, which is Redmond in August. Four of the five programs
in the root, plus one game data file, come out at **−9:00** — `CHECKER.EXE` and
`UNINSTALL.EXE` to the exact second, `LAUNCH.EXE` and `BIOVFWUS.BIN` one second
out, `SETUP.EXE` fifteen. Nine hours ahead of UTC is Japan. `LAUNCH.EXE` is the
prettiest of them: linked at 05:45:57 UTC, which is 14:45:**57** in Tokyo,
recorded as 14:45:**56** — FAT rounding an odd second down, caught in the act on
a file whose true second is known from a second source. The two tests corroborate
each other.

Every one of the 3,436 records declares a timezone of GMT+01:00, which is where
the disc was mastered, and is wrong about all of them. `RESIDENTEVIL.EXE` fits
neither pattern — its record sits two hours and fifty-two minutes after its own
link, which is no zone — and the repository says so and leaves it open rather
than rounding it into the story.

**The port converted the media and kept the model.**

Everything that is a recording of the world is in a PC format: 27 Cinepak `.AVI`
and 1,110 PCM `.WAV`, both RIFF, both playable by Video for Windows in 1997.
Everything that is a description of the world is in the PlayStation's:
**2,601 TIM textures and 828 TMD models**, validated, inside a Win32 product.
Zero bytes of film or speech sit in a PlayStation container and zero textures or
models sit in a RIFF one. The line does not run along any aesthetic judgement —
it runs exactly along the boundary of what Microsoft had already written a reader
for, which is the only sensible way to spend a porting budget and is legible in
the byte counts thirty years later.

Validation is the whole job on that count. The raw grep for the two identifiers
finds **44,047** candidates in 634 MB, because `0x00000010` is the integer
sixteen; requiring each candidate to satisfy the format's own length arithmetic
leaves **3,429**, and the ratio is the finding. Along the way `.IVM` stopped
being a puzzle: it shares its first eight bytes with `.TIM` and it is a **TIM
followed by a TMD** — a texture and the model it wraps — 77 of 77 closing on the
byte. `.ETM` is **eight TIMs and a trailing index of eight offsets in descending
order**, residue zero. And the TMD pointer base, about which published
descriptions disagree, was settled by arithmetic on one file: taken as the
address after the object table the normals end 28 bytes past the end of a
92,896-byte file, and taken as the address *of* the object table the primitives
start immediately after the table, the normals start exactly where the vertices
end, and the last normal lands on the last byte. One reading closes and the other
does not.

**`.PAK` was derived before it was described.**

The most numerous format after the sound, 1,112 files, nothing on the disc
describing it, and the executable containing no zigzag order, no quantisation
table and no format name. Asked cold, the bytes said five things: entropy 7.95,
so entropy-coded; **42,632 of 42,634 four-byte sequences distinct** in one
specimen, so not an LZ77 that emits literal bytes; sizes ending mid-byte;
a tail with a period of exactly **forty bits** whose successive groups differ by
`0x0040100401`, which is bits 0, 10, 20 and 30 — four ten-bit fields each one
greater than the last, the fingerprint of a dictionary coder emitting consecutive
codes at a ten-bit width; and, decisively, that the **first nine bits of every
file read 16**, which is `10 00 00 00`, which is the PlayStation TIM identifier
sitting in the open before a single dictionary entry exists.

It is LZW, and the published description confirmed all five. **1,112 of 1,112
decompress and close as a TIM with residue zero**, 38,754,842 bytes becoming
124,641,776 — 675 backgrounds at 320 × 240 in sixteen-bit direct colour, 436
sprite pages at 8 bits with a palette, compressing three to one and six to one
respectively.

And then they were rendered, which is the part arithmetic cannot do. A
decompression that produced the right *number* of scrambled bytes would close
just as well. The first render came out speckled with white, which was this
repository's bug — the PlayStation's rule that `0x0000` is transparent punches
holes in a background, which is never composited — and the second came out as a
dark room with a wardrobe, hanging coats and a rug. Then one did not: `RC2000.PAK`
rendered as diagonal bands. Measured rather than eyeballed, by finding the
horizontal shift between adjacent rows that minimises their difference, it shows
**+4 pixels per row on 190 of 239 row pairs**, and read at a stride of 316 it
resolves into a decorated glass skylight seen from below. The arithmetic finishes
it: 316 × 240 halfwords is 151,680 bytes, the pixel block is 153,600, and the
1,920-byte difference is exactly four columns of 240 rows, held back and written
after the last row.

Across the population, **28 of 676 backgrounds are like that** — 26 of them in
four contiguous rooms of `STAGE3` — and **nothing in the file distinguishes
them**: same frame-buffer coordinates, same declared width, same declared height
as the 643 that are right. Either the executable carries a per-room width that
overrides the header, or four rooms of the retail European release ship sheared.
The repository could not tell which and says so.

**Two kinds of recorded reality in one object, for the first time.**

The film is 245,601,342 bytes, **38.6910 %**, 12,598 frames — declared in the
headers and counted in the movie lists, agreeing on all 27 files — running
**1,199.7988 s** at two frame rates, so the 10.5 fps the population implies is
the ratio of two sums and is quoted nowhere. The sound is 189,466,918 bytes,
**5,027.658866213 s**, closed by two routes that use different header fields with
a largest disagreement of **0.000000000 s**, and by a third that walks the chunk
tree and accounts for every byte of 1,110 files of 1,110.

But 40.68 minutes of it is dialogue and 43.11 minutes is effects and music, and
**the music is eight-bit while every one of the 563 dialogue files is sixteen** —
a budget decision, and the opposite of the one most 1997 games made. Reported as
one number the object is 68.5388 % recorded reality, near the top of this index's
column; reported as *speech*, which is what that column was built to hold, it is
**16.9618 %** and near the bottom. Both are published with the layer named, and
the argument is that the column has been conflating filmed reality with recorded
speech since it was created.

The second denominator is new. `.AVI` + `.WAV` is 68.5388 % of the **file bytes**
and **59.1018 % of the raw image**, and the 9.4370 points between them are the CD
frame. No previous entry in this index could put that inside the fraction,
because every earlier object had already had its frame stripped off by whoever
copied it.

**The installer as a fourth descriptor.** `SETUP.EXE` contains 2,901
one-directory-deep references, 2,895 distinct names, occupying 19.33 % of the
file and followed by a pointer table. It describes something that does not exist
yet: a buyer's hard disc. Set against the disc, matched by bare filename so that
the eight names which break 8.3 are not lost, the result is clean in both
directions — **the set it never mentions is exactly the 27 `.AVI` files**,
245,601,342 bytes that stay on the CD and stream, and the set it names that is
not there is **empty**. No cut file, no other edition's asset, no ghost.

**Thirteen crossings, after eight sessions of zero.** `DOS4GW.EXE` in Diamond's
driver folder is byte-identical to the copy inside a Tomb Raider demo on CLIC
02/97, an Italian magazine disc from five months earlier — confirmed by reading
265,396 bytes out of the other image and comparing them one at a time, not by
comparing two hashes. And twelve DirectX driver files are identical to Final
Fantasy VIII's, two of them **under different names**: `883D_DIG.INI` here is
`5631_DIG.INI` there, 38,690 bytes, the same. Not one byte of game data crossed,
across 29 objects and 24,912 hash tokens. *Every disc is an island* becomes
*every disc is an island except for the software nobody on it wrote and everybody
copied*, and the difference between those two sentences is the only interesting
thing a DOS extender has ever had to say.

**What it cost to not be a console.** A PlayStation had one graphics chip and
every PlayStation had the same one. This disc ships DirectX 3a as a prerequisite
Windows 95 genuinely lacked, the development drivers of three of the six
accelerator cards its readme names — admitted in writing, the first documented
leftover in this index — six command-line switches named after those cards, and a
`LAUNCH.EXE` that is **66.82 % the size of the game** and exists only to work out
what is in the machine. **3.7889 %** of the file bytes, and the shape of it
matters more than the size. It also ships, on a European disc, **4,137,303 bytes
of drivers for the NEC PC-9800**, a Japanese-market architecture that could not
have run the game, one of whose files opens with the ASCII string
`PC-9821Na13/12`. Nobody decided that. Somebody copied a directory.

The disc is otherwise almost perfectly tidy: **3,599,471 bytes of slack, 100 %
zero, 0 dirty files of 3,436**; 1,144 unclaimed sectors in 31 runs with **zero
runs containing anything**; no copy protection across eleven schemes; and one
person's work e-mail address, sixteen and a half megabytes inside the largest
video file, counted twice and written nowhere.

Sixty-two predictions were written before the image was opened: **36 hit, 17
half, 9 miss, 71.8 %**. Six of the nine misses are the same failure — believing
the session briefing's account of what a file header says instead of running a
twelve-byte head census — and the remedy is the one that worked last time.

### [Resident Evil 2](https://github.com/vs-sr-dev/pc-residentevil2-doc)

The thirtieth object, and the first that is **two**. `RES2 LEON.bin` is
758,583,504 bytes and `RES2 CLAIRE.bin` is 722,626,128, both raw — 322,527 and
307,239 sectors of 2,352, remainder zero on each — and the first question a
two-disc product has to answer is how much of one is the other.

**1,696 shared content hashes, 357,785,576 bytes, 54.4374 % of Leon and
57.1645 % of Claire.** Four of the seven layers are duplicated perfectly:
`COMMON` (1,005 files, 251,181,574 bytes), `ZMOVIE`, `GALLERY` and `DRIVERS` are
byte-identical between the discs, file for file, with zero differing and zero
present on one side only. Outside the scenario directories **exactly three files
differ**: `AUTORUN.INF` by two bytes, `REGIST/RES2_INST.EXE` by 25.3019 %, and
`RESIDENTEVIL2.EXE` — same 1,001,984 bytes on both discs, **809,643 of them
different, 80.8040 %, in 55,023 runs**. That is not one build with a flag
changed; it is two compilations twenty-six days apart, and they carry different
strings: Leon's holds `http://www.virgin.com` and Claire's holds
`http://www.vie.co.uk`. The measurement forced six denominators where every
earlier object here needed two, and every figure in the repository names which
one it uses.

**The sectors are Mode 2 Form 1 and nothing on either disc uses Mode 2.** Both
cue sheets say `MODE2/2352` and both tell the truth: mode byte 2 on 100 % of
629,766 sectors, Form 1 on 100 %, Form 2 on none, and **629,766 of 629,766 EDCs
verified with zero mismatches of any kind**. But the eight bytes that
distinguish Mode 2 from Mode 1 — the subheader, which exists to say *this sector
is data* or *audio* or *the end of a record* — are `00 00 00 00 00 00 00 00` on
**every sector of both discs**. Submode 0 does not have the `data` bit set, so
by the letter of CD-ROM XA every sector on this object declares itself to be
nothing in particular. There is no `CD-XA001` marker on any of the four
descriptors and **0 of 2,230 and 0 of 2,260 directory records** carry XA's
System Use area. The discs spend 5,038,128 bytes writing, into the field Mode 2
reserves for meaning, exactly the bytes Mode 1 reserves for nothing. Both modes
cost 304 bytes a sector — **12.9252 % on both discs, which is 304 ÷ 2,352 and
was proved a constant last session, so it is cited here and not re-derived** —
and the choice was therefore free and empty. This is a Mode 1 disc in a Mode 2
wrapper, and the one practical consequence, that the payload starts at offset 24
instead of 16, is what killed a tool written twenty-four hours earlier.

**The unclaimed space is not empty, for the first time in thirty objects.** Each
disc has 304 sectors the filesystem does not reach and both runs contain
something. Sector 19 holds `CeQuadrat Joliet directory link table` followed by a
count of **37** and **37 pairs of dwords** — a complete map from Joliet
directory extents to primary ones, in path-table order, **all 37 of 37
resolved**, referenced by neither namespace. The last sector of the volume space
holds `CeQuadrat ISO 9660 formatter information block`, then **its own sector
address written both-endian**, which is ISO 9660's own convention applied to a
structure ISO 9660 knows nothing about, then 1,908 zero bytes and `AA 55 55 AA`.
168 non-null bytes across the two discs, and the sector accounting closes on
them with **residue 0**: 16 + 3 + 1 + 4 + 161 + 322,039 + 1 = 322,225, the
declared volume space exactly. So the collection's oldest question gets its
sharpest answer in eighteen: the descriptor is not merely silent about the
lead-out, it counts two sectors into its own volume size that its own author
wrote and provides no way to reach them. The mastering program's timezone bytes
are **−66 and +113** on both discs, and ECMA-119 allows −48 to +52.

**Last session's proof about dates does not work here, and finding out why is
the result.** Yesterday's demonstration that a volume's file dates came from a
FAT source was a contrast: every file record even, the mastering program's
directory records even only by chance. Here both populations are even — 2,194 of
2,194, 2,224 of 2,224, 36 of 36 and 36 of 36 — so the contrast is gone. A new
test settles it: **all 36 directory records on each disc are dated the burn day**,
inside a five-minute window, which makes them CeQuadrat's own work; and Claire's
volume-descriptor creation stamp carries an **odd** second, `14:35:11.95`, which
proves CeQuadrat's clock is not restricted to even ones. The program therefore
has two code paths at two resolutions, and the parity of the file dates is
**fully explained by the writer**. The evidence is consumed before it reaches the
question, the FAT origin here is undetermined, and last year's conclusion is not
inherited. What survives without needing parity is that the dates are the work's:
1,446 and 1,478 distinct timestamps over 159 and 153 days, spanning **835 days**
from 1996-10-20 to 1999-02-01, with **zero records at midnight**.

**Tokyo is on a European disc for the second year running, and this time the
exception explains itself.** Four CAPCOM binaries on Leon and **five on Claire**
sit between −32,399 and −32,412 seconds from their own COFF stamps — nine hours,
which is Japan — while every one of the 4,418 records declares GMT+00:00. Last
session's open question was why the game executable was the one binary that did
*not* sit there. Here it exists twice: **Claire's copy is at −32,401 seconds like
the rest, and Leon's is the only file of 2,194 whose internal clock is newer than
its own directory record**, by 25 days 2:02:31. A file cannot be copied before it
exists, so Leon's master was assembled in January, the executable was rebuilt on
16 February, and the new binary was dropped in without its timestamp being
updated. The main executable is the file that gets rebuilt last, and on the disc
where nobody rebuilt it, it sits with the others exactly.

**The largest extension on the object is a lie about 55.7755 % of it.** `.BIN` is
254 files and 715,671,936 bytes and it is six unrelated formats: 32 RIFF/AVI
films, five indexed archives, 100 in-game documents, four PlayStation TIMs, one
Microsoft PE, and one third-party blob. Classified by signature instead of by
name, all five archives have their offset tables verified and **all five close
with residue 0** — `ROOMCUT.BIN` at 71,948,686 bytes uses 1,287 of 3,584 slots
and its members run from 179 bytes to 107,235, and three different
unused-slot conventions turned up where the first file opened showed one.

**Forty-two minutes of Indeo 5, counted and not decoded.** The 32 films are
`IV50` at **320 × 160** on 32 of 32 — 320 × 240 letterboxed to two thirds the
pixels, which is what made 555,978,176 bytes of full-motion video fit on two
CDs at all — 52,780 frames, **2,532.5314 seconds**. The inherited AVI counter
reported *0 frames, DISAGREE* on 32 files of 32 without saying why, because
these files name their video chunks `00iv` rather than the `00dc` every reader
expects; the repaired tool takes the stream number from the header, prints the
full inventory of chunk ids it sees, and closes declared frames against counted
frames on **34 of 34 files**. The mean film wants **219,536 bytes a second =
1.4293×** a single-speed drive and the fastest single file wants 1.95×, against
a readme that demands 4× and recommends 8×. Two years earlier the same
publisher's film wanted 1.33× and its readme asked for 2×. **The film's appetite
grew seven per cent; the machine the publisher assumed you owned doubled.**

**The `.SAP` sound bank was derived from the bytes and its header is not what it
looks like.** Eight bytes, then one or more self-delimiting `RIFF….WAVE` chunks.
The obvious reading of the first dword is a count of streams; it is a **bit
mask**. `WEAPON01.SAP` carries 481 — `1 1110 0001`, five bits set — and holds
five streams, and the tool asserts `popcount(mask) == streams walked` on every
file and passes on **1,495 of 1,495**, with container residue **0 bytes** and
zero files failing to close. Sixteen files per disc are eight bytes long and
hold nothing: empty sound banks for rooms with no sound of their own. Behind it,
a Microsoft ADPCM decoder written from the published definition — coefficients
read from each file's own `fmt` chunk, not hard-coded, checked block by block
against a scalar reference **19/19** before any census ran — decodes all 5,195
streams: **18,450.146848075 seconds, 307.5024 minutes**, closing to the byte.
Against 1997's 1,110 uncompressed files and 5,027.658866213 seconds, that is
**3.7 times the recorded sound in 1.7 times the bytes**, bought with one codec
decision: 4.0474 bits a sample against sixteen.

**The texture did not move and the model did.** Yesterday's object validated
2,601 PlayStation TIMs and **828 TMDs**; these validate 1,445 TIMs and **ten**
TMDs each. The characters are still there — 169 files of `.EMD`, `.PLD` and
`.PLW` on Leon — and the container was derived from the population by a single
equation, `dword0 == size − 4 × dword1`, which holds on **169 of 169** files on
Leon and 168 of 168 on Claire; the section table sits at `dword0`, ascends, and
begins at byte 8, on every one of them. Eight sections for an enemy, four for a
player or a weapon. And the geometry inside is **not TMD**: 277 of the 337 model
files contain the bytes `41 00 00 00` somewhere and **0 of 337** have a TMD
header that validates there. The music moved the other way — 232 `.BGM` files
whose first four bytes are `pQES`, the PlayStation sequence format, where 1997's
score was PCM in a Microsoft container.

**What would not open is named with its readings attached.** The background
compressor — 224 `.ADT` files and the 1,287 members of `ROOMCUT.BIN`, the same
format as each other, 147,670,436 bytes across the two discs — shares a role, a
directory and the `RC####` naming scheme with 1997's `.PAK` and shares no
algorithm: last session's decompressor raises `ValueError` on all of them. Four
of the five indicators that opened `.PAK` fire cleanly — entropy 7.9489 mean,
603 aligned four-byte repeats in four megabytes, 702 of 1,399 streams an odd
number of bytes long, and **every one of 1,399 streams ending `00 00`**, often
after runs of `AA` and `55` that are the same alternating bit pattern one bit
apart. The fifth does not: the first 32 bits take 17 distinct values and decode
to nothing under any of **twenty-four byte-oriented LZSS configurations**, every
one of which underflows within five output bytes. Declared underived. So is the
interior of the model container, and so is the other half of the `.RDT` room
record, of which **45.82 % validates as PlayStation texture** and the rest does
not resolve.

**Twelve files in common with its own predecessor, and 221 with Final Fantasy
VIII.** Swept against 58 repositories and 28,382 hash tokens, the discs cross
**222 times, 10,539,308 bytes, and every single crossing is in
`REGIST/DIRECTX`** — Microsoft's redistributable, eleven display drivers and a
licence in the case of the twelve it shares with Resident Evil. Zero textures,
zero models, zero sound, zero film, zero CAPCOM code. By shared bytes this game
is thirty times closer to a Squaresoft role-playing game than to the game it is
the sequel to, **which is what rewrote this index's Saga rule** — argued in the
repository's chapter 13 and in the paragraph above the table. Kinship measured
structurally runs the other way: seven traits shared with Resident Evil, of which
one is that both games carry exactly one `.ESP` file, both call it `CORE00.ESP`,
both put it in the engine's data directory, and the two files share **no bytes
at all**.

**Recorded reality: 75.3264 % of the distinct content, 68.9810 % of what was
manufactured, 59.7562 % of the raw images** — three figures because there are
six defensible denominators and mixing them silently would move the answer by
twenty-six points. The naive-sum figure lands within half a point of 1997's
68.5388 % and the raw-image figure within 0.7 of its 59.1018 %, and neither
coincidence is a fact about the games: it is what a CD full of film and speech
looks like twice. The honest number is the deduplicated one, and it is six
points higher than the manufactured one because the duplicated half of the
product is disproportionately film and sound.

**The price of not being a console rose from 3.7889 % to 5.3744 %**, and its
composition inverted: the runtime half nearly doubled while the driver half
shrank by a quarter and the number of supported chipsets went from six named by
brand to fourteen named by chip. There are **three** prerequisites now instead
of one — DirectX 6, DirectXMedia 6 and Indeo Video 5.06, all named in the
readme's imperative — and the third is a new kind of case, because a codec whose
absence makes 43.34 % of the object unreadable is not software the object fails
to need. Leftovers come to **11,490,859 bytes, 1.2418 %**, of which 4,703,784 is
a fourth DirectXMedia installer that is on Leon, is on no line of any readme, and
is not on Claire at all.

The discs are otherwise clean: slack **100.0000 % zero** on both, 0 dirty files
of 2,194 and 2,224; no copy protection across eleven schemes; **zero absolute
paths belonging to a CAPCOM or Virgin build machine in 1,481,209,632 bytes**,
against one in 736 MB last year; and no personal data — the single
person-shaped string on each disc sits at offset 163,960 inside the pixel block
of a TIM that closes with residue 0, and a second, wider pattern over all
558,219,896 bytes of Indeo video found one piece of compressed-video noise and
zero domains.

Seventy predictions were written before either image was opened. The briefing
they were written against contained **eight** errors, the largest of which
invented a chapter that does not exist — forty-nine `COMMON` files said to
differ between the discs, where the true number is zero and the 956 that
suggested it was a count of distinct hashes inside one disc rather than a
comparison between two.

### [Deadly Premonition: The Director's Cut](https://github.com/vs-sr-dev/pc-deadlypremonitiondc-doc)

The thirty-first object, and the first that is **not a disc**. It is a live GOG
installation on a working hard drive — 958 files, 6,877,549,781 bytes, somebody
else's save file in it — read once, in place, and never written to. Half the
apparatus this branch has built over eight sessions has no surface on it:
`toolclass.py` puts **149 of 226 tools** in a class that does not apply, and
**sixty-nine of those are one loss** — every reader of a raw sector, a volume
descriptor, an EDC field, a gap, a lead-out, a subchannel or a second disc,
retired in a single step.

**In exchange it is the first object in this collection that came with a list of
itself.** `goggame-galaxyFileList.ini` declares 1,098 entries, and the
comparison against a directory walk closes twice on the byte: **930 declared and
present, 6,855,369,290 bytes; 28 present and undeclared, 22,180,491; 930 + 28 =
958 and the two byte totals sum to the whole.** Seven of the manifest's entries
are directories rather than files and all seven exist, so the count of things
the publisher declared and the disk lacks is **zero, of anything**. That makes
the boundary of the object a document rather than a judgement, for the first
time in thirty-one — and the reason it exists is not the publisher but the
**installer**: this is the first title here installed through the GOG Galaxy
client rather than from an offline installer, which is what writes the list.

The 28 undeclared files sort into four classes with no residue: **seventeen
mods** (DXVK, 2024-11-18, and DPfix, 2013-10-29 to 2013-12-03), **five files
belonging to the player**, and **six GOG's own**, including the list itself,
which cannot list itself. Not one file of the game is missing from the
publisher's list. The two mods are a stratigraphy: DPfix is a `d3d9.dll` wrapper
and the `d3d9.dll` in the folder is DXVK's, so **the second repair silently
disabled the first** eleven years later, and of DXVK's five libraries **four
cannot be reached by this game at all** — `DP.exe` imports one function from
`d3d9.dll` and nothing from the other four.

**The program is 10,809,344 bytes, which is 0.157677 % of the object — one part
in 634.** Everything else is something it reads, and three things account for
**96.7204 %**: 2,972,941,025 bytes of Windows Media (43.3666 %), 2,228,707,120
of one archive (32.5104 %), 1,428,894,575 of sound (20.8437 %).

**The archive is the finding.** `updata\_flink\DPSerial.001/.002/.003` are
three independent containers with no table of contents. Every member is preceded
by a fixed 256-byte record holding nothing but the **absolute path that file had
on the machine which built it**, NUL-terminated and padded with `0xCC`:

    D:\programmer_PC\main\UPDATA/BG/BG.PRM

Note the separators: backslash for the first three components and forward slash
below, on **14,328 of 14,328 paths**, because a Windows constant was pasted in
front of a console-style relative list. Two readers were written and made to
argue — a signature scanner that knows nothing about the format, and a walker
that hops by the length field at offset 256 — and they agree on **every one of
the 14,328 record offsets and names, with residue 0 on all three archives**.
Every byte of 2,228,707,120 is a record, a length, a member or zero padding.

And they are **not a residue**. There is no other index; the archives close with
no room for one; `D:\programmer_PC` appears **zero** times in `DP.exe`, which
instead carries 17,991 occurrences of `UPDATA/` in relative forward-slash form.
So the runtime matches on the tail and steps over a 22-byte prefix 14,328 times
— **315,216 bytes of a stranger's drive letter and home directory that the
program deliberately skips and cannot remove**. Reconstructed, the paths give
something this collection has never had: **the complete asset tree of a shipped
game's development machine**, 3,015 directories deep to eight components, with
`ZZZ` and `DEB` branches in it, three PlayStation 3 `PARAM.SFO`, three sets of
XMB icons, and **three Windows Explorer `THUMBS.DB`** — thumbnail caches created
by somebody looking at their own folder, swept into a retail archive and given
entries in its index.

**The sound exists twice, and the proof is arithmetic.** `updata\sound\` (26
files, 505,061,852 bytes) and `updata\soundex\` (27 files, 923,832,723) share
eighteen file names and **not one byte**. One is Microsoft XACT — `WBND`, `SDBK`,
`XGSF`, thirteen banks, 6,704 entries — and its fourteen headers are stamped
**2013-09-27 10:25:42 UTC with platform byte 1, Windows**. The other is Access
Games' own `XSB2`, derived here from the bytes, 6,673 entries, and it **closes on
the byte on 13 of 13 banks**. Computed independently from each side, the two hold
**38,592.4 and 38,614.9 seconds** — 643.21 minutes against 643.58, **0.06 %
apart**. Forty-eight six-channel cues on each side, exactly. Ninety-one music
cues in one bank on one side and 43 + 20 + 16 + 12 = **91** across four banks on
the other. It is the same ten hours and forty-three minutes, repacked and
re-encoded, and one of the two copies is dead weight: `sound\`'s codec has a
constant 152-byte frame on 6,673 of 6,673 streams, no Windows decoder, and
nothing in the folder supplies one.

**The film is three strata and a duplicate.** Forty-one ASF files, 70.90 minutes,
1280×720 on all, and the internal creation dates partition them in a way that
agrees with the codec and the audio format in every single case: four encoded in
**2007**, twenty-three in **2009**, twelve with **no date and no encoder string
at all** in Windows Media Video 8, and **two** encoded as VC-1 on a Windows 7 SP1
machine in October 2013. Those two, 194,085,716 bytes, are the only film in this
object made for this platform. And `add08_us.wmv` and `add09_us.wmv` are
**byte-identical**: the same 318,384,245 bytes, the same 469.715 seconds, shipped
twice under two names — **4.6443 % of the whole object**, and on its own
**27.6 times** the largest leftover this collection had previously measured.

**And it still asks for a disc that was never pressed.** `DP.exe` contains, six
times and in six languages, the message `Please insert Rainy Woods disc.` —
*Rainy Woods* being the title this game was announced under in **2007** and then
withdrawn from. Two unrelated measurements corroborate each other across four
chapters: that string, and the fact that the four oldest films in the object
carry ASF creation dates of **2007-09-10 to 2007-10-12** and are the only ones
encoded at 44.1 kHz 24-bit. The credit roll agrees from a third direction — it
is a `.prm` parameter table, 502,368 bytes, present **thirteen times** in this
object, naming seven companies and closing with a **2010** copyright line three
years before the binary that displays it.

**The reputation was the reason this object was chosen, and the structure does
not confirm it.** Deadly Premonition is famous for being broken. Measured against
a criterion stated before the verdict — an indicator *fires* only if it names a
mechanism visible in the bytes — **nine fire, seven turn out to be cosmetic, and
nine acquit**. `TODO: <Company name>` is in the second column: a version resource
is metadata about a file and changes nothing the program does. What is in the
first column is duller and real: **three imported libraries absent** (36 of 183
functions, 19.67 % of the import surface), of which `PhysXLoader.dll` belongs to
a **2009** physics API whose prerequisite installer, on a modern machine,
correctly reports that a newer version is already present and installs nothing;
**no ASLR and no DEP on the game while its own launcher has both**, from the same
linker in the same fortnight, which the Rich headers prove is a project setting
and not a toolchain; **zlib 1.2.1 of 2003** statically linked into a 2013 build;
and a localisation record, `RAINCOAT000.DLC`, whose four non-English names are
`EMILY002.DLC`'s **character for character**. What acquits it is the code:
`DP.exe` is four clean sections, `.text` at 6.616 bits, **99.99 % of the file
inside its sections and zero bytes after the last one**, no packer, no protection
residue, an intact Rich header. The verdict is that **the code is ordinary and
the box was filled by copying a directory** — and the box contains, in a Windows
game, thirty-two PlayStation 3 `.EDAT` licence stubs, two PS3 disc codes
(`BLES01776`, `BLUS30426`), three PS3 icon sets, a PlayStation Eye camera-check
screen in five languages, and an `X360` component in a build path.

Against the two Capcom ports of the previous two sessions this is the third point
of a line, and it is the first from another studio, another console and another
decade. In 1997 and 1999 a PlayStation and a PC shared no format, so Capcom
converted the media the operating system insisted on and kept the models. In 2013
an Xbox 360 and a PC shared a **vendor** — the console's video codec was Windows
Media, its audio tool had a Windows runtime, its graphics API was a Direct3D 9
derivative — so almost nothing had to be converted, and almost nothing was. The
third-party code this object ships is **514,608 bytes, 0.0075 %**, against 3.7889
% and 5.3744 % on the two discs: sixteen years cut the price of being a PC by a
factor of five hundred, because the operating system now supplies what the disc
used to carry. Accounted end to end, **16.4765 % of this object was made for
Windows and 98.97 % of that is audio and two movies**; the other **83.5160 %**
came off the console project untouched.

Seventy predictions were written before a byte was read, and scored **38 hits, 26
halves, 6 misses = 51.0 of 70**. The briefing they were written against contained
**fourteen** errors, the most of any in this branch, and nine of the fourteen are
the same mistake: a count of a set presented as a reading of it — seven entries
counted without checking whether they were files or directories, seventeen files
counted and fifteen added up, twenty-six sound banks counted and one signature
read, forty-one films counted and one header read. The sharpest of the six
misses is the same error committed by the predictions themselves: one clause
searched `DP.exe` for `Access Games`, found nothing, and declared the studio
absent from its own product. The string in that file is `ACCESS GAMES INC.`, and
across the object the name occurs **79 times in eight files**.

### [Broken Sword: The Sleeping Dragon](https://github.com/vs-sr-dev/pc-brokensword3-doc)

A live GOG installation on a hard disk: **6,748 files, 7 directories,
1,724,710,597 bytes, 6,748 distinct sha1 of 6,748**. It is the fifth live object
in this collection and the first to carry **both** of the files GOG writes — the
Galaxy client's `goggame-galaxyFileList.ini` and the offline installer's
`goggame-1207658708.hashdb` — which is why it can answer a question the two
previous installations could each only half ask.

**Three counters give three numbers and none of them is wrong.** Galaxy's file
list has three sections and **6,897** entries; the installer's database has
**6,736** records; the disk has **6,748** files. Put all three against each
other and the seven regions of three sets come out as 6,736 declared by both and
present, **3** declared by Galaxy alone and present, **158** declared by Galaxy
and absent, **0** declared by the installer alone in either direction, and
**9** present and declared by neither. Read forwards that is a chronology rather
than a disagreement: 6,736 is what the installer had hashed when it stopped,
6,739 is what the client declares when it has finished, 6,748 is the disk after
the uninstaller and the shortcut arrive, and 6,897 is 6,739 plus a DirectX
redistributable folder that was promised and never delivered. The denominator
published is the disk.

**The installer's record has a bug in it and the bug is derivable on paper.**
Yesterday's `hashdb` had a constant 1,056-byte stride; this one does not divide,
and `hashdb.py` refused to print rather than guess. The names here are UTF-16LE
and the stride runs 1066, 1078, 1065, 1066, 1067, 1064, 1090… Against the name
lengths — ten, twenty-two, nine, ten, eleven, eight, thirty-four — the
difference is **1,056 every time**, so `record = 1024 + n + 32`: a 1,024-byte
buffer sized for an eight-bit name, an MD5 written as thirty-two hex characters,
and an overrun of exactly one byte per character because the name went in as
sixteen-bit. The rule predicts that the 6,736 names contain **201,034**
characters between them, and taking the 6,739 the manifest declares, dropping
the three GOG writes last and summing their path lengths gives 201,034 — **delta
zero**, computed from a directory listing before a byte of the object was
opened. Then the digests: **6,736 MD5 of 6,736 match**, 1,721,421,870 bytes
proved intact, the second manifest in this collection that can be checked rather
than only read.

**The engine has a name, a version and a decimal point**, which is a first in
thirty-three objects. Every one of the 6,721 stream files carries the packed
library ID `0x1803FFFF`; the published unpacking gives `0x36003` = **RenderWare
3.6.0.3**, build `0xFFFF`, a released-SDK sentinel. The executable confirms it
from the other side with **110 source paths** reading
`RenderWare/RW36Active/rwsdk/…`, twenty-one of them under `driver/d3d8/`, and
carries two of the engine's own PE sections, `_rwcseg` and `_rwdseg`. The
archive disagrees with itself in a useful way: its 2,975 RenderWare members
carry **four** versions — 3.3.0.2, 3.4.0.5, 3.5.0.0 and 3.6.0.3 — which is what
three years of a licensed engine leaves behind when you re-export what you must
and let the rest alone.

**Forty-seven points of the thesis hung on one word in a table of chunk
identifiers**, and it was settled without decoding a sample. Chunk `0x0000080D`
is in RenderWare's plugin range, and three measurements say what is in it: the
writing tool's console log is shipped inside 76 of the files and one of its
verbs is **Deinterleaving**; the payload's nibble histogram is sign-symmetric
about eight, with 1 against 9 at 10.6 % against 10.1 % and frequency falling
monotonically with magnitude, which is a four-bit ADPCM code and nothing else;
and the branch whose descriptor field reads `0x0204` shows a **byte-equality
peak at lag four** that the branch reading `0x0104` does not — two channels
interleaved on a four-byte grain, exactly as the header predicted. The
entropy told the opposite story and told it wrongly: 5.9504 bits per byte with
**zero** blocks above 7.5 looks like proof that nothing is compressed, and
everything is, four to one.

**The 39 % nobody could read opened, and it moved the thesis by eleven points.**
`data.pak`'s obvious framing — 16-byte records from offset zero — survives
thousands of records and is off by one word: several members are Windows
bitmaps, a bitmap declares its own length, and under the obvious framing that
length matches the *next* record's size field. Shift by four and the file is
`u32 count = 19751`, then 19,751 records of `(zero, key, offset, size)`, then a
zero word, then the members — which **tile the file with zero gaps and zero
overlaps**, the last one ending on the last byte. Inside: 5,744 bitmaps, 1,188
PNG, 2,975 RenderWare chunks, and **732 RIFF/WAVE members, format tag 1,
sixteen bits, 187,408,118 bytes** of uncompressed sound that the arithmetic had
been done without.

So the thesis is **1,228,042,538 of 1,724,710,597 = 71.2028 %** recorded sound
and film, fifth of eleven objects, where without the archive it would have been
seventh. In seconds rather than bytes it is starker: **eight and a half to
eleven and a half hours of recorded sound against nine minutes and seventeen
seconds of film**, a ratio of sixty to one, in a product whose program is
**0.1012 %** and carries no version resource at all.

**And one data build was made for three machines and never stripped.** The
evidence is in the bytes and not in a release date: thirty UTF-16 occurrences of
`PlayStation` inside `data.pak`, all of them the **PlayStation 2 memory-card
dialogue** — *…ory card (8MB) (for PlayStation 2) in MEMORY CARD slot 1…* —
shipped inside the retail Windows product, and a build path ending
`Data\streams\pc`, which is a platform folder in a multi-platform tree.
RenderWare was sold to make exactly that possible, and this is the first object
in the collection where the claim can be made from the file rather than from the
box. **What the bytes do not support is a direction.** `pc` is a *sibling* in
that tree, not a destination, and almost nothing in the object is dated — 6,746
of 6,748 files carry one copy stamp and the stream format has no date field —
so no artefact of one platform can be shown to precede an artefact of another.
The tempting sentence, *the Windows version is a port of the PlayStation 2 one*,
is one step further than the file goes. So is the sector alignment that first
looked like proof: all 6,721 streams are a whole number of 2,048-byte units
because each one's header is exactly one sector, and 2,048 is a CD and DVD
sector on every platform including the one this game shipped on for Windows in
2003.

The leftovers column records its worst figure: **145,169,513 bytes, 8.4170 %**,
of which 118,607,373 are trailing zeros inside the shipped stream payloads — 37 %
of the dialogue branch — with the caveat that a four-bit codec encodes silence as
zero and the boundary between padding and silence is not visible from outside
the decoder. The other rows are 26 MB of attract-mode loop sold to people who
have already bought it, a 0.8-second teaser, and 47,640 bytes of a build tool's
`WARNING` messages that nobody read before shipping.

Seventy predictions were written before a byte was opened and scored **45 hits,
20 halves, 4 misses = 55.0 of 69 = 79.71 %**. All four misses are about the
archive, and all four were made from inside the framing the briefing handed
over — which had asked *where does the table break*, when the answer was that it
never broke, because it had never been framed right.

### [Broken Sword: The Angel of Death](https://github.com/vs-sr-dev/pc-brokensword4-doc)

A live GOG installation on a hard disk: **31 files, 9 directories,
2,668,075,144 bytes, 31 distinct sha1 of 31**. It is the sixth live object in
this collection, the fourth with GOG's manifests, and **the first with a
predecessor already measured in the same branch** — *The Sleeping Dragon*, the
row above, was opened the day before.

**Thirty-one files is not a small object, it is a closed one.** Three of them
are 99.3801 % of the bytes — `bs4.pak` 1,979,623,974, `english.pak` 408,731,612,
`audio.pak` 263,180,854 — and all three begin with the same eight ASCII bytes,
`EmPackFi`, which are documented nowhere. Either they opened or the repository
was a list of thirty-one filenames.

**The record is twelve bytes and its first field is a pointer to itself.**
`u32 name_delta, u32 size, u32 offset`, table at offset 24, names in a blob
after it, every offset a multiple of 256 — 17,978 of 17,978. The trap is the
first field: it points at the member's name **relative to its own record**, and
record 0's value is exactly `12 × count`, which is also the distance from offset
24 to the name blob. So the obvious reading agrees perfectly on record 0 and
drifts twelve bytes per record afterwards, returning plausible filenames — the
tails of the previous entries' paths — for all 17,978 members without ever
failing. It was caught by a closure the wrong reading cannot satisfy: under the
right one the names **tile the blob exactly**, first at `24 + 12·count`, last
ending at `header_end`, no gap and no overlap, on three archives of three.

**And the arithmetic was not believed because it closed.** In each archive
**exactly one** record satisfies `offset + size == filesize`, and the bytes it
names are the bytes the file visibly ends with: in `bs4.pak` **thirty-eight**
bytes of UTF-16LE reading `4096 Hello there`, whose name is
`…\congo1\logic\english\text.txt` — a placeholder in a level that is not in the
game; in `audio.pak` 2,358 bytes of XML ending `<!-- Emmersion Xml file EOF -->`,
named `…_preview.evw`; in `english.pak` a 62,703,068-byte Bink video whose own
size field declares 62,703,060, and 62,703,060 + 8 is 62,703,068. Three
different lengths, three different formats, and the table predicted each one's
tail to the byte and then named what it was. **Header + members + slack = the
file size, delta zero, on three of three.** The whole framing costs 0.0855 % in
256-byte alignment and the largest gap anywhere in 2.65 gigabytes is 255 bytes.

**17,978 members, and none of the three archive names is right.** `audio.pak` is
98.56 % sound but 238 of its members are the audio department's XML project
files; `english.pak` is not text at all — 6,098 numbered MP3 lines, 6,101
lip-sync tracks paired with 6,097 of them, and one 62 MB video; and `bs4.pak`,
the game, carries the text — in **six languages**, 19,161,131 bytes of which are
French, German, Italian, Spanish and Russian, in a build whose `.info` declares
`["en-US"]`.

**The largest thing in the object is not a recording, and that is a first.**
1,987 members are `.epc`, **1,557,790,042 bytes, 58.3863 %**, and they are
compiled 3D scenes: geometry, skinned animation, baked lightmaps, collision.
Every one begins `EMDF` after four or eight zero bytes; the header is 312 bytes;
the string table after it names the **Maya `.mb` scene** the room was modelled in
and every `.tga` and `.bmp` that went into it, on a mapped drive `Z:/BS4Art/`;
and the padding between the strings is not zeros but the repeating ASCII word
`ALIGN`, which is why the object contains that word **30,266 times**.

**At byte 200 of that header there is a date, in ASCII, in the clear.**
`HH MM SS DD MM YYYY`, on **1,967 of 1,987** members, spanning **100 distinct
days over 117, from 2006-04-20 09:24:55 to 2006-08-14 12:07:50**. Two days carry
a third of it — 327 and 261 — which are re-exports rather than work. The hour
histogram peaks at ten in the morning with 503, dips at noon, peaks again at
four, and trails to two in the morning; Thursday is the biggest day with 580 and
the weekend is 9.35 %. **The object contains its own production calendar to the
second, and its filesystem contains nothing at all.** The field is not
consistently zero-padded — 362 members write `08 59 5 23 05 2006`, a `%d` where
the author meant `%02d` — so a fixed-width reader finds 1,605 and loses 362.

**Eleven hours and twenty-two minutes of sound against two minutes and nineteen
seconds of film.** 7,870 MPEG 1 layer III members, every one proved by chaining
**fifty consecutive frame headers** rather than trusting one — the control that
justifies the chain is a UTF-16 byte-order mark, `ff fe`, which satisfies eleven
sync bits and which the chain threw out twenty-eight times in `bs4.pak`, all
twenty-eight of them text. Voice is mono at 160 kbit/s, 6,098 files at one
setting with no exception; music is stereo at 192; effects are three quarters
mono. Thirty-two members are uncompressed 16-bit PCM and `pcmtest.py` confirms
the declaration from the samples, 0.2709 against 1.414 for noise. Eight Bink
videos close `size + 8 == member size` on 8 of 8, and **more than half the film
is a 231×253 screen-capture tutorial with no audio track**. The thesis:
**37.6177 %** of the object is sound and film, against 71.2028 % for the
previous game — because 139 MB of RenderWare geometry became **1.56 GB** of
Emmersion scenes.

**The rule that had held for twelve sessions broke.** `crossall.py` finds four
whole-file crossings and all four are storefront housekeeping. But this is the
first session in which two members of one series are both installed and **both
containers are readable**, so the members could be hashed against each other:
17,977 against 19,751, and **291 distinct digests are identical**. That is 535
members of `bs4.pak`, 18,409,077 bytes — **87.83 % of the game's bitmaps, 99.07 %
of its PNG, 100 % of its 42 animation event maps and 22 `.dnm`** — and **zero of
its 7,909 sound and video members and zero of its 1,987 compiled scenes**. Fire,
smoke, a tyre, a door flap: a studio's shared effects library carried whole from
2003 into 2006. The two absences have two different causes and they are the
sharper half of the result — the sound could not cross because the codec changed,
the geometry could not cross because the engine did; only the engine-independent
formats could, and those are exactly the ones that did.

**`PlayStation` occurs zero times, and there are fifty-three PlayStation 2
textures.** The string tests are worthless and the structure test is not: all 17
`Xbox` hits recur at a 48-byte vertex stride inside compiled meshes and all 123
`Wii` hits are RGB triples in bitmaps — `###===WWWiiikkk` — so not one of the 140
is a console. But the archives keep their build paths, so the question can be
asked of the directory tree instead, and `ps2` is a folder with **53 members and
547,275 bytes**, against `pc` with 8. They are character textures at **128×128
where the `pc` siblings are 256×256**, and two of the fifty-three are
`thumbs.db`, Windows Explorer's thumbnail cache, which is how you can tell
somebody had that folder open. There is no console executable and no console
format: thirty console-only extensions checked against 33 in the object, and ten
console magics checked against the first four bytes of all 17,978 members —
**zero of ten, with a RIFF control firing 32 times**.

The leftovers column comes to **64,557,327 bytes, 2.4197 %**, and none of it is
padding: 579 duplicate members (41 MB, including one lightmap stored **twenty
times**), 19 MB of five unused languages, 1,069,056 bytes of 64-bit code a PE32
program cannot load, a developer level-warp menu of 55 sections with instructions
in its comments and a test bed whose chapter is called `george_goes_mad`, 27
`thumbs.db`, and a zero-byte member named `.nomp3`. Against it, the column that
is not the object's: **159 files the manifest declares and the disk does not
have**, among them the cab that would install the one DLL the game imports and
cannot find, and the runtime the 2017 Direct3D proxy needs.

Sixty-six predictions were written before an archive was opened and scored
**48 hits, 11 halves, 6 misses = 53.5 of 65 = 82.31 %**. The misses are worth
more than the hits: the thesis was predicted at 45–75 % and came out at 37.6, the
`audio.pak` archive was predicted *not* to be predominantly MP3 and is 84.7 %
MP3, `d3dx9_30.dll` was predicted absent everywhere and is on the reading machine
twice — and the crossing clause predicted **zero bytes of game data** would cross
with the previous game, which is exactly the sentence the session's new tool was
written to test, and exactly the sentence it refuted.

### [Broken Sword 5: The Serpent's Curse](https://github.com/vs-sr-dev/pc-brokensword5-doc)

A live GOG installation on a hard disk: **33 files, 2 directories,
6,608,639,638 bytes, 33 distinct sha1 of 33**. It is the largest object this
branch has measured, the seventh live one, and **the third Broken Sword in three
sessions** — one studio, eleven years, three archive formats.

**Seventeen files are 99.8996 % of it and neither of their two formats is
published.** `VT7A`, seven archives and 93.49 %: sixteen-byte header, sixteen-
byte record `(key, offset, size_raw, size_stored)`, every offset a multiple of
4,096. The record's fourth field is the trap. Read as a flag — with the length
always in field 3 — the arithmetic closes on six archives of seven and
**overshoots `graphics_common.vt7a` by 201,604 bytes**, whose field-3 sum is
235.2705 % of the file. Read correctly, field 3 is the *uncompressed* size and
field 4 the *stored* size with zero meaning stored raw, and
`max(offset + extent)` falls inside the file on **seven of seven**. The proof is
not the arithmetic: at every one of 15,776 declared offsets, a member with a
non-zero field 4 begins with a zlib header and a member with a zero field 4 does
not — 15,776 predictions, 15,776 right.

**`AUFS` is eight bytes of header, not sixteen.** The ten `.osa` voice archives
were briefed as `'AUFS'`, `u32 count`, `u32 A`, `u32 B`, with `B = 12 × count +
8` holding on ten files of ten and `A` identical across five languages. There is
no such header: the file is `'AUFS'`, `u32 count`, then twelve-byte records
`(id, offset, size)` from +8. `B` is record zero's offset, which **is** the end
of the table by construction — one tautology, not ten confirmations — and `A` is
record zero's id. What is true, and was not claimed, is that
`offset[i] + size[i] == offset[i+1]` on every adjacent pair and
`offset[last] + size[last] == file size` **exactly, delta 0, on ten of ten**;
that `OggS` sits at all **56,162** declared offsets; and that all 56,162 Ogg page
chains close to the byte, 287,931 pages.

**71,938 members, none unidentified.** 3,991 `STRM` animation streams
(4,481,283,405 bytes, **67.81 %** of the installation, format unpublished,
401,317 declared frames); 3,138 WebP, every one decoded with zero failures;
12 Ogg Skeleton + Theora 1280×720 + Vorbis films running **34:56**; 1,623 Vorbis
music and effects, 5:13; 56,162 Opus voice recordings, **44:22:25** across five
languages; and 6,933 zlib members which are the whole game — 4,648 XML documents
and eight `TEXT` string tables of 15,924 lines each, in **eight** tables for
seven languages, two of them English differing on 257 lines by *colored* against
*coloured*.

**Three quarters of the object is the same artwork twice, and only the pixels
could say so.** `graphics_720.vt7a` and `graphics_1080.vt7a` share **not one key
and 17 members of 9,042**; the smaller file has *more* members than the larger.
They are nevertheless the same pictures: **pixel-area ratio 2.2890 against the
2.2500 of an exact 1.5×**, animation frame counts **200,636 against 200,681**,
and every large scene in the 1080 archive reconstructible as tiles of the 720
one — `2047 + 1023 = 3070 = 2045 × 1.5`, exactly, with a two-pixel bleed. Above
a 2,047-pixel limit a 1080 scene is **cut into columns**, which is why a 1080
member can show *less* of a scene than its 720 counterpart while holding more
pixels. Two of the three controls run on that comparison **fired** and are
published as having fired: a 16×16 fingerprint matched 13.88 % of deliberately
shuffled pairs, and 38 % of each archive's members are near-copies of each other,
so the 84 % match rate is an upper bound and the verdict rests on area instead.

**The thesis is 23.0583 % on the disk and 31.0952 % without the resolution
nobody loads**, against 71.2028 % in 2003 and 37.6177 % in 2006 — and the
program fell the same way, 0.1012 % → 0.1798 % → **0.0333 %**, while the object
nearly quadrupled. The leftovers are **1,758,685,265 bytes = 26.6119 %**, the
worst this column has recorded, and **0.7656 %** without that one file — the best.
`general.vt7a` is separately **82.3 % empty**: 5,012 members averaging 812 bytes,
each rounded up to 4,096, so the whole script and rules of the game occupy four
megabytes and ship in twenty-three. The ten `.osa` archives, by the same studio
in the same build, have **zero** slack.

**A tool said nineteen where the answer was 290.** `deps.py` walked `BS5.exe`'s
64-bit import table four bytes at a time and reported exactly one imported
function from each of nineteen libraries, without erroring — a PE32 thunk reader
pointed at a PE32+ image. Third session running in which a tool stated something
false with confidence. Two of the author's own tools did it too: `oggtime.py`
reported the films at **13:59:59**, wrong by a factor of twenty-four because a
multiplexed Ogg ends on whichever stream finishes last, and it was the *bitrate*
and not the arithmetic that caught it; and `pixels.py` read 4 KiB of each member,
silently decoded 288 of 1,563, and reported a pixel-area ratio of 1.0043 that
would have reversed the session's central conclusion.

Forty-eight predictions were written before a byte was opened and scored
**35 hits, 10 halves, 3 misses = 40.0 of 48 = 83.3 %**. All three misses are a
quantity attached to a correct mechanism: the two graphics archives were
predicted to share **zero** members and share 17; `BS5.exe` was predicted to
import 400–1,200 symbols and imports 290. The clause that mattered stated two
mutually exclusive readings of the `VT7A` record, named which one it expected,
and named the single number that would fail loudly if it had chosen wrong.

### [FINAL FANTASY XI (PC, Steam)](https://github.com/vs-sr-dev/pc-finalfantasy11-doc)

A live Steam installation on a hard disk: **66,192 files, 1,167 directories,
15,150,034,054 bytes, 61,184 distinct sha1 of 66,192**. It is the largest object
this branch has measured by a factor of 2.29, the eighth live one, the first
from Steam, the first MMORPG, and **the first whose product is a running service
— which means half of it is not in the folder and cannot be measured from it.**
Nothing was executed, nothing was registered, and nothing was contacted: this is
an online game whose strings are full of host names, and they are counted as
artefacts and never resolved.

**It is also the exact inverse of the object before it.** That one was 98.44 %
above entropy 7.5 and nothing could be read until a container opened. This one
is **8.2777 %**, almost every file begins with printable ASCII, and the problem
is not opening but drowning: 52,631 files called `<number>.DAT`, in 385
directories called `<number>`, with no name anywhere on the disk, holding
**73.2738 %** of the object at a mean entropy of 6.0058.

**Nine complete indexes over one id space, and they never overlap.** Each `ROM*`
directory carries its own `VTABLE`/`FTABLE` pair — all eighteen files exactly
109,701 and 219,402 bytes, the base pair sitting in the branch root rather than
in `ROM\`, which is how a careless reader finds eight layers and prints a table
that looks like it worked. Read as one byte of volume and one `u16` splitting as
`dir = v >> 7, file = v & 0x7F`, the tables produce an address for every id they
claim, and **every address exists on the disk: 48,044 of 48,044 on the base
layer and all of all on nine.** The arithmetic is not the proof — `FTABLE = 2 ×
VTABLE` would close on random bytes — the existence of the files is.

And then the intersection matrix is **zero everywhere off the diagonal**. Not
one id of 109,701 is claimed twice; each layer's volume table contains exactly
two values, zero and its own number; and the nine could be concatenated into a
single 109,701-byte table without losing a bit. **It is not a stack of
overwrites, it is a partition.** The layering story handed to this session was
right about the intuition and wrong about the mechanism, and the real overlap
is elsewhere: **113 distinct contents present in two layers** for 78,627,600
bytes, of which the largest is 12,175,968 bytes sitting under two different ids
in the 2002 directory and the nominally-last one; and the fact that **`ROM`, the
2002 layer, contains the names of every expansion including *Seekers of Adoulin*
(2013) and *Rhapsodies of Vana'diel* (2015) — and contains them nowhere else.**
Nothing covers anything. Things are simply in two places at once.

Running the same check the other way finds **1,363 files, 397,553,640 bytes,
that no id in any of the nine tables points at**, and 23,343 ids that no layer
claims, in **437 separate runs** — six of them exactly 477 long at a stride of
exactly 512, which is a shape and not erosion.

**The `.DAT` opened, and the proof is a picture.** A chunk is sixteen bytes of
header — four ASCII bytes of tag, then a `u32` packing a 7-bit type, a **21-bit**
length in units of sixteen, and 4 flag bits — followed by its body, laid end to
end and terminated by a tag reading `end\0`. The derivation failed three times
first, and each failure changed the reading rather than the code: a tag rule
demanding four printable bytes rejected the terminator, which occurs **97,301**
times; `(v >> 7) * 16` gives 201,327,088 bytes for a chunk in a 539,776-byte
file; and a 22-bit mask survives that counter-example and dies on a chunk whose
real length is 192. Walking the corrected chain lands on the **exact last byte
of 48,757 of 52,626 files, 92.6481 %**, holding 8,859,947,696 bytes and
2,019,932 chunks with 105,987 distinct tags — and the identical walk over 130
files that are **not** `.DAT` closes on **none of them**.

That is a chain that closes, which is arithmetic. The external fact is that
type-32 chunks turn out to carry a **Win32 `BITMAPINFOHEADER`** — `biSize` 40 on
every one — followed by `3TXD` or `1TXD`, which are `DXT3` and `DXT1` with the
four bytes the other way round, or a small integer meaning an 8-bit palette. The
pixel offset was first derived as `chunk length − payload length`, which gives
96 and produces unmistakable noise; the correct offset, **85**, was found by a
statistic rather than by eye — a real DXT block has `colour0 > colour1` far more
often than not, and offset 85 scores **100.0 % on 2,000 blocks** while every
neighbour scores between 0 and 96. Decoded, one chunk of `ROM\0\1.DAT` is a
**legible ASCII font sheet** and another is 1024×2048 of kanji and kana.
`biHeight` is positive, which in a Windows bitmap means bottom-up, and obeying
it renders the glyph sheet upside down: it is a Win32 structure carrying
Direct3D data and only some of the conventions came along.

**A checksum nobody had read.** All four manifests — `file.txt` and `patch.txt`,
in both branches, **126,899 entries** — carry a 22-character field in a
64-character alphabet containing `@` and `_`. 22 × 6 = 132 = 128 + 4, so if it
is a 128-bit digest the **last character can take only four values**, and that
was tested first, before anything was hashed: positions 0 to 20 carry all 64
characters and position 21 carries exactly **four**. The alphabet was then
recovered from **forty files** with zero conflicts —
`TSG8IncW3HFKokOg79qzeCmZs2yBYEQVAUxR5rbwi4P@jMDLtpvad0f_J1hlN6uX`, whose
indices 0, 16, 32 and 48 are `T`, `7`, `A` and `t`, exactly the four observed
before it was known. **MD5 reproduces 126,865 of 126,865 present fields,
100.0000 %.** SHA-1 is refused before it starts, on width: 160 bits do not fit
in 132. CRC-32 under the identical procedure gives 64 conflicts of 64, and so
does little-endian bit order.

The four manifests **do not agree on line endings** — one CRLF, three LF — which
is not cosmetic: a reader that splits on CRLF returns *one entry* for three of
the four and prints a table that looks correct, and did. And in the PlayOnline
branch the two manifests disagree on exactly one entry of 1,191, which is
**`file.txt` describing itself**: it declares 84,909 bytes and it is 85,167,
because it hashed itself and then kept writing. It is the only self-referential
entry in 126,899 and the only one that is wrong.

**The audio decodes, and a human named it.** `.spw` and `.bgw` say `SeWave` and
`BGMStream` in their own first bytes — 12,041 of 12,041 and 261 of 262 — the
size field matches the file on **12,302 of 12,302**, and the whole container
census costs **787,392 bytes of reading** because nothing about it needs the
body. Two header bytes give the channel count and a codec, and the unit count
times a per-codec constant reproduces every body length exactly: nine bytes per
unit is 4-bit ADPCM at sixteen samples per nine bytes, two is 16-bit linear PCM.
Decoded, the correlation between adjacent samples is **0.9846** — against
**0.0361** for the identical bytes read as the other codec, which is the
measurement. Then `se000007.spw` was played, and the person running the session
recognised it: **the Final Fantasy victory fanfare**, filed under sound
*effects* because in this game it is an event jingle. The 262nd `.bgw` is not a
`BGMStream` at all but a complete uncompressed **48 kHz stereo WAV of exactly
seven minutes**, sitting in `mov\` beside the opening movie whose soundtrack it
is.

**And the pre-briefing's headline does not survive.** It states that `PS2`
occurs 479 times against a chance expectation of **3.53** — the figure for a
*four*-byte string — and concludes 136 times chance. `PS2` is three bytes,
chance over 15,150,034,054 is **903.01**, and 479 is **0.53 of chance**: below
it, in the same band as `Ogg` at 0.54 and `Wii` at 0.52, the two strings the
briefing correctly calls noise. Mapping every occurrence into the structure that
holds it — which is what a count without a location is missing — puts **195
inside `.bgw`, 147 inside `.spw`, 10 inside base64 hash fields in the
manifests**, and shows that the two hits in `FFXiMain.dll` are the low three
bytes of the pointers `0x10325350`, `0x10325358` and `0x10325363`. **`PS2` does
not occur as a token in the game's executable at all.** Where it does occur is
`appEU.dll` and `polcoreEU.dll`, in a NUL-separated table reading
`PS2 · FFXI · W20 · W2U · IXFF` — one string table, in the launcher, and worth
more than 479 coincidences because it can be pointed at. The direction of the
port is argued instead from four structural facts that need no count: a
streaming format with no directory, a three-byte index limited to 128 files per
directory, textures re-encoded to DXT that the PS2 could not sample, and a
Windows bitmap header bolted onto an older shape.

`SedB`, which the briefing calls "probably the music magic", is not one:
all eighteen of its occurrences in audio files sit at **arbitrary offsets inside
the ADPCM payload**, from 1.52 % to 80.34 % of the body, never at a header
offset. `Kraken` at 122 is two million times chance and is a monster.
`Vulkan` occurs four times, in two adjacent `.DAT`, and is not the API.

**The store executes rather than describes.** `installscript.vdf`, 5,514 bytes,
writes 24 registry values across 10 keys, registers a DirectShow media type
whose detection string is literally `0, 4, FFFFFFFF, 504D5553` — `PMUS`, which
is exactly the first four bytes of the two video files, so the registry and the
bytes agree to the byte — and hands **nine DLLs to `regsvr32`**, because this
game is not an executable but a set of in-process COM servers. On the way out it
hands over **ten**, and the tenth is `TetraMaster\TM.dll`: a withdrawn *Final
Fantasy IX* card game that is not on the disk, has never been on the disk, and
whose eleven gamepad-button DWORDs are configured anyway. **Zero bytes and
eleven registry values** is the most complete leftover this branch has measured.

**And the two video files are MPEG under eight bytes of XOR.** They were the
last thing left closed, and the decoder could not help: `polmvfINT.dll`, the
DirectShow filter the installer registers for `PMUS`, is packed — `.text` raw
size **zero**, code in a section called `POL1` at entropy 7.3966. So the
ciphertext was read instead. `mov999.pmv` has a mean block entropy of **4.9864**,
impossibly low for 315 megabytes of video, and its byte histogram says why: the
**eight** commonest values are **8.36 % each**, two thirds of the file in eight
values at equal frequency, which is a repeating eight-byte keystream over a
constant plaintext and nothing else. The per-position histogram hands over
**`C2 EE 9C D9 BD 6C 4D 72`** — the same key from both files, at 89.0 % signal
in one and **4.13 %** in the other, and a four-per-cent signal getting all eight
positions right is the confirmation. Under it, byte four is `00 00 01 B3` in one
file and `00 00 01 BA` in the other: an MPEG **video elementary stream** of
512×336, 29.970 fps, **12,620 pictures = 7 m 01 s** against the 420.42-second
WAV beside it, and an MPEG **program stream** of 640×480 and 11.93 s. The
identical procedure over 49 files that are not `PMUS` produced a start code in
**0** of them, and a human identified both films on sight. **And 75.2800 % of
the 315-megabyte file is zero after the XOR** — 237,745,800 bytes, **1.5693 % of
the whole object** — because a 6 Mbit/s constant-bit-rate envelope is carrying
1.4832 Mbit/s of picture. It is the largest single piece of nothing this branch
has weighed, and it moved the leftovers ceiling from 15.3937 % to **16.9630 %**
after the repository had already been published.

`buildpaths.py` reported **99,881 Macintosh-shaped paths** on a Windows-only
object, every one a manifest line read as `volume:folder:file`. The first repair
anchored at the start of the string and left 69,677, because the Mac rule
matches from the first uppercase letter *inside* the 22-character hash; the
second rejects any candidate whose middle component is nothing but digits and
leaves 1,572. **123,765 false positives across two repairs**, and the
publishable figure for Macintosh paths in this object is zero. The DOS figure is
**274, of which 56 belong to Microsoft**, and the nine surviving sound-path
templates in `FFXiMain.dll` name the developers' tree directly — `ffxi`,
`ffxi_ex`, `ffxi_ex2`, `ffxi_ex3`, `ffxi_ex4`, `ffxi_ex5`, `ffxi_dl`, `ffxi_gf`,
five of them under a directory called `TestUser` — which is why there is no
`sound1`: the first expansion's tree is `ffxi_ex` and not `ffxi_ex1`.

**This is the first object in the collection with a person inside it.** 178
files and 2,421,300 bytes — 0.015982 % — of one player's character state,
macros, client logs, launcher cookies, mail spool and screenshots directory,
counted and characterised and not printed, with the account identifier redacted.
The seventeen person-shaped strings `contacts.py` finds are not compression
noise, because there is no compression: they are `@` bytes inside DXT blocks and
inside a second `.DAT` format called `DMB` that the session identified and did
not derive. **`.DAT` is not one format but at least six** — `SQLE` on 532 files,
`d_ms` on 257, `DMB` on 80, `XIST` on 53, and **130 that are ordinary PNG files
with a `.DAT` extension**.

Fifty-five predictions were written before a byte was opened and scored
**39 hits, 11 halves, 5 misses = 44.5 of 55 = 80.9 %** — and for the first time
in eleven attempts **the distribution was close too**: predicted 38 / 12 / 5,
got 39 / 11 / 5. Every miss is a magnitude attached to a correct mechanism
except two: one clause **inherited the pre-briefing's arithmetic error** on
`PS2` instead of doing a division it could have done in its head, and one
reasoned a `Saga` decision from a cell it had not looked at. The clause that
mattered stated a falsifiable positional signature — *one position of 22 will
carry four characters, and it will be the last* — that cost one pass over four
text files and would have killed two other clauses loudly if it had failed.

Twelve pre-briefing figures did not survive re-derivation, and five of the
author's own errors are recorded beside them, including **breaking the branch's
own backslash rule twice in one session**: the second time a shell heredoc wrote
a form feed and a backspace into a Python source, because `\f` and `\b` are
escape sequences and a heredoc does not know it is quoting a Windows path. All
271 tools were then scanned for control bytes; there are none.

    26.2100 % of the client is recorded sound and film, by extension
    24.5362 % by branch, printed beside it
    and it does not move when the 73 % is opened: SeWave 0, BGMStream 0
    inside 11,101,005,949 bytes of .DAT

    of which the film is 7 m 13 s in two files, and the sound is between
    20 and 31 hours -- a band, because the sample rate is not in the header


### [Simulman V](https://github.com/vs-sr-dev/pc-simulman5-doc)

*Simulman V* (MS-DOS, 1993) — **120 files, 2,056,643 bytes, twelve
directories.** The seventh Italian object in this list, the second from
**Simulmondo** after *1000 Miglia*, and the smallest thing measured here since
the branch left the floppy era: it is **7,367 times smaller than the object
measured the day before it**. That changes the method and not the ambition.
Yesterday the work was choosing what not to measure; here every byte fits in
memory twice over, sixteen of the nineteen extensions were unknown when the
session started, and **all sixteen are derived from the bytes**. What is left
unread is 3.06 % — the small index tables and the numeric body of the room
records — and it is unread because the answers are in 8086 machine code and
this repository has no disassembler, not because nobody looked.

**There is not one compressed or encrypted block in it.** 557 blocks of 4,096
bytes, **zero above entropy 7.5**, against 8.2777 % for the object before it
and 98.44 % for the one before that. This is the far end of that scale, and it
does not mean everything was legible: it means every format was derivable and
there was no excuse.

**58.3509 % of the object is one extension with no magic number.** The 38
`.ANI` are a container — version, element count, declared length, and a `u32`
offset table whose **first entry is the length of the table itself**, so the
first element begins immediately after it. That identity, `offset[0] == 4n`,
holds on the 38 `.ANI`, the 6 `.ELE` and the 5 `.CHV`, and at `2n` on the one
`.TIL`: **fifty files, four formats, one habit.** Element 0 is a six-bit VGA
palette, and `SMAN5/STA/ARCADE.PAL` is one of those elements standing alone in
a file. The pictures are a skip/copy run encoder — a byte of pixels to leave
alone, a byte of pixels to copy, `0xFF` to end the row — and **156 of 156
decode consuming every byte but the last two**. The first run reported *0 of
155*, each leaving exactly two bytes over, never one and never three; the two
bytes are `ff ff` and are the end marker, and recognising them took the count
from zero to all of them without changing another line.

**The sprites are four bits per pixel and they index the top sixteen colours,
not the bottom sixteen.** Which sixteen was measured, not assumed: split the
256-entry palette into aligned blocks and ask which holds a pure white, a
three-step flesh ramp and a three-step blue ramp, and **two blocks qualify**,
12 and 15, being the same colours rotated by one. The tie breaks on the sprites
themselves — **index 15 is drawn zero times in 96,515 pixels and it is the
magenta**, a key colour being the one index a sprite never draws, while index 0
under the other reading is drawn 843 times. Base 240, and the character's
colours therefore do not change when the room does. Nibble order was settled
the same way rather than by eye: a run with an odd pixel count wastes half its
last byte, and over **5,712 odd runs of 5,712** the high nibble is zero, so the
low nibble is written first.

**The five `.MAT` screens are not scanlines.** 64,000 bytes each, which is
320×200 at one byte per pixel, and rendered as rows they are horizontal noise.
The byte that best predicts a byte is the one **sixteen** away, not 320 — mean
absolute difference 1.658 against 5.207 — so they are stored as tiles of
16×10, twenty across and twenty bands down, and reassembled that way they are
rooms with `CLOAK ROOM` and `PRIVATE` legible in them. **No byte in 320,000
exceeds 15**, so 160,000 bytes carry four bits of nothing each; and the usual
excuse, that mode 13h demands a byte per pixel, does not survive here, because
this object contains its own four-bit packer and uses it on 162 sprites, ten
tiles and a mouse pointer before storing its five biggest pictures unpacked.

**The dialogue is XOR'd with a key stored in the file's own first byte.** The
ten `.KEY` are the highest-entropy data here and looked like nothing. 2,304
candidate transforms were tried — XOR, add and subtract at all 256 keys, then
the same three after bit reversal, nibble swap, complement and seven rotations
— and scored on printable fraction: **96 cleared 85 % and 95 of them were
nonsense**, because 0xCB and 0xCC differ in one low bit and printability cannot
tell them apart. Scored again on Italian function words, exactly one reading
survives, and the key is byte 0. Six files begin `0xCB` and four begin `0xDA`.
The text writes **`_` for space 2,158 times against 3 real spaces**, because
the font's first glyph is `0x21` and there is no glyph for a space — and its
last glyph is `0x97`, which is **CP437's `ù`, the last letter the Italian
language asks for**. There are 110 accented vowels in 16,498 bytes of dialogue,
where *1000 Miglia* a year earlier has **none in 1,588,227 bytes** and writes
`e'` throughout.

**The reference graph closes in both directions and has two levels.** The
fifteen `.PLA` scripts are a stream of **big-endian** 16-bit tokens — 88.4737 %
of them below 0x0100 — in an object whose every other multi-byte field is
little-endian, with NUL-terminated string operands padded to even length. Five
tokens introduce a filename and the map from token to extension is one-to-one
in both directions over all fifteen scripts. **Every one of the 369 paths they
name resolves to a file that exists: zero dangling references**, which an
installed directory usually cannot manage. Adding the second namer — the
Pascal executables' own length-prefixed filename strings — leaves **38 files
that nothing in the object names at all**, and the list is the finding: the
eleven episode scripts themselves are among them, because they are called
`AN00` through `AN0B` and the program builds the name from a **hexadecimal
counter**. An episode is not a string in this object; it is an integer. Also on
that list: **two music tracks nothing plays**, `ST1.MDI` and `ST2.MDI`, which
are the two longest sequences here at 234.5 and 208.7 seconds — seven and a
half minutes, a third of all the music in the game, that no script reaches.

**Twenty-two minutes of music that never chooses an instrument.** Nine Standard
MIDI files, format 0, one track, division **420** — not 96, 120, 192, 384 or
480, and 420 divides by three, five and seven. 13,825 notes, and **zero
program-change events**: the sequences say which note and never which sound.
The timbres are the **12,345 bytes** appended past the declared load image of
`NEWMIDIL.EXE`, which the DOS loader never reads and the program fetches
itself. All nine also declare an `MTrk` length **four bytes short of their own
End-of-Track event**, so a conforming reader refuses them — they have been
unplayable for thirty-three years and nobody noticed, because the only program
that ever read them did not care. Raising one 32-bit field by four makes all
nine play, and they come out on Acoustic Grand Piano on every channel, which is
what the zero program changes predicted.

**And nineteen bytes reboot the computer.** `RESETTA.COM` writes `0000` and
`FFFF` into the four bytes immediately past its own last instruction and jumps
through them: `FFFF:0000` is the processor's reset vector. Its name is an
imperative in Italian, nothing in the object calls it, and there is no `.BAT`
here to call it from. It is a development tool that shipped — the same habit
as *1000 Miglia*'s five Turbo Pascal utilities that nothing calls — and it is
the most compressed statement of what this object is: somebody's working
folder, copied whole onto a Christmas Eve in 1996, with the game and the tools
and the release note from the people who pirated it all sitting in the same
directory.

**`TNC.NFO` is not the product** and is quarantined like the six such files in
*1000 Miglia*, inside the denominator rather than subtracted from it. It is
also the only place in the object that states a date correctly in text, it
declares `Cracked by: N/A` — which an eleven-scheme scan over the four
executables independently confirms — and its author writes that he cannot tell
whether the game is *"italian or spanish (don't know exactly, nor I care too
much)"*. The bytes settle it in one line. Its nine pseudonyms are counted and
not printed; the two engineers who signed `PLAYER.EXE` and the name on the
title card are printed, on the stated criterion that **a name placed by its own
owner inside a product they sold to the public is published, and a pseudonym
placed by a third party inside a document that is not the product is not**.

**The thesis is 0.0000 %**, the second zero in that table and the first
measured with the object fully open rather than blind. There is no `.WAV`,
`.VOC`, `.SND`, `.SMP` or `.CMF`; no PCM inside the executables or the
animations; the music is sequence and the pictures are cel animation with
transparency at 38 different sizes, which is not what a film frame looks like.
`PLAYER.EXE` reserves two sample buffers on its command line and the game ships
nothing to put in them. The alternative figure is published beside it —
`.ANI` + `.MAT` + `.MDI` + `.ELE` = **83.3007 %** of the object is picture and
music — which is higher than any row in the thesis table and every byte of it
is drawn or sequenced. A 1993 newsstand game spends five sixths of itself on
art and sound without recording a single second of anything.
