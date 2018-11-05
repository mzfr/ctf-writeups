# hertz

__PROBLEM__

 Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with nc 2018shell1.picoctf.com 43324.

__HINT__

NOTE: Flag is not in the usual flag format

__SOLUTION__

We connect to the given port and we are greeted by:
```
-------------------------------------------------------------------------------
xerzoyvs cfof ds gewo qhyz - swjsvdvwvder_xdmcfos_yof_sehiyjhf_blfvvqfsir
-------------------------------------------------------------------------------
xyhh bf dscbyfh. sebf gfyos yze-rfifo bdra cel herz mofxdsfhg-cyidrz hdvvhf eo re berfg dr bg mwosf, yra revcdrz myovdxwhyo ve drvfofsv bf er sceof, d vcewzcv d lewha sydh yjewv y hdvvhf yra sff vcf lyvfog myov eq vcf leoha. dv ds y lyg d cyif eq aodidrz eqq vcf smhffr yra ofzwhyvdrz vcf xdoxwhyvder. lcfrfifo d qdra bgsfhq zoeldrz zodb yjewv vcf bewvc; lcfrfifo dv ds y aybm, aodtthg reifbjfo dr bg sewh; lcfrfifo d qdra bgsfhq driehwrvyodhg mywsdrz jfqeof xeqqdr lyofcewsfs, yra jodrzdrz wm vcf ofyo eq fifog qwrfoyh d bffv; yra fsmfxdyhhg lcfrfifo bg cgmes zfv swxc yr wmmfo cyra eq bf, vcyv dv ofnwdofs y svoerz beoyh modrxdmhf ve mofifrv bf qoeb afhdjfoyvfhg svfmmdrz drve vcf svoffv, yra bfvceadxyhhg krexkdrz mfemhf's cyvs eqq-vcfr, d yxxewrv dv cdzc vdbf ve zfv ve sfy ys seer ys d xyr. vcds ds bg swjsvdvwvf qeo mdsveh yra jyhh. ldvc y mcdhesemcdxyh qhewodsc xyve vcoels cdbsfhq wmer cds sleoa; d nwdfvhg vykf ve vcf scdm. vcfof ds revcdrz swomodsdrz dr vcds. dq vcfg jwv krfl dv, yhbesv yhh bfr dr vcfdo afzoff, sebf vdbf eo evcfo, xcfodsc ifog rfyohg vcf sybf qffhdrzs velyoas vcf exfyr ldvc bf.

vcfof rel ds gewo drswhyo xdvg eq vcf byrcyvvefs, jfhvfa oewra jg lcyoifs ys dradyr dshfs jg xeoyh offqs-xebbfoxf swooewras dv ldvc cfo swoq. odzcv yra hfqv, vcf svoffvs vykf gew lyvfolyoa. dvs fuvofbf aelrvelr ds vcf jyvvfog, lcfof vcyv rejhf behf ds lyscfa jg lyifs, yra xeehfa jg jofftfs, lcdxc y qfl cewos mofidews lfof ewv eq sdzcv eq hyra. heek yv vcf xoelas eq lyvfo-zytfos vcfof.

xdoxwbybjwhyvf vcf xdvg eq y aofybg syjjyvc yqvforeer. ze qoeb xeohfyos ceek ve xefrvdfs shdm, yra qoeb vcfrxf, jg lcdvfcyhh, reovclyoa. lcyv ae gew sff?-mesvfa hdkf sdhfrv sfrvdrfhs yhh yoewra vcf velr, svyra vcewsyras wmer vcewsyras eq beovyh bfr qdufa dr exfyr ofifodfs. sebf hfyrdrz yzydrsv vcf smdhfs; sebf sfyvfa wmer vcf mdfo-cfyas; sebf heekdrz eifo vcf jwhlyoks eq scdms qoeb xcdry; sebf cdzc yheqv dr vcf odzzdrz, ys dq svodidrz ve zfv y svdhh jfvvfo sfylyoa mffm. jwv vcfsf yof yhh hyrasbfr; eq lffk aygs mfrv wm dr hyvc yra mhysvfo-vdfa ve xewrvfos, rydhfa ve jfrxcfs, xhdrxcfa ve afsks. cel vcfr ds vcds? yof vcf zoffr qdfhas zerf? lcyv ae vcfg cfof?

jwv heek! cfof xebf beof xoelas, myxdrz svoydzcv qeo vcf lyvfo, yra sffbdrzhg jewra qeo y adif. svoyrzf! revcdrz ldhh xervfrv vcfb jwv vcf fuvofbfsv hdbdv eq vcf hyra; hedvfodrz wrafo vcf scyag hff eq gerafo lyofcewsfs ldhh rev swqqdxf. re. vcfg bwsv zfv pwsv ys rdzc vcf lyvfo ys vcfg messdjhg xyr ldvcewv qyhhdrz dr. yra vcfof vcfg svyra-bdhfs eq vcfb-hfyzwfs. drhyrafos yhh, vcfg xebf qoeb hyrfs yra yhhfgs, svoffvs yra yifrwfs-reovc, fysv, sewvc, yra lfsv. gfv cfof vcfg yhh wrdvf. vfhh bf, aefs vcf byzrfvdx idovwf eq vcf rffahfs eq vcf xebmyssfs eq yhh vcesf scdms yvvoyxv vcfb vcdvcfo
```

As the questions says `made a bunch of substitutions` so meaning its a substituion cipher

Using [this](https://www.guballa.de/substitution-solver) we break the cipher and get plaintext
```
-------------------------------------------------------------------------------
congrats here is your flag - substitution_ciphers_are_solvable_mwettfesvn
-------------------------------------------------------------------------------
call me ishmael. some years ago-never mind how long precisely-having little or no money in my purse, and nothing particular to interest me on shore, i thought i would sail about a little and see the watery part of the world. it is a way i have of driving off the spleen and regulating the circulation. whenever i find myself growing grim about the mouth; whenever it is a damp, drizzly november in my soul; whenever i find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral i meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off-then, i account it high time to get to sea as soon as i can. this is my substitute for pistol and ball. with a philosophical flourish cato throws himself upon his sword; i quietly take to the ship. there is nothing surprising in this. if they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.

there now is your insular city of the manhattoes, belted round by wharves as indian isles by coral reefs-commerce surrounds it with her surf. right and left, the streets take you waterward. its extreme downtown is the battery, where that noble mole is washed by waves, and cooled by breezes, which a few hours previous were out of sight of land. look at the crowds of water-gazers there.

circumambulate the city of a dreamy sabbath afternoon. go from corlears hook to coenties slip, and from thence, by whitehall, northward. what do you see?-posted like silent sentinels all around the town, stand thousands upon thousands of mortal men fixed in ocean reveries. some leaning against the spiles; some seated upon the pier-heads; some looking over the bulwarks of ships from china; some high aloft in the rigging, as if striving to get a still better seaward peep. but these are all landsmen; of week days pent up in lath and plaster-tied to counters, nailed to benches, clinched to desks. how then is this? are the green fields gone? what do they here?

but look! here come more crowds, pacing straight for the water, and seemingly bound for a dive. strange! nothing will content them but the extremest limit of the land; loitering under the shady lee of yonder warehouses will not suffice. no. they must get just as nigh the water as they possibly can without falling in. and there they stand-miles of them-leagues. inlanders all, they come from lanes and alleys, streets and avenues-north, east, south, and west. yet here they all unite. tell me, does the magnetic virtue of the needles of the compasses of all those ships attract them thither
```

FLAG - `picoCTF{substitution_ciphers_are_solvable_mwettfesvn}`
