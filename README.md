# pc-gamelist-doc

**Index of the PC and portable-C game documentation** — 35 titles, one
repository each. This family has no shared platform checklist: a DOS game from
1987 and a PhyreEngine remaster from 2018 have almost nothing in common except
the machine they end up on, which is exactly why the index is per platform and
not per engine.

Two strands run through it. The first is format archaeology from the DOS and
early-Windows era — containers, sprite codecs, map formats and the editor work
files that shipped by accident.
The second is modern remasters and PC ports, where the interesting layer is the
older console the build is still pretending to be. No repository here contains
game assets or executables — only measurements and the code to reproduce them.

## The titles

Listed in the order they were documented. The **Saga** column is filled in where
the title belongs to a series that may one day earn its own index; it is empty
where it does not. Three of them — Final Fantasy twice, and Mana — already point
at a Square Enix cluster that is one title away from deserving its own repo.
**HeroQuest** is one of three sagas of two here, and its other half is on a
different machine entirely: *HeroQuest II: Legacy of Sorasil* sits in the CD32 list as
[cd32-heroquest2-doc](https://github.com/vs-sr-dev/cd32-heroquest2-doc). Two
titles across two families is not yet an index of its own.
**Baron Baldric** is the second saga of two, and the mirror image of that
arrangement: both halves are on this machine and in this list, *Baron Baldric:
A Grave Adventure* and its sequel *Mystic Towers*. Its Saga cell was empty
until the sequel arrived, because a saga of one is not a saga; two titles in
one family is a column entry and still not an index of its own. What the two
have in common turns out to be a protagonist, a Borland runtime and three
asset files — different studio, different publisher, different engine, and a
different machine underneath.

One entry is the only one that **is not a game**, and it is in the list on
purpose. *Viaggio al centro del Mondo* is the data session of an 883 CD Extra:
put the disc in a stereo and it plays an album, put it in a computer and it
opens a Macromedia Director program with a slot machine inside it. The slot
machine is 2.7 % of the data track and the rest is a hypertext menu, nineteen
QuickTime movies and an installer for a 3D avatar chat world. An index that
admits its edge cases is more useful than one that hides them, and the What-it-is
cell says plainly that this is not a game — because leaving it out would lose
the fact that an Italian record label shipped an Activeworlds client in every
copy of an album in 1999.

The newest pair of *games* in the list is the first to share an **engine**, and
its Saga cells are deliberately **empty**. *Blood & Lace* and *Zero Comico* are both
GMM Entertainment, both running `japotek3d.dll`, seven months apart — and
they have no characters, setting or fiction in common, which is what the Saga
column is for. The Studio column already carries the link that exists. What
the two discs say about each other is a great deal, and it is said in prose,
in [pc-bloodandlace-doc chapter
11](https://github.com/vs-sr-dev/pc-bloodandlace-doc/blob/master/docs/11-two-discs-one-engine-seven-months.md),
which is the first side-by-side comparison in this family: the engine *lost*
237,568 bytes of code between them, and three claims in the older repository
are corrected by the newer one.

**Three counts, and they do not all agree, on purpose.** Re-derived by command
rather than incremented: the heading says **34 titles**, the table has **35
rows**, and the write-ups section has **34 entries**. The extra row is *Tales of
Berseria*, which has a row and no write-up because its primary index is
[tales-gamelist-doc](https://github.com/vs-sr-dev/tales-gamelist-doc) — the
format it documents belongs to the saga, not to the platform. The heading
counts documents, the table counts titles reachable from here, and the gap is
one crosslink. Raising the heading to 34 would claim a write-up that does not
exist here; dropping the row would hide a title that is on this platform.

**Mega Man** is the third saga of two, and it is the one that shows what the
Saga column is actually for. Its cell was deliberately empty when *Mega Man*
(PC/DOS, 1990) was the only entry, with the reason written out: *Mega Man* is an
enormous series, this is a licensed title written from scratch for the PC with
Robot Masters and stages the NES game does not have, and **the column is filled
only when another object in this collection shares bytes with it**. A saga of
one is not a saga and a licence is not a saga either.

The newest entry is that other object. *Mega Man 3: The Robots are Revolting*
(PC/DOS, 1992) is the same studio, the same programmer and the same platform
twenty-one months later, and the two programs share **1,855 bytes** in runs of
32 or more — 98 of them the options display list, 32 of them both palette
tables, the rest EGA blitter code — measured with the threshold named before the
comparison was run. So both cells are filled now, on that measurement and on
nothing else. **There is still no PC *Mega Man 2*:** the first DOS game is
called *Mega Man* and the second is called *Mega Man 3*.

*Grande Fratello Il Gioco* makes it three Italian discs in the list and is
**not** a third member of that pair: different studio, different city, two
years later, and — measured file by file by content hash — **not one byte in
common** with either of them. The only thing all three share is somebody
else's: `fmod.dll`, in two different versions. Three discs from one country
are not a national school, and the comparison chapter says so; what it does
say is that the differences are almost all differences of *year* rather than
of place, and that the third disc, by arriving with its subchannel, was able
to correct the other two rather than merely be compared with them.

*Lucignolo Il Videogioco* is the fourth Italian disc and the first that could
be set against a genuine like-for-like — two tie-ins to Mediaset television
programmes, four years apart. It closes the question rather than extending
it: **not one file on it is byte-identical to any file on the other three,
and the set of filenames common to all four is empty.** `fmod.dll`, the one
thing the first three shared, does not survive; this game uses Audiere. Four
discs and three studios are no more a national school than three were, and
the useful result is the negative one: the only crossing anywhere in the four
is between the two discs that share a studio.

*Tesla Effect: A Tex Murphy Adventure* is the newest entry and the largest object
in this family by four orders of magnitude — 17.5 gigabytes against the 392,593
bytes measured before it. **Its Saga cell is empty, and the reason is the rule
and not an oversight.** It is the sixth and last *Tex Murphy*, a series of six
that began in 1989; the column is famous-title-proof and fills only when another
object in this collection shares bytes with it, and today there is no other *Tex
Murphy* here. The one thing this object contains that points at its own series is
a video file called `meanstreets_newspaperarticle.bk2`, naming the 1989 game the
series began with — and **a reference is not a shared byte.** When the rest of
the series is measured, the cell fills itself, on a measurement, exactly as
*Mega Man*'s did after a session of standing empty.

It is also the first entry here whose subject is a **live installation on
somebody's disk** rather than a disc, an image or a folder of files, and the
first with personal data in it. Two fields of its Steam manifest belong to the
person who owns the copy and are redacted in the repository; the game's own
runtime log, written on that machine, is neither copied nor quoted. The
distinction the document draws is worth carrying: a name found *in the object* —
`masonj`, `courtneyj`, `steve w` — is a measurement, and a name belonging to the
person who installed it is not.

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
| [**Blood & Lace**](https://github.com/vs-sr-dev/pc-bloodandlace-doc) | 2001 | GMM Entertainment |  | The game that engine was built for, seven months earlier: a signed licence notice from its author inside `japotek3d.dll`, 237,568 bytes of code the later disc no longer has, and a combat system the comedy could not use |
| [**Grande Fratello Il Gioco**](https://github.com/vs-sr-dev/pc-grandefratello-doc) | 2003 | Trecision |  | The official Big Brother tie-in, and the first disc here dumped with its subchannel: 43 wrong bits in 12 MB of Q prove the read, the 155-sector tail three discs share turns out to be 150 of Red Book, and 2,934 files come out of one cabinet |
| [**Lucignolo Il Videogioco**](https://github.com/vs-sr-dev/pc-lucignolo-doc) | 2007–08 | 7Th Sense s.r.l. |  | An eight-file DVD of which one file is 96.79 %: the copy protection is a six-byte file containing the word `codice`, every file's sector padding is a verbatim echo of the data 65,536 bytes earlier, and the engine names itself in a log the developers shipped by accident |
| [**Viaggio al centro del Mondo** (883 CD Extra)](https://github.com/vs-sr-dev/pc-883d-doc) | 1999 | Moltimedia |  | **Not a game** — the multimedia session of a music CD Extra, holding a slot-machine minigame that is 2.7 % of the data track and an installer for **883D**, an Activeworlds chat world whose object-path server survived in a cache directory name: `http://vrml.moltimedia.it/aw` |
| [**1000 Miglia**](https://github.com/vs-sr-dev/pc-1000miglia-doc) | 1991–92 | Simulmondo *(attributed externally; the material names no studio)* | | The Brescia–Rome–Brescia road race, whose sixteen route files are named for the city at each end and whose sixteen filenames are therefore a graph — one closed circuit through fifteen towns with Bologna visited twice. **What survives is not the product**: it is one installation, made on 9 November 1992, of a March 1992 bulletin-board distribution, and 37.93 % of it is PowerPacker with the bits in an order the standard depacker cannot read |
| [**Harry Potter and the Philosopher's Stone**](https://github.com/vs-sr-dev/pc-harrypotter1-doc) | 2001 | KnowWonder / Electronic Arts *(the game's own credits name no studio, only "PC Team"; `KnowWonder` appears once in 540 files, as a Windows domain inside a developer's path, and on the printed case)* | Harry Potter | The first object here measured from the disc itself rather than a copy. A **table hidden in the primary volume descriptor**, in 344 bytes ISO 9660 requires to be zero, naming six boundaries of the disc including both edges of a 9,280-sector unreadable region — whose near border **a binary search cannot find**, because the drive reads 64 sectors at a time. 249 Unreal Engine 1 packages in seven format versions, 91 music files with no tracker module in them, and 31 levels in a single line recovered twice from two independent sources |
| [**Harry Potter and the Goblet of Fire**](https://github.com/vs-sr-dev/pc-harrypotter4-doc) | 2005 | Electronic Arts *(publisher; the disc names no development studio at all — it names RenderWare, RealCore 6.27.01, RealGraph 6 and Havok, and one Perforce path, `d:\P4\Eauk\HPGoF\`)* | Harry Potter | A DVD that is **93.98 % one file**, and whose 126 unallocated gaps are not gaps: 79 of them are exactly 20 sectors, one every twenty files, and they hold a complete **second filesystem** — UDF File Entries, one per file, agreeing with ISO 9660 on all 1,659 of them. Six sources disagree by one sector about how long the disc is, and the sector in dispute is **UDF's closing anchor**: unreachable through Windows, read with a SCSI `READ(10)`. SafeDisc 4.50.000, whose version is written a second time as two integers in a descriptor field ISO 9660 requires to be zero |
| [**Harry Potter and the Order of the Phoenix**](https://github.com/vs-sr-dev/pc-harrypotter5-doc) | 2007 | Electronic Arts *(publisher; the disc names no development studio as a company, but `hp.exe`'s Authenticode certificate reads `O=Electronic Arts, OU=UK Studio, L=Guildford, ST=Surrey, C=GB` and eleven source paths sit under `z:\phoenix\code`)* | Harry Potter | A **pressed** DVD whose image was assembled with a desktop ISO editor — `UltraISO V8.5`, signed 1,222 times where the 2005 disc said `GEAR` 1,717 times — and whose ISO 9660 primary namespace is **not ISO 9660**: zero `;1` version suffixes, 1,185 lower-case names, 67 with spaces, which is exactly why it carries no Joliet. A lead-out reported **674,807 sectors before the end of the disc**, proved to be a one-byte MSF field saturating. SecuROM instead of SafeDisc, with **no version string anywhere in 10,329,160 bytes** and four PE sections named `ars` / `est` / `artem` / `celare`. And the eight-disc run of zero shared files **ends**: 500 files here are byte-identical to files on the 2005 disc |
| [**Age of Wonders II: The Wizard's Throne**](https://github.com/vs-sr-dev/pc-ageofwonders2-doc) | 2002 | Triumph Studios *(the disc names it in `AoW2.~ex`'s version resource and four times in a plaintext credits block; the publisher, Gathering of Developers, holds the copyright in the English readme)* |  | The first disc here whose **unallocated space is the subject**: 23.91 % of it belongs to no file, and 143,595,520 bytes of that are reproduced from two integers. A volume descriptor that writes down the disc's own first and last unreadable sector. A Delphi 5 game, and two files shared with a 2001 disc from a different publisher |
| [**Il cane di terracotta**](https://github.com/vs-sr-dev/pc-canediterracotta-doc) | 2000 | IM*MEDIA (software), Sellerio (publisher) |  | **Not a game** — an interactive cartoon from Camilleri's novel, and the first hybrid in this list: Windows mounts 2,374 files in 4 folders, the HFS volume on the same sectors holds 2,401 in 11, and 2,372 of the 2,373 they share begin on the **same sector**. Macromedia Director 7.0.2, a 10,240-byte grid whose padding has a closed form at 100.0000 %, and 517 Macintosh audio files each leaking the same Windows 95 `KERNEL32.DLL` return address |
| [**CLIC 11**](https://github.com/vs-sr-dev/pc-clic11-doc) | 1997 | CLIC *(the magazine; the disc names its own maker in the volume identifier `CLIC_11` and in no other field — `publisher`, `data preparer` and `copyright file` are empty on both descriptors, and `Clic95.exe`'s `CompanyName` reads `Macromedia, Inc.`, which is the engine's vendor and not the disc's)* |  | **Not a game, and not a work** — the CD bound into an Italian magazine, and the first object here with no author and no centre: eleven separately-assembled bodies of software spanning **1,636 days**, of which the magazine itself made **3.37 %**. A hybrid whose file count is a property of the walker — Windows shows 857, the ISO volume holds **875** records because eighteen carry the ECMA-119 **Associated-File** flag and describe Macintosh resource forks, and the HFS catalogue adds 23 files that exist nowhere else: **26,607,777 bytes no Windows machine can read**. An ownership map over all 322,926 sectors leaves **two** belonging to nobody. **99.11 % of the directory records have an even seconds field** — MS-DOS's two-second grid, on a disc mastered by a Macintosh program — and the eight exceptions are three Mac files with resource forks. The eight-disc run of zero shared files ends properly: 21,870 records compared, **two crossings, both Microsoft redistributables** |
| [**Tubular Worlds**](https://github.com/vs-sr-dev/pc-tubularworlds-doc) | 1993–94 *(the file mtimes, 1993-10-11 to 1994-05-31; there is no descriptor here to separate the date of the product from the date of this copy, and the last file is a player's high score)* | *(none — the object names **nineteen people** in `PART2.EXE`'s credits and no organisation anywhere; the only copyright string in 3,432,758 bytes is Clarion Software's, and it belongs to the compiler of an 8 KB DOS version check)* |  | **The first object in this list that is not a medium** — not a disc, not an image, but a downloaded folder of 107 files, and therefore the first with **no volume descriptor, no lead-out and no field anywhere that says when it was made or where it ends**. What a folder can prove instead was proved: **106 of its 107 files are reachable from `TUBWORLD.BAT`** and the 107th is `TUBWORLD.BAT`, so nothing is missing and nothing is spare; and **107 of 107 timestamps sit on the MS-DOS two-second grid** with a zero sub-second field, which is the fingerprint of a DOS-era archive restored onto NTFS. The whole game is drawn from a **64-byte 8×8 tile**, recovered from arithmetic — seven of fifteen banks are exact multiples of 64 once a 768-byte VGA palette comes off the end, and the tile indices across all 21 maps form the dense range **0..2639 with every gap equal to 1** — and rendering it turns two unnamed files into **GET READY** and **GAME OVER**. `size = w·h·k + 4` holds on **35 of 37** level grids; the two that break are level 3, in both files, with the same bytes — and the header is **right**: the autocorrelation of the payload peaks at 169 and is at chance at 200, so the file is 1,488 cells too long rather than the header being wrong. The loading screens are **IFF ILBM written by Deluxe Paint** (`DPPS`, `CRNG`, `TINY`) with a six-bit VGA palette in an eight-bit chunk, decoding to exactly 153,600 bytes each. And a **58-byte German QWERTZ scancode table** is compiled into both game programs, forced by two positions and not one: `Z` at scancode 0x15 and `Y` at 0x2C. **85.447 % of the bytes are structured, 74.383 % decoded, 0.263 % leftover**, and zero of 23,631 records cross with anything else in this collection |
| [**Mega Man**](https://github.com/vs-sr-dev/pc-megaman-doc) | 1990 *(28 of the 29 files carry mtimes from 1990-09-30 to 1990-11-29 and the executable is the last of them; the 29th is a BBS descriptor written 2011-01-22. As with the other loose-file object in this list there is no descriptor, no version field and nothing to separate the date of the product from the date of this copy — except that here the executable's own filename table names every data file the folder holds)* | *(none as a company — the object credits a **person**: `CREDITS.STA`, rendered, gives **design, graphics, programming and sound to Stephen Rozner** and the concept to **Capcom**, and `LOGO.STA` carries `© 1990 CAPCOM CO.,LTD.` — all of it drawn as pixels, none of it as text. The publisher, **Hi-Tech Expressions, Inc.**, is named by exactly one file, the `file_id.diz` added in 2011, and by nothing in the 28 files of 1990)* | Mega Man | **Not the NES game and not a conversion of one** — a licensed DOS original, and the second folder of loose files in this list. 29 files, 346,995 bytes, five undocumented formats and an EXEPACK'd executable, and every one of them closes: `MM.EXE` unpacks to **exactly 211,712 bytes with zero packed input left over**, of which **91.8 % is zero** and 17,415 is program — so the famous *twenty kilobytes for a whole game* is a fact about a linker's BSS, and the real answer is that **71 % of this game's code is not in its executable** but in five per-stage 8086 modules that far-return to it, whose 2,318 CS-relative references land inside their own files **2,318 times**. One run-length coder serves all four compressed families and it is **PackBits with `0x80` meaning a run of 129 rather than a no-op** — decode it Apple's way and the stage maps come out short and still look plausible. Two planar layouts, not one: backgrounds are four EGA planes interleaved **per row**, sprites five planes interleaved **per byte** with the **mask first**, and reading the mask last gives 305 sprites of the right shape in the wrong colours. `.SCN` closes as `13 + width·height` on 5 of 5; `.BLK` as 41,984 = 328 × 128-byte 16×16 tiles on 5 of 5, of which a map can address only **0..215**; `.FRM` as 305 chained per-frame records ending exactly on EOF on 8 of 8; `.STA` as 30,720 = **320 × 192** on 4 of 4. The 234 bytes shared by all five `.BIN` are **13 × 18** — the hit boxes of the thirteen sprite frames the five `.FRM` also share. The blitter's row pitch is **42 bytes** and the buffers it asks DOS for are 34,944 = (42 × 4) × 208: a **336 × 208 page for a 320 × 192 screen**, sixteen pixels of scroll margin, derived twice from two unrelated numbers. The game has **no text**: twenty-two string literals in the whole executable, no copyright, no build path, **no compiler banner at all**, and the only attribution anywhere had to be *rendered*. And the copy protection is not a password system — it is a manual lookup whose **twelve answers** sit in the executable in a private alphabet that is the glyph's own frame index minus thirteen, the first of them `BATVIRE` |
| [**Mega Man 3: The Robots are Revolting**](https://github.com/vs-sr-dev/pc-megaman3-doc) | 1992 *(64 of the 64 files carry DOS mtimes from 1992-07-18 to 1992-08-02, and this is the first object in this list whose year is also **drawn into it**: `LOGO.STA`, rendered, carries `© 1992 CAPCOM CO.,LTD.` and `™ and © 1992 CAPCOM, USA, INC.`. The container disagrees and says **2008-06-23**, which is the date of the archiving and of nothing else — one ZIP record in 65)* | **Rozner Labs**, and for once the object says so — but in pixels, not in text: `ROZLABS.STA` renders as a circuit board reading `A` / `ROZNER` / `LABS` (spelled on four seven-segment displays) / `PRODUCTION`, `HITECHLO.STA` renders as the **Hi Tech Expressions** logo over the word `PRESENTS`, and `CREDITS.STA` gives **design, programming and sound to Stephen Rozner** and **graphics to William Rozner**, with the concept to **Capcom**. None of those six words exists as ASCII anywhere in the 55,456 bytes of unpacked executable | Mega Man | **The second Mega Man on PC is called the third, because there was never a second** — and it is the first object in this collection with a sibling already measured to the byte, which is what makes it worth a row rather than a footnote. 64 files, 392,593 bytes, inside a ZIP whose 65 CRC-32s all verify and whose 65 local headers agree with their central-directory twins in every field. **One codec for all four families and it is not the 1990 codec**: twelve-bit LZW, MSB first, no clear code, dictionary frozen at 0xFFE — confirmed twice, by 63 of 63 files ending on the 0xFFF end code with only their byte padding left over, and by the decompressor itself at 0xb280 in the unpacked image. Run the 1990 PackBits reader on a 1992 screen and it **consumes 2,926 bytes of a 2,866-byte file**, which is the loudest way a wrong codec can fail. **The pixel changed too**: one byte per pixel, chunky, sixteen colours — against 1990's four EGA planes — so every byte of art is converted to planes once per tile at load time by a routine the `Graphics Card:` setting switches, and the menu that selects it has **dropped the VGA option** the 1990 game offered. `.STA` closes as 64,000 = **320 × 200** on 6 of 6; `.ZSC` as `width·height + 6 + 16·count` with the count read from inside the same stream, on 7 of 7; `.ZBL` as 256 tiles × 256 + 256 records × 32 + four 256-byte tables = 74,752, which is not arithmetic but the loader's own three read constants; `.VFR` as 326 chained frame records ending exactly on EOF on 43 of 43. **The `.BIN` family is gone**: the 1990 game shipped 71 % of its code in five per-stage 8086 modules and this one has none, because a stage is now data — 366 sixteen-byte object records in the `.ZSC` files, and a four-word hit box on each of 326 frames. The executable's filename table names **49 files in full and 7 as padded stems, which is all 63 data files, with no name unfulfilled and no file unnamed** — the closest thing a folder has to a volume descriptor, closing exactly. And **the two games share 1,855 bytes**, in runs of 32 or more, including 98 bytes of the options display list and the 32 bytes of both palette tables: the Saga cell in this row and in the row above it is filled on that measurement and on nothing else |
| [**Tesla Effect: A Tex Murphy Adventure**](https://github.com/vs-sr-dev/pc-teslaeffect-doc) | 2014 *(and the first object in this list whose **filesystem dates nothing**: Steam rewrote all 4,769 mtimes into one six-minute window on the day this copy was downloaded, so the year comes only from inside file contents — the five script workbooks were created 2013-11-20T17:42:33Z and last saved between 2014-04-14 and 2014-05-09, and the studio's own code carries a linker stamp of **2014-06-11T21:55:36Z**. The `.exe` is stamped 2014-01-08 and dates the **engine**, not the game)* | **`BigFinishGames`**, and the object says so in exactly two places, neither of them a credit: as Unity's `companyName` in `mainData`, and inside `/Documents/BigFinishGames/TeslaEffect/` in the assembly — **the only place in 17.5 GB where the studio names itself in text is the path your saved games go to**. `TeslaEffect.exe`'s version resource has no `CompanyName`, no `ProductName` and no copyright; `Assembly-CSharp.dll` has every field present and every one **empty**; and the only binary here that names its maker is **RAD Game Tools**, in the video codec. The credits are `MainCredits.bk2`, 271.1 seconds, and a document that counts bytes cannot read them |  | **Fourteen and a half gigabytes of video with a program around it** — 4,769 files, **17,519,466,565 bytes**, agreed to the byte by `du -sb`, by 4,769 `stat` calls and by the distributor's own `SizeOnDisk`; the first object here with an **external, dated, versioned volume descriptor** (`buildid 297944`, depot manifest `6231652133838335837`) and the first with personal data in it, two fields redacted. **82.93 % of the bytes are film**: 1,035 Bink 2 files, all 1,035 headers parsing, all 1,035 declared lengths matching `stat`, **all 1,035 at 2048 × 1024** — a power-of-two texture, not a picture — 1,028 at 23.976 fps, all 1,035 with exactly one audio track, and **20,014.286 seconds = 5 h 33 m 34.3 s of running time summed from 1,035 exact frame counts with zero frames decoded**. **4,570 distinct SHA-1s for 4,769 files**: 1,330,831,607 bytes — 7.596 % — already exist elsewhere, 99.994 % of it video, because the story graph is stored as a directory tree and a scene reachable from six branches is written six times while its subtitle file is written once. The script is **five Excel 2003 workbooks** shipped with their `DocumentProperties` intact — `Author James`, `LastAuthor masonj` and `courtneyj`, all five **created in the same second**, English and Spanish saved in the same second, and **the English one printed on 2014-04-24 at 20:59:23 UTC**, the only record of paper in the object. The 1992 sibling's name-table closure closed exactly, 56 names for 63 files; **this one fails both ways** — 294 of 3,262 requested string IDs have no English text, at least 3,250 of 6,535 English keys are named by nothing visible — because the join is `GetSubtitleDataFilePath`, a function that concatenates a directory, a stem and an extension, and nothing in the build ever checked it. English has the **fewest** keys of the five languages, not the most: the 1,223-row gap is 1,404 blank rows where its section headings were cleared, and the translators kept and translated theirs, instruction rows included. A `???` left in a retail English line was patched four different ways — Italian **invented a name**; a writer's note reading *XXX (Deep, lonely, noir-esque voice-over goes here. Once we finish writing it of course.) XXX* shipped **translated into German and French**. **101 drive-lettered build paths** in the executable from five vendors and **none** from the studio, against **zero of any kind** in the 1992 object; `Assembly-CSharp.dll` has zero. That assembly is **0.0090 % of the object** and 59 of its 882 types came from elsewhere — Unity's *Stealth* tutorial, a bought FPS kit, iTween — while of its 5,002 string literals only **65** are a line of script and **319** are *keys*: the code contains the names of text, not text. Seventeen files named `- Copy`, six of them older versions; four files a conforming XML parser rejects; four editor GUIDs duplicated by one folder copy; `browscap.ini`, a 311,984-byte web-browser table, as the largest non-video leftover. **16.86 % — 2,954,047,069 bytes of Unity serialized data — was not opened**, stated in its own chapter, and the one probe into it found 48,821,155 more duplicated bytes that a per-file hash census structurally cannot see. **Fifty-six predictions plus two named inferences scored at 81.6 %**, method 17.5 of 18 — and the largest miss, the running time by 50 %, came from trusting a sample of five files out of 1,035 |
| [**Lands of Lore: The Throne of Chaos**](https://github.com/vs-sr-dev/pc-landsoflore-doc) | 1993/94 *(and the messiest this column has been, because the object carries **four dates and three of them are not the product's**. The game is 1993; this is the **CD revision**, and the disc names its own version in the one field built for it — `volume_id` = `LOL_V102`. Its 209 directory records date 1992-06-11 to 1994-08-16 — 1 file from 1992, 51 from 1993, 157 from 1994 — and the `DATA` directory record, which dates the mastering rather than the content, says **1994-10-14**. The ISO primary volume descriptor says **2011-09-13T11:39:37**, seventeen years late, and it is the only descriptor in this list with a field designed to date a product and a wrong value in it. Two storefront icons say 2017 and a web cache says 2019. And 62 of the 65 filesystem mtimes say the day this copy was installed, inside a **ten-second window**)* | **Westwood Studios**, and for the first time in this collection the object states its maker **in a field built for the purpose**: `publisher_id` of the volume descriptor reads `WESTWOOD STUDIOS`, with `preparer_id` naming the mastering software, `EASY-CD PRO INCAT SYSTEMS INC.`. It repeats it in `SETUP.EXE` (`Westwood Studios -- Lands of Lore`) and 38 times in `INSTALL.EXE` — and **zero times in `MAIN.EXE`**, the game itself. The only third-party copyright anywhere in the game layer is `Copyright (C) 1991,1992 Miles Design, Inc.`, in six `.ADV` sound drivers: as in 2014, the vendor whose name survives inside a shipped binary is the audio middleware. The credits are a member of an archive inside a disc image, and they name a different product coordinator in German than in English and French |  | **A CD-ROM inside a file, an emulator that has never heard of it, and a shop wrapper around both** — and the first object in this list that is openly the work of **three groups of people twenty years apart**, so every figure names its layer: the game 33 files / 310,242,796 B / **95.24 %**, DOSBox 14 / 5,883,321 / 1.81 %, GOG 18 / 9,632,811 / 2.96 %, summing to 325,758,928 exactly. **94.17 % of the object is one file and that file is a disc**: `GAME.DAT` is an ISO 9660 image, 149,781 sectors, two descriptors, no Joliet, no El Torito and **no HFS — the first object here where that absence is measured** rather than inferred, the 32,768-byte system area holding one distinct byte value and it is zero. The **sector map closes exactly** — 149,753 file + 8 directory + 2 path table + 16 system + 2 descriptors = 149,781, **zero unowned and zero doubly-owned**, where the CLIC 11 disc left two of 322,926 — with zero gaps between extents and 211,233 bytes of inter-file padding, all of it zero. The disc's head was edited in 2011 and **the timezone byte is the map of what was touched**: 224 of 226 directory records carry GMT offset 0 and the two that say 2011 carry 8, and the root directory's 34-byte record exists **four times in the image with three different dates and one refusal** — `1970-01-01T01:00:00` in the descriptor (a tool formatting a zero it had no value for), `2011-09-13T11:39:37` twice in the root's own extent 104 bytes apart from a 1994 record, and all seven date bytes zero in `DATA`'s parent entry. **77.815 % of the object is a recorded human performance**: 5,508 Creative Voice Files, **8-bit unsigned PCM, mono, uncompressed** at 22,222.22 Hz — not 22,050, because the rate is a one-byte time constant and the format cannot express it — **3 h 12 m 11.50 s**, summed from declared block headers with zero samples decoded and then confirmed by decoding all 5,508 to PCM with a largest disagreement of **0.000000000 s**. Of those, 4,912 are lines of dialogue in thirty `.TLK` files: **median 1.907 s, longest 6.566 s, not one over seven seconds**, and addressed by bare coordinate — line `001A0` in archive `22` is the member `001A0.22` — so that **not one word appears in 4,912 names**. **A `.TLK` is a `.PAK`**: 132 `.PAK` and 30 `.TLK`, **162 of 162 close to the byte**, 7,209 members, every name 8.3 and upper case and none holding a path separator — and the archive terminator is **nine bytes, not five**, all 132 disagreeing with the five-byte reading by exactly four zero bytes. Format80 and Format40 were implemented from scratch: **265 of 265 `.CPS` decompress to exactly the 64,000 bytes they declare and 529 of 529 `.WSA` offset tables land on the end of their file**, both verified by extracting and looking at the pictures; 236 of 236 `.SHP` containers close in two variants told apart by a closure test, and **2,191 of 7,299 sprite frames come out**, which is where this document stops and says so. The game is here **three times** — installed loose, as files inside the image, and inside `WESTWOOD.001`, a fourth container format whose 22 records close to the byte and whose text table of contents names the paths on Westwood's own build machine (`\projects\lol_cd\project\run\voc.pak`), the only source tree on the disc and something the inherited path scanner did not see. **28.670 % of the CD is content the CD already carries elsewhere**, and 128,461,128 bytes across all 7,504 leaves of the object — where the inherited file-level `dupes.py` sees **64,230**, wrong by a factor of 2,000, which is the question `pc-teslaeffect-doc` left open and this object closes. Of 32 loose Westwood files **31 are inside the image and one is not**: `LANDS.CFG`, **ten bytes**, the only part of the game layer this installation produced. A translation costs **142,617 bytes — 0.739 %** of the language trees, 368 of 377 archive members being byte-identical in English, French and German, and 133,011 of those bytes are repainted pictures rather than text. `MAIN.EXE` and `MAINW.EXE` differ by 4,272 bytes and **69.18 % of one is byte-identical to the other**, neither compressed and neither a Windows binary; the oldest byte on the disc, 1992-06-11, is **not Westwood's** but a Borland C++ 1991 progress-bar control. **Absolute paths in the shipped executables: 0 in 1990, 0 in 1992, 0 here, 0 in `DOSBox.exe`, 101 in 2014.** GOG's `goggame-*.hashdb` — a ZIP holding 35 records of 1,056 bytes, 1,024 of name and 32 of MD5 — is **the first descriptor in this collection that can be wrong**, and all 35 verify; what it covers is the finding, being the 33 files of the game plus the manual and the icon, and **not the emulator, not the installer and not itself**. Leftovers are **502,100 bytes, 0.1541 %**, and **99.96 % of them belong to the two groups who did not make the game** — Westwood's whole share is a **187-byte text-editor session** left in the French directory in December 1993, naming a batch file on a drive `R:`. **Sixty-one predictions plus three named inferences, 77.3 %**, method 88.9 % and content 75.5 %, and seven of the thirteen misses are the same error: assuming that things which resemble each other were made the same way. The **Saga** cell is empty on purpose: *Lands of Lore* is a trilogy, but **there is no other Westwood Studios object in this collection**, and this index fills that cell only when a second object **shares measured bytes** with the first — the rule that filled it for the two *Mega Man* rows on 1,855 bytes and on nothing else. It will fill itself when a second Westwood arrives, and it will fill on bytes rather than on a series name |

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
