# pc-gamelist-doc

**Index of the PC and portable-C game documentation** — 21 titles, one
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
**HeroQuest** is a saga of two, and its other half is on a different machine
entirely: *HeroQuest II: Legacy of Sorasil* sits in the CD32 list as
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

The newest pair in the list is the first to share an **engine**, and its Saga
cells are deliberately **empty**. *Blood & Lace* and *Zero Comico* are both
GMM Entertainment, both running `japotek3d.dll`, seven months apart — and
they have no characters, setting or fiction in common, which is what the Saga
column is for. The Studio column already carries the link that exists. What
the two discs say about each other is a great deal, and it is said in prose,
in [pc-bloodandlace-doc chapter
11](https://github.com/vs-sr-dev/pc-bloodandlace-doc/blob/master/docs/11-two-discs-one-engine-seven-months.md),
which is the first side-by-side comparison in this family: the engine *lost*
237,568 bytes of code between them, and three claims in the older repository
are corrected by the newer one.

*Grande Fratello Il Gioco* makes it three Italian discs in the list and is
**not** a third member of that pair: different studio, different city, two
years later, and — measured file by file by content hash — **not one byte in
common** with either of them. The only thing all three share is somebody
else's: `fmod.dll`, in two different versions. Three discs from one country
are not a national school, and the comparison chapter says so; what it does
say is that the differences are almost all differences of *year* rather than
of place, and that the third disc, by arriving with its subchannel, was able
to correct the other two rather than merely be compared with them.

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
