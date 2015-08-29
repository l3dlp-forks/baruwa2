# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# Baruwa - Web 2.0 MailScanner front-end.
# Copyright (C) 2010-2015  Andrew Colin Kissa <andrew@topdog.za.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""Free mail domain"""

FREE_DOMAINS = [
    '020.co.uk', '123.com',
    '123india.com', '123mail.cl',
    '123qwe.co.uk', '138mail.com',
    '150mail.com', '150ml.com',
    '1963chevrolet.com', '1963pontiac.com',
    '1st-website.com', '1stpd.net',
    '20after4.com', '21cn.com',
    '24horas.com', '271soundview.com',
    '2mydns.com', '2net.us',
    '3ammagazine.com', '3email.com',
    '444.net', '4email.com',
    '4newyork.com', '50mail.com',
    '5fm.za.com', '6210.hu',
    '702mail.co.za', '7110.hu',
    '8m.com', '8m.net',
    '8u8.com', '8u8.hk',
    '9.cn', 'a-topmail.at',
    'abv.bg', 'acceso.or.cr',
    'accessgcc.com', 'accountant.com',
    'activist.com', 'adexec.com',
    'adinet.com.uy', 'adres.nl',
    'aeiou.pt', 'aeneasmail.com',
    'afrik.com', 'afropoets.com',
    'ahaa.dk', 'aichi.com',
    'airpost.net', 'aiutamici.com',
    'aknet.kg', 'alabama.usa.com',
    'alavatotal.com', 'albafind.com',
    'alburaq.net', 'aldeax.com',
    'alex4all.com', 'alexandria.cc',
    'alice.it', 'alinto.com',
    'allmail.net', 'alskens.dk',
    'altbox.org', 'alternativagratis.com',
    'alumni.com', 'alumnidirector.com',
    'alvilag.hu', 'amenworld.com',
    'americamail.com', 'amnetsal.com',
    'ananzi.co.za', 'anet.ne.jp',
    'angelfire.com', 'angelic.com',
    'aniverse.com', 'anjungcafe.com',
    'antedoonsub.com', 'antwerpen.com',
    'anytimenow.com', 'aol.*',
    'aon.at', 'apexmail.com',
    'approvers.net', 'aprava.com',
    'archaeologist.com', 'arcor.de',
    'argentina.com', 'arizona.usa.com',
    'armmail.com', 'army.com',
    'aroma.com', 'arrl.net',
    'aruba.it', 'asheville.com',
    'asia-mail.com', 'asia.com',
    'assala.com', 'assamesemail.com',
    'atheist.com', 'atl.lv',
    'atlas.sk', 'atozasia.com',
    'att.net', '*.att.ne.jp',
    'aubenin.com', 'aus-city.com',
    'australiamail.com', 'avasmail.com.mv',
    'ayna.com', 'azet.sk',
    'badgers.com', 'bakpaka.com',
    'balochistan.org', 'baluch.com',
    'bancora.net', 'bankersmail.com',
    'barlick.net', 'bartender.net',
    'beehive.org', 'been-there.com',
    'beirut.com', 'belizehome.com',
    'belizeweb.com', 'bellsouth.net',
    'berlin.de', 'bestmail.us',
    'bgnmail.com', 'bharatmail.com',
    'bigboss.cz', 'bigfoot.com',
    'bigmailbox.com', 'bigmir.net',
    'bikerider.com', 'bip.net',
    'bitwiser.com', 'biz.by',
    'black-sea.ro', 'blackburnmail.com',
    'blink182.net', 'blue.devils.com',
    'bluemail.ch', 'blumail.org',
    'boardermail.com', 'bol.com.br',
    'bollywood2000.com', 'bollywoodz.com',
    'bombka.dyn.pl', 'bonbon.net',
    'bootmail.com', 'bostonoffice.com',
    'boxbg.com', 'boxemail.com',
    'brasilia.net', 'bravanese.com',
    'brazilmail.com.br', 'breathe.com',
    'brew-master.com', 'brfree.com.br',
    'btcc.org', 'buffaloes.com',
    'bulldogs.com', 'bumerang.ro',
    'butch-femme.net', 'buzy.com',
    'c-box.cz', 'c3.hu',
    'cadinfo.net', 'calcfacil.com.br',
    'california.usa.com', 'californiamail.com',
    'camaroclubsweden.com', 'canada-11.com',
    'canal21.com', 'canoemail.com',
    'cardblvd.com', 'care-mail.com',
    'caress.com', 'carioca.net',
    'casino.com', 'casinomail.com',
    'catalunyamail.com', 'cataz.com',
    'catholic.org', 'caths.co.uk',
    'caxess.net', 'cbrmail.com',
    'cemelli.com', 'centoper.it',
    'centrum.cz', 'centrum.sk',
    'cgac.es', 'chaiyo.com',
    'chance2mail.com', 'channelonetv.com',
    'checkitmail.at', 'cheerful.com',
    'chelny.com', 'chemist.com',
    'chil-e.com', 'chillimail.com',
    'chinamail.com', 'christianmail.org',
    'cine.com', 'ciphercom.net',
    'cititrustbank1.cjb.net', 'citromail.hu',
    'ciudad.com.ar', 'claramail.com',
    'clerk.com', 'cliffhanger.com',
    'close2you.net', 'cluemail.com',
    'collector.org', 'collegeclub.com',
    'colorado.usa.com', 'columnist.com',
    'comfortable.com', 'comic.com',
    'compuserve.com', 'computer.net',
    'computhouse.com', 'conevyt.org.mx',
    'connecticut.usa.com', 'consultant.com',
    'coolgoose.com', 'coolkiwi.com',
    'coolmail.com', 'coolmail.net',
    'cooltoad.com', 'cooperation.net',
    'copticmail.com', 'corporateattorneys.com',
    'correios.net.br', 'correomagico.com',
    'cosmosurf.net', 'cougars.com',
    'count.com', 'countrybass.com',
    'criticalpath.net', 'critterpost.com',
    'crosswinds.net', 'cryingmail.com',
    'csucsposta.hu', 'cumbriamail.com',
    'custmail.com', 'cutey.com',
    'cwazy.net', 'cww.de',
    'cyberaccess.com.pk', 'cyberdude.com',
    'cybergirls.dk', 'cyberguys.dk',
    'cymail.net', 'dabsol.net',
    'dadanet.it', 'dailypioneer.com',
    'damuc.org.br', 'dansegulvet.com',
    'data54.com', 'davegracey.com',
    'dbmail.com', 'dbzmail.com',
    'dcsi.net', 'deacons.com',
    'deal-maker.com', 'dearriba.com',
    'delajaonline.org', 'delaware.usa.com',
    'delhimail.com', 'deliveryman.com',
    'desertonline.com', 'desidrivers.com',
    'despammed.com', 'detik.com',
    'dexara.net', 'dhmail.net',
    'didamail.com', 'digitaltrue.com',
    'direccion.com', 'director-general.com',
    'discardmail.com', 'disciples.com',
    'disinfo.net', 'disposable.com',
    'dmailman.com', 'dnsmadeeasy.com',
    'doctor.com', 'dodgeit.com',
    'dogmail.co.uk', 'doityourself.com',
    'domainmanager.com', 'doneasy.com',
    'doramail.com', 'dores.com',
    'dot5hosting.com', 'dotcom.fr',
    'dott.it', 'doubt.com',
    'dr.com', 'dragoncon.net',
    'dropzone.com', 'dserver.org',
    'dublin.com', 'dublin.ie',
    'dutchmail.com', 'dynamitemail.com',
    'e-apollo.lv', 'e-hkma.com',
    'e-mail.ph', 'e-mailanywhere.com',
    'e-tapaal.com', 'e-webtec.com',
    'earthling.net', 'eastmail.com',
    'easy-pages.com', 'easy.com',
    'easypeasy.com', 'echina.com',
    'ecplaza.net', 'eircom.net',
    'educacao.te.pt', 'edumail.co.za',
    'ego.co.th', 'ekolay.net',
    'elitemail.org', 'elsitio.com',
    'elvis.com', 'elvisfan.com',
    'email.com.br', 'email.cz',
    'email.it', 'email.lu',
    'email.nu', 'email.ro',
    'email2me.com', 'emailacc.com',
    'emailaddresses.com', 'emailchoice.com',
    'emailengine.net', 'emailengine.org',
    'emailgroups.net', 'emailhut.net',
    'emailplanet.com', 'emailplus.org',
    'ematic.com', 'embroideryforums.com',
    'emoka.ro', 'emptymail.com',
    'enelpunto.net', 'engineer.com',
    'englandmail.com', 'enterate.com.ar',
    'entusiastisk.com', 'enusmail.com',
    'epix.net', 'epomail.com',
    'eprompter.com', 'eqqu.com',
    'eresmas.com', 'eriga.lv',
    'esde-s.org', 'esfera.cl',
    'etllao.com', 'euromail.net',
    'europemail.com', 'euroseek.com',
    'evafan.com', 'everyday.com.kh',
    'everyone.net', 'excite.*',
    'execs.com', 'execs2k.com',
    'expn.com', 'ezilon.com',
    'f-m.fm', 'facilmail.com',
    'fadrasha.org', 'faithhighway.com',
    'familymailbox.com', 'familyroll.com',
    'fan.com', 'fan.net',
    'fast-email.com', 'fast-mail.org',
    'fastemail.us', 'fastemailer.com',
    'fastest.cc', 'fastimap.com',
    'fastmail.co*.*', 'fastmailbox.net',
    'fastwebmail.it', 'fawz.net',
    'federalcontractors.com', 'fedxmail.com',
    'female.ru', 'fepg.net',
    'fiberia.com', 'filipinolinks.com',
    'financier.com', 'findmail.com',
    'fiscal.net', 'flashmail.com',
    'florida.usa.com', 'floridagators.com',
    'fmailbox.com', 'fmgirl.com',
    'fnmail.com', 'footballer.com',
    'forsythmissouri.org', 'fortuncity.com',
    'free.com.pe', 'free.fr',
    'freeaccess.nl', 'freegates.be',
    'freehosting.nl', 'freei.co.th',
    'freemail.*', 'freemail.*.*',
    'freemuslim.net', 'freenet.de',
    'freeola.net', 'freepgs.com',
    'freeserve.co.uk', 'freeservers.com',
    'freesurf.ch', 'freesurf.fr',
    'freeuk.com', 'freeuk.net',
    'freewebemail.com', 'freeyellow.com',
    'fsmail.net', 'fsnet.co.uk',
    'fuelie.org', 'fun-greetings-jokes.com',
    'fusemail.com', 'fut.es',
    'galmail.co.za', 'gamebox.net',
    'gardener.com', 'gawab.com',
    'gaymailbox.com', 'gaza.net',
    'gci.net', 'gdi.net',
    'gemari.or.id', 'genxemail.com',
    'geopia.com', 'georgia.usa.com',
    'ggaweb.ch', 'giga4u.de',
    'glay.org', 'glendale.net',
    'globalpinoy.com', 'globalsite.com.br',
    'globetrotter.net', 'gmail.com',
    'go-bama.com', 'go-cavs.com',
    'go-dawgs.com', 'go-gators.com',
    'go-irish.com', 'go-spartans.com',
    'go.aggies.com', 'go.air-force.com',
    'go.big-orange.com', 'go.blue.devils.com',
    'go.bulldogs.com', 'go.com',
    'go.dores.com', 'go.gamecocks.com',
    'go.longhorns.com', 'go.mustangs.com',
    'go.ro', 'go.ru',
    'go.wildcats.com', 'go.wolverines.com',
    'go2net.com', 'go4.it',
    'golfemail.com', 'goliadtexas.com',
    'gonowmail.com', 'gonuts4free.com',
    'goplay.com', 'gorontalo.net',
    'gotomy.com', 'govzone.com',
    'graduate.org', 'graffiti.net',
    'gratisweb.com', 'gtechnics.com',
    'guessmail.com', 'gwalla.com',
    'haberx.com', 'hailmail.net',
    'halejob.com', 'hamptonroads.com',
    'happemail.com', 'happycounsel.com',
    'hawaii.usa.com', 'hayahaya.tg',
    'heesun.net', 'heremail.com',
    'highveldmail.co.za', 'hilarious.com',
    'hingis.org', 'hispavista.com',
    'hockeyghiaccio.com', 'hockeymail.com',
    'home.no.net', 'home.ro',
    'homelocator.com', 'homemail.co.za',
    'homestead.com', 'homosexual.net',
    'hong-kong-1.com', 'hopthu.com',
    'hot-shot.com', 'hot.ee',
    'hotbox.ru', 'hotcoolmail.com',
    'hotfire.net', 'hotinbox.com',
    'hotmail.co*.*', 'hotpop.com',
    'hour.com', 'housemail.com',
    'huhmail.com', 'humanoid.net',
    'hurra.de', 'hush.ai',
    'hushmail.com', 'huskies.com',
    'i-france.com', 'i-p.com',
    'i2828.com', 'ibatam.com',
    'ibizdns.com', 'icafe.com',
    'icestorm.com', 'icq.com',
    'icrazy.com', 'id.ru',
    'idirect.com', 'idncafe.com',
    'iespalomeras.net', 'iespana.es',
    'ig.com.br', 'ignazio.it',
    'ilse.net', 'ilse.nl',
    'imailbox.com', 'imap-mail.com',
    'imapmail.org', 'imel.org',
    'iname.com', 'inbox.com',
    'inbox.lv', 'inbox.net',
    'incamail.com', 'indexa.fr',
    'indiamail.com', 'indiana.usa.com',
    'induquimica.org', 'inet.com.ua',
    'infoapex.com', 'infohq.com',
    'infomart.or.jp', 'infosat.net',
    'inicia.es', 'inmail.sk',
    'innocent.com', 'inorbit.com',
    'instruction.com', 'instructor.net',
    'intelnet.net.gt', 'intelnett.com',
    'interfree.it', 'interia.pl',
    'intermail.hu', 'internet-e-mail.com',
    'internet.lu', 'internetegypt.com',
    'internetmailing.net', 'inwind.it',
    'iobox.fi', 'iol.it',
    'iowa.usa.com', 'ip3.com',
    'iqemail.com', 'iquebec.com',
    'irangate.net', 'irelandmail.com',
    'islandmama.com', 'ismart.net',
    'isonfire.com', 'isp9.net',
    'israelmail.com', 'italymail.com',
    'itloox.com', 'itmom.com',
    'iwan-fals.com', 'iwon.com',
    'japan.com', 'jaydemail.com',
    'jetemail.net', 'jingjo.net',
    'jmail.co.za', 'jojomail.com',
    'jovem.te.pt', 'joymail.com',
    'jubiipost.dk', 'jumpy.it',
    'justemail.net', 'justmailz.com',
    'kaazoo.com', 'kabissa.org',
    'kalluritimes.com', 'kalpoint.com',
    'katamail.com', 'kataweb.it',
    'keko.com.ar', 'kentucky.usa.com',
    'keromail.com', 'kittymail.com',
    'klik.it', 'klikni.cz',
    'koko.com', 'kolozsvar.ro',
    'koreamail.com', 'koreanmail.com',
    'krunis.com', 'kukamail.com',
    'kyokodate.com', 'kyokofukada.net',
    'lagoon.nc', 'lahaonline.com',
    'lancsmail.com', 'land.ru',
    'latinmail.com', 'lawyer.com',
    'lawyerzone.com', 'lebanonatlas.com',
    'legislator.com', 'leonardo.it',
    'letsjam.com', 'letterbox.org',
    'levele.com', 'lexpress.net',
    'liberomail.com', 'libertysurf.net',
    'lightwines.org', 'linkmaster.com',
    'linuxmail.org', 'lionsfan.com.au',
    'livedoor.com', 'llandudno.com',
    'lmxmail.sk', 'lobbyist.com',
    'loggain.nu', 'lolnetwork.net',
    'longhorns.com', 'look.com',
    'looksmart.com', 'looksmart.com.au',
    'lotonazo.com', 'louisiana.usa.com',
    'loveable.com', 'lovemail.com',
    'lpemail.com', 'luckymail.com',
    'lusoweb.pt', 'luukku.com',
    'lycos.co*.*', 'lycosmail.com',
    'machinecandy.com', 'macmail.com',
    'madcrazy.com', 'madonnafan.com',
    'madrid.com', 'magicmail.co.za',
    'mail-atlas.net', 'mail-awu.de',
    'mail-center.com', 'mail-central.com',
    'mail-online.dk', 'mail-page.com',
    'mail.austria.com', 'mail.az',
    'mail.be', 'mail.bg',
    'mail.co.za', 'mail.com',
    'mail.ee', 'mail.goo.ne.jp',
    'mail.lawguru.com', 'mail.md',
    'mail.org', 'mail.pf',
    'mail.ru', 'mail.yahoo.co.jp',
    'mail2*.com', 'mail3000.com',
    'mail8.com', 'mailandftp.com',
    'mailas.com', 'mailasia.com',
    'mailblocks.com', 'mailbolt.com',
    'mailbox.co.za', 'mailbox.gr',
    'mailbox.sk', 'mailc.net',
    'mailcircuit.com', 'mailclub.fr',
    'maildozy.com', 'mailfly.com',
    'mailftp.com', 'mailglobal.net',
    'mailinator.com', 'mailingaddress.org',
    'mailisent.com', 'mailite.com',
    'mailmight.com', 'mailmij.nl',
    'mailops.com', 'mailpanda.com',
    'mailroom.com', 'mailru.com',
    'mailsent.net', 'mailserver.dk',
    'mailsnare.net', 'mailsurf.com',
    'mailvault.com', 'mailworks.org',
    'majorana.martina-franca.ta.it', 'maktoob.com',
    'malayalapathram.com', 'male.ru',
    'manlymail.net', 'mantrafreenet.com',
    'mantraonline.com', 'marchmail.com',
    'marijuana.nl', 'marketweighton.com',
    'masrawy.com', 'massachusetts.usa.com',
    'mbox.com.au', 'mcrmail.com',
    'medicinatv.com', 'meetingmall.com',
    'merseymail.com', 'mesra.net',
    'metacrawler.com', 'mexico.com',
    'miaoweb.net', 'michigan.usa.com',
    'miesto.sk', 'mighty.co.za',
    'milmail.com', 'mindless.com',
    'minister.com', 'minnesota.usa.com',
    'missouri.usa.com', 'mixmail.com',
    'ml2clan.com', 'mlanime.com',
    'mmail.com', 'mobimail.mn',
    'mobstop.com', 'modemnet.net',
    'moldova.com', 'moldovacc.com',
    'montana.usa.com', 'montevideo.com.uy',
    'moose-mail.com', 'mosaicfx.com',
    'motormania.com', 'movemail.com',
    'mrspender.com', 'ms*.hinet.net',
    'msn.com', 'msn.co.uk',
    'mundo-r.com', 'munich.com',
    'muslim.com', 'muslimsonline.com',
    'mxs.de', 'myblue.cc',
    'mycity.com', 'mycommail.com',
    'mydomain.com', 'myeweb.com',
    'myfunnymail.com', 'mygamingconsoles.com',
    'myjazzmail.com', 'mymacmail.com',
    'mymail.ph.inter.net', 'mymail.ro',
    'mynet.com.tr', 'myotw.net',
    'mypersonalemail.com', 'myplace.com',
    'myself.com', 'myspace.com',
    'myway.com', 'mzgchaos.de',
    'n2business.com', 'n2mail.com',
    'nabble.com', 'name.com',
    'nanamail.co.il', 'nanaseaikawa.com',
    'naseej.com', 'nastything.com',
    'nativeweb.net', 'narod.ru',
    'nebraska.usa.com', 'nemra1.com',
    'nerdshack.com', 'nervhq.org',
    'net4b.pt', 'net4jesus.com',
    'netbounce.com', 'netcabo.pt',
    'netcourrier.com', 'netexecutive.com',
    'netkushi.com', 'netmongol.com',
    'netposta.net', 'netscape.com',
    'netscapeonline.co.uk', 'netsquare.com',
    'netti.fi', 'networld.com',
    'netzero.net', 'neustreet.com',
    'newhampshire.usa.com', 'newjersey.usa.com',
    'newmail.net', 'newmail.ok.com',
    'newmexico.usa.com', 'newspaperemail.com',
    'newyork.usa.com', 'newyorkcity.com',
    'nicegal.com', 'nightimeuk.com',
    'nightmail.com', 'nightmail.ru',
    'noemail.com', 'nonomail.com',
    'noolhar.com', 'northcarolina.usa.com',
    'nospammail.net', 'nowzer.com',
    'ny.com', 'nyc.com',
    'nz11.com', 'nzoomail.com',
    'oath.com', 'oceanfree.net',
    'oddpost.com', 'odeon.pl',
    'offshorewebmail.com', 'ofir.dk',
    'oicexchange.com', 'ok.ru',
    'ole.com', 'oleco.net',
    'omaninfo.com', 'onatoo.com',
    'onebox.com', 'onenet.com.ar',
    'ongc.net', 'oninet.pt',
    'online.ru', 'onlinewiz.com',
    'openbg.com', 'openforyou.com',
    'operamail.com', 'oplusnet.com',
    'orange.*', 'orangehome.co.uk',
    'orcon.net.nz', 'oregon.usa.com',
    'organizer.net', 'orgio.net',
    'orthodox.com', 'osite.com.br',
    'ourbrisbane.com', 'ournet.md',
    'ourwest.com', 'outgun.com',
    'ownmail.net', 'oxfoot.com',
    'pacer.com', 'pacific-ocean.com',
    'paginasamarillas.com', 'pakistanmail.com',
    'pando.com', 'pandora.be',
    'parsimail.com', 'parspage.com',
    'pattayacitythailand.com', 'pc4me.us',
    'pediatrician.com', 'penguinmaster.com',
    'peopleweb.com', 'personal.ro',
    'peru.com', 'petlover.com',
    'photographer.net', 'phreaker.net',
    'pigeonportal.com', 'pilu.com',
    'pinoymail.com', 'pipni.cz',
    'planet-school.de', 'planetaccess.com',
    'plasa.com', 'playersodds.com',
    'pluno.com', 'plusmail.com.br',
    'pnetmail.co.za', 'pobox.ru',
    'pochtamt.ru', 'pochta.ru',
    'poetic.com', 'pogowave.com',
    'polbox.com', 'politician.com',
    'pop.co.th', 'popmail.com',
    'popsmail.com', 'popstar.com',
    'portaldosalunos.com', 'portugalmail.com',
    'post.com', 'post.cz',
    'post.pl', 'post.sk',
    'postaccesslite.com', 'postiloota.net',
    'postino.ch', 'postino.it',
    'postpro.net', 'praize.com',
    'press.co.jp', 'priest.com',
    'printesamargareta.ro', 'private.21cn.com',
    'profesional.com', 'profession.freemail.com.br',
    'proinbox.com', 'promessage.com',
    'protestant.com', 'provincial.net',
    'publicist.com', 'punkass.com',
    'qatar.io', 'qlmail.com',
    'qrio.com', 'qsl.net',
    'queerplaces.com', 'quepasa.com',
    'quickwebmail.com', 'r-o-o-t.com',
    'raakim.com', 'rbcmail.ru',
    'radicalz.com', 'radiojobbank.com',
    'ragingbull.com', 'raisingadaughter.com',
    'ranmamail.com', 'ravearena.com',
    'razormail.com', 'real.ro',
    'reallyfast.biz', 'reallyfast.info',
    'rebels.com', 'reborn.com',
    'recme.net', 'rediffmail.com',
    'redseven.de', 'redwhitearmy.com',
    'registerednurses.com', 'relia.com',
    'repairman.com', 'representative.com',
    'revenue.com', 'rexian.com',
    'ritmes.net', 'rn.com',
    'rochester-mail.com', 'rock.com',
    'rocketship.com', 'rockfan.com',
    'rojname.com', 'rol.ro',
    'rome.com', 'romymichele.com',
    'rpharmacist.com', 'rt.nl',
    'rushpost.com', 'russiamail.com',
    's-mail.com', 'saabnet.com',
    'sacmail.com', 'safe-mail.net',
    'safrica.com', 'saigonnet.vn',
    'saintly.com', 'salesperson.net',
    'samilan.net', 'sandiego.com',
    'sanook.com', 'sanriotown.com',
    'sapo.pt', 'saturnfans.com',
    'sbcglobal.com', 'scfn.net',
    'sci.fi', 'sciaga.pl',
    'scotlandmail.com', 'scrapbookscrapbook.com',
    'search417.com', 'seark.com',
    'secretary.net', 'secretservices.net',
    'seductive.com', 'sendmail.ru',
    'sent.as', 'sent.at',
    'serga.com.ar', 'sermix.com',
    'serverwench.com', 'sesmail.com',
    'seznam.cz', 'shadango.com',
    'shuf.com', 'siamlocalhost.com',
    'sify.com', 'sinamail.com',
    'singmail.com', 'singnet.com.sg',
    'sirindia.com', 'sirunet.com',
    'sistersbrothers.com', 'sizzling.com',
    'slickriffs.co.uk', 'slingshot.com',
    'slomusic.net', 'smartemail.co.uk',
    'snail-mail.net', 'snakebite.com',
    'sneakemail.com', 'snoopymail.com',
    'so-simple.org', 'socamail.com',
    'sociologist.com', 'softhome.net',
    'solidmail.com', 'songwriter.net',
    'sos.lv', 'soundvillage.org',
    'southdakota.usa.com', 'sp.nl',
    'spacetowns.com', 'spainmail.com',
    'spartapiet.com', 'speed-racer.com',
    'speedymail.org', 'spils.com',
    'sportemail.com', 'spray.net',
    'spray.se', 'spymac.com',
    'srilankan.net', 'ssan.com',
    'stade.fr', 'stalag13.com',
    'starbuzz.com', 'starline.ee',
    'starmail.org', 'starmedia.com',
    'start.com.au', 'start.no',
    'strompost.*', 'student.com',
    'studmail.com', 'sudanmail.net',
    'suisse.org', 'sunbella.net',
    'sunpoint.net', 'sunrise.ch',
    'sunuweb.net', 'suomi24.fi',
    'supereva.com', 'supereva.it',
    'superposta.com', 'surf3.net',
    'surfsupnet.net', 'surfy.net',
    'surimail.com', 'surnet.cl',
    'svizzera.org', 'sweb.cz',
    'swift-mail.com', 'swissinfo.org',
    'swissmail.net', 'switzerland.org',
    'syriamail.com', 't-mail.com',
    't2mail.com', 'tabasheer.com',
    'talkcity.com', 'tangmonkey.com',
    'taxcutadvice.com', 'teachers.org',
    'techie.com', 'technisamail.co.za',
    'teenmail.co.uk', 'teenmail.co.za',
    'telebot.com', 'telefonica.net',
    'teleline.es', 'telinco.net',
    'telpage.net', 'telstra.com',
    'tempting.com', 'tenchiclub.com',
    'terra.*', 'terra.co*.*',
    'texas.usa.com', 'texascrossroads.com',
    'thai.com', 'thaimail.com',
    'the-fastest.net', 'the-quickest.com',
    'theinternetemail.com', 'theoffice.net',
    'thepostmaster.net', 'theracetrack.com',
    'theserverbiz.com', 'thewatercooler.com',
    'thinkpost.net', 'thirdage.com',
    'tim.it', 'timemail.com',
    'tinati.net', 'tiscali.*',
    'tiscalinet.it', 'tjohoo.se',
    'tlcfan.com', 'tlen.pl',
    'todito.com', 'todoperros.com',
    'tokyo.com', 'toothfairy.com',
    'topmail.com.ar', 'topmail.dk',
    'toquedequeda.com', 'torba.com',
    'torontomail.com', 'totalmail.com',
    'totonline.net', 'tough.com',
    'trav.se', 'trevas.net',
    'triton.net', 'trmailbox.com',
    'turbonett.com', 'turkey.com',
    'tvstar.com', 'typemail.com',
    'uae.ac', 'ubbi.com',
    'uboot.com', 'ugeek.com',
    'uk2net.com', 'ukr.net',
    'ukrpost.ua', 'uku.co.uk',
    'ummah.org', 'umpire.com',
    'unican.es', 'unicum.de',
    'unitedemailsystems.com', 'universal.pt',
    'universia.edu.ve', 'universia.es',
    'universia.net.mx', 'universia.pr',
    'universiabrasil.net', 'unofree.it',
    'uol.com.br', 'uole.com',
    'uomail.com', 'uraniomail.com',
    'ureach.com', 'usa.com',
    'userbeam.com', 'utah.usa.com',
    'uyuyuy.com', 'v-sexi.com',
    'vegetarisme.be', 'velnet.com',
    'vercorreo.com', 'verizonmail.com',
    'verticalheaven.com', 'veryfast.biz',
    'vfemail.net', 'vietmedia.com',
    'virgilio.it', 'virgin.net',
    'virtual-mail.com', 'visitmail.com',
    'vivelared.com', 'vjtimail.com',
    'vodamail.co.za', 'voila.fr',
    'vosforums.com', 'w.cn',
    'wallet.com', 'wam.co.za',
    'wanadoo.es', 'wanadoo.fr',
    'wap.hu', 'wapda.com',
    'wappi.com', 'warpmail.net',
    'wassup.com', 'waterloo.com',
    'wazmail.com', 'wearab.net',
    'web.de', 'web.nl',
    'webaddressbook.com', 'webbworks.com',
    'webdream.com', 'webemaillist.com',
    'webinfo.fi', 'webjump.com',
    'webmail.co.yu', 'webmail.co.za',
    'webmailv.com', 'webname.com',
    'webspawner.com', 'webstation.com',
    'webtopmail.com', 'webtribe.net',
    'weedmail.com', 'weekonline.com',
    'westvirginia.usa.com', 'whale-mail.com',
    'who.net', 'whoever.com',
    'wildmail.com', 'williams.net.ar',
    'winningteam.com', 'winwinhosting.com',
    'witelcom.com', 'witty.com',
    'wooow.it', 'worker.com',
    'worldcrossing.com', 'worldemail.com',
    'worldonline.de', 'wowmail.com',
    'wprost.pl', 'writeme.com',
    'wtonetwork.com', 'wurtele.net',
    'www.consulcredit.it', 'wyoming.usa.com',
    'xasa.com', 'xfreehosting.com',
    'xmsg.com', 'xnmsn.cn',
    'xtra.co.nz', 'xpectmore.com',
    'xsmail.com', 'xzapmail.com',
    'yahala.co.il', 'yaho.com',
    'yahoo.co*.*', 'yalla.com.lb',
    'yamal.info', 'yandex.*',
    'yawmail.com', 'yebox.com',
    'yellow-jackets.com', 'yellowstone.net',
    'yepmail.net', 'yifan.net',
    'your-mail.com', 'yours.com',
    'yyhmail.com', 'z11.com',
    'zednet.co.uk', 'zeeman.nl',
    'ziplip.com', 'zipmail.com.br',
    'zmail.pt', 'zmail.ru',
    'zonai.com', 'zoneview.net',
    'zoomshare.com', 'zoznam.sk',
    'zuvio.com', 'zwallet.com',
    'zybermail.com', 'zzn.com',
    'vip.163.com', 'vip.sina.com',
    'sohu.com', 'vip.tom.com',
    'adogperson.com', 'all4theskins.com',
    'alwaysgrilling.com', 'alwaysinthekitchen.com',
    'alwayswatchingtv.com', 'asylum.com',
    'beabookworm.com', 'beagolfer.com',
    'believeinliberty.com', 'bestcoolcars.com',
    'besure2vote.com', 'bigtimecatperson.com',
    'bigtimereader.com', 'bigtimesportsfan.com',
    'capsfanatic.com', 'capshockeyfan.com',
    'car-nut.net', 'cat-person.com',
    'chat-with-me.com', 'cheatasrule.com',
    'crazy4homeimprovement.com', 'crazy4mail.com',
    'crazycarfan.com', 'crazyforemail.com',
    'descriptivemail.com', 'differentmail.com',
    'dogpeoplerule.com', 'easydoesit.com',
    'expressivemail.com', 'fanaticos.com',
    'fanofcomputers.com', 'fanofcooking.com',
    'fieldmail.com', 'fleetmail.com',
    'focusedonreturns.com', 'futboladdict.com',
    'getintobooks.com', 'hail2theskins.com',
    'i-dig-movies.com', 'i-love-restaurants.com',
    'idigelectronics.com', 'idigvideos.com',
    'ilike2invest.com', 'ilike2workout.com',
    'ilikeworkingout.com', 'ilovehomeprojects.com',
    'iloveworkingout.com', 'in2autos.net',
    'intomotors.com', 'iwatchrealitytv.com',
    'love2exercise.com', 'love2workout.com',
    'lovetoexercise.com', 'luvfishing.com',
    'luvsoccer.com', 'mail4me.com',
    'majorshopaholic.com', 'majortechie.com',
    'motor-nut.com', 'moviefan.com',
    'mycatiscool.com', 'myfantasyteamrules.com',
    'netbusiness.com', 'news-fanatic.com',
    'onlinevideosrock.com', 'realbookfan.com',
    'realitytvaddict.net', 'realitytvnut.com',
    'realtravelfan.com', 'redskinscheer.com',
    'redskinsfancentral.com', 'redskinshog.com',
    'redskinsspecialteams.com', 'redskinsultimatefan.com',
    'skins4life.com', 'stargate2.com',
    'stargatefanclub.com', 'stargatesg1.com',
    'switched.com', 'thegamefanatic.com',
    'totalfoodnut.com', 'totally-into-cooking.com',
    'totallyintobasketball.com', 'totallyintocooking.com',
    'totallyintogolf.com', 'totallyintohockey.com',
    'totallyintoreading.com', 'totallyintosports.com',
    'totalmoviefan.com', 'travel2newplaces.com',
    'ultimateredskinsfan.com', 'videogamesrock.com',
    'wayintocomputers.com', 'whatmail.com',
    'wild4music.com', 'wildaboutelectronics.com',
    'workingonthehouse.com', 'writesoon.com',
    'arab.ir', 'denmark.ir',
    'icq.ir', 'ir.ae',
    'ire.ir', 'ireland.ir',
    'jpg.ir', 'ksa.ir',
    'london.ir', 'paltalk.ir',
    'sweden.ir', 'tokyo.ir',
]
