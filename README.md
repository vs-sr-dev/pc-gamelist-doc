# pc-gamelist-doc

**Index of the PC and portable-C game documentation** — 25 titles, one
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

The newest entry is the first that **is not a game**, and it is in the list on
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
| [**Harry Potter and the Philosopher's Stone**](https://github.com/vs-sr-dev/pc-harrypotter1-doc) | 2001 | KnowWonder / Electronic Arts *(the game's own credits name no studio, only "PC Team"; `KnowWonder` appears once in 540 files, as a Windows domain inside a developer's path, and on the printed case)* |  | The first object here measured from the disc itself rather than a copy. A **table hidden in the primary volume descriptor**, in 344 bytes ISO 9660 requires to be zero, naming six boundaries of the disc including both edges of a 9,280-sector unreadable region — whose near border **a binary search cannot find**, because the drive reads 64 sectors at a time. 249 Unreal Engine 1 packages in seven format versions, 91 music files with no tracker module in them, and 31 levels in a single line recovered twice from two independent sources |

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
