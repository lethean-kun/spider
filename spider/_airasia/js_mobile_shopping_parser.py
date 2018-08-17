# -*- coding: utf-8 -*-

js_mobile_shopping = r"""
/**
 *三字码全局变量
 */
var CITY_JSON = JSON.parse("{\"BBA\":\"BBA\",\"SCQ\":\"SCQ\",\"JRH\":\"JRH\",\"BBC\":\"BBC\",\"JRK\":\"JRK\",\"BBB\":\"BBB\",\"BBE\":\"BBE\",\"SCU\":\"SCU\",\"BBD\":\"BBD\",\"SCT\":\"SCT\",\"BBG\":\"BBG\",\"JRO\":\"JRO\",\"SCW\":\"SCW\",\"SCV\":\"SCV\",\"BBI\":\"BBI\",\"SCY\":\"SCY\",\"SCX\":\"SCX\",\"BBK\":\"BBK\",\"JRS\":\"JRS\",\"SCZ\":\"SCZ\",\"BBM\":\"BBM\",\"BBO\":\"BBO\",\"BBN\":\"BBN\",\"BBQ\":\"BBQ\",\"BBP\":\"BBP\",\"BBS\":\"BBS\",\"SDD\":\"SDD\",\"BBR\":\"BBR\",\"BBU\":\"BUH\",\"SDF\":\"SDF\",\"SDE\":\"SDE\",\"BBV\":\"BBV\",\"SDG\":\"SDG\",\"SDJ\":\"SDJ\",\"BBX\":\"BBX\",\"JSA\":\"JSA\",\"SDL\":\"SDL\",\"BBZ\":\"BBZ\",\"SDK\":\"SDK\",\"SDN\":\"SDN\",\"JSH\":\"JSH\",\"SDP\":\"SDP\",\"BCB\":\"BCB\",\"SDR\":\"SDR\",\"BCA\":\"BCA\",\"JSI\":\"JSI\",\"SDQ\":\"SDQ\",\"BCD\":\"BCD\",\"SDT\":\"SDT\",\"SDU\":\"RIO\",\"BCH\":\"BCH\",\"JSR\":\"JSR\",\"BCI\":\"BCI\",\"SDY\":\"SDY\",\"BCL\":\"BCL\",\"JST\":\"JST\",\"BCK\":\"BCK\",\"JSS\":\"JSS\",\"BCN\":\"BCN\",\"BCM\":\"BCM\",\"SEA\":\"SEA\",\"BCO\":\"BCO\",\"BCR\":\"BCR\",\"JSY\":\"JSY\",\"SEB\":\"SEB\",\"BCT\":\"BCT\",\"BCU\":\"BCU\",\"BCX\":\"BCX\",\"BCW\":\"BCW\",\"BCY\":\"BCY\",\"SEN\":\"SEN\",\"BDA\":\"BDA\",\"SES\":\"SES\",\"BDB\":\"BDB\",\"SER\":\"SER\",\"BDD\":\"BDD\",\"BDG\":\"BDG\",\"SEV\":\"SEV\",\"BDI\":\"BDI\",\"SEY\":\"SEY\",\"BDH\":\"BDH\",\"BDK\":\"BDK\",\"BDJ\":\"BDJ\",\"JTR\":\"JTR\",\"SEZ\":\"SEZ\",\"BDM\":\"BDM\",\"BDL\":\"HFD\",\"BDO\":\"BDO\",\"BDN\":\"BDN\",\"BDQ\":\"BDQ\",\"JTY\":\"JTY\",\"SFB\":\"ORL\",\"BDP\":\"BDP\",\"SFA\":\"SFA\",\"BDS\":\"BDS\",\"SFD\":\"SFD\",\"SFC\":\"SFC\",\"BDU\":\"BDU\",\"SFE\":\"SFE\",\"BDW\":\"BDW\",\"SFG\":\"SFG\",\"BDY\":\"BDY\",\"JUB\":\"JUB\",\"SFJ\":\"SFJ\",\"SFL\":\"SFL\",\"SFN\":\"SFN\",\"SFM\":\"SFM\",\"JUH\":\"JUH\",\"SFO\":\"SFO\",\"BEB\":\"BEB\",\"JUJ\":\"JUJ\",\"JUI\":\"JUI\",\"SFQ\":\"GNY\",\"BED\":\"BED\",\"JUL\":\"JUL\",\"SFT\":\"SFT\",\"BEC\":\"ICT\",\"SFS\":\"SFS\",\"BEE\":\"BEE\",\"JUM\":\"JUM\",\"SFU\":\"SFU\",\"BEG\":\"BEG\",\"BEJ\":\"BEJ\",\"BEL\":\"BEL\",\"BEN\":\"BEN\",\"JUV\":\"JUV\",\"BEP\":\"BEP\",\"BER\":\"BER\",\"SGC\":\"SGC\",\"JUZ\":\"JUZ\",\"BEQ\":\"BEQ\",\"BET\":\"BET\",\"BES\":\"BES\",\"SGD\":\"SGD\",\"BEV\":\"BEV\",\"BEU\":\"BEU\",\"SGF\":\"SGF\",\"JVA\":\"JVA\",\"BEW\":\"BEW\",\"SGH\":\"SGH\",\"BEZ\":\"BEZ\",\"BEY\":\"BEY\",\"SGJ\":\"SGJ\",\"SGO\":\"SGO\",\"SGN\":\"SGN\",\"BFC\":\"BFC\",\"SGU\":\"SGU\",\"BFD\":\"BFD\",\"JVL\":\"JVL\",\"BFG\":\"BFG\",\"BFF\":\"BFF\",\"BFI\":\"SEA\",\"SGY\":\"SGY\",\"BFJ\":\"BFJ\",\"BFM\":\"MOB\",\"BFL\":\"BFL\",\"BFO\":\"BFO\",\"BFN\":\"BFN\",\"SHB\":\"SHB\",\"BFP\":\"BFP\",\"SHA\":\"SHA\",\"BFS\":\"BFS\",\"SHD\":\"SHD\",\"BFT\":\"BFT\",\"SHE\":\"SHE\",\"BFV\":\"BFV\",\"SHJ\":\"SHJ\",\"BFX\":\"BFX\",\"SHL\":\"SHL\",\"SHM\":\"SHM\",\"SHP\":\"SHP\",\"BGB\":\"BGB\",\"SHR\":\"SHR\",\"BGA\":\"BGA\",\"BGD\":\"BGD\",\"SHT\":\"SHT\",\"BGC\":\"BGC\",\"SHS\":\"SHS\",\"BGF\":\"BGF\",\"JWN\":\"JWN\",\"SHV\":\"SHV\",\"BGE\":\"BGE\",\"SHW\":\"SHW\",\"BGJ\":\"BGJ\",\"BGI\":\"BGI\",\"SHY\":\"SHY\",\"BGL\":\"BGL\",\"BGM\":\"BGM\",\"BGO\":\"BGO\",\"BGR\":\"BGR\",\"SIC\":\"SIC\",\"SID\":\"SID\",\"SIF\":\"SIF\",\"JXA\":\"JXA\",\"BGW\":\"BGW\",\"SIH\":\"SIH\",\"BGZ\":\"BGZ\",\"SIK\":\"SIK\",\"BGY\":\"MIL\",\"SIJ\":\"SIJ\",\"SIN\":\"SIN\",\"BHA\":\"BHA\",\"SIQ\":\"SIQ\",\"SIP\":\"SIP\",\"BHB\":\"BHB\",\"SIR\":\"SIR\",\"BHE\":\"BHE\",\"BHD\":\"BFS\",\"SIT\":\"SIT\",\"BHI\":\"BHI\",\"BHH\":\"BHH\",\"SIX\":\"SIX\",\"BHK\":\"BHK\",\"BHJ\":\"BHJ\",\"BHM\":\"BHM\",\"BHO\":\"BHO\",\"BHN\":\"BHN\",\"BHQ\":\"BHQ\",\"SJB\":\"SJB\",\"BHP\":\"BHP\",\"BHS\":\"BHS\",\"SJD\":\"SJD\",\"BHR\":\"BHR\",\"SJC\":\"SJC\",\"BHU\":\"BHU\",\"BHT\":\"BHT\",\"SJE\":\"SJE\",\"BHV\":\"BHV\",\"SJJ\":\"SJJ\",\"BHY\":\"BHY\",\"BHX\":\"BHX\",\"SJI\":\"SJI\",\"SJK\":\"SJK\",\"SJP\":\"SJP\",\"SJO\":\"SJO\",\"BIB\":\"BIB\",\"BIA\":\"BIA\",\"SJQ\":\"SJQ\",\"BID\":\"BID\",\"SJT\":\"SJT\",\"SJV\":\"SJV\",\"BIE\":\"BIE\",\"SJU\":\"SJU\",\"BIH\":\"BIH\",\"SJW\":\"SJW\",\"SJZ\":\"SJZ\",\"BII\":\"BII\",\"SJY\":\"SJY\",\"BIL\":\"BIL\",\"BIK\":\"BIK\",\"JYV\":\"JYV\",\"BIM\":\"BIM\",\"BIO\":\"BIO\",\"BIR\":\"BIR\",\"BIQ\":\"BIQ\",\"SKB\":\"SKB\",\"BIT\":\"BIT\",\"SKE\":\"SKE\",\"BIS\":\"BIS\",\"SKD\":\"SKD\",\"SKG\":\"SKG\",\"BIU\":\"BIU\",\"SKI\":\"SKI\",\"BIW\":\"BIW\",\"SKH\":\"SKH\",\"SKK\":\"SKK\",\"BIY\":\"BIY\",\"SKO\":\"SKO\",\"SKN\":\"SKN\",\"BJA\":\"BJA\",\"SKP\":\"SKP\",\"JZH\":\"JZH\",\"SKR\":\"SKR\",\"SKU\":\"SKU\",\"BJD\":\"BJD\",\"SKT\":\"SKT\",\"SKW\":\"SKW\",\"BJF\":\"BJF\",\"SKV\":\"SKV\",\"BJI\":\"BJI\",\"BJH\":\"BJH\",\"SKX\":\"SKX\",\"BJK\":\"BJK\",\"BJJ\":\"BJJ\",\"SKZ\":\"SKZ\",\"BJM\":\"BJM\",\"BJL\":\"BJL\",\"SLA\":\"SLA\",\"SLD\":\"SLD\",\"BJR\":\"BJR\",\"SLC\":\"SLC\",\"BJU\":\"BJU\",\"SLE\":\"SLE\",\"BJW\":\"BJW\",\"SLH\":\"SLH\",\"BJV\":\"BJV\",\"BJX\":\"BJX\",\"SLI\":\"SLI\",\"SLL\":\"SLL\",\"BJZ\":\"BJZ\",\"SLK\":\"SLK\",\"SLN\":\"SLN\",\"SLM\":\"SLM\",\"SLP\":\"SLP\",\"BKB\":\"BKB\",\"SLR\":\"SLR\",\"BKA\":\"MOW\",\"SLQ\":\"SLQ\",\"SLT\":\"SLT\",\"SLS\":\"SLS\",\"BKF\":\"BKF\",\"SLV\":\"SLV\",\"BKE\":\"BKE\",\"SLU\":\"SLU\",\"SLX\":\"SLX\",\"SLW\":\"SLW\",\"SLZ\":\"SLZ\",\"BKI\":\"BKI\",\"SLY\":\"SLY\",\"BKL\":\"CLE\",\"BKK\":\"BKK\",\"BKN\":\"BKN\",\"BKM\":\"BKM\",\"BKP\":\"BKP\",\"SMA\":\"SMA\",\"BKO\":\"BKO\",\"BKQ\":\"BKQ\",\"BKS\":\"BKS\",\"BKU\":\"BKU\",\"SMF\":\"SAC\",\"SMI\":\"SMI\",\"BKW\":\"BKW\",\"BKZ\":\"BKZ\",\"BKY\":\"BKY\",\"SML\":\"SML\",\"SMO\":\"SMO\",\"SMN\":\"SMN\",\"BLA\":\"BLA\",\"SMQ\":\"SMQ\",\"SMS\":\"SMS\",\"SMR\":\"SMR\",\"BLE\":\"BLE\",\"BLD\":\"BLD\",\"SMT\":\"SMT\",\"BLG\":\"BLG\",\"SMW\":\"SMW\",\"SMV\":\"SMV\",\"BLI\":\"BLI\",\"BLH\":\"BLH\",\"SMX\":\"SMX\",\"BLK\":\"BLK\",\"BLJ\":\"BLJ\",\"BLM\":\"BLM\",\"BLL\":\"BLL\",\"BLO\":\"BLO\",\"BLQ\":\"BLQ\",\"SNA\":\"SNA\",\"BLS\":\"BLS\",\"BLR\":\"BLR\",\"SNC\":\"SNC\",\"SNF\":\"SNF\",\"SNE\":\"SNE\",\"SNH\":\"SNH\",\"BLX\":\"BLX\",\"BLZ\":\"BLZ\",\"SNK\":\"SNK\",\"SNN\":\"SNN\",\"SNP\":\"SNP\",\"SNO\":\"SNO\",\"SNR\":\"SNR\",\"BMA\":\"STO\",\"SNQ\":\"SNQ\",\"BMD\":\"BMD\",\"BMC\":\"BMC\",\"SNV\":\"SNV\",\"BME\":\"BME\",\"SNW\":\"SNW\",\"BMI\":\"BMI\",\"BMK\":\"BMK\",\"BMM\":\"BMM\",\"BMO\":\"BMO\",\"SOC\":\"SOC\",\"BMT\":\"BPT\",\"BMS\":\"BMS\",\"SOD\":\"SOD\",\"BMV\":\"BMV\",\"SOG\":\"SOG\",\"BMU\":\"BMU\",\"SOF\":\"SOF\",\"BMX\":\"BMX\",\"SOI\":\"SOI\",\"BMW\":\"BMW\",\"BMY\":\"BMY\",\"SOJ\":\"SOJ\",\"SOM\":\"SOM\",\"SOL\":\"SOL\",\"SON\":\"SON\",\"BNA\":\"BNA\",\"SOQ\":\"SOQ\",\"BNE\":\"BNE\",\"SOU\":\"SOU\",\"BND\":\"BND\",\"SOT\":\"SOT\",\"BNG\":\"BNG\",\"SOW\":\"SOW\",\"SOV\":\"SOV\",\"BNI\":\"BNI\",\"SOY\":\"SOY\",\"BNH\":\"HFD\",\"BNK\":\"BNK\",\"BNO\":\"BNO\",\"BNN\":\"BNN\",\"BNP\":\"BNP\",\"SPA\":\"SPA\",\"SPC\":\"SPC\",\"BNU\":\"BNU\",\"SPF\":\"SPF\",\"BNY\":\"BNY\",\"BNX\":\"BNX\",\"SPI\":\"SPI\",\"SPN\":\"SPN\",\"SPP\":\"SPP\",\"BOB\":\"BOB\",\"SPR\":\"SPR\",\"BOD\":\"BOD\",\"BOC\":\"BOC\",\"SPU\":\"SPU\",\"BOH\":\"BOH\",\"BOG\":\"BOG\",\"BOJ\":\"BOJ\",\"BOI\":\"BOI\",\"BON\":\"BON\",\"BOM\":\"BOM\",\"BOO\":\"BOO\",\"BOR\":\"BOR\",\"BOS\":\"BOS\",\"BOV\":\"BOV\",\"SQG\":\"SQG\",\"BOU\":\"BOU\",\"BOX\":\"BOX\",\"KAA\":\"KAA\",\"SQH\":\"SQH\",\"KAC\":\"KAC\",\"SQK\":\"SQK\",\"BOY\":\"BOY\",\"KAB\":\"KAB\",\"SQJ\":\"SQJ\",\"KAD\":\"KAD\",\"KAG\":\"KAG\",\"SQO\":\"SQO\",\"SQN\":\"SQN\",\"BPC\":\"BPC\",\"KAK\":\"KAK\",\"KAJ\":\"KAJ\",\"SQR\":\"SQR\",\"KAM\":\"KAM\",\"BPG\":\"BPG\",\"KAO\":\"KAO\",\"SQW\":\"SQW\",\"KAN\":\"KAN\",\"SQV\":\"SQV\",\"BPI\":\"BPI\",\"KAQ\":\"KAQ\",\"BPH\":\"BPH\",\"KAS\":\"KAS\",\"KAU\":\"KAU\",\"KAT\":\"KAT\",\"BPL\":\"BPL\",\"KAW\":\"KAW\",\"BPN\":\"BPN\",\"KAV\":\"KAV\",\"KAX\":\"KAX\",\"BPS\":\"BPS\",\"SRD\":\"SRD\",\"KAZ\":\"KAZ\",\"SRC\":\"SRC\",\"BPT\":\"BPT\",\"SRE\":\"SRE\",\"SRH\":\"SRH\",\"SRG\":\"SRG\",\"BPY\":\"BPY\",\"SRJ\":\"SRJ\",\"KBA\":\"KBA\",\"SRI\":\"SRI\",\"BPX\":\"BPX\",\"KBC\":\"KBC\",\"SRK\":\"SRK\",\"SRN\":\"SRN\",\"SRM\":\"SRM\",\"KBH\":\"KBH\",\"SRP\":\"SRP\",\"KBG\":\"KBG\",\"BQB\":\"BQB\",\"KBJ\":\"KBJ\",\"SRQ\":\"SRQ\",\"KBL\":\"KBL\",\"SRT\":\"SRT\",\"SRV\":\"SRV\",\"BQH\":\"LON\",\"KBP\":\"IEV\",\"SRX\":\"SRX\",\"KBR\":\"KBR\",\"SRZ\":\"SRZ\",\"KBQ\":\"KBQ\",\"SRY\":\"SRY\",\"BQL\":\"BQL\",\"KBT\":\"KBT\",\"KBS\":\"KBS\",\"BQN\":\"BQN\",\"KBV\":\"KBV\",\"KBU\":\"KBU\",\"KBX\":\"KBX\",\"SSA\":\"SSA\",\"BQO\":\"BQO\",\"KBY\":\"KBY\",\"BQS\":\"BQS\",\"SSG\":\"SSG\",\"BQU\":\"BQU\",\"KCA\":\"KCA\",\"SSH\":\"SSH\",\"SSJ\":\"SSJ\",\"SSO\":\"SSO\",\"BRA\":\"BRA\",\"KCH\":\"KCH\",\"BRC\":\"BRC\",\"KCK\":\"KCK\",\"SSR\":\"SSR\",\"BRE\":\"BRE\",\"KCM\":\"KCM\",\"BRD\":\"BRD\",\"SST\":\"SST\",\"SSW\":\"SSW\",\"BRI\":\"BRI\",\"SSY\":\"SSY\",\"KCP\":\"KCP\",\"SSX\":\"SSX\",\"BRK\":\"BRK\",\"SSZ\":\"SSZ\",\"BRM\":\"BRM\",\"KCU\":\"KCU\",\"BRL\":\"BRL\",\"BRO\":\"BRO\",\"BRN\":\"BRN\",\"BRQ\":\"BRQ\",\"STB\":\"STB\",\"STA\":\"STA\",\"BRS\":\"BRS\",\"STD\":\"STD\",\"BRR\":\"BRR\",\"KCZ\":\"KCZ\",\"BRU\":\"BRU\",\"BRT\":\"BRT\",\"STE\":\"STE\",\"BRW\":\"BRW\",\"STH\":\"STH\",\"BRV\":\"BRV\",\"STG\":\"STG\",\"BRY\":\"BRY\",\"STJ\":\"STJ\",\"STI\":\"STI\",\"KDD\":\"KDD\",\"STL\":\"STL\",\"BRZ\":\"BRZ\",\"KDC\":\"KDC\",\"STK\":\"STK\",\"STN\":\"LON\",\"STM\":\"STM\",\"KDH\":\"KDH\",\"BSB\":\"BSB\",\"STR\":\"STR\",\"BSA\":\"BSA\",\"KDI\":\"KDI\",\"STT\":\"STT\",\"BSD\":\"BSD\",\"BSC\":\"BSC\",\"KDK\":\"ADQ\",\"STS\":\"STS\",\"KDN\":\"KDN\",\"STV\":\"STV\",\"KDM\":\"KDM\",\"STX\":\"STX\",\"BSG\":\"BSG\",\"KDO\":\"KDO\",\"STW\":\"STW\",\"BSJ\":\"BSJ\",\"KDR\":\"KDR\",\"STY\":\"STY\",\"BSL\":\"EAP\",\"BSK\":\"BSK\",\"KDU\":\"KDU\",\"SUA\":\"SUA\",\"BSO\":\"BSO\",\"BSR\":\"BSR\",\"SUC\":\"SUC\",\"BSQ\":\"BSQ\",\"SUB\":\"SUB\",\"BST\":\"BST\",\"BSS\":\"BSS\",\"SUD\":\"SUD\",\"SUG\":\"SUG\",\"SUF\":\"SUF\",\"BSX\":\"BSX\",\"SUI\":\"SUI\",\"BSW\":\"BSW\",\"SUH\":\"SUH\",\"BSZ\":\"BSZ\",\"BSY\":\"BSY\",\"KEB\":\"KEB\",\"SUJ\":\"SUJ\",\"KED\":\"KED\",\"SUL\":\"SUL\",\"KEF\":\"REK\",\"SUN\":\"SUN\",\"BTA\":\"BTA\",\"KEI\":\"KEI\",\"SUQ\":\"SUQ\",\"SUP\":\"SUP\",\"BTC\":\"BTC\",\"KEK\":\"KEK\",\"KEJ\":\"KEJ\",\"SUR\":\"SUR\",\"KEM\":\"KEM\",\"KEL\":\"KEL\",\"KEO\":\"KEO\",\"SUW\":\"SUW\",\"BTF\":\"BTF\",\"SUV\":\"SUV\",\"BTI\":\"BTI\",\"KEQ\":\"KEQ\",\"BTH\":\"BTH\",\"SUX\":\"SUX\",\"BTK\":\"BTK\",\"BTJ\":\"BTJ\",\"KER\":\"KER\",\"BTM\":\"BTM\",\"BTL\":\"BTL\",\"KET\":\"KET\",\"KEW\":\"KEW\",\"KEY\":\"KEY\",\"SVB\":\"SVB\",\"KEX\":\"KEX\",\"BTS\":\"BTS\",\"SVD\":\"SVD\",\"BTR\":\"BTR\",\"SVC\":\"SVC\",\"BTU\":\"BTU\",\"BTT\":\"BTT\",\"BTW\":\"BTW\",\"SVH\":\"SVH\",\"BTV\":\"BTV\",\"SVG\":\"SVG\",\"SVJ\":\"SVJ\",\"BTX\":\"BTX\",\"KFA\":\"KFA\",\"SVI\":\"SVI\",\"SVL\":\"SVL\",\"BTZ\":\"BTZ\",\"SVK\":\"SVK\",\"SVP\":\"SVP\",\"KFG\":\"KFG\",\"SVO\":\"MOW\",\"BUA\":\"BUA\",\"SVQ\":\"SVQ\",\"BUD\":\"BUD\",\"BUC\":\"BUC\",\"SVS\":\"SVS\",\"BUF\":\"BUF\",\"SVV\":\"SVV\",\"SVU\":\"SVU\",\"KFP\":\"KFP\",\"SVX\":\"SVX\",\"BUG\":\"BUG\",\"SVW\":\"SVW\",\"BUI\":\"BUI\",\"SVY\":\"SVY\",\"BUL\":\"BUL\",\"BUK\":\"BUK\",\"BUN\":\"BUN\",\"SWA\":\"SWA\",\"BUO\":\"BUO\",\"BUR\":\"BUR\",\"SWC\":\"SWC\",\"BUQ\":\"BUQ\",\"BUT\":\"BUT\",\"BUS\":\"BUS\",\"SWD\":\"SWD\",\"BUV\":\"BUV\",\"SWF\":\"SWF\",\"BUX\":\"BUX\",\"KGA\":\"KGA\",\"BUW\":\"BUW\",\"SWH\":\"SWH\",\"BUZ\":\"BUZ\",\"KGC\":\"KGC\",\"BUY\":\"BUY\",\"SWJ\":\"SWJ\",\"KGE\":\"KGE\",\"KGD\":\"KGD\",\"SWO\":\"SWO\",\"KGG\":\"KGG\",\"KGF\":\"KGF\",\"KGI\":\"KGI\",\"KGH\":\"KGH\",\"BVC\":\"BVC\",\"KGK\":\"KGK\",\"BVB\":\"BVB\",\"KGJ\":\"KGJ\",\"SWR\":\"SWR\",\"BVE\":\"BVE\",\"KGM\":\"KGM\",\"BVD\":\"BVD\",\"KGL\":\"KGL\",\"BVG\":\"BVG\",\"KGO\":\"KGO\",\"SWW\":\"SWW\",\"BVI\":\"BVI\",\"BVH\":\"BVH\",\"SWX\":\"SWX\",\"KGS\":\"KGS\",\"KGU\":\"KGU\",\"KGT\":\"KGT\",\"BVO\":\"BVO\",\"KGY\":\"KGY\",\"SXB\":\"SXB\",\"KGX\":\"KGX\",\"BVR\":\"BVR\",\"SXC\":\"AVX\",\"SXF\":\"BER\",\"SXE\":\"SXE\",\"BVW\":\"BVW\",\"SXH\":\"SXH\",\"SXG\":\"SXG\",\"SXJ\":\"SXJ\",\"BVX\":\"BVX\",\"KHD\":\"KHD\",\"BVZ\":\"BVZ\",\"KHC\":\"KHC\",\"SXK\":\"SXK\",\"KHE\":\"KHE\",\"SXM\":\"SXM\",\"KHH\":\"KHH\",\"SXP\":\"SXP\",\"SXO\":\"SXO\",\"KHG\":\"KHG\",\"BWB\":\"BWB\",\"SXR\":\"SXR\",\"BWA\":\"BWA\",\"KHI\":\"KHI\",\"SXQ\":\"SXQ\",\"BWD\":\"BWD\",\"SXT\":\"SXT\",\"BWC\":\"BWC\",\"KHK\":\"KHK\",\"SXS\":\"SXS\",\"BWF\":\"BWF\",\"KHN\":\"KHN\",\"BWE\":\"BWE\",\"KHM\":\"KHM\",\"SXU\":\"SXU\",\"SXW\":\"SXW\",\"SXZ\":\"SXZ\",\"BWI\":\"BWI\",\"SXY\":\"SXY\",\"BWL\":\"BWL\",\"KHT\":\"KHT\",\"BWK\":\"BWK\",\"KHS\":\"KHS\",\"BWN\":\"BWN\",\"KHV\":\"KHV\",\"BWM\":\"BWM\",\"SYA\":\"SYA\",\"BWO\":\"BWO\",\"BWQ\":\"BWQ\",\"SYB\":\"SYB\",\"BWT\":\"BWT\",\"SYE\":\"SYE\",\"BWS\":\"BWS\",\"SYD\":\"SYD\",\"BWU\":\"BWU\",\"KIA\":\"KIA\",\"KIE\":\"KIE\",\"SYM\":\"SYM\",\"KID\":\"KID\",\"SYO\":\"SYO\",\"KIF\":\"KIF\",\"BXA\":\"BXA\",\"KIH\":\"KIH\",\"BXC\":\"BXC\",\"KIK\":\"KIK\",\"BXB\":\"BXB\",\"KIJ\":\"KIJ\",\"SYR\":\"SYR\",\"KIM\":\"KIM\",\"BXD\":\"BXD\",\"KIO\":\"KIO\",\"SYW\":\"SYW\",\"KIN\":\"KIN\",\"BXI\":\"BXI\",\"SYY\":\"SYY\",\"BXH\":\"BXH\",\"KIP\":\"SPS\",\"SYX\":\"SYX\",\"KIS\":\"KIS\",\"BXJ\":\"BXJ\",\"KIR\":\"KIR\",\"SYZ\":\"SYZ\",\"KIT\":\"KIT\",\"BXO\":\"BXO\",\"KIW\":\"KIW\",\"BXN\":\"BXN\",\"KIV\":\"KIV\",\"KIY\":\"KIY\",\"SZB\":\"KUL\",\"KIX\":\"OSA\",\"SZA\":\"SZA\",\"BXS\":\"BXS\",\"SZC\":\"SZC\",\"BXU\":\"BXU\",\"SZF\":\"SSX\",\"SZE\":\"SZE\",\"BXV\":\"BXV\",\"SZG\":\"SZG\",\"BXX\":\"BXX\",\"KJA\":\"KJA\",\"SZI\":\"SZI\",\"SZK\":\"SZK\",\"KJH\":\"KJH\",\"BYB\":\"BYB\",\"BYA\":\"BYA\",\"SZQ\":\"SZQ\",\"KJI\":\"KJI\",\"BYD\":\"BYD\",\"SZT\":\"SZT\",\"BYC\":\"BYC\",\"SZS\":\"SZS\",\"SZV\":\"SZV\",\"SZX\":\"SZX\",\"SZZ\":\"SZZ\",\"BYK\":\"BYK\",\"BYM\":\"BYM\",\"BYO\":\"BYO\",\"BYW\":\"BYW\",\"KKC\":\"KKC\",\"KKE\":\"KKE\",\"KKD\":\"KKD\",\"KKG\":\"KKG\",\"BZA\":\"BZA\",\"KKH\":\"KKH\",\"BZB\":\"BZB\",\"KKJ\":\"KKJ\",\"BZE\":\"BZE\",\"BZD\":\"BZD\",\"BZG\":\"BZG\",\"KKO\":\"KKO\",\"KKN\":\"KKN\",\"BZI\":\"BZI\",\"BZH\":\"BZH\",\"BZK\":\"BZK\",\"KKR\":\"KKR\",\"KKU\":\"KKU\",\"BZL\":\"BZL\",\"KKT\":\"KKT\",\"BZO\":\"BZO\",\"BZN\":\"BZN\",\"BZP\":\"BZP\",\"KKX\":\"KKX\",\"BZS\":\"WAS\",\"BZR\":\"BZR\",\"KKZ\":\"KKZ\",\"BZV\":\"BZV\",\"KLB\":\"KLB\",\"KLF\":\"KLF\",\"KLH\":\"KLH\",\"KLG\":\"KLG\",\"KLL\":\"KLL\",\"KLO\":\"KLO\",\"KLR\":\"KLR\",\"KLS\":\"KLS\",\"KLV\":\"KLV\",\"KLU\":\"KLU\",\"KLX\":\"KLX\",\"KLW\":\"KLW\",\"KLZ\":\"KLZ\",\"KMA\":\"KMA\",\"KMC\":\"KMC\",\"KMG\":\"KMG\",\"KMF\":\"KMF\",\"KMI\":\"KMI\",\"KMH\":\"KMH\",\"KMJ\":\"KMJ\",\"KMM\":\"KMM\",\"KMQ\":\"KMQ\",\"KMS\":\"KMS\",\"KMU\":\"KMU\",\"KMT\":\"KMT\",\"KMV\":\"KMV\",\"KMY\":\"KMY\",\"KMZ\":\"KMZ\",\"KNA\":\"KNA\",\"KND\":\"KND\",\"KNH\":\"KNH\",\"KNG\":\"KNG\",\"KNI\":\"KNI\",\"KNK\":\"KNK\",\"KNO\":\"MES\",\"KNQ\":\"KNQ\",\"KNS\":\"KNS\",\"KNV\":\"KNV\",\"KNU\":\"KNU\",\"KNX\":\"KNX\",\"KNW\":\"KNW\",\"KOA\":\"KOA\",\"KOC\":\"KOC\",\"KOB\":\"KOB\",\"KOE\":\"KOE\",\"KOD\":\"KOD\",\"KOG\":\"KOG\",\"KOI\":\"KOI\",\"KOK\":\"KOK\",\"KOJ\":\"KOJ\",\"KON\":\"KON\",\"KOP\":\"KOP\",\"KOS\":\"KOS\",\"KOU\":\"KOU\",\"KOT\":\"KOT\",\"KOW\":\"KOW\",\"KOV\":\"KOV\",\"TAB\":\"TAB\",\"KOX\":\"KOX\",\"TAA\":\"TAA\",\"TAC\":\"TAC\",\"TAF\":\"ORN\",\"TAE\":\"TAE\",\"TAH\":\"TAH\",\"TAG\":\"TAG\",\"TAJ\":\"ATP\",\"TAI\":\"TAI\",\"KPD\":\"KPD\",\"TAL\":\"TAL\",\"TAK\":\"TAK\",\"TAM\":\"TAM\",\"TAP\":\"TAP\",\"TAO\":\"TAO\",\"TAR\":\"TAR\",\"KPI\":\"KPI\",\"TAT\":\"TAT\",\"TAS\":\"TAS\",\"TAV\":\"TAV\",\"TAX\":\"TAX\",\"KPO\":\"KPO\",\"TAW\":\"TAW\",\"TAZ\":\"TAZ\",\"TAY\":\"TAY\",\"KPS\":\"KPS\",\"TBC\":\"TBC\",\"KPY\":\"KPY\",\"TBB\":\"TBB\",\"TBG\":\"TBG\",\"KQA\":\"KQA\",\"TBI\":\"TBI\",\"TBH\":\"TBH\",\"TBJ\":\"TBJ\",\"TBM\":\"TBM\",\"TBO\":\"TBO\",\"TBP\":\"TBP\",\"CAC\":\"CAC\",\"TBS\":\"TBS\",\"CAB\":\"CAB\",\"TBR\":\"TBR\",\"CAE\":\"CAE\",\"TBU\":\"TBU\",\"CAD\":\"CAD\",\"TBT\":\"TBT\",\"CAG\":\"CAG\",\"TBW\":\"TBW\",\"CAF\":\"CAF\",\"CAI\":\"CAI\",\"CAH\":\"CAH\",\"CAK\":\"CAK\",\"TBZ\":\"TBZ\",\"CAM\":\"CAM\",\"CAL\":\"CAL\",\"CAN\":\"CAN\",\"CAQ\":\"CAQ\",\"TCB\":\"TCB\",\"CAP\":\"CAP\",\"TCA\":\"TCA\",\"CAS\":\"CAS\",\"TCD\":\"TCD\",\"TCC\":\"TCC\",\"TCE\":\"TCE\",\"CAW\":\"CAW\",\"TCH\":\"TCH\",\"TCG\":\"TCG\",\"CAY\":\"CAY\",\"KRB\":\"KRB\",\"KRA\":\"KRA\",\"TCI\":\"TCI\",\"TCL\":\"TCL\",\"CAZ\":\"CAZ\",\"KRC\":\"KRC\",\"KRF\":\"KRF\",\"TCN\":\"TCN\",\"TCP\":\"TCP\",\"TCO\":\"TCO\",\"CBB\":\"CBB\",\"TCR\":\"TCR\",\"CBA\":\"CBA\",\"KRI\":\"KRI\",\"TCQ\":\"TCQ\",\"TCT\":\"TCT\",\"KRL\":\"KRL\",\"KRK\":\"KRK\",\"CBF\":\"CBF\",\"KRN\":\"KRN\",\"TCV\":\"TET\",\"CBE\":\"CBE\",\"CBH\":\"CBH\",\"KRP\":\"KRP\",\"KRO\":\"KRO\",\"TCW\":\"TCW\",\"KRR\":\"KRR\",\"TCZ\":\"TCZ\",\"KRQ\":\"KRQ\",\"KRT\":\"KRT\",\"CBK\":\"CBK\",\"KRS\":\"KRS\",\"CBN\":\"CBN\",\"CBP\":\"CBP\",\"CBO\":\"CBO\",\"KRW\":\"KRW\",\"CBR\":\"CBR\",\"CBQ\":\"CBQ\",\"KRY\":\"KRY\",\"CBT\":\"CBT\",\"TDD\":\"TDD\",\"TDG\":\"TDG\",\"CBX\":\"CBX\",\"KSC\":\"KSC\",\"TDK\":\"TDK\",\"CBY\":\"CBY\",\"KSE\":\"KSE\",\"KSD\":\"KSD\",\"TDL\":\"TDL\",\"KSH\":\"KSH\",\"CCC\":\"CCC\",\"CCE\":\"SFG\",\"KSM\":\"KSM\",\"KSL\":\"KSL\",\"TDT\":\"TDT\",\"CCG\":\"CCG\",\"KSO\":\"KSO\",\"CCF\":\"CCF\",\"KSN\":\"KSN\",\"KSQ\":\"KSQ\",\"TDX\":\"TDX\",\"CCK\":\"CCK\",\"CCJ\":\"CCJ\",\"KSR\":\"KSR\",\"TDZ\":\"TOL\",\"CCM\":\"CCM\",\"KSU\":\"KSU\",\"CCL\":\"CCL\",\"KSW\":\"KSW\",\"KSY\":\"KSY\",\"TEB\":\"TEB\",\"CCP\":\"CCP\",\"TEA\":\"TEA\",\"CCS\":\"CCS\",\"KSZ\":\"KSZ\",\"TEC\":\"TEC\",\"CCU\":\"CCU\",\"CCT\":\"CCT\",\"TEE\":\"TEE\",\"CCW\":\"CCW\",\"TEH\":\"TEH\",\"CCV\":\"CCV\",\"CCY\":\"CCY\",\"KTB\":\"KTB\",\"CCX\":\"CCX\",\"KTA\":\"KTA\",\"KTD\":\"KTD\",\"CCZ\":\"CCZ\",\"TEK\":\"TEK\",\"KTF\":\"KTF\",\"TEN\":\"TEN\",\"KTE\":\"KTE\",\"TEM\":\"TEM\",\"TEP\":\"TEP\",\"KTG\":\"KTG\",\"TEO\":\"TEO\",\"CDB\":\"CDB\",\"TER\":\"TER\",\"KTL\":\"KTL\",\"TET\":\"TET\",\"CDC\":\"CDC\",\"CDF\":\"CDF\",\"KTN\":\"KTN\",\"KTM\":\"KTM\",\"TEU\":\"TEU\",\"TEX\":\"TEX\",\"CDG\":\"PAR\",\"CDJ\":\"CDJ\",\"TEZ\":\"TEZ\",\"CDI\":\"CDI\",\"TEY\":\"TEY\",\"CDL\":\"CDL\",\"KTT\":\"KTT\",\"KTS\":\"KTS\",\"KTV\":\"KTV\",\"KTW\":\"KTW\",\"CDR\":\"CDR\",\"CDQ\":\"CDQ\",\"CDV\":\"CDV\",\"TFF\":\"TFF\",\"KUA\":\"KUA\",\"TFI\":\"TFI\",\"CDW\":\"CDW\",\"CDY\":\"CDY\",\"KUD\":\"KUD\",\"KUF\":\"KUF\",\"TFN\":\"TCI\",\"CEA\":\"ICT\",\"KUI\":\"KUI\",\"KUH\":\"KUH\",\"CEC\":\"CEC\",\"KUK\":\"KUK\",\"TFS\":\"TCI\",\"CEB\":\"CEB\",\"CEE\":\"CEE\",\"KUM\":\"KUM\",\"CED\":\"CED\",\"KUL\":\"KUL\",\"KUO\":\"KUO\",\"KUN\":\"KUN\",\"CEI\":\"CEI\",\"KUQ\":\"KUQ\",\"CEH\":\"CEH\",\"CEK\":\"CEK\",\"KUS\":\"KUS\",\"CEJ\":\"CEJ\",\"CEM\":\"CEM\",\"KUU\":\"KUU\",\"KUT\":\"KUT\",\"CEO\":\"CEO\",\"KUW\":\"KUW\",\"CEN\":\"CEN\",\"KUV\":\"KUV\",\"CEQ\":\"CEQ\",\"KUY\":\"KUY\",\"CES\":\"CES\",\"TGD\":\"TGD\",\"CEU\":\"CEU\",\"TGF\":\"TGF\",\"TGE\":\"TGE\",\"TGH\":\"TGH\",\"TGG\":\"TGG\",\"CEY\":\"CEY\",\"TGJ\":\"TGJ\",\"CEX\":\"CEX\",\"KVA\":\"KVA\",\"TGI\":\"TGI\",\"KVD\":\"KVD\",\"CEZ\":\"CEZ\",\"KVC\":\"KVC\",\"TGN\":\"TGN\",\"KVE\":\"KVE\",\"TGM\":\"TGM\",\"KVG\":\"KVG\",\"TGO\":\"TGO\",\"CFB\":\"CFB\",\"TGR\":\"TGR\",\"CFA\":\"CFA\",\"CFD\":\"CFD\",\"TGT\":\"TGT\",\"KVL\":\"KVL\",\"CFC\":\"CFC\",\"KVK\":\"KVK\",\"TGV\":\"TGV\",\"CFE\":\"CFE\",\"TGU\":\"TGU\",\"CFG\":\"CFG\",\"TGZ\":\"TGZ\",\"CFI\":\"CFI\",\"CFK\":\"CFK\",\"CFN\":\"CFN\",\"KVU\":\"KVU\",\"CFP\":\"CFP\",\"KVX\":\"KVX\",\"CFR\":\"CFR\",\"THB\":\"THB\",\"THE\":\"THE\",\"CFS\":\"CFS\",\"THD\":\"THD\",\"THG\":\"THG\",\"CFU\":\"CFU\",\"THF\":\"BER\",\"KWA\":\"KWA\",\"THH\":\"THH\",\"THK\":\"THK\",\"KWE\":\"KWE\",\"THL\":\"THL\",\"KWG\":\"KWG\",\"THO\":\"THO\",\"THN\":\"THN\",\"KWI\":\"KWI\",\"THQ\":\"THQ\",\"THP\":\"THP\",\"KWK\":\"KWK\",\"THS\":\"THS\",\"CGB\":\"CGB\",\"KWJ\":\"KWJ\",\"KWM\":\"KWM\",\"CGE\":\"CGE\",\"CGD\":\"CGD\",\"KWL\":\"KWL\",\"KWN\":\"KWN\",\"CGI\":\"CGI\",\"CGH\":\"SAO\",\"CGK\":\"JKT\",\"CGJ\":\"CGJ\",\"THZ\":\"THZ\",\"CGM\":\"CGM\",\"KWU\":\"KWU\",\"KWT\":\"KWT\",\"CGO\":\"CGO\",\"CGN\":\"CGN\",\"KWY\":\"KWY\",\"CGQ\":\"CGQ\",\"CGP\":\"CGP\",\"TIA\":\"TIA\",\"TID\":\"TID\",\"CGR\":\"CGR\",\"TIC\":\"TIC\",\"CGU\":\"CGU\",\"TIF\":\"TIF\",\"TIE\":\"TIE\",\"TIH\":\"TIH\",\"CGV\":\"CGV\",\"CGY\":\"CGY\",\"TIJ\":\"TIJ\",\"CGZ\":\"CGZ\",\"TIN\":\"TIN\",\"TIM\":\"TIM\",\"TIP\":\"TIP\",\"CHB\":\"CHB\",\"TIR\":\"TIR\",\"CHA\":\"CHA\",\"TIQ\":\"TIQ\",\"CHC\":\"CHC\",\"KXK\":\"KXK\",\"CHF\":\"CHF\",\"TIV\":\"TIV\",\"TIU\":\"TIU\",\"CHH\":\"CHH\",\"TIW\":\"TIW\",\"CHG\":\"CHG\",\"TIZ\":\"TIZ\",\"CHI\":\"CHI\",\"TIY\":\"TIY\",\"CHM\":\"CHM\",\"CHP\":\"CHP\",\"TJA\":\"TJA\",\"CHO\":\"CHO\",\"CHR\":\"CHR\",\"CHQ\":\"CHQ\",\"TJB\":\"TJB\",\"CHT\":\"CHT\",\"CHS\":\"CHS\",\"CHV\":\"CHV\",\"TJG\":\"TJG\",\"CHU\":\"CHU\",\"CHX\":\"CHX\",\"KYA\":\"KYA\",\"CHW\":\"CHW\",\"TJK\":\"TJK\",\"CHY\":\"CHY\",\"TJM\":\"TJM\",\"KYD\":\"KYD\",\"TJN\":\"TJN\",\"CIA\":\"ROM\",\"TJQ\":\"TJQ\",\"CIC\":\"CIC\",\"KYK\":\"KYK\",\"TJS\":\"TJS\",\"CIB\":\"AVX\",\"CIE\":\"CIE\",\"CID\":\"CID\",\"KYL\":\"KYL\",\"CIF\":\"CIF\",\"KYP\":\"KYP\",\"CIH\":\"CIH\",\"CIK\":\"CIK\",\"CIJ\":\"CIJ\",\"KYU\":\"KYU\",\"CIL\":\"CIL\",\"CIN\":\"CIN\",\"CIP\":\"CIP\",\"TKA\":\"TKA\",\"CIS\":\"CIS\",\"TKD\":\"TKD\",\"CIU\":\"SSM\",\"CIT\":\"CIT\",\"TKE\":\"TKE\",\"CIW\":\"CIW\",\"CIV\":\"CIV\",\"TKG\":\"TKG\",\"CIY\":\"CIY\",\"TKJ\":\"TKJ\",\"CIX\":\"CIX\",\"TKI\":\"TKI\",\"TKK\":\"TKK\",\"KZF\":\"KZF\",\"TKN\":\"TKN\",\"KZH\":\"KZH\",\"TKP\":\"TKP\",\"CJB\":\"CJB\",\"CJA\":\"CJA\",\"KZI\":\"KZI\",\"TKQ\":\"TKQ\",\"TKT\":\"TKT\",\"CJC\":\"CJC\",\"TKS\":\"TKS\",\"KZN\":\"KZN\",\"TKV\":\"TKV\",\"TKU\":\"TKU\",\"TKX\":\"TKX\",\"KZO\":\"KZO\",\"CJJ\":\"CJJ\",\"CJI\":\"CJI\",\"CJL\":\"CJL\",\"KZS\":\"KZS\",\"CJM\":\"CJM\",\"TLC\":\"TLC\",\"CJT\":\"CJT\",\"TLE\":\"TLE\",\"CJS\":\"CJS\",\"TLD\":\"TLD\",\"TLG\":\"TLG\",\"CJU\":\"CJU\",\"TLF\":\"TLF\",\"TLI\":\"TLI\",\"TLH\":\"TLH\",\"TLM\":\"TLM\",\"TLL\":\"TLL\",\"TLN\":\"TLN\",\"TLQ\":\"TLQ\",\"CKC\":\"CKC\",\"TLS\":\"TLS\",\"CKB\":\"CKB\",\"CKE\":\"CKE\",\"CKD\":\"CKD\",\"TLT\":\"TLT\",\"CKG\":\"CKG\",\"TLV\":\"TLV\",\"CKI\":\"CKI\",\"TLZ\":\"TLZ\",\"CKN\":\"CKN\",\"TMA\":\"TMA\",\"CKS\":\"CKS\",\"CKR\":\"CKR\",\"TMC\":\"TMC\",\"TME\":\"TME\",\"TMH\":\"TMH\",\"TMG\":\"TMG\",\"CKY\":\"CKY\",\"TMJ\":\"TMJ\",\"CKX\":\"CKX\",\"TMI\":\"TMI\",\"TML\":\"TML\",\"TMK\":\"TMK\",\"CKZ\":\"CKZ\",\"TMM\":\"TMM\",\"TMP\":\"TMP\",\"TMO\":\"TMO\",\"TMR\":\"TMR\",\"CLA\":\"CLA\",\"CLD\":\"CLD\",\"TMT\":\"TMT\",\"CLC\":\"CLC\",\"TMS\":\"TMS\",\"CLE\":\"CLE\",\"TMU\":\"TMU\",\"CLH\":\"CLH\",\"TMX\":\"TMX\",\"TMW\":\"TMW\",\"CLJ\":\"CLJ\",\"CLL\":\"CLL\",\"CLN\":\"CLN\",\"CLM\":\"CLM\",\"CLP\":\"CLP\",\"TNA\":\"TNA\",\"CLO\":\"CLO\",\"CLR\":\"CLR\",\"CLQ\":\"CLQ\",\"CLT\":\"CLT\",\"TNE\":\"TNE\",\"CLS\":\"CLS\",\"CLV\":\"CLV\",\"TNG\":\"TNG\",\"CLU\":\"CLU\",\"CLX\":\"CLX\",\"TNH\":\"TNH\",\"CLZ\":\"CLZ\",\"TNK\":\"TNK\",\"CLY\":\"CLY\",\"TNJ\":\"TNJ\",\"TNL\":\"TNL\",\"TNO\":\"TNO\",\"TNN\":\"TNN\",\"CMA\":\"CMA\",\"TNP\":\"TNP\",\"TNS\":\"TNS\",\"CMB\":\"CMB\",\"TNR\":\"TNR\",\"CME\":\"CME\",\"CMD\":\"CMD\",\"CMG\":\"CMG\",\"CMF\":\"CMF\",\"CMI\":\"CMI\",\"CMH\":\"CMH\",\"TNX\":\"TNX\",\"CMK\":\"CMK\",\"CMJ\":\"CMJ\",\"CML\":\"CML\",\"CMO\":\"CMO\",\"CMN\":\"CAS\",\"CMQ\":\"CMQ\",\"TOB\":\"TOB\",\"TOD\":\"TOD\",\"CMR\":\"CMR\",\"TOC\":\"TOC\",\"CMU\":\"CMU\",\"TOF\":\"TOF\",\"CMT\":\"CMT\",\"TOE\":\"TOE\",\"CMW\":\"CMW\",\"TOH\":\"TOH\",\"CMV\":\"CMV\",\"TOG\":\"TOG\",\"CMY\":\"CMY\",\"CMX\":\"CMX\",\"TOL\":\"TOL\",\"TOK\":\"TOK\",\"TOM\":\"TOM\",\"CNB\":\"CNB\",\"CNA\":\"CNA\",\"CND\":\"CND\",\"CNC\":\"CNC\",\"TOS\":\"TOS\",\"CNF\":\"BHZ\",\"CNE\":\"CNE\",\"TOU\":\"TOU\",\"TOX\":\"TOX\",\"CNG\":\"CNG\",\"CNJ\":\"CNJ\",\"TOY\":\"TOY\",\"CNI\":\"CNI\",\"CNL\":\"CNL\",\"CNK\":\"CNK\",\"CNN\":\"CNN\",\"CNM\":\"CNM\",\"CNP\":\"CNP\",\"TPA\":\"TPA\",\"CNO\":\"CNO\",\"TPC\":\"TPC\",\"CNQ\":\"CNQ\",\"CNT\":\"CNT\",\"TPE\":\"TPE\",\"CNS\":\"CNS\",\"TPG\":\"TPG\",\"CNU\":\"CNU\",\"CNX\":\"CNX\",\"CNW\":\"ACT\",\"TPH\":\"TPH\",\"TPK\":\"TPK\",\"CNY\":\"CNY\",\"TPJ\":\"TPJ\",\"TPQ\":\"TPQ\",\"TPP\":\"TPP\",\"COC\":\"COC\",\"TPS\":\"TPS\",\"COB\":\"COB\",\"TPR\":\"TPR\",\"COE\":\"COE\",\"TPU\":\"TPU\",\"COD\":\"COD\",\"COG\":\"COG\",\"COI\":\"COI\",\"COK\":\"COK\",\"COJ\":\"COJ\",\"COM\":\"COM\",\"COL\":\"COL\",\"COO\":\"COO\",\"CON\":\"CON\",\"COQ\":\"COQ\",\"COS\":\"COS\",\"COR\":\"COR\",\"COU\":\"COU\",\"COV\":\"COV\",\"COY\":\"COY\",\"COX\":\"COX\",\"LAA\":\"LAA\",\"LAD\":\"LAD\",\"LAC\":\"LAC\",\"LAE\":\"LAE\",\"LAH\":\"LAH\",\"LAG\":\"LAG\",\"CPB\":\"CPB\",\"LAJ\":\"LAJ\",\"TQR\":\"TQR\",\"LAI\":\"LAI\",\"CPD\":\"CPD\",\"LAL\":\"LAL\",\"CPC\":\"CPC\",\"LAN\":\"LAN\",\"CPE\":\"CPE\",\"LAM\":\"LAM\",\"CPH\":\"CPH\",\"LAP\":\"LAP\",\"CPG\":\"CPG\",\"LAO\":\"LAO\",\"LAR\":\"LAR\",\"CPI\":\"CPI\",\"LAQ\":\"LAQ\",\"LAS\":\"LAS\",\"LAV\":\"LAV\",\"CPM\":\"CPM\",\"LAU\":\"LAU\",\"LAX\":\"LAX\",\"TRA\":\"TRA\",\"CPO\":\"CPO\",\"LAW\":\"LAW\",\"CPR\":\"CPR\",\"TRC\":\"TRC\",\"CPQ\":\"CPQ\",\"TRB\":\"TRB\",\"CPT\":\"CPT\",\"TRE\":\"TRE\",\"TRD\":\"TRD\",\"CPV\":\"CPV\",\"TRG\":\"TRG\",\"TRF\":\"OSL\",\"CPX\":\"CPX\",\"LBA\":\"LBA\",\"TRI\":\"TRI\",\"TRK\":\"TRK\",\"LBB\":\"LBB\",\"LBE\":\"LBE\",\"LBD\":\"LBD\",\"TRO\":\"TRO\",\"LBF\":\"LBF\",\"TRN\":\"TRN\",\"LBI\":\"LBI\",\"TRQ\":\"TRQ\",\"TRS\":\"TRS\",\"LBJ\":\"LBJ\",\"TRR\":\"TRR\",\"TRU\":\"TRU\",\"CQD\":\"CQD\",\"LBL\":\"LBL\",\"TRT\":\"TRT\",\"TRW\":\"TRW\",\"CQF\":\"CQF\",\"TRV\":\"TRV\",\"LBQ\":\"LBQ\",\"TRY\":\"TRY\",\"LBP\":\"LBP\",\"LBS\":\"LBS\",\"TRZ\":\"TRZ\",\"LBU\":\"LBU\",\"LBW\":\"LBW\",\"LBV\":\"LBV\",\"LBY\":\"LBY\",\"TSB\":\"TSB\",\"TSA\":\"TPE\",\"TSE\":\"TSE\",\"TSJ\":\"TSJ\",\"LCA\":\"LCA\",\"LCD\":\"LCD\",\"LCC\":\"LCC\",\"TSN\":\"TSN\",\"LCE\":\"LCE\",\"LCH\":\"LCH\",\"TSP\":\"TSP\",\"LCG\":\"LCG\",\"TSO\":\"ISC\",\"CRB\":\"CRB\",\"LCJ\":\"LCJ\",\"TSR\":\"TSR\",\"CRA\":\"CRA\",\"LCI\":\"LCI\",\"CRD\":\"CRD\",\"TST\":\"TST\",\"CRC\":\"CRC\",\"LCN\":\"LCN\",\"TSV\":\"TSV\",\"CRE\":\"MYR\",\"LCM\":\"LCM\",\"TSX\":\"TSX\",\"LCR\":\"LCR\",\"TSZ\":\"TSZ\",\"TSY\":\"TSY\",\"CRK\":\"CRK\",\"CRN\":\"CRN\",\"CRM\":\"CRM\",\"CRP\":\"CRP\",\"TTA\":\"TTA\",\"LCX\":\"LCX\",\"CRO\":\"CRO\",\"CRR\":\"CRR\",\"CRQ\":\"CRQ\",\"LCY\":\"LON\",\"TTB\":\"TTB\",\"CRT\":\"CRT\",\"TTE\":\"TTE\",\"CRS\":\"CRS\",\"CRV\":\"CRV\",\"TTG\":\"TTG\",\"CRX\":\"CRX\",\"CRW\":\"CRW\",\"CRZ\":\"CRZ\",\"LDC\":\"LDC\",\"TTK\":\"TTK\",\"CRY\":\"CRY\",\"LDB\":\"LDB\",\"TTJ\":\"TTJ\",\"LDE\":\"LDE\",\"TTL\":\"TTL\",\"TTN\":\"TTN\",\"LDI\":\"LDI\",\"TTQ\":\"TTQ\",\"LDH\":\"LDH\",\"LDK\":\"LDK\",\"TTS\":\"TTS\",\"CSB\":\"CSB\",\"LDJ\":\"LDJ\",\"TTR\":\"TTR\",\"CSE\":\"CSE\",\"TTU\":\"TTU\",\"TTT\":\"TTT\",\"CSG\":\"CSG\",\"LDN\":\"LDN\",\"CSI\":\"CSI\",\"CSK\":\"CSK\",\"LDS\":\"LDS\",\"LDR\":\"LDR\",\"LDU\":\"LDU\",\"CSN\":\"CSN\",\"CSQ\":\"CSQ\",\"LDY\":\"LDY\",\"TUB\":\"TUB\",\"TUA\":\"TUA\",\"TUD\":\"TUD\",\"LDZ\":\"LDZ\",\"TUF\":\"TUF\",\"CST\":\"CST\",\"CSV\":\"CSV\",\"TUG\":\"TUG\",\"CSY\":\"CSY\",\"LEB\":\"LEB\",\"TUJ\":\"TUJ\",\"LEA\":\"LEA\",\"TUI\":\"TUI\",\"CSX\":\"CSX\",\"LED\":\"LED\",\"TUL\":\"TUL\",\"LEC\":\"LEC\",\"TUK\":\"TUK\",\"TUN\":\"TUN\",\"LEE\":\"LEE\",\"TUM\":\"TUM\",\"LEH\":\"LEH\",\"TUP\":\"TUP\",\"TUO\":\"TUO\",\"CTB\":\"CTB\",\"LEJ\":\"LEJ\",\"TUR\":\"TUR\",\"CTA\":\"CTA\",\"LEI\":\"LEI\",\"LEL\":\"LEL\",\"CTC\":\"CTC\",\"TUS\":\"TUS\",\"LEN\":\"LEN\",\"TUV\":\"TUV\",\"LEM\":\"LEM\",\"TUU\":\"TUU\",\"CTH\":\"CTH\",\"CTG\":\"CTG\",\"LER\":\"LER\",\"TUZ\":\"TUZ\",\"LEQ\":\"LEQ\",\"CTL\":\"CTL\",\"LET\":\"LET\",\"CTN\":\"CTN\",\"CTM\":\"CTM\",\"LEU\":\"LEU\",\"LEX\":\"LEX\",\"TVA\":\"TVA\",\"CTO\":\"CTO\",\"TVC\":\"TVC\",\"CTQ\":\"CTQ\",\"CTT\":\"CTT\",\"CTS\":\"SPK\",\"TVF\":\"TVF\",\"CTU\":\"CTU\",\"CTX\":\"CTX\",\"CTW\":\"CTW\",\"CUC\":\"CUC\",\"LFK\":\"OCH\",\"TVS\":\"TVS\",\"CUE\":\"CUE\",\"LFM\":\"LFM\",\"TVU\":\"TVU\",\"CUG\":\"CUG\",\"LFO\":\"LFO\",\"CUF\":\"CUF\",\"TVY\":\"TVY\",\"CUK\":\"CUK\",\"LFR\":\"LFR\",\"CUL\":\"CUL\",\"LFT\":\"LFT\",\"LFW\":\"LFW\",\"CUN\":\"CUN\",\"CUQ\":\"CUQ\",\"TWB\":\"TWB\",\"TWA\":\"TWA\",\"TWD\":\"TWD\",\"CUR\":\"CUR\",\"CUU\":\"CUU\",\"TWF\":\"TWF\",\"CUT\":\"CUT\",\"TWE\":\"TWE\",\"CUW\":\"CUW\",\"CUV\":\"CUV\",\"CUY\":\"CUY\",\"LGB\":\"LGB\",\"LGA\":\"NYC\",\"CUZ\":\"CUZ\",\"LGC\":\"LGC\",\"LGH\":\"LGH\",\"TWP\":\"TWP\",\"LGG\":\"LGG\",\"LGI\":\"LGI\",\"LGL\":\"LGL\",\"TWT\":\"TWT\",\"CVC\":\"CVC\",\"LGK\":\"LGK\",\"CVF\":\"CVF\",\"TWU\":\"TWU\",\"CVH\":\"CVH\",\"LGP\":\"LGP\",\"CVG\":\"CVG\",\"CVJ\":\"CVJ\",\"TWZ\":\"MON\",\"CVI\":\"CVI\",\"LGQ\":\"LGQ\",\"CVL\":\"CVL\",\"LGS\":\"LGS\",\"CVN\":\"CVN\",\"CVM\":\"CVM\",\"LGU\":\"LGU\",\"LGX\":\"LGX\",\"LGW\":\"LON\",\"CVR\":\"CVR\",\"CVQ\":\"CVQ\",\"LGY\":\"LGY\",\"CVU\":\"CVU\",\"TXF\":\"TXF\",\"TXK\":\"TXK\",\"LHB\":\"LHB\",\"LHE\":\"LHE\",\"TXM\":\"TXM\",\"TXL\":\"BER\",\"LHG\":\"LHG\",\"TXN\":\"TXN\",\"CWA\":\"AUW\",\"LHI\":\"LHI\",\"CWC\":\"CWC\",\"CWB\":\"CWB\",\"TXR\":\"TXR\",\"CWI\":\"CWI\",\"LHS\":\"LHS\",\"LHR\":\"LON\",\"LHU\":\"LHU\",\"CWL\":\"CWL\",\"LHW\":\"LHW\",\"TYA\":\"TYA\",\"CWS\":\"CWS\",\"TYD\":\"TYD\",\"TYF\":\"TYF\",\"CWW\":\"CWW\",\"LIA\":\"LIA\",\"LID\":\"LID\",\"TYL\":\"TYL\",\"LIF\":\"LIF\",\"TYN\":\"TYN\",\"LIE\":\"LIE\",\"TYM\":\"TYM\",\"LIH\":\"LIH\",\"LIG\":\"LIG\",\"CXB\":\"CXB\",\"LIJ\":\"LIJ\",\"TYR\":\"TYR\",\"CXA\":\"CXA\",\"LII\":\"LII\",\"LIL\":\"LIL\",\"TYT\":\"TYT\",\"CXC\":\"CXC\",\"LIK\":\"LIK\",\"TYS\":\"TYS\",\"CXF\":\"CXF\",\"LIN\":\"MIL\",\"LIM\":\"LIM\",\"CXJ\":\"CXJ\",\"LIR\":\"LIR\",\"CXI\":\"CXI\",\"CXL\":\"CXL\",\"LIT\":\"LIT\",\"LIS\":\"LIS\",\"CXN\":\"CXN\",\"LIV\":\"LIV\",\"CXP\":\"CXP\",\"LIX\":\"LIX\",\"TZA\":\"BZE\",\"CXO\":\"CXO\",\"LIW\":\"LIW\",\"CXR\":\"NHA\",\"CXT\":\"CXT\",\"CXY\":\"CXY\",\"LJG\":\"LJG\",\"CYC\":\"CYC\",\"CYB\":\"CYB\",\"LJN\":\"LJN\",\"CYI\":\"CYI\",\"TZX\":\"TZX\",\"LJU\":\"LJU\",\"CYO\":\"CYO\",\"CYP\":\"CYP\",\"CYS\":\"CYS\",\"CYT\":\"CYT\",\"LKA\":\"LKA\",\"CYZ\":\"CYZ\",\"LKH\":\"LKH\",\"LKG\":\"LKG\",\"CZA\":\"CZA\",\"LKL\":\"LKL\",\"LKK\":\"LKK\",\"CZF\":\"CZF\",\"LKN\":\"LKN\",\"CZE\":\"CZE\",\"LKP\":\"LKP\",\"LKO\":\"LKO\",\"LKR\":\"LKR\",\"CZL\":\"CZL\",\"LKS\":\"LKS\",\"CZN\":\"CZN\",\"LKV\":\"LKV\",\"CZM\":\"CZM\",\"LKY\":\"LKY\",\"CZS\":\"CZS\",\"CZU\":\"CZU\",\"LLA\":\"LLA\",\"CZX\":\"CZX\",\"CZW\":\"CZW\",\"CZY\":\"CZY\",\"LLB\":\"LLB\",\"LLG\":\"LLG\",\"LLF\":\"LLF\",\"LLI\":\"LLI\",\"LLU\":\"LLU\",\"LLW\":\"LLW\",\"LLX\":\"LLX\",\"LMB\":\"LMB\",\"LMA\":\"LMA\",\"LMD\":\"LMD\",\"LMC\":\"LMC\",\"LME\":\"LME\",\"LMI\":\"LMI\",\"LMN\":\"LMN\",\"LMM\":\"LMM\",\"LMP\":\"LMP\",\"LMQ\":\"LMQ\",\"LMT\":\"LMT\",\"LNB\":\"LNB\",\"LNE\":\"LNE\",\"LND\":\"LND\",\"LNG\":\"LNG\",\"LNI\":\"LNI\",\"LNK\":\"LNK\",\"LNJ\":\"LNJ\",\"LNO\":\"LNO\",\"LNP\":\"LNP\",\"LNS\":\"LNS\",\"LNV\":\"LNV\",\"LNY\":\"LNY\",\"LNX\":\"LNX\",\"LNZ\":\"LNZ\",\"LOD\":\"LOD\",\"LOF\":\"LOF\",\"LOE\":\"LOE\",\"LOH\":\"LOH\",\"LOL\":\"LOL\",\"LOK\":\"LOK\",\"LOM\":\"LOM\",\"LOP\":\"LOP\",\"LOO\":\"LOO\",\"LOQ\":\"LOQ\",\"LOS\":\"LOS\",\"LPA\":\"LPA\",\"UAH\":\"UAH\",\"UAK\":\"UAK\",\"LPB\":\"LPB\",\"LPD\":\"LPD\",\"LPG\":\"LPG\",\"LPI\":\"LPI\",\"UAQ\":\"UAQ\",\"LPH\":\"LPH\",\"UAP\":\"UAP\",\"LPK\":\"LPK\",\"UAS\":\"UAS\",\"LPJ\":\"LPJ\",\"LPM\":\"LPM\",\"LPL\":\"LPL\",\"LPO\":\"LPO\",\"LPQ\":\"LPQ\",\"LPP\":\"LPP\",\"LPS\":\"LPS\",\"LPT\":\"LPT\",\"LPW\":\"LPW\",\"LPY\":\"LPY\",\"UBA\":\"UBA\",\"UBJ\":\"UBJ\",\"UBP\":\"UBP\",\"DAB\":\"DAB\",\"DAD\":\"DAD\",\"DAC\":\"DAC\",\"LQN\":\"LQN\",\"LQM\":\"LQM\",\"DAH\":\"DAH\",\"DAG\":\"DAG\",\"DAL\":\"DFW\",\"DAK\":\"DAK\",\"DAM\":\"DAM\",\"DAP\":\"DAP\",\"DAR\":\"DAR\",\"DAT\":\"DAT\",\"DAV\":\"DAV\",\"DAU\":\"DAU\",\"LRA\":\"LRA\",\"DAX\":\"DAX\",\"UCK\":\"UCK\",\"DAY\":\"DAY\",\"LRB\":\"LRB\",\"LRE\":\"LRE\",\"LRD\":\"LRD\",\"LRG\":\"LRG\",\"DBA\":\"DBA\",\"LRH\":\"LRH\",\"LRM\":\"LRM\",\"LRL\":\"LRL\",\"UCT\":\"UCT\",\"UCY\":\"UCY\",\"LRS\":\"LRS\",\"LRR\":\"LRR\",\"DBM\":\"DBM\",\"LRT\":\"LRT\",\"DBO\":\"DBO\",\"DBN\":\"DBN\",\"LRV\":\"LRV\",\"DBQ\":\"DBQ\",\"DBT\":\"DBT\",\"DBV\":\"DBV\",\"DBY\":\"DBY\",\"LSB\":\"LSB\",\"UDJ\":\"UDJ\",\"LSA\":\"LSA\",\"UDI\":\"UDI\",\"LSC\":\"LSC\",\"LSE\":\"LSE\",\"LSH\":\"LSH\",\"UDR\":\"UDR\",\"DCA\":\"WAS\",\"LSL\":\"LSL\",\"DCF\":\"DOM\",\"LSN\":\"LSN\",\"LSM\":\"LSM\",\"LSP\":\"LSP\",\"LSR\":\"LSR\",\"DCI\":\"DCI\",\"LST\":\"LST\",\"DCK\":\"DCK\",\"DCM\":\"DCM\",\"LSW\":\"LSW\",\"LSZ\":\"LSZ\",\"LSY\":\"LSY\",\"UEE\":\"UEE\",\"DCY\":\"DCY\",\"LTD\":\"LTD\",\"UEL\":\"UEL\",\"UEO\":\"UEO\",\"LTI\":\"LTI\",\"DDC\":\"DDC\",\"LTK\":\"LTK\",\"LTL\":\"LTL\",\"UET\":\"UET\",\"LTO\":\"LTO\",\"DDG\":\"DDG\",\"LTN\":\"LON\",\"DDI\":\"DDI\",\"LTQ\":\"LTQ\",\"LTT\":\"LTT\",\"LTW\":\"LTW\",\"DDN\":\"DDN\",\"DDP\":\"DDP\",\"LTX\":\"LTX\",\"UFA\":\"UFA\",\"LUD\":\"LUD\",\"LUH\":\"LUH\",\"LUG\":\"LUG\",\"DEB\":\"DEB\",\"LUJ\":\"LUJ\",\"DEA\":\"DEA\",\"DED\":\"DED\",\"DEC\":\"DEC\",\"LUN\":\"LUN\",\"LUM\":\"LUM\",\"DEH\":\"DEH\",\"LUP\":\"LUP\",\"LUO\":\"LUO\",\"LUQ\":\"LUQ\",\"DEL\":\"DEL\",\"DEN\":\"DEN\",\"LUV\":\"LUV\",\"LUU\":\"LUU\",\"LUX\":\"LUX\",\"LUW\":\"LUW\",\"UGC\":\"UGC\",\"UGB\":\"PIP\",\"UGI\":\"UGI\",\"DEZ\":\"DEZ\",\"LVB\":\"LVB\",\"LVD\":\"LVD\",\"UGO\":\"UGO\",\"UGN\":\"UGN\",\"LVI\":\"LVI\",\"LVK\":\"LVK\",\"LVO\":\"LVO\",\"LVS\":\"LVS\",\"DFP\":\"DFP\",\"DFW\":\"DFW\",\"LWB\":\"LWB\",\"LWE\":\"LWE\",\"LWL\":\"LWL\",\"DGF\":\"DGF\",\"LWN\":\"LWN\",\"DGE\":\"DGE\",\"LWM\":\"LWM\",\"LWO\":\"LWO\",\"LWR\":\"LWR\",\"LWT\":\"LWT\",\"LWS\":\"LWS\",\"LWV\":\"LWV\",\"DGO\":\"DGO\",\"DGR\":\"DGR\",\"LWY\":\"LWY\",\"UIB\":\"UIB\",\"DGT\":\"DGT\",\"DGU\":\"DGU\",\"UII\":\"UII\",\"LXA\":\"LXA\",\"DGW\":\"DGW\",\"UIH\":\"UIH\",\"UIK\":\"UIK\",\"UIL\":\"UIL\",\"LXG\":\"LXG\",\"UIO\":\"UIO\",\"UIN\":\"UIN\",\"UIQ\":\"UIQ\",\"UIP\":\"UIP\",\"DHD\":\"DHD\",\"UIT\":\"UIT\",\"DHI\":\"DHI\",\"LXS\":\"LXS\",\"LXR\":\"LXR\",\"DHM\":\"DHM\",\"LXU\":\"LXU\",\"DHL\":\"DHL\",\"DHN\":\"DHN\",\"LXV\":\"LXV\",\"UJE\":\"UJE\",\"LYB\":\"LYB\",\"LYA\":\"LYA\",\"LYC\":\"LYC\",\"LYH\":\"LYH\",\"LYG\":\"LYG\",\"DIB\":\"DIB\",\"LYI\":\"LYI\",\"LYK\":\"LYK\",\"DIE\":\"DIE\",\"LYP\":\"LYP\",\"DIG\":\"DIG\",\"DIJ\":\"DIJ\",\"LYR\":\"LYR\",\"DIL\":\"DIL\",\"DIK\":\"DIK\",\"LYS\":\"LYS\",\"DIN\":\"DIN\",\"LYX\":\"LYX\",\"DIO\":\"DIO\",\"DIR\":\"DIR\",\"DIQ\":\"DIQ\",\"UKB\":\"UKB\",\"DIS\":\"DIS\",\"DIU\":\"DIU\",\"LZC\":\"LZC\",\"UKK\":\"UKK\",\"DIY\":\"DIY\",\"LZH\":\"LZH\",\"UKS\":\"UKS\",\"DJB\":\"DJB\",\"UKR\":\"UKR\",\"DJE\":\"DJE\",\"UKT\":\"UKT\",\"DJG\":\"DJG\",\"LZO\":\"LZO\",\"UKY\":\"UKY\",\"DJJ\":\"DJJ\",\"LZR\":\"LZR\",\"DJM\":\"DJM\",\"DJN\":\"DJN\",\"ULB\":\"ULB\",\"LZY\":\"LZY\",\"ULA\":\"ULA\",\"ULD\":\"ULD\",\"ULE\":\"ULE\",\"ULG\":\"ULG\",\"ULI\":\"ULI\",\"ULL\":\"ULL\",\"ULN\":\"ULN\",\"ULM\":\"ULM\",\"ULP\":\"ULP\",\"ULV\":\"ULV\",\"ULU\":\"ULU\",\"DKI\":\"DKI\",\"ULY\":\"ULY\",\"DKR\":\"DKR\",\"UMB\":\"UMB\",\"UME\":\"UME\",\"DKS\":\"DKS\",\"UMD\":\"UMD\",\"UMI\":\"UMI\",\"DLA\":\"DLA\",\"DLC\":\"DLC\",\"DLE\":\"DLE\",\"UMU\":\"UMU\",\"DLD\":\"DLD\",\"UMT\":\"UMT\",\"DLG\":\"DLG\",\"DLI\":\"DLI\",\"UMY\":\"UMY\",\"DLH\":\"DLH\",\"DLK\":\"DLK\",\"DLM\":\"DLM\",\"DLL\":\"DLL\",\"DLO\":\"DLO\",\"UNA\":\"UNA\",\"DLS\":\"DLS\",\"UND\":\"UND\",\"DLU\":\"DLU\",\"UNG\":\"UNG\",\"DLY\":\"DLY\",\"UNI\":\"UNI\",\"DLZ\":\"DLZ\",\"UNK\":\"UNK\",\"UNN\":\"UNN\",\"DMB\":\"DMB\",\"DMD\":\"DMD\",\"UNS\":\"UMB\",\"DME\":\"MOW\",\"DMK\":\"BKK\",\"DMM\":\"DMM\",\"DMO\":\"DMO\",\"DMR\":\"DMR\",\"DMU\":\"DMU\",\"UOL\":\"UOL\",\"DNB\":\"DNB\",\"DND\":\"DND\",\"DNF\":\"DNF\",\"DNH\":\"DNH\",\"DNK\":\"DNK\",\"DNL\":\"AGS\",\"DNN\":\"DNN\",\"DNQ\":\"DNQ\",\"DNS\":\"DNS\",\"DNR\":\"DNR\",\"UPC\":\"UPC\",\"UPF\":\"UPF\",\"UPG\":\"UPG\",\"DNZ\":\"DNZ\",\"UPN\":\"UPN\",\"UPP\":\"UPP\",\"DOA\":\"DOA\",\"DOD\":\"DOD\",\"DOC\":\"DOC\",\"DOF\":\"DOF\",\"DOH\":\"DOH\",\"DOG\":\"DOG\",\"DOK\":\"DOK\",\"DOM\":\"DOM\",\"DOP\":\"DOP\",\"DOR\":\"DOR\",\"UQE\":\"UQE\",\"DOU\":\"DOU\",\"DOX\":\"DOX\",\"MAA\":\"MAA\",\"MAB\":\"MAB\",\"DOY\":\"DOY\",\"MAD\":\"MAD\",\"MAG\":\"MAG\",\"MAF\":\"MAF\",\"MAH\":\"MAH\",\"MAK\":\"MAK\",\"MAJ\":\"MAJ\",\"MAM\":\"MAM\",\"MAL\":\"MAL\",\"MAO\":\"MAO\",\"MAN\":\"MAN\",\"MAQ\":\"MAQ\",\"DPK\":\"DPK\",\"MAS\":\"MAS\",\"MAR\":\"MAR\",\"MAU\":\"MAU\",\"DPL\":\"DPL\",\"DPO\":\"DPO\",\"MAW\":\"MAW\",\"MAV\":\"MAV\",\"URA\":\"URA\",\"DPS\":\"DPS\",\"MAZ\":\"MAZ\",\"URC\":\"URC\",\"URE\":\"URE\",\"URG\":\"URG\",\"URJ\":\"URJ\",\"MBA\":\"MBA\",\"MBD\":\"MBD\",\"MBC\":\"MBC\",\"MBE\":\"MBE\",\"URM\":\"URM\",\"MBH\":\"MBH\",\"URO\":\"URO\",\"URR\":\"URR\",\"MBJ\":\"MBJ\",\"MBI\":\"MBI\",\"DQA\":\"DQA\",\"MBL\":\"MBL\",\"URT\":\"URT\",\"URS\":\"URS\",\"MBP\":\"MBP\",\"MBO\":\"MBO\",\"MBQ\":\"MBQ\",\"URY\":\"URY\",\"MBT\":\"MBT\",\"MBS\":\"MBS\",\"MBU\":\"MBU\",\"MBX\":\"MBX\",\"USH\":\"USH\",\"USK\":\"USK\",\"MCB\":\"MCB\",\"MCE\":\"MCE\",\"USM\":\"USM\",\"MCD\":\"MCD\",\"USN\":\"USN\",\"MCI\":\"MKC\",\"USQ\":\"USQ\",\"MCH\":\"MCH\",\"MCK\":\"MCK\",\"MCJ\":\"MCJ\",\"DRE\":\"DRE\",\"USU\":\"USU\",\"MCL\":\"MCL\",\"UST\":\"UST\",\"MCO\":\"ORL\",\"DRF\":\"DRF\",\"MCQ\":\"MCQ\",\"MCP\":\"MCP\",\"MCS\":\"MCS\",\"MCU\":\"MCU\",\"MCT\":\"MCT\",\"DRO\":\"DRO\",\"MCW\":\"MCW\",\"DRN\":\"DRN\",\"MCV\":\"MCV\",\"MCY\":\"MCY\",\"MCX\":\"MCX\",\"UTA\":\"UTA\",\"DRS\":\"DRS\",\"UTD\":\"UTD\",\"DRR\":\"DRR\",\"MCZ\":\"MCZ\",\"DRT\":\"DRT\",\"UTE\":\"UTE\",\"DRW\":\"DRW\",\"UTH\":\"UTH\",\"MDB\":\"MDB\",\"UTL\":\"UTL\",\"MDC\":\"MDC\",\"UTK\":\"UTK\",\"UTN\":\"UTN\",\"MDE\":\"MDE\",\"UTP\":\"UTP\",\"MDG\":\"MDG\",\"UTR\":\"UTR\",\"DSA\":\"DSA\",\"MDI\":\"MDI\",\"DSD\":\"DSD\",\"MDL\":\"MDL\",\"UTT\":\"UTT\",\"MDK\":\"MDK\",\"DSE\":\"DSE\",\"MDP\":\"MDP\",\"MDO\":\"MDO\",\"MDR\":\"MDR\",\"MDQ\":\"MDQ\",\"MDT\":\"HAR\",\"MDS\":\"MDS\",\"DSN\":\"DSN\",\"DSM\":\"DSM\",\"MDU\":\"MDU\",\"MDX\":\"MDX\",\"UUA\":\"UUA\",\"MDW\":\"CHI\",\"MDZ\":\"MDZ\",\"MDY\":\"MDY\",\"UUD\":\"UUD\",\"MEA\":\"MEA\",\"MEC\":\"MEC\",\"MEE\":\"MEE\",\"MED\":\"MED\",\"MEG\":\"MEG\",\"DTA\":\"DTA\",\"MEI\":\"MEI\",\"MEH\":\"MEH\",\"MEK\":\"MEK\",\"UUS\":\"UUS\",\"MEJ\":\"MEJ\",\"DTE\":\"DTE\",\"MEM\":\"MEM\",\"MEL\":\"MEL\",\"MEO\":\"MEO\",\"MEN\":\"MEN\",\"DTH\":\"DTH\",\"MEP\":\"MEP\",\"MES\":\"MES\",\"DTM\":\"DTM\",\"MEU\":\"MEU\",\"DTL\":\"DTL\",\"DTN\":\"SHV\",\"MEV\":\"MEV\",\"MEX\":\"MEX\",\"UVA\":\"UVA\",\"DTR\":\"DTR\",\"UVF\":\"SLU\",\"UVE\":\"UVE\",\"DTW\":\"DTT\",\"MFA\":\"MFA\",\"MFD\":\"MFD\",\"UVL\":\"UVL\",\"MFF\":\"MFF\",\"MFE\":\"MFE\",\"MFH\":\"MFH\",\"MFG\":\"MFG\",\"UVO\":\"UVO\",\"DUB\":\"DUB\",\"MFI\":\"MFI\",\"DUD\":\"DUD\",\"MFK\":\"MFK\",\"MFN\":\"MFN\",\"DUE\":\"DUE\",\"MFM\":\"MFM\",\"MFO\":\"MFO\",\"DUJ\":\"DUJ\",\"MFR\":\"MFR\",\"MFQ\":\"MFQ\",\"MFT\":\"MFT\",\"DUM\":\"DUM\",\"MFU\":\"MFU\",\"MFW\":\"MFW\",\"DUR\":\"DUR\",\"MFZ\":\"MFZ\",\"MFY\":\"MFY\",\"DUT\":\"DUT\",\"DUS\":\"DUS\",\"MGA\":\"MGA\",\"MGC\":\"MGC\",\"MGB\":\"MGB\",\"MGD\":\"MGD\",\"MGF\":\"MGF\",\"DVA\":\"DVA\",\"MGH\":\"MGH\",\"MGM\":\"MGM\",\"MGN\":\"MGN\",\"MGQ\":\"MGQ\",\"MGS\":\"MGS\",\"MGR\":\"MGR\",\"DVL\":\"DVL\",\"MGT\":\"MGT\",\"DVO\":\"DVO\",\"MGW\":\"MGW\",\"DVN\":\"DVN\",\"MGV\":\"MGV\",\"MGX\":\"MGX\",\"DVR\":\"DVR\",\"MGZ\":\"MGZ\",\"MHD\":\"MHD\",\"MHH\":\"MHH\",\"MHG\":\"MHG\",\"DWB\":\"DWB\",\"MHJ\":\"MHJ\",\"DWD\":\"DWD\",\"DWC\":\"DXB\",\"MHK\":\"MHK\",\"MHO\":\"MHO\",\"MHQ\":\"MHQ\",\"MHT\":\"MHT\",\"MHV\":\"MHV\",\"MHU\":\"MHU\",\"MHX\":\"MHX\",\"MHZ\":\"MHZ\",\"MIA\":\"MIA\",\"MID\":\"MID\",\"UYL\":\"UYL\",\"MIG\":\"MIG\",\"MIF\":\"MIF\",\"UYN\":\"UYN\",\"MII\":\"MII\",\"MIK\":\"MIK\",\"MIJ\":\"MIJ\",\"DXB\":\"DXB\",\"MIM\":\"MIM\",\"MIS\":\"MIS\",\"MIR\":\"MIR\",\"MIU\":\"MIU\",\"MIW\":\"MIW\",\"MIV\":\"MIV\",\"DXR\":\"DXR\",\"MJB\":\"MJB\",\"MJA\":\"MJA\",\"MJD\":\"MJD\",\"MJC\":\"MJC\",\"MJF\":\"MJF\",\"MJE\":\"MJE\",\"DYA\":\"DYA\",\"MJL\":\"MJL\",\"MJK\":\"MJK\",\"MJN\":\"MJN\",\"MJM\":\"MJM\",\"UZU\":\"UZU\",\"MJP\":\"MJP\",\"MJO\":\"MJO\",\"DYG\":\"DYG\",\"DYL\":\"DYL\",\"MJT\":\"MJT\",\"MJV\":\"MJV\",\"MJU\":\"MJU\",\"DYR\":\"DYR\",\"MJZ\":\"MJZ\",\"DYU\":\"DYU\",\"DYW\":\"DYW\",\"MKB\":\"MKB\",\"MKE\":\"MKE\",\"MKG\":\"MKG\",\"DZA\":\"DZA\",\"MKK\":\"MKK\",\"MKJ\":\"MKJ\",\"MKM\":\"MKM\",\"MKL\":\"MKL\",\"MKO\":\"MKO\",\"MKN\":\"MKN\",\"MKQ\":\"MKQ\",\"MKP\":\"MKP\",\"MKS\":\"MKS\",\"MKR\":\"MKR\",\"MKU\":\"MKU\",\"MKT\":\"MKT\",\"DZO\":\"DZO\",\"MKW\":\"MKW\",\"DZN\":\"DZN\",\"MKY\":\"MKY\",\"MKX\":\"MKX\",\"MKZ\":\"MKZ\",\"MLB\":\"MLB\",\"MLA\":\"MLA\",\"MLC\":\"MLC\",\"MLF\":\"MLF\",\"MLE\":\"MLE\",\"MLG\":\"MLG\",\"MLJ\":\"MLJ\",\"MLI\":\"MLI\",\"MLN\":\"MLN\",\"MLM\":\"MLM\",\"MLP\":\"MLP\",\"MLO\":\"MLO\",\"MLQ\":\"MLQ\",\"MLS\":\"MLS\",\"MLU\":\"MLU\",\"MLX\":\"MLX\",\"MLZ\":\"MLZ\",\"MLY\":\"MLY\",\"MMB\":\"MMB\",\"MME\":\"MME\",\"MMD\":\"MMD\",\"MMG\":\"MMG\",\"MMH\":\"MMH\",\"MMK\":\"MMK\",\"MMJ\":\"MMJ\",\"MML\":\"MML\",\"MMO\":\"MMO\",\"MMN\":\"MMN\",\"MMQ\":\"MMQ\",\"MMP\":\"MMP\",\"MMU\":\"MMU\",\"MMY\":\"MMY\",\"MMX\":\"MMA\",\"MMZ\":\"MMZ\",\"MNA\":\"MNA\",\"MNF\":\"MNF\",\"MNH\":\"MNH\",\"MNG\":\"MNG\",\"MNJ\":\"MNJ\",\"MNI\":\"MNI\",\"MNL\":\"MNL\",\"MNK\":\"MNK\",\"MNR\":\"MNR\",\"MNT\":\"MNT\",\"MNS\":\"MNS\",\"MNU\":\"MNU\",\"MNX\":\"MNX\",\"MNZ\":\"MNZ\",\"MNY\":\"MNY\",\"MOA\":\"MOA\",\"MOC\":\"MOC\",\"MOB\":\"MOB\",\"MOD\":\"MOD\",\"MOG\":\"MOG\",\"MOF\":\"MOF\",\"MOI\":\"MOI\",\"MOL\":\"MOL\",\"MOQ\":\"MOQ\",\"MOS\":\"MOS\",\"MOU\":\"MOU\",\"MOT\":\"MOT\",\"MOV\":\"MOV\",\"VAA\":\"VAA\",\"MOZ\":\"MOZ\",\"VAG\":\"VAG\",\"VAI\":\"VAI\",\"MPD\":\"MPD\",\"VAL\":\"VAL\",\"VAK\":\"VAK\",\"VAN\":\"VAN\",\"MPH\":\"MPH\",\"VAO\":\"VAO\",\"VAR\":\"VAR\",\"MPL\":\"MPL\",\"VAT\":\"VAT\",\"MPK\":\"MPK\",\"VAS\":\"VAS\",\"MPN\":\"MPN\",\"VAV\":\"VAV\",\"MPM\":\"MPM\",\"MPO\":\"MPO\",\"VAW\":\"VAW\",\"MPR\":\"MPR\",\"MPT\":\"MPT\",\"MPV\":\"MPV\",\"MPU\":\"MPU\",\"MPW\":\"MPW\",\"MQB\":\"MQB\",\"MQD\":\"MQD\",\"MQF\":\"MQF\",\"EAA\":\"EAA\",\"MQH\":\"MQH\",\"EAB\":\"EAB\",\"MQJ\":\"BZI\",\"EAE\":\"EAE\",\"MQM\":\"MQM\",\"MQL\":\"MQL\",\"MQN\":\"MQN\",\"VBY\":\"VBY\",\"MQP\":\"NLP\",\"MQS\":\"MQS\",\"EAM\":\"EAM\",\"MQT\":\"MQT\",\"EAN\":\"EAN\",\"VCB\":\"VCB\",\"MQX\":\"MQX\",\"VCA\":\"VCA\",\"EAS\":\"EAS\",\"VCD\":\"VCD\",\"EAR\":\"EAR\",\"MQZ\":\"MQZ\",\"EAU\":\"EAU\",\"VCF\":\"VCF\",\"EAT\":\"EAT\",\"VCE\":\"VCE\",\"VCH\":\"VCH\",\"MRB\":\"MRB\",\"MRA\":\"MRA\",\"VCL\":\"VCL\",\"MRE\":\"MRE\",\"VCP\":\"SAO\",\"EBB\":\"EBB\",\"VCR\":\"VCR\",\"EBD\":\"EBD\",\"VCT\":\"VCT\",\"VCS\":\"VCS\",\"EBG\":\"EBG\",\"MRO\":\"MRO\",\"EBJ\":\"EBJ\",\"MRR\":\"MRR\",\"MRQ\":\"MRQ\",\"EBL\":\"EBL\",\"MRT\":\"MRT\",\"MRS\":\"MRS\",\"EBN\":\"EBN\",\"MRV\":\"MRV\",\"MRU\":\"MRU\",\"MRX\":\"MRX\",\"VDA\":\"VDA\",\"EBO\":\"EBO\",\"MRW\":\"MRW\",\"MRZ\":\"MRZ\",\"VDC\":\"VDC\",\"MRY\":\"MRY\",\"VDB\":\"VDB\",\"VDE\":\"VDE\",\"EBU\":\"EBU\",\"MSA\":\"MSA\",\"VDH\":\"VDH\",\"MSE\":\"MSE\",\"VDM\":\"VDM\",\"MSF\":\"MSF\",\"MSH\":\"MSH\",\"VDP\":\"VDP\",\"VDS\":\"VDS\",\"MSJ\":\"MSJ\",\"VDR\":\"VDR\",\"MSL\":\"MSL\",\"ECG\":\"ECG\",\"MSO\":\"MSO\",\"MSN\":\"MSN\",\"MSQ\":\"MSQ\",\"MSP\":\"MSP\",\"MSS\":\"MSS\",\"MSR\":\"MSR\",\"VDZ\":\"VDZ\",\"MSU\":\"MSU\",\"MSW\":\"MSW\",\"ECN\":\"ECN\",\"MSY\":\"MSY\",\"ECS\":\"ECS\",\"MSZ\":\"MSZ\",\"VEE\":\"VEE\",\"MTA\":\"MTA\",\"VEL\":\"VEL\",\"MTF\":\"MTF\",\"EDB\":\"EDB\",\"MTJ\":\"MTJ\",\"VER\":\"VER\",\"EDA\":\"EDA\",\"MTI\":\"MTI\",\"MTL\":\"MTL\",\"VEV\":\"VEV\",\"MTP\":\"MTP\",\"VEX\":\"VEX\",\"MTO\":\"MTO\",\"MTR\":\"MTR\",\"EDI\":\"EDI\",\"EDL\":\"EDL\",\"MTT\":\"MTT\",\"MTS\":\"MTS\",\"MTV\":\"MTV\",\"VFA\":\"VFA\",\"EDO\":\"EDO\",\"MTW\":\"MTW\",\"EDR\":\"EDR\",\"MTY\":\"MTY\",\"MUA\":\"MUA\",\"MUC\":\"MUC\",\"MUB\":\"MUB\",\"MUE\":\"MUE\",\"MUG\":\"MUG\",\"MUH\":\"MUH\",\"MUK\":\"MUK\",\"MUJ\":\"MUJ\",\"MUL\":\"MGR\",\"MUN\":\"MUN\",\"EEK\":\"EEK\",\"MUR\":\"MUR\",\"MUT\":\"MUT\",\"MUW\":\"MUW\",\"MUX\":\"MUX\",\"VGA\":\"VGA\",\"VGD\":\"VGD\",\"MUZ\":\"MUZ\",\"MVB\":\"MVB\",\"MVA\":\"MVA\",\"MVD\":\"MVD\",\"MVF\":\"MVF\",\"MVH\":\"MVH\",\"VGO\":\"VGO\",\"EFD\":\"HOU\",\"MVL\":\"MVL\",\"VGS\":\"VGS\",\"MVM\":\"MVM\",\"MVP\":\"MVP\",\"MVR\":\"MVR\",\"VGZ\":\"VGZ\",\"EFL\":\"EFL\",\"MVT\":\"MVT\",\"MVS\":\"MVS\",\"MVV\":\"MVV\",\"MVX\":\"MVX\",\"MVW\":\"MVW\",\"MVZ\":\"MVZ\",\"VHC\":\"VHC\",\"MWA\":\"MWA\",\"MWE\":\"MWE\",\"VHM\":\"VHM\",\"MWD\":\"MWD\",\"MWF\":\"MWF\",\"VHN\":\"VHN\",\"EGA\":\"EGA\",\"EGC\":\"EGC\",\"MWK\":\"MWK\",\"EGE\":\"EGE\",\"MWL\":\"MWL\",\"MWO\":\"MWO\",\"EGI\":\"VPS\",\"MWQ\":\"MWQ\",\"VHZ\":\"VHZ\",\"EGM\":\"EGM\",\"MWU\":\"MWU\",\"EGL\":\"EGL\",\"EGO\":\"EGO\",\"EGN\":\"EGN\",\"MWV\":\"MWV\",\"EGP\":\"EGP\",\"MWX\":\"MWX\",\"EGS\":\"EGS\",\"VID\":\"VID\",\"MWZ\":\"MWZ\",\"VIF\":\"VIF\",\"VIE\":\"VIE\",\"EGV\":\"EGV\",\"VIG\":\"VIG\",\"MXB\":\"MXB\",\"VIJ\":\"VIJ\",\"EGX\":\"EGX\",\"VII\":\"VII\",\"VIL\":\"VIL\",\"MXC\":\"MXC\",\"VIN\":\"VIN\",\"MXH\":\"MXH\",\"MXJ\":\"MXJ\",\"MXI\":\"MXI\",\"MXL\":\"MXL\",\"VIS\":\"VIS\",\"MXN\":\"MXN\",\"VIV\":\"VIV\",\"MXM\":\"MXM\",\"VIU\":\"VIU\",\"MXP\":\"MIL\",\"VIX\":\"VIX\",\"EHL\":\"EHL\",\"MXT\":\"MXT\",\"MXS\":\"MXS\",\"EHM\":\"EHM\",\"MXX\":\"MXX\",\"MXW\":\"MXW\",\"MXZ\":\"MXZ\",\"MXY\":\"MXY\",\"EHT\":\"EHT\",\"MYA\":\"MYA\",\"VJI\":\"VJI\",\"MYC\":\"MYC\",\"MYB\":\"MYB\",\"MYE\":\"MYE\",\"MYD\":\"MYD\",\"MYG\":\"MYG\",\"MYH\":\"MYH\",\"MYK\":\"MYK\",\"MYJ\":\"MYJ\",\"MYL\":\"MYL\",\"MYN\":\"MYN\",\"MYQ\":\"MYQ\",\"MYP\":\"MYP\",\"MYU\":\"MYU\",\"MYT\":\"MYT\",\"MYW\":\"MYW\",\"EIN\":\"EIN\",\"MYY\":\"MYY\",\"EIS\":\"EIS\",\"MYZ\":\"MYZ\",\"VKG\":\"VKG\",\"MZC\":\"MZC\",\"MZE\":\"MZE\",\"MZH\":\"MZH\",\"MZG\":\"MZG\",\"VKO\":\"MOW\",\"EJA\":\"EJA\",\"MZI\":\"MZI\",\"MZL\":\"MZL\",\"VKT\":\"VKT\",\"EJH\":\"EJH\",\"MZP\":\"MZP\",\"MZO\":\"MZO\",\"MZR\":\"MZR\",\"MZT\":\"MZT\",\"MZV\":\"MZV\",\"EJN\":\"EJN\",\"MZX\":\"MZX\",\"VLA\":\"VLA\",\"VLC\":\"VLC\",\"VLD\":\"VLD\",\"VLI\":\"VLI\",\"VLK\":\"VLK\",\"VLL\":\"VLL\",\"VLO\":\"VLO\",\"VLN\":\"VLN\",\"VLP\":\"VLP\",\"VLS\":\"VLS\",\"EKB\":\"EKB\",\"VLU\":\"VLU\",\"VLV\":\"VLV\",\"EKI\":\"EKI\",\"EKO\":\"EKO\",\"EKN\":\"EKN\",\"VME\":\"VME\",\"EKX\":\"EKX\",\"VMI\":\"VMI\",\"ELA\":\"ELA\",\"ELD\":\"ELD\",\"ELC\":\"ELC\",\"VMU\":\"VMU\",\"ELH\":\"ELH\",\"ELG\":\"ELG\",\"ELL\":\"ELL\",\"ELK\":\"ELK\",\"ELN\":\"ELN\",\"ELM\":\"ELM\",\"ELP\":\"ELP\",\"VNA\":\"VNA\",\"ELO\":\"ELO\",\"ELQ\":\"ELQ\",\"ELT\":\"ELT\",\"ELS\":\"ELS\",\"ELU\":\"ELU\",\"ELY\":\"ELY\",\"VNO\":\"VNO\",\"EMA\":\"NQT\",\"VNS\":\"VNS\",\"VNR\":\"VNR\",\"EME\":\"EME\",\"EMD\":\"EMD\",\"EMI\":\"EMI\",\"VNX\":\"VNX\",\"EMK\":\"EMK\",\"EMM\":\"EMM\",\"EMN\":\"EMN\",\"EMP\":\"EMP\",\"EMT\":\"EMT\",\"VOH\":\"VOH\",\"VOG\":\"VOG\",\"EMY\":\"EMY\",\"EMX\":\"EMX\",\"VOL\":\"VOL\",\"ENA\":\"ENA\",\"ENF\":\"ENF\",\"ENE\":\"ENE\",\"ENH\":\"ENH\",\"VOZ\":\"VOZ\",\"ENK\":\"ENK\",\"ENN\":\"ENN\",\"ENT\":\"ENT\",\"VPE\":\"VPE\",\"ENV\":\"ENV\",\"ENU\":\"ENU\",\"ENW\":\"ENW\",\"ENY\":\"ENY\",\"VPN\":\"VPN\",\"VPS\":\"VPS\",\"EOI\":\"EOI\",\"VPY\":\"VPY\",\"EOH\":\"MDE\",\"EOK\":\"EOK\",\"NAA\":\"NAA\",\"EOZ\":\"EOZ\",\"NAC\":\"NAC\",\"NAG\":\"NAG\",\"NAJ\":\"NAJ\",\"NAL\":\"NAL\",\"VQS\":\"VQS\",\"NAN\":\"NAN\",\"NAM\":\"NAM\",\"EPH\":\"EPH\",\"NAP\":\"NAP\",\"NAO\":\"NAO\",\"NAR\":\"NAR\",\"EPI\":\"EPI\",\"EPL\":\"EPL\",\"NAT\":\"NAT\",\"NAS\":\"NAS\",\"EPK\":\"EPK\",\"NAV\":\"NAV\",\"NAU\":\"NAU\",\"VRA\":\"VRA\",\"NAW\":\"NAW\",\"EPR\":\"EPR\",\"VRC\":\"VRC\",\"NAY\":\"BJS\",\"EPS\":\"EPS\",\"NBC\":\"NBC\",\"VRK\":\"VRK\",\"VRL\":\"VRL\",\"VRN\":\"VRN\",\"NBH\":\"NBH\",\"VRU\":\"VRU\",\"NBO\":\"NBO\",\"VRY\":\"VRY\",\"NBS\":\"NBS\",\"NBW\":\"GAO\",\"NBX\":\"NBX\",\"VSA\":\"VSA\",\"EQS\":\"EQS\",\"VSE\":\"VSE\",\"VSG\":\"VSG\",\"NCE\":\"NCE\",\"VSO\":\"VSO\",\"ERB\":\"ERB\",\"ERA\":\"ERA\",\"NCI\":\"NCI\",\"ERD\":\"ERD\",\"NCL\":\"NCL\",\"ERC\":\"ERC\",\"ERF\":\"ERF\",\"ERE\":\"ERE\",\"ERH\":\"ERH\",\"NCP\":\"NCP\",\"ERI\":\"ERI\",\"ERL\":\"ERL\",\"ERM\":\"ERM\",\"NCU\":\"NCU\",\"NCY\":\"NCY\",\"VTB\":\"VTB\",\"VTE\":\"VTE\",\"ERS\":\"WDH\",\"ERV\":\"ERV\",\"NDA\":\"NDA\",\"ERZ\":\"ERZ\",\"NDC\":\"NDC\",\"NDB\":\"NDB\",\"NDE\":\"NDE\",\"NDD\":\"NDD\",\"NDG\":\"NDG\",\"VTN\":\"VTN\",\"ESA\":\"ESA\",\"ESC\":\"ESC\",\"NDK\":\"NDK\",\"ESB\":\"ANK\",\"NDJ\":\"NDJ\",\"ESE\":\"ESE\",\"VTU\":\"VTU\",\"ESD\":\"ESD\",\"ESH\":\"ESH\",\"ESK\":\"ESK\",\"NDS\":\"NDS\",\"NDR\":\"NDR\",\"VTZ\":\"VTZ\",\"ESM\":\"ESM\",\"NDU\":\"NDU\",\"ESL\":\"ESL\",\"ESO\":\"ESO\",\"ESN\":\"ESN\",\"NDY\":\"NDY\",\"ESP\":\"ESP\",\"ESR\":\"ESR\",\"ESU\":\"ESU\",\"NEF\":\"NEF\",\"VUP\":\"VUP\",\"NEG\":\"NEG\",\"ETB\":\"ETB\",\"NEJ\":\"NEJ\",\"ETD\":\"ETD\",\"NEK\":\"NEK\",\"VUS\":\"VUS\",\"ETE\":\"ETE\",\"ETH\":\"ETH\",\"NER\":\"NER\",\"ETN\":\"ETN\",\"NEV\":\"NEV\",\"NEU\":\"NEU\",\"VVC\":\"VVC\",\"VVB\":\"VVB\",\"ETS\":\"ETS\",\"VVI\":\"SRZ\",\"ETZ\":\"ETZ\",\"VVK\":\"VVK\",\"NFG\":\"NFG\",\"VVO\":\"VVO\",\"EUA\":\"EUA\",\"EUG\":\"EUG\",\"NFO\":\"NFO\",\"EUF\":\"EUF\",\"VVZ\":\"VVZ\",\"EUN\":\"EUN\",\"NGB\":\"NGB\",\"EUX\":\"EUX\",\"NGA\":\"NGA\",\"NGD\":\"NGD\",\"NGC\":\"GCN\",\"NGE\":\"NGE\",\"EVA\":\"EVA\",\"EVD\":\"EVD\",\"EVE\":\"EVE\",\"EVH\":\"EVH\",\"EVG\":\"EVG\",\"NGO\":\"NGO\",\"NGQ\":\"NGQ\",\"NGS\":\"NGS\",\"EVN\":\"EVN\",\"EVM\":\"EVM\",\"NGX\":\"NGX\",\"NGW\":\"CRP\",\"VXC\":\"VXC\",\"VXE\":\"VXE\",\"EVV\":\"EVV\",\"NHA\":\"NHA\",\"EVW\":\"EVW\",\"VXO\":\"VXO\",\"NHF\":\"NHF\",\"NHK\":\"NHK\",\"EWB\":\"EWB\",\"EWE\":\"EWE\",\"EWD\":\"EWD\",\"EWI\":\"EWI\",\"NHS\":\"NHS\",\"NHT\":\"NHT\",\"EWN\":\"EWN\",\"NHV\":\"NHV\",\"EWR\":\"NYC\",\"NIB\":\"NIB\",\"NIC\":\"NIC\",\"NIE\":\"NIE\",\"VYS\":\"VYS\",\"NIN\":\"NIN\",\"NIM\":\"NIM\",\"NIS\":\"NIS\",\"NIX\":\"NIX\",\"EXT\":\"EXT\",\"NJC\":\"NJC\",\"NJF\":\"NJF\",\"EYP\":\"EYP\",\"EYR\":\"EYR\",\"EYW\":\"EYW\",\"NKC\":\"NKC\",\"NKG\":\"NKG\",\"NKI\":\"NKI\",\"EZE\":\"BUE\",\"NKM\":\"NGO\",\"EZS\":\"EZS\",\"NLA\":\"NLA\",\"NLD\":\"NLD\",\"NLG\":\"NLG\",\"NLK\":\"NLK\",\"NLP\":\"NLP\",\"NLS\":\"NLS\",\"NLT\":\"NLT\",\"NLV\":\"NLV\",\"NMB\":\"NMB\",\"NMA\":\"NMA\",\"NMC\":\"NMC\",\"NME\":\"NME\",\"NMP\":\"NMP\",\"NMU\":\"NMU\",\"NNB\":\"NNB\",\"NNG\":\"NNG\",\"NNK\":\"NNK\",\"NNM\":\"NNM\",\"NNL\":\"NNL\",\"NNU\":\"NNU\",\"NNT\":\"NNT\",\"NNY\":\"NNY\",\"NOB\":\"NOB\",\"NOA\":\"NOA\",\"NOC\":\"NOC\",\"NOE\":\"NOE\",\"NOG\":\"NOG\",\"NOJ\":\"NOJ\",\"NOI\":\"NOI\",\"NOR\":\"NOR\",\"NOT\":\"NOT\",\"NOS\":\"NOS\",\"NOV\":\"NOV\",\"NOU\":\"NOU\",\"NOZ\":\"NOZ\",\"WAC\":\"WAC\",\"WAE\":\"WAE\",\"WAD\":\"WAD\",\"WAG\":\"WAG\",\"WAI\":\"WAI\",\"WAH\":\"WAH\",\"NPE\":\"NPE\",\"WAM\":\"WAM\",\"WAN\":\"WAN\",\"WAQ\":\"WAQ\",\"NPH\":\"NPH\",\"WAR\":\"WAR\",\"WAU\":\"WAU\",\"NPL\":\"NPL\",\"WAT\":\"WAT\",\"WAW\":\"WAW\",\"WAV\":\"WAV\",\"NPT\":\"NPT\",\"WBA\":\"WBA\",\"WBC\":\"WBC\",\"WBE\":\"WBE\",\"WBM\":\"WBM\",\"WBO\":\"WBO\",\"WBQ\":\"WBQ\",\"NQL\":\"NQL\",\"FAC\":\"FAC\",\"NQN\":\"NQN\",\"FAE\":\"FAE\",\"FAJ\":\"FAJ\",\"FAI\":\"FAI\",\"FAL\":\"FAL\",\"FAK\":\"FAK\",\"FAN\":\"FAN\",\"NQU\":\"NQU\",\"FAO\":\"FAO\",\"FAR\":\"FAR\",\"NQY\":\"NQY\",\"FAV\":\"FAV\",\"NRA\":\"NRA\",\"WCH\":\"WCH\",\"FAY\":\"FAY\",\"NRD\":\"NRD\",\"NRG\":\"NRG\",\"NRI\":\"NRI\",\"NRK\":\"NRK\",\"WCR\":\"WCR\",\"FBE\":\"FBE\",\"FBD\":\"FBD\",\"NRL\":\"NRL\",\"FBM\":\"FBM\",\"FBL\":\"FBL\",\"NRT\":\"TYO\",\"NRY\":\"NRY\",\"WDA\":\"WDA\",\"FBR\":\"FBR\",\"WDH\":\"WDH\",\"WDN\":\"WDN\",\"NSH\":\"NSH\",\"FCB\":\"FCB\",\"FCA\":\"FCA\",\"NSI\":\"YAO\",\"NSK\":\"NSK\",\"NSN\":\"NSN\",\"NSM\":\"NSM\",\"FCH\":\"FAT\",\"NSO\":\"NSO\",\"WDY\":\"ADQ\",\"NST\":\"NST\",\"NSV\":\"NSV\",\"WEA\":\"WEA\",\"FCO\":\"ROM\",\"WED\":\"WED\",\"WEF\":\"WEF\",\"WEI\":\"WEI\",\"WEH\":\"WEH\",\"FCY\":\"FCY\",\"NTB\":\"NTB\",\"NTE\":\"NTE\",\"WEL\":\"WEL\",\"NTG\":\"NTG\",\"NTI\":\"NTI\",\"NTJ\":\"NTJ\",\"FDE\":\"FDE\",\"NTL\":\"NTL\",\"WET\":\"WET\",\"NTO\":\"NTO\",\"WEW\":\"WEW\",\"FDF\":\"FDF\",\"NTN\":\"NTN\",\"NTQ\":\"NTQ\",\"FDH\":\"FDH\",\"FDK\":\"FDK\",\"NTT\":\"NTT\",\"NTY\":\"NTY\",\"FDY\":\"FDY\",\"NUB\":\"NUB\",\"WFI\":\"WFI\",\"WFK\":\"WFK\",\"NUE\":\"NUE\",\"FEB\":\"FEB\",\"FEA\":\"FEA\",\"NUI\":\"NUI\",\"NUL\":\"NUL\",\"FEC\":\"FEC\",\"NUK\":\"NUK\",\"NUP\":\"NUP\",\"FEG\":\"FEG\",\"NUR\":\"NUR\",\"NUQ\":\"NUQ\",\"NUS\":\"NUS\",\"FEN\":\"FEN\",\"NUU\":\"NUU\",\"NUX\":\"NUX\",\"WGA\":\"WGA\",\"WGB\":\"WGB\",\"NVA\":\"NVA\",\"FEZ\":\"FEZ\",\"NVG\":\"NVG\",\"WGN\":\"WGN\",\"NVI\":\"NVI\",\"WGP\":\"WGP\",\"NVK\":\"NVK\",\"WGT\":\"WGT\",\"NVP\":\"NVP\",\"NVT\":\"NVT\",\"WHF\":\"WHF\",\"FFT\":\"FFT\",\"WHL\":\"WHL\",\"WHK\":\"WHK\",\"WHO\":\"WHO\",\"NWI\":\"NWI\",\"WHT\":\"WHT\",\"WHS\":\"WHS\",\"WHU\":\"WHU\",\"FGL\":\"FGL\",\"NWT\":\"NWT\",\"WIC\":\"WIC\",\"FGU\":\"FGU\",\"WIK\":\"WIK\",\"WIO\":\"WIO\",\"WJA\":\"WJA\",\"FHZ\":\"FHZ\",\"NYE\":\"NYE\",\"WJR\":\"WJR\",\"NYI\":\"NYI\",\"FID\":\"FID\",\"FIC\":\"FIC\",\"NYK\":\"NYK\",\"NYN\":\"NYN\",\"FIE\":\"FIE\",\"NYM\":\"NYM\",\"WJU\":\"WJU\",\"FIH\":\"FIH\",\"FIL\":\"FIL\",\"NYT\":\"NYT\",\"FIK\":\"FIK\",\"FIN\":\"FIN\",\"NYU\":\"NYU\",\"WKA\":\"WKA\",\"WKI\":\"WKI\",\"WKK\":\"WKK\",\"WKJ\":\"WKJ\",\"WKL\":\"WKL\",\"WKN\":\"WKN\",\"NZH\":\"NZH\",\"WKR\":\"WKR\",\"WLB\":\"WLB\",\"WLD\":\"WLD\",\"FJR\":\"FJR\",\"WLC\":\"WLC\",\"WLH\":\"WLH\",\"WLG\":\"WLG\",\"WLL\":\"WLL\",\"WLK\":\"WLK\",\"WLM\":\"WLM\",\"FKB\":\"FKB\",\"FKJ\":\"FKJ\",\"FKI\":\"FKI\",\"FKL\":\"FKL\",\"WMA\":\"WMA\",\"WMC\":\"WMC\",\"FKQ\":\"FKQ\",\"WMB\":\"WMB\",\"WME\":\"WME\",\"FKS\":\"FKS\",\"WMD\":\"WMD\",\"WMI\":\"WMI\",\"WMN\":\"WMN\",\"FLA\":\"FLA\",\"WMP\":\"WMP\",\"FLC\":\"FLC\",\"WMR\":\"WMR\",\"FLG\":\"GCN\",\"FLH\":\"FLH\",\"WMX\":\"WMX\",\"FLL\":\"FLL\",\"FLO\":\"FLR\",\"FLN\":\"FLN\",\"FLP\":\"FLP\",\"FLS\":\"FLS\",\"WND\":\"WND\",\"FLR\":\"FLR\",\"FLT\":\"FLT\",\"FLW\":\"FLW\",\"WNH\":\"WNH\",\"FLY\":\"FLY\",\"WNN\":\"WNN\",\"WNP\":\"WNP\",\"WNR\":\"WNR\",\"FMA\":\"FMA\",\"FMC\":\"FMC\",\"WNS\":\"WNS\",\"WNZ\":\"WNZ\",\"FMI\":\"FMI\",\"FMN\":\"FMN\",\"FMO\":\"FMO\",\"FMS\":\"FMS\",\"WOK\":\"WOK\",\"FMY\":\"FMY\",\"FNA\":\"FNA\",\"FNC\":\"FNC\",\"FNE\":\"FNE\",\"WOT\":\"WOT\",\"FNG\":\"FNG\",\"FNI\":\"FNI\",\"FNH\":\"FNH\",\"FNJ\":\"FNJ\",\"FNL\":\"FNL\",\"WPB\":\"WPB\",\"FNT\":\"FNT\",\"WPM\":\"WPM\",\"FOB\":\"FOB\",\"FOD\":\"FOD\",\"FOC\":\"FOC\",\"FOG\":\"FOG\",\"FOK\":\"FOK\",\"FON\":\"FON\",\"FOO\":\"FOO\",\"FOR\":\"FOR\",\"FOT\":\"FOT\",\"FOS\":\"FOS\",\"FOU\":\"FOU\",\"OAG\":\"OAG\",\"OAK\":\"OAK\",\"OAJ\":\"OAJ\",\"OAM\":\"OAM\",\"OAL\":\"OAL\",\"FPO\":\"FPO\",\"OAX\":\"OAX\",\"WRA\":\"WRA\",\"FPR\":\"FPR\",\"WRE\":\"WRE\",\"FPY\":\"FPY\",\"WRL\":\"WRL\",\"WRO\":\"WRO\",\"OBI\":\"OBI\",\"OBO\":\"OBO\",\"WRY\":\"WRY\",\"OBS\":\"OBS\",\"WSF\":\"WSF\",\"OCA\":\"OCA\",\"WSH\":\"WSH\",\"OCC\":\"OCC\",\"OCE\":\"OCE\",\"WSM\":\"WSM\",\"WSN\":\"WSN\",\"FRA\":\"FRA\",\"WSP\":\"WSP\",\"FRC\":\"FRC\",\"FRB\":\"FRB\",\"WSR\":\"WSR\",\"FRE\":\"FRE\",\"FRD\":\"FRD\",\"WST\":\"WST\",\"FRG\":\"FRG\",\"WSY\":\"WSY\",\"FRH\":\"FRH\",\"WSX\":\"WSX\",\"FRJ\":\"FRJ\",\"WSZ\":\"WSZ\",\"FRL\":\"FRL\",\"FRO\":\"FRO\",\"OCV\":\"OCV\",\"FRP\":\"FRP\",\"WTA\":\"WTA\",\"FRS\":\"FRS\",\"FRU\":\"FRU\",\"WTE\":\"WTE\",\"FRW\":\"FRW\",\"WTL\":\"WTL\",\"WTO\":\"WTO\",\"FSD\":\"FSD\",\"ODL\":\"ODL\",\"FSC\":\"FSC\",\"WTS\":\"WTS\",\"ODN\":\"ODN\",\"FSL\":\"FSL\",\"FSK\":\"FSK\",\"ODS\":\"ODS\",\"FSM\":\"FSM\",\"FSP\":\"FSP\",\"WUA\":\"WUA\",\"ODY\":\"ODY\",\"FST\":\"FST\",\"FSS\":\"FSS\",\"WUD\":\"WUD\",\"FSU\":\"FSU\",\"OEA\":\"OEA\",\"WUH\":\"WUH\",\"FSZ\":\"FSZ\",\"OEC\":\"OEC\",\"WUM\":\"WUM\",\"WUL\":\"WUL\",\"WUN\":\"WUN\",\"FTA\":\"FTA\",\"WUS\":\"WUS\",\"FTE\":\"FTE\",\"WUU\":\"WUU\",\"OEL\":\"OEL\",\"OEO\":\"OEO\",\"FTI\":\"FTI\",\"WUX\":\"WUX\",\"OES\":\"OES\",\"OER\":\"OER\",\"WUZ\":\"WUZ\",\"FTL\":\"FTL\",\"WVB\":\"WVB\",\"FTU\":\"FTU\",\"FTW\":\"FTW\",\"FTX\":\"FTX\",\"WVL\":\"WVL\",\"WVK\":\"WVK\",\"FUE\":\"FUE\",\"FUG\":\"FUG\",\"FUJ\":\"FUJ\",\"FUL\":\"FUL\",\"FUK\":\"FUK\",\"FUN\":\"FUN\",\"OFU\":\"OFU\",\"WWA\":\"WWA\",\"FUO\":\"FUO\",\"WWD\":\"WWD\",\"OGA\":\"OGA\",\"WWK\":\"WWK\",\"OGB\":\"OGB\",\"OGG\":\"OGG\",\"WWP\":\"WWP\",\"WWR\":\"WWR\",\"WWT\":\"WWT\",\"OGO\":\"OGO\",\"OGN\":\"OGN\",\"WWY\":\"WWY\",\"OGS\":\"OGS\",\"OGR\":\"OGR\",\"OGX\":\"OGX\",\"OGZ\":\"OGZ\",\"OHD\":\"OHD\",\"WXN\":\"WXN\",\"OHE\":\"OHE\",\"FWA\":\"FWA\",\"OHO\":\"OHO\",\"FWL\":\"FWL\",\"OHT\":\"OHT\",\"WYA\":\"WYA\",\"OIA\":\"OIA\",\"WYN\":\"WYN\",\"WYS\":\"WYS\",\"OIM\":\"OIM\",\"OIR\":\"OIR\",\"OIT\":\"OIT\",\"FXY\":\"FXY\",\"FYT\":\"FYT\",\"FYV\":\"FYV\",\"FYU\":\"FYU\",\"OKA\":\"OKA\",\"OKC\":\"OKC\",\"OKK\":\"OKK\",\"OKJ\":\"OKJ\",\"OKN\":\"OKN\",\"OKR\":\"OKR\",\"OKU\":\"OKU\",\"FZO\":\"FZO\",\"OKY\":\"OKY\",\"OLB\":\"OLB\",\"OLA\":\"OLA\",\"OLF\":\"OLF\",\"OLE\":\"OLE\",\"OLJ\":\"OLJ\",\"OLL\":\"OLL\",\"OLP\":\"OLP\",\"OLO\":\"OLO\",\"OMA\":\"OMA\",\"OMC\":\"OMC\",\"OMB\":\"OMB\",\"OME\":\"OME\",\"OMD\":\"OMD\",\"OMH\":\"OMH\",\"OMK\":\"OMK\",\"OMO\":\"OMO\",\"OMS\":\"OMS\",\"OMR\":\"OMR\",\"ONB\":\"ONB\",\"ONA\":\"ONA\",\"OND\":\"OND\",\"ONE\":\"ONE\",\"ONH\":\"ONH\",\"ONG\":\"ONG\",\"ONJ\":\"ONJ\",\"ONI\":\"ONI\",\"ONN\":\"ONN\",\"ONM\":\"ONM\",\"ONP\":\"ONP\",\"ONO\":\"ONO\",\"ONT\":\"ONT\",\"ONS\":\"ONS\",\"ONY\":\"ONY\",\"OOL\":\"OOL\",\"OPB\":\"OPB\",\"OPA\":\"OPA\",\"XAP\":\"XAP\",\"OPO\":\"OPO\",\"XAY\":\"XAY\",\"OPU\":\"OPU\",\"XBE\":\"XBE\",\"XBJ\":\"XBJ\",\"XBN\":\"XBN\",\"GAE\":\"GAE\",\"GAD\":\"GAD\",\"GAF\":\"GAF\",\"GAI\":\"GAI\",\"GAJ\":\"GAJ\",\"GAL\":\"GAL\",\"GAO\":\"GAO\",\"GAN\":\"GAN\",\"GAQ\":\"GAQ\",\"GAU\":\"GAU\",\"XCH\":\"XCH\",\"GAV\":\"GAV\",\"GAY\":\"GAY\",\"GAX\":\"GAX\",\"ORD\":\"CHI\",\"GAZ\":\"GAZ\",\"ORF\":\"ORF\",\"XCN\":\"XCN\",\"ORE\":\"ORE\",\"ORH\":\"ORH\",\"XCO\":\"XCO\",\"GBA\":\"GBA\",\"GBD\":\"GBD\",\"ORL\":\"ORL\",\"ORK\":\"ORK\",\"ORN\":\"ORN\",\"GBE\":\"GBE\",\"ORM\":\"ORM\",\"GBH\":\"GBH\",\"ALL1\":\"ALL\",\"GBJ\":\"GBJ\",\"ORR\":\"ORR\",\"GBL\":\"GBL\",\"ORT\":\"ORT\",\"GBM\":\"GBM\",\"ORU\":\"ORU\",\"ORX\":\"ORX\",\"ORW\":\"ORW\",\"ORY\":\"PAR\",\"GBT\":\"GBT\",\"GBV\":\"GBV\",\"OSB\":\"OSB\",\"OSD\":\"OSD\",\"OSI\":\"OSI\",\"GCC\":\"GCC\",\"OSK\":\"OSK\",\"OSM\":\"OSM\",\"OSL\":\"OSL\",\"GCI\":\"GCI\",\"OSP\":\"OSP\",\"GCK\":\"GCK\",\"OSS\":\"OSS\",\"OSR\":\"OSR\",\"GCM\":\"GCM\",\"OST\":\"OST\",\"OSW\":\"OSW\",\"GCN\":\"GCN\",\"OSY\":\"OSY\",\"OSX\":\"OSX\",\"OSZ\":\"OSZ\",\"OTD\":\"OTD\",\"XEN\":\"XEN\",\"OTH\":\"OTH\",\"OTG\":\"OTG\",\"XEO\":\"XEO\",\"OTI\":\"OTI\",\"GDD\":\"GDD\",\"XES\":\"XES\",\"GDE\":\"GDE\",\"OTP\":\"BUH\",\"XEX\":\"PAR\",\"GDG\":\"GDG\",\"OTR\":\"OTR\",\"GDL\":\"GDL\",\"GDN\":\"GDN\",\"OTV\":\"OTV\",\"OTU\":\"OTU\",\"GDO\":\"GDO\",\"OTZ\":\"OTZ\",\"GDQ\":\"GDQ\",\"GDT\":\"GDT\",\"GDV\":\"GDV\",\"GDX\":\"GDX\",\"OUA\":\"OUA\",\"XFH\":\"XFH\",\"GDZ\":\"GDZ\",\"OUD\":\"OUD\",\"OUG\":\"OUG\",\"XFN\":\"XFN\",\"OUH\":\"OUH\",\"GEC\":\"GEC\",\"OUL\":\"OUL\",\"GEG\":\"GEG\",\"GEF\":\"GEF\",\"OUN\":\"OUN\",\"GEK\":\"GEK\",\"OUS\":\"OUS\",\"OUR\":\"OUR\",\"GEL\":\"GEL\",\"GEO\":\"GEO\",\"GES\":\"GES\",\"GER\":\"GER\",\"OUZ\":\"OUZ\",\"GET\":\"GET\",\"GEV\":\"GEV\",\"GEY\":\"GEY\",\"OVB\":\"OVB\",\"GEX\":\"GEX\",\"OVA\":\"OVA\",\"OVD\":\"OVD\",\"XGN\":\"XGN\",\"OVE\":\"OVE\",\"GFB\":\"GFB\",\"XGR\":\"XGR\",\"GFF\":\"GFF\",\"GFL\":\"GFL\",\"GFK\":\"GFK\",\"GFN\":\"GFN\",\"OWB\":\"OWB\",\"GGG\":\"GGG\",\"GGN\":\"GGN\",\"GGR\":\"GGR\",\"XIC\":\"XIC\",\"GGT\":\"GGT\",\"GGW\":\"GGW\",\"OXB\":\"OXB\",\"XIL\":\"XIL\",\"XIK\":\"MIL\",\"GHA\":\"GHA\",\"XIQ\":\"XIQ\",\"GHD\":\"GHD\",\"GHC\":\"GHC\",\"XIY\":\"SIA\",\"GHN\":\"GHN\",\"GHT\":\"GHT\",\"GHU\":\"GHU\",\"OYA\":\"OYA\",\"OYE\":\"OYE\",\"OYG\":\"OYG\",\"GIC\":\"GIC\",\"OYK\":\"OYK\",\"GIB\":\"GIB\",\"GID\":\"GID\",\"GIG\":\"RIO\",\"OYO\":\"OYO\",\"OYS\":\"OYS\",\"GIL\":\"GIL\",\"GIS\":\"GIS\",\"GIR\":\"GIR\",\"XKH\":\"XKH\",\"OZA\":\"OZA\",\"GIZ\":\"GIZ\",\"OZC\":\"OZC\",\"OZH\":\"OZH\",\"XKR\":\"KRS\",\"GJA\":\"GJA\",\"XKS\":\"XKS\",\"XKY\":\"XKY\",\"GJR\":\"GJR\",\"OZZ\":\"OZZ\",\"XLB\":\"XLB\",\"GJT\":\"GJT\",\"XLO\":\"XLO\",\"GKA\":\"GKA\",\"XLS\":\"XLS\",\"XLU\":\"XLU\",\"GKH\":\"GKH\",\"GKN\":\"GKN\",\"XMB\":\"XMB\",\"XMC\":\"XMC\",\"XMH\":\"XMH\",\"XMG\":\"XMG\",\"XMI\":\"XMI\",\"XML\":\"XML\",\"XMN\":\"XMN\",\"GLA\":\"GLA\",\"GLC\":\"GLC\",\"XMS\":\"XMS\",\"GLH\":\"GLH\",\"GLI\":\"GLI\",\"XMY\":\"XMY\",\"GLL\":\"GLL\",\"GLK\":\"GLK\",\"GLN\":\"GLN\",\"XNA\":\"FYV\",\"GLO\":\"GLO\",\"GLR\":\"GLR\",\"XNB\":\"DXB\",\"GLT\":\"GLT\",\"XNG\":\"XNG\",\"GLX\":\"GLX\",\"XNN\":\"XNN\",\"GMA\":\"GMA\",\"GMB\":\"GMB\",\"GME\":\"GME\",\"XNT\":\"XNT\",\"GMI\":\"GMI\",\"GMP\":\"SEL\",\"GMR\":\"GMR\",\"GMT\":\"GMT\",\"GMZ\":\"GMZ\",\"GND\":\"GND\",\"GNE\":\"GNE\",\"GNI\":\"GNI\",\"GNN\":\"GNN\",\"GNR\":\"GNR\",\"GNT\":\"GNT\",\"GNS\":\"GNS\",\"GNV\":\"GNV\",\"GNU\":\"GNU\",\"GNZ\":\"GNZ\",\"XPK\":\"XPK\",\"GNY\":\"GNY\",\"GOA\":\"GOA\",\"GOB\":\"GOB\",\"GOE\":\"GOE\",\"GOI\":\"GOI\",\"GOH\":\"GOH\",\"GOJ\":\"GOJ\",\"XPZ\":\"LTT\",\"GOM\":\"GOM\",\"GOL\":\"GOL\",\"GOO\":\"GOO\",\"GOQ\":\"GOQ\",\"GOP\":\"GOP\",\"GOS\":\"GOS\",\"GOR\":\"GOR\",\"GOU\":\"GOU\",\"GOT\":\"GOT\",\"GOV\":\"GOV\",\"GOY\":\"GOY\",\"PAA\":\"PAA\",\"PAD\":\"PAD\",\"GOZ\":\"GOZ\",\"PAF\":\"PAF\",\"PAH\":\"PAH\",\"XQP\":\"XQP\",\"PAG\":\"PAG\",\"GPB\":\"GPB\",\"PAJ\":\"PAJ\",\"GPA\":\"GPA\",\"PAN\":\"PAN\",\"PAP\":\"PAP\",\"PAO\":\"PAO\",\"GPI\":\"GPI\",\"PAT\":\"PAT\",\"PAS\":\"PAS\",\"GPN\":\"GPN\",\"PAV\":\"PAV\",\"GPO\":\"GPO\",\"PAZ\":\"PAZ\",\"PAY\":\"PAY\",\"GPT\":\"GPT\",\"GPS\":\"GPS\",\"PBA\":\"BRW\",\"PBC\":\"PBC\",\"PBB\":\"PBB\",\"PBE\":\"PBE\",\"PBD\":\"PBD\",\"PBF\":\"PBF\",\"PBI\":\"PBI\",\"PBH\":\"PBH\",\"PBJ\":\"PBJ\",\"PBM\":\"PBM\",\"PBL\":\"PBL\",\"PBO\":\"PBO\",\"PBN\":\"PBN\",\"XRY\":\"XRY\",\"PBP\":\"PBP\",\"PBU\":\"PBU\",\"GQQ\":\"GQQ\",\"XSD\":\"TPH\",\"PBZ\":\"PBZ\",\"XSC\":\"XSC\",\"PCA\":\"PCA\",\"XSI\":\"XSI\",\"PCD\":\"PCD\",\"PCE\":\"PCE\",\"PCG\":\"PCG\",\"GRB\":\"GRB\",\"GRD\":\"GRD\",\"PCL\":\"PCL\",\"PCK\":\"PCK\",\"PCN\":\"PCN\",\"PCM\":\"PCM\",\"GRJ\":\"GRJ\",\"PCR\":\"PCR\",\"GRI\":\"GRI\",\"PCS\":\"PCS\",\"GRP\":\"GRP\",\"GRO\":\"GRO\",\"GRR\":\"GRR\",\"GRQ\":\"GRQ\",\"GRT\":\"GRT\",\"GRS\":\"GRS\",\"GRV\":\"GRV\",\"XTG\":\"XTG\",\"GRU\":\"SAO\",\"GRX\":\"GRX\",\"PDA\":\"PDA\",\"GRW\":\"GRW\",\"GRZ\":\"GRZ\",\"GRY\":\"GRY\",\"PDB\":\"PDB\",\"XTL\":\"XTL\",\"PDG\":\"PDG\",\"XTO\":\"XTO\",\"PDF\":\"PDF\",\"GSA\":\"GSA\",\"XTR\":\"XTR\",\"PDL\":\"PDL\",\"PDN\":\"PDN\",\"GSH\":\"GSH\",\"PDP\":\"PDP\",\"PDS\":\"PDS\",\"PDU\":\"PDU\",\"PDT\":\"PDT\",\"GSO\":\"GSO\",\"GSN\":\"GSN\",\"PDV\":\"PDV\",\"GSP\":\"GSP\",\"PDX\":\"PDX\",\"GSR\":\"GSR\",\"PDZ\":\"PDZ\",\"PEB\":\"PEB\",\"PED\":\"PED\",\"PEE\":\"PEE\",\"PEH\":\"PEH\",\"PEG\":\"PEG\",\"GTB\":\"GTB\",\"GTA\":\"GTA\",\"PEI\":\"PEI\",\"GTC\":\"GTC\",\"PEK\":\"BJS\",\"GTF\":\"GTF\",\"PEN\":\"PEN\",\"GTE\":\"GTE\",\"PEM\":\"PEM\",\"PER\":\"PER\",\"XUZ\":\"XUZ\",\"GTI\":\"GTI\",\"PEQ\":\"PEQ\",\"PET\":\"PET\",\"PES\":\"PES\",\"GTN\":\"MON\",\"PEX\":\"PEX\",\"PEW\":\"PEW\",\"GTR\":\"UBS\",\"PEZ\":\"PEZ\",\"GTT\":\"GTT\",\"GTS\":\"GTS\",\"PFA\":\"PFA\",\"GTW\":\"GTW\",\"PFB\":\"PFB\",\"PFD\":\"PFD\",\"XVL\":\"XVL\",\"GUA\":\"GUA\",\"GUC\":\"GUC\",\"PFJ\":\"PFJ\",\"GUD\":\"GUD\",\"GUG\":\"GUG\",\"PFO\":\"PFO\",\"PFN\":\"PFN\",\"GUI\":\"GUI\",\"GUH\":\"GUH\",\"GUM\":\"GUM\",\"GUL\":\"GUL\",\"GUQ\":\"GUQ\",\"GUR\":\"GUR\",\"GUT\":\"GUT\",\"GUW\":\"GUW\",\"GUY\":\"GUY\",\"PGA\":\"PGA\",\"PGD\":\"PGD\",\"GUZ\":\"GUZ\",\"PGF\":\"PGF\",\"PGH\":\"PGH\",\"GVA\":\"GVA\",\"PGL\":\"PGL\",\"PGK\":\"PGK\",\"GVE\":\"GVE\",\"PGM\":\"PGM\",\"PGS\":\"PGS\",\"PGV\":\"PGV\",\"PGX\":\"PGX\",\"GVR\":\"GVR\",\"PGZ\":\"PGZ\",\"GVX\":\"GVX\",\"PHC\":\"PHC\",\"PHB\":\"PHB\",\"PHE\":\"PHE\",\"PHG\":\"PHC\",\"PHF\":\"PHF\",\"GWE\":\"GWE\",\"PHL\":\"PHL\",\"GWD\":\"GWD\",\"PHN\":\"PHN\",\"PHS\":\"PHS\",\"PHR\":\"PHR\",\"GWL\":\"GWL\",\"PHW\":\"PHW\",\"PHX\":\"PHX\",\"XYA\":\"XYA\",\"GWT\":\"GWT\",\"XYE\":\"XYE\",\"PIB\":\"LUL\",\"PIA\":\"PIA\",\"PIF\":\"PIF\",\"PIH\":\"PIH\",\"PIK\":\"GLA\",\"GXF\":\"GXF\",\"PIP\":\"PIP\",\"GXH\":\"GXH\",\"GXG\":\"GXG\",\"PIR\":\"PIR\",\"PIT\":\"PIT\",\"PIS\":\"PIS\",\"PIU\":\"PIU\",\"PIX\":\"PIX\",\"PIZ\":\"PIZ\",\"GXX\":\"GXX\",\"PJA\":\"PJA\",\"PJC\":\"PJC\",\"GXY\":\"GXY\",\"GYA\":\"GYA\",\"GYE\":\"GYE\",\"PJM\":\"PJM\",\"GYD\":\"BAK\",\"GYI\":\"GYI\",\"GYM\":\"GYM\",\"GYL\":\"GYL\",\"GYN\":\"GYN\",\"GYP\":\"GYP\",\"GYS\":\"GYS\",\"GYU\":\"GYU\",\"PKB\":\"PKB\",\"PKC\":\"PKC\",\"PKE\":\"PKE\",\"PKG\":\"PKG\",\"GZA\":\"GZA\",\"PKK\":\"PKK\",\"PKN\":\"PKN\",\"PKP\":\"PKP\",\"PKR\":\"PKR\",\"PKV\":\"PKV\",\"GZM\":\"GZM\",\"PKU\":\"PKU\",\"GZP\":\"GZP\",\"GZO\":\"GZO\",\"PKW\":\"PKW\",\"PKZ\":\"PKZ\",\"PKY\":\"PKY\",\"GZT\":\"GZT\",\"PLD\":\"PLD\",\"PLK\":\"PLK\",\"PLJ\":\"PLJ\",\"PLM\":\"PLM\",\"PLO\":\"PLO\",\"PLN\":\"PLN\",\"PLQ\":\"PLQ\",\"PLS\":\"PLS\",\"PLU\":\"BHZ\",\"PLW\":\"PLW\",\"PLV\":\"PLV\",\"PLX\":\"PLX\",\"PLZ\":\"PLZ\",\"PMC\":\"PMC\",\"PMF\":\"PMF\",\"PMG\":\"PMG\",\"PMI\":\"PMI\",\"PMN\":\"PMN\",\"PMO\":\"PMO\",\"PMR\":\"PMR\",\"PMV\":\"PMV\",\"PMW\":\"PMW\",\"PMY\":\"PMY\",\"PNA\":\"PNA\",\"PNB\":\"PNB\",\"PNF\":\"PNF\",\"PNI\":\"PNI\",\"PNH\":\"PNH\",\"PNK\":\"PNK\",\"PNL\":\"PNL\",\"PNQ\":\"PNQ\",\"PNP\":\"PNP\",\"PNS\":\"PNS\",\"PNR\":\"PNR\",\"PNT\":\"PNT\",\"PNX\":\"PNX\",\"PNZ\":\"PNZ\",\"POA\":\"POA\",\"POC\":\"POC\",\"POF\":\"POF\",\"POE\":\"POE\",\"POG\":\"POG\",\"POJ\":\"POJ\",\"POI\":\"POI\",\"POL\":\"POL\",\"POM\":\"POM\",\"POP\":\"POP\",\"POR\":\"POR\",\"POQ\":\"POQ\",\"POT\":\"POT\",\"POS\":\"POS\",\"POV\":\"POV\",\"POX\":\"POX\",\"YAA\":\"YAA\",\"POW\":\"POW\",\"POZ\":\"POZ\",\"YAC\":\"YAC\",\"POY\":\"POY\",\"YAB\":\"YAB\",\"YAG\":\"YAG\",\"YAI\":\"YAI\",\"PPC\":\"PPC\",\"YAK\":\"YAK\",\"PPB\":\"PPB\",\"YAJ\":\"YAJ\",\"YAM\":\"YAM\",\"PPD\":\"HUC\",\"PPG\":\"PPG\",\"PPF\":\"PPF\",\"YAQ\":\"YAQ\",\"YAP\":\"YAP\",\"PPK\":\"PPK\",\"PPM\":\"PPM\",\"PPL\":\"PPL\",\"YAT\":\"YAT\",\"PPN\":\"PPN\",\"YAV\":\"YAV\",\"PPQ\":\"PPQ\",\"YAY\":\"YAY\",\"PPP\":\"PPP\",\"YAX\":\"YAX\",\"PPS\":\"PPS\",\"PPT\":\"PPT\",\"PPW\":\"PPW\",\"PPV\":\"PPV\",\"PPY\":\"PPY\",\"YBC\":\"YBC\",\"YBE\":\"YBE\",\"YBG\":\"YBG\",\"YBL\":\"YBL\",\"PQC\":\"PQC\",\"YBK\":\"YBK\",\"YBP\":\"YBP\",\"YBR\":\"YBR\",\"HAA\":\"HAA\",\"PQI\":\"PQI\",\"YBQ\":\"YBQ\",\"HAD\":\"HAD\",\"YBT\":\"YBT\",\"HAC\":\"HAC\",\"HAE\":\"HAE\",\"PQM\":\"PQM\",\"HAH\":\"YVA\",\"YBX\":\"YBX\",\"YBW\":\"YBW\",\"HAJ\":\"HAJ\",\"PQQ\":\"PQQ\",\"HAL\":\"HAL\",\"PQS\":\"PQS\",\"HAK\":\"HAK\",\"HAN\":\"HAN\",\"HAM\":\"HAM\",\"YCB\":\"YCB\",\"HAS\":\"HAS\",\"HAV\":\"HAV\",\"YCG\":\"YCG\",\"HAU\":\"HAU\",\"HAX\":\"MKO\",\"HAW\":\"HAW\",\"PRC\":\"PRC\",\"YCK\":\"YCK\",\"HAY\":\"HAY\",\"PRB\":\"PRB\",\"YCL\":\"YCL\",\"PRG\":\"PRG\",\"YCO\":\"YCO\",\"YCN\":\"YCN\",\"HBA\":\"HBA\",\"PRI\":\"PRI\",\"YCQ\":\"YCQ\",\"PRH\":\"PRH\",\"YCS\":\"YCS\",\"HBB\":\"HOB\",\"YCR\":\"YCR\",\"HBE\":\"ALY\",\"PRM\":\"PRM\",\"YCU\":\"YCU\",\"PRN\":\"PRN\",\"PRQ\":\"PRQ\",\"YCY\":\"YCY\",\"HBH\":\"HBH\",\"PRS\":\"PRS\",\"YCZ\":\"YCZ\",\"HBN\":\"HBN\",\"YDB\":\"YDB\",\"PRY\":\"PRY\",\"YDA\":\"YDA\",\"YDC\":\"YDC\",\"HBR\":\"HBR\",\"YDF\":\"YDF\",\"HBT\":\"HBT\",\"PSB\":\"PSB\",\"HBX\":\"HBX\",\"PSA\":\"PSA\",\"YDI\":\"YDI\",\"PSD\":\"PSD\",\"YDL\":\"YDL\",\"PSC\":\"PSC\",\"PSF\":\"PSF\",\"PSE\":\"PSE\",\"YDP\":\"YDP\",\"PSG\":\"PSG\",\"YDO\":\"YDO\",\"HCB\":\"HCB\",\"PSJ\":\"PSJ\",\"HCA\":\"HCA\",\"PSI\":\"PSI\",\"YDQ\":\"YDQ\",\"YDS\":\"YDS\",\"PSN\":\"PSN\",\"PSP\":\"PSP\",\"YDX\":\"YDX\",\"PSO\":\"PSO\",\"PSR\":\"PSR\",\"PSS\":\"PSS\",\"HCN\":\"HCN\",\"PSV\":\"PSV\",\"HCM\":\"HCM\",\"PSU\":\"PSU\",\"HCR\":\"HCR\",\"YEG\":\"YEA\",\"PTA\":\"PTA\",\"YEI\":\"BTZ\",\"HCW\":\"HCW\",\"PTC\":\"PTC\",\"YEK\":\"YEK\",\"PTD\":\"PTD\",\"PTG\":\"PTG\",\"YEO\":\"YEO\",\"YEN\":\"YEN\",\"HDA\":\"HDA\",\"PTH\":\"PTH\",\"PTK\":\"PTK\",\"PTJ\":\"PTJ\",\"YER\":\"YER\",\"HDD\":\"HDD\",\"YET\":\"YET\",\"PTO\":\"PTO\",\"HDG\":\"HDG\",\"HDF\":\"HDF\",\"PTN\":\"PTN\",\"YEV\":\"YEV\",\"PTP\":\"PTP\",\"HDM\":\"HDM\",\"PTU\":\"PTU\",\"HDN\":\"HDN\",\"PTV\":\"PTV\",\"PTY\":\"PTY\",\"YFB\":\"YFB\",\"PTX\":\"PTX\",\"YFA\":\"YFA\",\"HDS\":\"HDS\",\"YFC\":\"YFC\",\"YFH\":\"YFH\",\"HDY\":\"HDY\",\"PUB\":\"PUB\",\"YFJ\":\"YFJ\",\"PUC\":\"PUC\",\"PUF\":\"PUF\",\"PUG\":\"PUG\",\"YFO\":\"YFO\",\"PUJ\":\"PUJ\",\"HEA\":\"HEA\",\"PUK\":\"PUK\",\"PUM\":\"PUM\",\"HEH\":\"HEH\",\"YFX\":\"YFX\",\"PUO\":\"PUO\",\"HEI\":\"HEI\",\"PUQ\":\"PUQ\",\"HEL\":\"HEL\",\"PUT\":\"PUT\",\"PUS\":\"PUS\",\"HEK\":\"HEK\",\"PUU\":\"PUU\",\"PUW\":\"PUW\",\"HER\":\"HER\",\"PUY\":\"PUY\",\"HET\":\"HET\",\"HES\":\"HES\",\"YGG\":\"YGG\",\"PVA\":\"PVA\",\"YGH\":\"YGH\",\"PVC\":\"PVC\",\"YGK\":\"YGK\",\"YGJ\":\"YGJ\",\"PVD\":\"PVD\",\"YGL\":\"YGL\",\"YGO\":\"YGO\",\"PVG\":\"SHA\",\"YGN\":\"YGN\",\"YGQ\":\"YGQ\",\"PVH\":\"PVH\",\"YGP\":\"YGP\",\"PVK\":\"PVK\",\"YGR\":\"YGR\",\"HFE\":\"HFE\",\"YGT\":\"YGT\",\"PVO\":\"PVO\",\"YGW\":\"YGW\",\"YGV\":\"YGV\",\"YGX\":\"YGX\",\"PVR\":\"PVR\",\"YGZ\":\"YGZ\",\"PVU\":\"PVU\",\"HFN\":\"HFN\",\"YHA\":\"YHA\",\"HFS\":\"HFS\",\"YHD\":\"YHD\",\"YHF\":\"YHF\",\"HFT\":\"HFT\",\"YHK\":\"YHK\",\"PWE\":\"PWE\",\"YHM\":\"YHM\",\"YHP\":\"YHP\",\"YHO\":\"YHO\",\"YHR\":\"YHR\",\"HGA\":\"HGA\",\"PWI\":\"PWI\",\"HGD\":\"HGD\",\"PWM\":\"PWM\",\"HGH\":\"HGH\",\"YHZ\":\"YHZ\",\"PWQ\":\"PWQ\",\"YHY\":\"YHY\",\"HGL\":\"HGL\",\"HGN\":\"HGN\",\"HGO\":\"HGO\",\"HGR\":\"HGR\",\"YIC\":\"YIC\",\"YIE\":\"YIE\",\"HGS\":\"FNA\",\"HGU\":\"HGU\",\"YIF\":\"YIF\",\"YIH\":\"YIH\",\"YIK\":\"YIK\",\"YIO\":\"YIO\",\"YIN\":\"YIN\",\"YIP\":\"DTT\",\"HHE\":\"HHE\",\"PXM\":\"PXM\",\"PXO\":\"PXO\",\"YIW\":\"YIW\",\"YIV\":\"YIV\",\"HHH\":\"HHH\",\"PXS\":\"PXS\",\"PXU\":\"PXU\",\"HHZ\":\"HHZ\",\"PYE\":\"PYE\",\"PYH\":\"PYH\",\"HIB\":\"HIB\",\"PYJ\":\"PYJ\",\"HIA\":\"HIA\",\"HID\":\"HID\",\"YJT\":\"YJT\",\"HIE\":\"HIE\",\"HIJ\":\"HIJ\",\"HII\":\"HII\",\"HIL\":\"HIL\",\"HIN\":\"HIN\",\"YKA\":\"YKA\",\"HIR\":\"HIR\",\"YKG\":\"YKG\",\"YKF\":\"YKF\",\"PZB\":\"PZB\",\"PZE\":\"PZE\",\"YKM\":\"YKM\",\"YKL\":\"YKL\",\"YKN\":\"YKN\",\"YKQ\":\"YKQ\",\"PZI\":\"PZI\",\"PZH\":\"PZH\",\"PZK\":\"PZK\",\"YKS\":\"YKS\",\"YKU\":\"YKU\",\"YKT\":\"YKT\",\"PZO\":\"PZO\",\"YKX\":\"YKX\",\"YKZ\":\"YTO\",\"HJJ\":\"HJJ\",\"PZU\":\"PZU\",\"PZY\":\"PZY\",\"HJR\":\"HJR\",\"YLC\":\"YLC\",\"YLE\":\"YLE\",\"YLH\":\"YLH\",\"YLI\":\"YLI\",\"YLL\":\"YLL\",\"HKB\":\"HKB\",\"YLR\":\"YLR\",\"HKA\":\"HKA\",\"HKD\":\"HKD\",\"YLS\":\"YLS\",\"HKG\":\"HKG\",\"YLW\":\"YLW\",\"HKK\":\"HKK\",\"HKN\":\"HKN\",\"YMA\":\"YMA\",\"HKT\":\"HKT\",\"YMG\":\"YMG\",\"HKY\":\"HKY\",\"YMM\":\"YMM\",\"YML\":\"YML\",\"YMO\":\"YMO\",\"YMN\":\"YMN\",\"YMP\":\"YMP\",\"YMS\":\"YMS\",\"YMT\":\"YMT\",\"HLD\":\"HLD\",\"HLG\":\"HLG\",\"HLF\":\"HLF\",\"YMX\":\"YMQ\",\"HLH\":\"HLH\",\"HLM\":\"HLM\",\"HLN\":\"HLN\",\"YNB\":\"YNB\",\"HLP\":\"JKT\",\"YNA\":\"YNA\",\"HLS\":\"HLS\",\"YNC\":\"YNC\",\"YNE\":\"YNE\",\"HLW\":\"HLW\",\"YNG\":\"YNG\",\"HLY\":\"HLY\",\"YNJ\":\"YNJ\",\"YNL\":\"YNL\",\"HLZ\":\"HLZ\",\"YNK\":\"YNK\",\"YNP\":\"YNP\",\"YNO\":\"YNO\",\"HMB\":\"HMB\",\"HMA\":\"HMA\",\"YNT\":\"YNT\",\"YNS\":\"YNS\",\"HME\":\"HME\",\"HMJ\":\"HMJ\",\"YNZ\":\"YNZ\",\"YNY\":\"YNY\",\"HMI\":\"HMI\",\"HMO\":\"HMO\",\"HMR\":\"HMR\",\"YOC\":\"YOC\",\"YOD\":\"YOD\",\"HMV\":\"HMV\",\"YOG\":\"YOG\",\"YOH\":\"YOH\",\"YOK\":\"YOK\",\"YOJ\":\"YOJ\",\"YOL\":\"YOL\",\"HNA\":\"HNA\",\"YOP\":\"YOP\",\"HNB\":\"HNB\",\"HND\":\"TYO\",\"YOW\":\"YOW\",\"HNG\":\"HNG\",\"HNH\":\"HNH\",\"HNM\":\"HNM\",\"HNL\":\"HNL\",\"YPB\":\"YPB\",\"YPA\":\"YPA\",\"HNS\":\"HNS\",\"YPH\":\"YPH\",\"YPJ\":\"YPJ\",\"HNY\":\"HNY\",\"HNX\":\"HNX\",\"YPL\":\"YPL\",\"YPN\":\"YPN\",\"YPM\":\"YPM\",\"YPO\":\"YPO\",\"HOB\":\"HOB\",\"YPR\":\"YPR\",\"HOD\":\"HOD\",\"YPT\":\"YPT\",\"HOF\":\"HOF\",\"HOE\":\"HOE\",\"YPX\":\"YPX\",\"HOG\":\"HOG\",\"YPW\":\"YPW\",\"HOI\":\"HOI\",\"YPY\":\"YPY\",\"HOL\":\"HOL\",\"HOK\":\"HOK\",\"HON\":\"HON\",\"HOM\":\"HOM\",\"HOO\":\"HOO\",\"HOR\":\"HOR\",\"YQC\":\"YQC\",\"HOQ\":\"HOQ\",\"YQB\":\"YQB\",\"HOT\":\"HOT\",\"YQD\":\"YQD\",\"HOV\":\"HOV\",\"YQG\":\"YQG\",\"HOU\":\"HOU\",\"HOX\":\"HOX\",\"YQI\":\"YQI\",\"YQK\":\"YQK\",\"HOY\":\"HOY\",\"YQM\":\"YQM\",\"YQL\":\"YQL\",\"YQN\":\"YQN\",\"HPA\":\"HPA\",\"YQQ\":\"YQQ\",\"YQR\":\"YQR\",\"YQU\":\"YQU\",\"YQT\":\"YQT\",\"YQY\":\"YQY\",\"HPH\":\"HPH\",\"YQX\":\"YQX\",\"YQZ\":\"YQZ\",\"HPN\":\"HPN\",\"YRB\":\"YRB\",\"YRA\":\"YRA\",\"YRD\":\"YRD\",\"YRG\":\"YRG\",\"HPY\":\"HPY\",\"YRJ\":\"YRJ\",\"YRL\":\"YRL\",\"QBC\":\"QBC\",\"YRT\":\"YRT\",\"HQM\":\"HQM\",\"YSB\":\"YSB\",\"YSG\":\"YSG\",\"YSK\":\"YSK\",\"YSJ\":\"YSJ\",\"YSM\":\"YSM\",\"YSO\":\"YSO\",\"HRA\":\"HRA\",\"HRC\":\"HRC\",\"YSR\":\"YSR\",\"HRB\":\"HRB\",\"HRE\":\"HRE\",\"YST\":\"YST\",\"HRG\":\"HRG\",\"HRI\":\"HRI\",\"HRK\":\"HRK\",\"HRJ\":\"HRJ\",\"HRM\":\"HRM\",\"HRL\":\"HRL\",\"HRO\":\"HRO\",\"HRS\":\"HRS\",\"YTF\":\"YTF\",\"YTE\":\"YTE\",\"YTH\":\"YTH\",\"YTG\":\"YTG\",\"YTL\":\"YTL\",\"HRZ\":\"HRZ\",\"YTM\":\"YTM\",\"YTQ\":\"YTQ\",\"YTS\":\"YTS\",\"HSC\":\"HSC\",\"HSG\":\"HSG\",\"YTZ\":\"YTO\",\"YTY\":\"YTY\",\"HSL\":\"HSL\",\"HSN\":\"HSN\",\"YUB\":\"YUB\",\"YUD\":\"YUD\",\"HSV\":\"HSV\",\"YUM\":\"YUM\",\"YUL\":\"YMQ\",\"HTA\":\"HTA\",\"YUS\":\"YUS\",\"YUT\":\"YUT\",\"HTG\":\"HTG\",\"HTI\":\"HTI\",\"YUY\":\"YUY\",\"HTH\":\"HTH\",\"YUX\":\"YUX\",\"HTO\":\"HTO\",\"HTN\":\"HTN\",\"YVB\":\"YVB\",\"YVA\":\"YVA\",\"HTS\":\"HTS\",\"HTR\":\"HTR\",\"HTY\":\"HTY\",\"YVM\":\"YVM\",\"YVP\":\"YVP\",\"YVR\":\"YVR\",\"YVQ\":\"YVQ\",\"HUC\":\"HUC\",\"HUE\":\"HUE\",\"HUH\":\"HUH\",\"HUJ\":\"HUJ\",\"YVZ\":\"YDF\",\"HUI\":\"HUI\",\"HUL\":\"HUL\",\"HUN\":\"HUN\",\"HUQ\":\"HUQ\",\"YWB\":\"YWB\",\"HUS\":\"HUS\",\"HUV\":\"HUV\",\"YWG\":\"YWG\",\"HUU\":\"HUU\",\"HUX\":\"HUX\",\"YWK\":\"YWK\",\"HUZ\":\"HUZ\",\"HUY\":\"HUY\",\"YWJ\":\"YWJ\",\"YWL\":\"YWL\",\"HVA\":\"HVA\",\"YWQ\":\"YWQ\",\"HVB\":\"HVB\",\"HVG\":\"HVG\",\"HVN\":\"HVN\",\"HVS\":\"HVS\",\"HVR\":\"HVR\",\"YXC\":\"YXC\",\"YXE\":\"YXE\",\"YXH\":\"YXH\",\"YXJ\":\"YXJ\",\"YXL\":\"YXL\",\"YXK\":\"YXK\",\"YXN\":\"YXN\",\"YXP\":\"YXP\",\"YXR\":\"YXR\",\"HWD\":\"HWD\",\"YXT\":\"YXT\",\"YXS\":\"YXS\",\"YXU\":\"YXU\",\"YXX\":\"YXX\",\"HWI\":\"HWI\",\"YXY\":\"YXY\",\"HWK\":\"HWK\",\"HWN\":\"HWN\",\"YYA\":\"YYA\",\"YYC\":\"YYC\",\"YYB\":\"YYB\",\"YYE\":\"YYE\",\"YYD\":\"YYD\",\"YYG\":\"YYG\",\"YYF\":\"YYF\",\"YYH\":\"YYH\",\"YYJ\":\"YYJ\",\"YYL\":\"YYL\",\"YYU\":\"YYU\",\"YYT\":\"YYT\",\"YYY\":\"YYY\",\"YYZ\":\"YTO\",\"YZF\":\"YZF\",\"YZE\":\"YZE\",\"YZG\":\"YZG\",\"HXX\":\"HXX\",\"YZP\":\"YZP\",\"YZR\":\"YZR\",\"HYA\":\"HYA\",\"HYD\":\"HYD\",\"YZT\":\"YZT\",\"HYC\":\"HYC\",\"YZS\":\"YZS\",\"YZV\":\"YZV\",\"YZY\":\"YZY\",\"HYN\":\"HYN\",\"HYS\":\"HYS\",\"HZG\":\"HZG\",\"HZH\":\"HZH\",\"HZK\":\"HZK\",\"HZL\":\"HZL\",\"QLS\":\"QLS\",\"QOW\":\"QOW\",\"ZAD\":\"ZAD\",\"ZAC\":\"ZAC\",\"ZAH\":\"ZAH\",\"ZAG\":\"ZAG\",\"ZAL\":\"ZAL\",\"ZAM\":\"ZAM\",\"ZAO\":\"ZAO\",\"ZAR\":\"ZAR\",\"ZAT\":\"ZAT\",\"ZAZ\":\"ZAZ\",\"ZBF\":\"ZBF\",\"ZBL\":\"ZBL\",\"ZBO\":\"ZBO\",\"IAA\":\"IAA\",\"ZBR\":\"ZBR\",\"IAD\":\"WAS\",\"ZBY\":\"ZBY\",\"IAH\":\"HOU\",\"IAM\":\"IAM\",\"IAO\":\"IAO\",\"IAS\":\"IAS\",\"IAR\":\"IAR\",\"ZCL\":\"ZCL\",\"ZCO\":\"ZCO\",\"IBA\":\"IBA\",\"IBE\":\"IBE\",\"QRO\":\"QRO\",\"IBI\":\"IBI\",\"IBP\":\"IBP\",\"QRW\":\"QRW\",\"IBR\":\"IBR\",\"QRY\":\"QRY\",\"IBZ\":\"IBZ\",\"QSF\":\"QSF\",\"ICA\":\"ICA\",\"QSR\":\"QSR\",\"ICL\":\"ICL\",\"ICN\":\"SEL\",\"ICT\":\"ICT\",\"ICY\":\"ICY\",\"ZEL\":\"ZEL\",\"ZEM\":\"ZEM\",\"IDB\":\"IDB\",\"IDA\":\"IDA\",\"IDI\":\"IDI\",\"IDO\":\"IDO\",\"IDR\":\"IDR\",\"ZFD\":\"ZFD\",\"ZFN\":\"ZFN\",\"IEG\":\"IEG\",\"QUO\":\"QUO\",\"IEJ\":\"IEJ\",\"IEV\":\"IEV\",\"ZGM\":\"ZGM\",\"ZGS\":\"ZGS\",\"ZGU\":\"ZGU\",\"IFJ\":\"IFJ\",\"IFN\":\"IFN\",\"ZHA\":\"ZHA\",\"IFO\":\"IFO\",\"IGB\":\"IGB\",\"IGG\":\"IGG\",\"ZHY\":\"ZHY\",\"IGM\":\"IGM\",\"IGO\":\"IGO\",\"IGN\":\"IGN\",\"IGR\":\"IGR\",\"IGU\":\"IGU\",\"ZIH\":\"ZIH\",\"ZIG\":\"ZIG\",\"IHA\":\"IHA\",\"IHN\":\"IHN\",\"IHO\":\"IHO\",\"IHU\":\"IHU\",\"ZJN\":\"ZJN\",\"IIN\":\"IIN\",\"ZKB\":\"ZKB\",\"IIS\":\"IIS\",\"ZKE\":\"ZKE\",\"ZKG\":\"ZKG\",\"IJK\":\"IJK\",\"ZLO\":\"ZLO\",\"IKA\":\"THR\",\"IKB\":\"IKB\",\"ZLT\":\"ZLT\",\"IKI\":\"IKI\",\"IKK\":\"IKK\",\"IKS\":\"IKS\",\"ZMD\":\"ZMD\",\"IKT\":\"IKT\",\"ILA\":\"ILA\",\"ILE\":\"ILE\",\"ILL\":\"ILL\",\"ILN\":\"ILN\",\"ILM\":\"ILM\",\"ILP\":\"ILP\",\"ZNA\":\"YCD\",\"ILO\":\"ILO\",\"ILR\":\"ILR\",\"ZNC\":\"ZNC\",\"ZNE\":\"ZNE\",\"ZND\":\"ZND\",\"ILZ\":\"ILZ\",\"ILY\":\"ILY\",\"IMF\":\"IMF\",\"IMI\":\"IMI\",\"IMK\":\"IMK\",\"ZNZ\":\"ZNZ\",\"IMP\":\"IMP\",\"ZOF\":\"ZOF\",\"IMT\":\"IMT\",\"INB\":\"INB\",\"INA\":\"INA\",\"IND\":\"IND\",\"ZOS\":\"ZOS\",\"INC\":\"INC\",\"INF\":\"INF\",\"INH\":\"INH\",\"ING\":\"ING\",\"INI\":\"INI\",\"INL\":\"INL\",\"INK\":\"INK\",\"INN\":\"INN\",\"ZPC\":\"ZPC\",\"ZPB\":\"ZPB\",\"INV\":\"INV\",\"INU\":\"INU\",\"INX\":\"INX\",\"INW\":\"INW\",\"INZ\":\"INZ\",\"IOA\":\"IOA\",\"IOK\":\"IOK\",\"IOM\":\"IOM\",\"ION\":\"ION\",\"IOS\":\"IOS\",\"IOR\":\"IOR\",\"IOW\":\"IOW\",\"RAB\":\"RAB\",\"RAF\":\"RAF\",\"ZQN\":\"ZQN\",\"RAE\":\"RAE\",\"RAH\":\"RAH\",\"RAJ\":\"RAJ\",\"IPA\":\"IPA\",\"RAI\":\"RAI\",\"IPC\":\"IPC\",\"RAK\":\"RAK\",\"RAM\":\"RAM\",\"IPH\":\"IPH\",\"RAP\":\"RAP\",\"RAO\":\"RAO\",\"RAR\":\"RAR\",\"ZQZ\":\"ZQZ\",\"IPI\":\"IPI\",\"RAQ\":\"RAQ\",\"IPL\":\"IPL\",\"RAT\":\"RAT\",\"RAS\":\"RAS\",\"IPN\":\"IPN\",\"RAZ\":\"RAZ\",\"IPT\":\"IPT\",\"RBA\":\"RBA\",\"ZRI\":\"ZRI\",\"ZRH\":\"ZRH\",\"ZRJ\":\"ZRJ\",\"RBE\":\"RBE\",\"ZRM\":\"ZRM\",\"RBG\":\"RBG\",\"RBF\":\"RBF\",\"RBI\":\"RBI\",\"RBH\":\"RBH\",\"RBJ\":\"RBJ\",\"RBL\":\"RBL\",\"RBN\":\"RBN\",\"RBQ\":\"RBQ\",\"AAA\":\"AAA\",\"RBP\":\"RBP\",\"RBR\":\"RBR\",\"IQM\":\"IQM\",\"AAE\":\"AAE\",\"RBV\":\"RBV\",\"IQN\":\"IQN\",\"IQQ\":\"IQQ\",\"RBY\":\"RBY\",\"ZSA\":\"ZSA\",\"AAL\":\"AAL\",\"IQT\":\"IQT\",\"ZSE\":\"ZSE\",\"AAN\":\"AAN\",\"RCB\":\"RCB\",\"ZSJ\":\"ZSJ\",\"AAQ\":\"AAQ\",\"AAR\":\"AAR\",\"AAT\":\"AAT\",\"RCE\":\"RCE\",\"AAX\":\"AAX\",\"IRB\":\"IRB\",\"AAY\":\"AAY\",\"IRA\":\"IRA\",\"IRD\":\"IRD\",\"RCL\":\"RCL\",\"IRC\":\"IRC\",\"RCM\":\"RCM\",\"IRG\":\"IRG\",\"ABA\":\"ABA\",\"IRJ\":\"IRJ\",\"ABB\":\"ABB\",\"ABC\":\"ABC\",\"ABD\":\"ABD\",\"IRK\":\"IRK\",\"ABE\":\"ABE\",\"RCU\":\"RCU\",\"IRP\":\"IRP\",\"ZTA\":\"ZTA\",\"ABI\":\"ABI\",\"ABJ\":\"ABJ\",\"ZTB\":\"ZTB\",\"ABL\":\"ABL\",\"IRS\":\"IRS\",\"ABM\":\"ABM\",\"ABN\":\"ABN\",\"ZTH\":\"ZTH\",\"ABQ\":\"ABQ\",\"RDC\":\"RDC\",\"ABR\":\"ABR\",\"RDB\":\"RDB\",\"ABS\":\"ABS\",\"ABT\":\"ABT\",\"RDD\":\"RDD\",\"ABV\":\"ABV\",\"ABW\":\"ABW\",\"ISA\":\"ISA\",\"ABX\":\"ABX\",\"ABY\":\"ABY\",\"ABZ\":\"ABZ\",\"ISB\":\"ISB\",\"ZTR\":\"ZTR\",\"ISE\":\"ISE\",\"RDM\":\"RDM\",\"ISG\":\"ISG\",\"RDN\":\"RDN\",\"ACA\":\"ACA\",\"ISH\":\"ISH\",\"ACB\":\"ACB\",\"ISK\":\"ISK\",\"RDS\":\"RDS\",\"ACC\":\"ACC\",\"ISJ\":\"ISJ\",\"ISM\":\"ISM\",\"RDU\":\"RDU\",\"ACE\":\"ACE\",\"ISN\":\"ISN\",\"RDV\":\"RDV\",\"ACH\":\"ACH\",\"ACI\":\"ACI\",\"ISP\":\"ISP\",\"ISS\":\"ISS\",\"ACK\":\"ACK\",\"RDZ\":\"RDZ\",\"ISU\":\"ISU\",\"IST\":\"IST\",\"ISW\":\"ISW\",\"ZUH\":\"ZUH\",\"REA\":\"REA\",\"ACR\":\"ACR\",\"RED\":\"RED\",\"REC\":\"REC\",\"ACT\":\"ACT\",\"ZUM\":\"ZUM\",\"ACV\":\"ACV\",\"REH\":\"REH\",\"REG\":\"REG\",\"ITB\":\"ITB\",\"ACX\":\"ACX\",\"ACY\":\"AIY\",\"REL\":\"REL\",\"REN\":\"REN\",\"ITH\":\"ITH\",\"REP\":\"REP\",\"ADA\":\"ADA\",\"ADB\":\"IZM\",\"RET\":\"RET\",\"ADD\":\"ADD\",\"RES\":\"RES\",\"ADE\":\"ADE\",\"ITN\":\"ITN\",\"ADF\":\"ADF\",\"ITM\":\"OSA\",\"REU\":\"REU\",\"ITP\":\"ITP\",\"REX\":\"REX\",\"ZVA\":\"ZVA\",\"ITO\":\"ITO\",\"REZ\":\"REZ\",\"ADL\":\"ADL\",\"ADO\":\"ADO\",\"ADP\":\"ADP\",\"ZVK\":\"ZVK\",\"ADT\":\"ADT\",\"RFD\":\"RFD\",\"ADU\":\"ADU\",\"ADV\":\"ADV\",\"ADY\":\"ADY\",\"ADZ\":\"ADZ\",\"IUE\":\"IUE\",\"RFN\":\"RFN\",\"RFP\":\"RFP\",\"AEB\":\"AEB\",\"IUL\":\"IUL\",\"ZWA\":\"ZWA\",\"AEP\":\"BUE\",\"RGA\":\"RGA\",\"AER\":\"AER\",\"ZWL\":\"ZWL\",\"AES\":\"AES\",\"RGE\":\"RGE\",\"AEX\":\"AEX\",\"AEY\":\"AEY\",\"IVA\":\"IVA\",\"RGI\":\"RGI\",\"RGL\":\"RGL\",\"IVC\":\"IVC\",\"RGN\":\"RGN\",\"AFA\":\"AFA\",\"IVL\":\"IVL\",\"RGT\":\"RGT\",\"IVR\":\"IVR\",\"AFL\":\"AFL\",\"AFN\":\"AFN\",\"IVW\":\"IVW\",\"RHD\":\"RHD\",\"IWA\":\"IWA\",\"RHI\":\"RHI\",\"AFY\":\"AFY\",\"IWD\":\"IWD\",\"RHO\":\"RHO\",\"AGA\":\"AGA\",\"RHP\":\"RHP\",\"IWJ\":\"IWJ\",\"AGD\":\"AGD\",\"RHT\":\"RHT\",\"AGF\":\"AGF\",\"AGH\":\"AGH\",\"AGL\":\"AGL\",\"AGN\":\"AGN\",\"AGP\":\"AGP\",\"RIB\":\"RIB\",\"RIA\":\"RIA\",\"ZYI\":\"ZYI\",\"AGR\":\"AGR\",\"ZYL\":\"ZYL\",\"AGS\":\"AGS\",\"RIC\":\"RIC\",\"AGT\":\"AGT\",\"RIF\":\"RIF\",\"AGU\":\"AGU\",\"RIE\":\"RIE\",\"AGW\":\"AGW\",\"RIG\":\"RIG\",\"AGX\":\"AGX\",\"IXB\":\"IXB\",\"RIJ\":\"RIJ\",\"AGY\":\"AGY\",\"IXA\":\"IXA\",\"IXD\":\"IXD\",\"RIL\":\"RIL\",\"IXC\":\"IXC\",\"RIN\":\"RIN\",\"IXE\":\"IXE\",\"IXH\":\"IXH\",\"IXG\":\"IXG\",\"IXJ\":\"IXJ\",\"RIR\":\"RAL\",\"AHB\":\"AHB\",\"IXI\":\"IXI\",\"IXL\":\"IXL\",\"IXK\":\"IXK\",\"RIS\":\"RIS\",\"IXM\":\"IXM\",\"IXP\":\"IXP\",\"RIX\":\"RIX\",\"RIW\":\"RIW\",\"IXR\":\"IXR\",\"RIY\":\"RIY\",\"IXS\":\"IXS\",\"IXV\":\"IXV\",\"AHN\":\"AHN\",\"IXU\":\"IXU\",\"AHO\":\"AHO\",\"RJA\":\"RJA\",\"IXZ\":\"IXZ\",\"IXY\":\"IXY\",\"RJB\":\"RJB\",\"AHU\":\"AHU\",\"RJH\":\"RJH\",\"RJK\":\"RJK\",\"ZZU\":\"ZZU\",\"RJL\":\"RJL\",\"ZZV\":\"ZZV\",\"AIA\":\"AIA\",\"IYK\":\"IYK\",\"AIC\":\"AIC\",\"AIM\":\"AIM\",\"AIN\":\"AIN\",\"AIP\":\"AIP\",\"RKD\":\"RKD\",\"AIT\":\"AIT\",\"RKH\":\"RKH\",\"AIY\":\"AIY\",\"AJA\":\"AJA\",\"RKU\":\"RKU\",\"IZO\":\"IZO\",\"AJI\":\"AJI\",\"RKZ\":\"RKZ\",\"IZT\":\"IZT\",\"AJL\":\"AJL\",\"AJO\":\"AJO\",\"RLA\":\"RLA\",\"AJR\":\"AJR\",\"RLD\":\"RLD\",\"AJU\":\"AJU\",\"RLG\":\"RLG\",\"AJY\":\"AJY\",\"RLK\":\"RLK\",\"AKA\":\"AKA\",\"AKB\":\"AKB\",\"RLU\":\"RLU\",\"RLT\":\"RLT\",\"AKF\":\"AKF\",\"AKI\":\"AKI\",\"AKJ\":\"AKJ\",\"AKL\":\"AKL\",\"AKN\":\"AKN\",\"AKP\":\"AKP\",\"RMA\":\"RMA\",\"AKS\":\"AKS\",\"RMF\":\"RMF\",\"AKU\":\"AKU\",\"AKV\":\"AKV\",\"AKX\":\"AKX\",\"RMI\":\"RMI\",\"RMK\":\"RMK\",\"RMP\":\"RMP\",\"ALA\":\"ALA\",\"ALB\":\"ALB\",\"RMQ\":\"RMQ\",\"ALC\":\"ALC\",\"ALF\":\"ALF\",\"ALG\":\"ALG\",\"ALH\":\"ALH\",\"ALJ\":\"ALJ\",\"ALK\":\"ALK\",\"ALM\":\"ALM\",\"ALO\":\"ALO\",\"ALP\":\"ALP\",\"ALQ\":\"ALQ\",\"RNB\":\"RNB\",\"ALS\":\"ALS\",\"RNE\":\"RNE\",\"ALW\":\"ALW\",\"RNI\":\"RNI\",\"RNL\":\"RNL\",\"RNO\":\"RNO\",\"RNN\":\"RNN\",\"AMA\":\"AMA\",\"RNP\":\"RNP\",\"RNS\":\"RNS\",\"AMD\":\"AMD\",\"AME\":\"AME\",\"RNT\":\"RNT\",\"AMI\":\"AMI\",\"AMK\":\"DRO\",\"AML\":\"AML\",\"AMM\":\"AMM\",\"ROB\":\"MLW\",\"AMQ\":\"AMQ\",\"ROA\":\"ROA\",\"AMR\":\"AMR\",\"AMS\":\"AMS\",\"ROC\":\"ROC\",\"AMW\":\"AMW\",\"ROG\":\"ROG\",\"AMY\":\"AMY\",\"ROI\":\"ROI\",\"ROL\":\"ROL\",\"ROK\":\"ROK\",\"ROP\":\"ROP\",\"ROO\":\"ROO\",\"ROR\":\"ROR\",\"ANC\":\"ANC\",\"ROT\":\"ROT\",\"ROS\":\"ROS\",\"ANE\":\"ANE\",\"ROV\":\"ROV\",\"ANF\":\"ANF\",\"ROU\":\"ROU\",\"ROW\":\"ROW\",\"ANI\":\"ANI\",\"ANK\":\"ANK\",\"RPA\":\"RPA\",\"ANP\":\"ANP\",\"ANR\":\"ANR\",\"ANU\":\"ANU\",\"ANW\":\"ANW\",\"ANX\":\"ANX\",\"ANZ\":\"ANZ\",\"RPM\":\"RPM\",\"RPN\":\"RPN\",\"RPR\":\"RPR\",\"AOE\":\"ESK\",\"AOG\":\"AOG\",\"AOI\":\"AOI\",\"AOJ\":\"AOJ\",\"AOK\":\"AOK\",\"AOL\":\"AOL\",\"AOO\":\"AOO\",\"AOR\":\"AOR\",\"AOS\":\"AOS\",\"JAC\":\"JAC\",\"JAF\":\"JAF\",\"JAG\":\"JAG\",\"JAI\":\"JAI\",\"JAL\":\"JAL\",\"JAN\":\"JAN\",\"APF\":\"APF\",\"JAR\":\"JAR\",\"JAQ\":\"JAQ\",\"APL\":\"APL\",\"JAV\":\"JAV\",\"APN\":\"APN\",\"JAU\":\"JAU\",\"APO\":\"APO\",\"JAX\":\"JAX\",\"APU\":\"APU\",\"APW\":\"APW\",\"RRI\":\"RRI\",\"RRK\":\"RRK\",\"APZ\":\"APZ\",\"JBK\":\"JBK\",\"RRS\":\"RRS\",\"AQG\":\"AQG\",\"AQI\":\"AQI\",\"AQJ\":\"AQJ\",\"JBR\":\"JBR\",\"AQP\":\"AQP\",\"RSA\":\"RSA\",\"RSD\":\"RSD\",\"RSN\":\"RSN\",\"RSP\":\"RSP\",\"ARB\":\"ARB\",\"ARC\":\"ARC\",\"RST\":\"RST\",\"ARD\":\"ARD\",\"JCK\":\"JCK\",\"RSS\":\"RSS\",\"ARE\":\"ARE\",\"RSU\":\"RSU\",\"ARG\":\"ARG\",\"RSX\":\"RSX\",\"ARH\":\"ARH\",\"RSW\":\"FMY\",\"ARI\":\"ARI\",\"ARK\":\"ARK\",\"ARM\":\"ARM\",\"ARN\":\"STO\",\"ARP\":\"ARP\",\"RTB\":\"RTB\",\"ARS\":\"ARS\",\"ART\":\"ART\",\"ARU\":\"ARU\",\"RTG\":\"RTG\",\"RTI\":\"RTI\",\"RTM\":\"RTM\",\"JDF\":\"JDF\",\"JDH\":\"JDH\",\"ASB\":\"ASB\",\"RTS\":\"RTS\",\"ASD\":\"ASD\",\"ASE\":\"ASE\",\"ASF\":\"ASF\",\"JDO\":\"JDO\",\"RTW\":\"RTW\",\"ASH\":\"ASH\",\"ASJ\":\"ASJ\",\"ASK\":\"ASK\",\"ASM\":\"ASM\",\"ASO\":\"ASO\",\"ASP\":\"ASP\",\"RUA\":\"RUA\",\"ASR\":\"ASR\",\"JDZ\":\"JDZ\",\"AST\":\"AST\",\"ASU\":\"ASU\",\"ASV\":\"ASV\",\"RUH\":\"RUH\",\"ASW\":\"ASW\",\"JED\":\"JED\",\"JEF\":\"JEF\",\"RUN\":\"RUN\",\"RUM\":\"RUM\",\"JEG\":\"JEG\",\"ATA\":\"ATA\",\"JEJ\":\"JEJ\",\"RUR\":\"RUR\",\"ATB\":\"ATB\",\"RUT\":\"RUT\",\"ATD\":\"ATD\",\"RUS\":\"RUS\",\"ATE\":\"ATE\",\"ATF\":\"ATF\",\"ATH\":\"ATH\",\"ATI\":\"ATI\",\"JER\":\"JER\",\"ATJ\":\"ATJ\",\"ATK\":\"ATK\",\"ATL\":\"ATL\",\"ATM\":\"ATM\",\"ATN\":\"ATN\",\"RVA\":\"RVA\",\"ATQ\":\"ATQ\",\"ATR\":\"ATR\",\"ATS\":\"ATS\",\"RVE\":\"RVE\",\"ATT\":\"ATT\",\"RVD\":\"RVD\",\"ATU\":\"ATU\",\"ATW\":\"ATW\",\"ATY\":\"ATY\",\"RVK\":\"RVK\",\"ATZ\":\"ATZ\",\"RVN\":\"RVN\",\"AUA\":\"AUA\",\"AUB\":\"AUB\",\"JFK\":\"NYC\",\"AUC\":\"AUC\",\"RVR\":\"RVR\",\"AUD\":\"AUD\",\"RVT\":\"RVT\",\"AUG\":\"AUG\",\"AUH\":\"AUH\",\"AUK\":\"AUK\",\"AUL\":\"AUL\",\"AUN\":\"AUN\",\"AUP\":\"AUP\",\"RWB\":\"RWB\",\"AUQ\":\"AUQ\",\"AUR\":\"AUR\",\"AUS\":\"AUS\",\"RWF\":\"RWF\",\"AUU\":\"AUU\",\"AUV\":\"AUV\",\"AUW\":\"AUW\",\"AUX\":\"AUX\",\"AUY\":\"AUY\",\"JGA\":\"JGA\",\"RWL\":\"RWL\",\"JGD\":\"JGD\",\"RWN\":\"RWN\",\"AVA\":\"AVA\",\"AVB\":\"AVB\",\"JGN\":\"JGN\",\"AVG\":\"AVG\",\"JGO\":\"JGO\",\"AVI\":\"AVI\",\"AVL\":\"AVL\",\"JGS\":\"JGS\",\"AVN\":\"AVN\",\"AVP\":\"AVP\",\"AVU\":\"AVU\",\"AVV\":\"MEL\",\"AVX\":\"AVX\",\"JHB\":\"JHB\",\"JHE\":\"JHE\",\"JHG\":\"JHG\",\"AWA\":\"AWA\",\"RXS\":\"RXS\",\"AWD\":\"AWD\",\"JHM\":\"JHM\",\"AWH\":\"AWH\",\"JHS\":\"JHS\",\"AWK\":\"AWK\",\"AWN\":\"AWN\",\"JHW\":\"JHW\",\"AWP\":\"AWP\",\"RYG\":\"OSL\",\"JIB\":\"JIB\",\"AWZ\":\"AWZ\",\"RYK\":\"RYK\",\"JIC\":\"JIC\",\"AXA\":\"AXA\",\"JIJ\":\"JIJ\",\"AXB\":\"AXB\",\"AXC\":\"AXC\",\"AXD\":\"AXD\",\"JIK\":\"JIK\",\"JIM\":\"JIM\",\"AXF\":\"AXF\",\"AXG\":\"AXG\",\"JIQ\":\"JIQ\",\"AXK\":\"AXK\",\"AXM\":\"AXM\",\"JIU\":\"JIU\",\"AXP\":\"AXP\",\"JIW\":\"JIW\",\"AXR\":\"AXR\",\"AXS\":\"LTS\",\"RZE\":\"RZE\",\"AXT\":\"AXT\",\"AXU\":\"AXU\",\"AXX\":\"AXX\",\"RZN\":\"RZN\",\"JJI\":\"JJI\",\"AYA\":\"AYA\",\"RZR\":\"RZR\",\"AYD\":\"AYD\",\"AYG\":\"AYG\",\"JJN\":\"JJN\",\"AYI\":\"AYI\",\"AYK\":\"AYK\",\"RZZ\":\"RZZ\",\"AYL\":\"AYL\",\"AYP\":\"AYP\",\"AYQ\":\"AYQ\",\"AYS\":\"AYS\",\"AYT\":\"AYT\",\"AYW\":\"AYW\",\"JKH\":\"JKH\",\"JKG\":\"JKG\",\"AZB\":\"AZB\",\"JKL\":\"JKL\",\"AZD\":\"AZD\",\"JKR\":\"JKR\",\"JKT\":\"JKT\",\"AZN\":\"AZN\",\"AZO\":\"AZO\",\"AZR\":\"AZR\",\"JLN\":\"JLN\",\"JLR\":\"JLR\",\"JMK\":\"JMK\",\"JMM\":\"MMA\",\"JMS\":\"JMS\",\"JMU\":\"JMU\",\"JNB\":\"JNB\",\"JNG\":\"JNG\",\"JNN\":\"JNN\",\"JNU\":\"JNU\",\"JNX\":\"JNX\",\"JNZ\":\"JNZ\",\"JOE\":\"JOE\",\"JOG\":\"JOG\",\"JOI\":\"JOI\",\"JOL\":\"JOL\",\"JOK\":\"JOK\",\"JOT\":\"JOT\",\"SAC\":\"SAC\",\"SAB\":\"SAB\",\"SAD\":\"SAD\",\"SAG\":\"SAG\",\"SAF\":\"SAF\",\"JPA\":\"JPA\",\"SAH\":\"SAH\",\"SAK\":\"SAK\",\"SAM\":\"SAM\",\"SAL\":\"SAL\",\"SAN\":\"SAN\",\"SAP\":\"SAP\",\"SAU\":\"SAU\",\"SAT\":\"SAT\",\"SAW\":\"SAW\",\"SAV\":\"SAV\",\"JPR\":\"JPR\",\"SBA\":\"SBA\",\"SBH\":\"SBH\",\"SBG\":\"SBG\",\"JQA\":\"JQA\",\"SBK\":\"SBK\",\"SBN\":\"SBN\",\"SBM\":\"SBM\",\"SBP\":\"CSL\",\"BAA\":\"BAA\",\"SBQ\":\"SBQ\",\"SBS\":\"SBS\",\"SBU\":\"SBU\",\"BAG\":\"BAG\",\"BAH\":\"BAH\",\"SBW\":\"SBW\",\"SBZ\":\"SBZ\",\"SBY\":\"SBY\",\"BAK\":\"BAK\",\"BAL\":\"BAL\",\"BAM\":\"BAM\",\"BAQ\":\"BAQ\",\"SCC\":\"SCC\",\"BAS\":\"BAS\",\"SCE\":\"SCE\",\"BAT\":\"BAT\",\"BAU\":\"BAU\",\"SCG\":\"SCG\",\"BAV\":\"BAV\",\"BAX\":\"BAX\",\"BAY\":\"BAY\",\"SCK\":\"SCK\",\"SCJ\":\"SCJ\",\"SCL\":\"SCL\",\"SCO\":\"SCO\",\"SCN\":\"SCN\"}");

/**
 * 格式化价格
 * @param src_fare
 * @returns {number}
 */
function formatFare(src_fare) {

    src_fare = src_fare.replace("≈", "");

    //如果有src_fare中有","  按分号切割
    if (src_fare.search(/\,/) >= 0) {

        var src_fare_arr = src_fare.split(/\,/);

        var i = 0;
        src_fare = "";
        while (i < src_fare_arr.length) {
            src_fare += src_fare_arr[i];
            i += 1;
        }
        return Math.ceil(src_fare);
    }
    return Math.ceil(src_fare);
}

/**
 * 时间转化
 * @param now_day
 * @param arr_time
 * @returns {string}
 */
function addDate(dd, dadd) {
    var a = new Date(dd);
    a = a.valueOf();
    a = a + dadd * 24 * 60 * 60 * 1000;
    var now_day = new Date(a);
    var m_str = (now_day.getMonth() + 1);
    m_str = m_str < 10 ? "0" + m_str : m_str;
    var d_str = now_day.getDate();
    d_str = d_str < 10 ? "0" + d_str : d_str;

    return now_day.getFullYear() + "-" + m_str + "-" + d_str;
}

/**
 * 根据date_arr返回格式化时间字符串
 * @param date_arr
 * @returns {{now_day: *, depTime: string, arrTime: string}}
 */
function formatTime(date_arr) {


    var now_day = date_arr[0];
    var depTime_temp = now_day + " " + date_arr[1].substring(0, 2) + ":" + date_arr[1].substring(2, 4) + ":00";
    var arrTime_temp = now_day + " " + date_arr[2].substring(0, 2) + ":" + date_arr[2].substring(2, 4) + ":00";

    var depMill = new Date(depTime_temp).valueOf();
    var arrMill = new Date(arrTime_temp).valueOf();
    if (depMill > arrMill) {
        var now_day_temp = addDate(arrMill, 1);
        arrTime_temp = now_day_temp + " " + date_arr[2].substring(0, 2) + ":" + date_arr[1].substring(2, 4) + ":00";
    }


    return {
        now_day: now_day,
        depTime: depTime_temp,
        arrTime: arrTime_temp
    };


}

/**
 * 格式化时间到分钟单位
 * @param time_arr
 * @returns {number}
 */
function formatTimeToMinute(time_arr) {
    var minutes = 0;
    var i = 0;

    while (i < time_arr.length) {

        if ((time_arr[i] + "").trim() == "") {
            i += 1;
            continue;
        }


        if ((time_arr[i + 1] + "").search(/Days/g) >= 0 || (time_arr[i + 1] + "").search(/天/g) >= 0) {
            minutes += parseInt(time_arr[i]) * 24 * 60;
        }
        if ((time_arr[i + 1] + "").search(/Hours/g) >= 0 || (time_arr[i + 1] + "").search(/小时/g) >= 0) {
            minutes += parseInt(time_arr[i]) * 60;
        }
        if ((time_arr[i + 1] + "").search(/Minutes/g) >= 0 || (time_arr[i + 1] + "").search(/分钟/g) >= 0) {
            minutes += parseInt(time_arr[i]);
        }

        i += 2;
    }

    return minutes;
}


/**
 * 用基础数据为segment中其他数据赋值
 * @param segment
 * @returns {*}
 */
function assignmentSegment(segment) {

    segment.flightNumber = segment.carrier + segment.aircraftCode;
    segment.marketingCarrier = segment.carrier;
    segment.operatingCarrier = segment.carrier;
    segment.operatingFlightNo = segment.carrier + segment.aircraftCode;

    return segment;
}


/**
 * 获行程详细信息
 * @param selectorStr
 * @returns {*}
 */
function getPlanInfo(selectorStr) {

    var fromTime = gtmDataLayer[0].searchedFlightStartDate;

    var retTime = gtmDataLayer[0].searchedFlightEndDate;

    var segments_li = null;
    if ("from" == selectorStr) {
        segments_li = $("#departflight-panel #departflightForm #contentfare-depart .active  .skin-minimal .flightcheck-listing > li");
    } else if ("ret" == selectorStr) {
        segments_li = $("#returnflight-panel #returnflightForm #contentfare-return .active  .skin-minimal .flightcheck-listing > li");
        if (segments_li.length == 0) {
            return {
                routings: []
            };

        }
    }

    var plan_data_arr = [];

    if (segments_li.length != null || segments_li.length != undefined || segments_li.length != 0) {
        segments_li.each(function (index, cell) {

            var now_day = selectorStr == "from" ? fromTime : retTime;

            //进入到 行程信息li标签中

            //初始化该行程信息
            var routing = {
                fareType: "public",
                flightClass: "Economy",
                flightClassCode: "E",
                flightOption: "oneWay",
                fromSegments: [],
                fromPriceInfos: [],
                routeCodes: {
                    airports: "",
                    cabins: "",
                    carriers: "",
                    flightNumbers: "",
                    flightTimes: "",
                    marketingCarriers: "",
                    operatingCarriers: ""
                }

            };

            //截去座位基数，为后面中的每个segment的seatsMain赋值

            var seatsRemain = $(this).find("label > ul").text().replace(/[^0-9]/ig, "");

            console.log("seatsRemain : " + seatsRemain);


            var fromPrice = [];

            //从.price-flight遍历获得乘客信息的价格
            $(this).find("label .price-flight").children().each(function (index, cell) {
                var price_data = $(this).text().replace(/\n/g, " "); //del \n
                var price_arr = price_data.split(" ");
                var i = 0;
                var temp_arr = [];
                while (i < price_arr.length) {
                    if (price_arr[i].trim() != "") {
                        temp_arr.push(price_arr[i]);
                    }
                    i += 1;
                }
                fromPrice.push({
                    baseFare: formatFare(temp_arr[2] + (temp_arr[3] == undefined || temp_arr[3] == null ? "" : temp_arr[3])),
                    currency: temp_arr[0].trim(),
                    passengerType: temp_arr[1].search(/成人/) >= 0 || temp_arr[1].search(/Adult/) >= 0 ? "ADT" : "CHD",
                    quantity: "1",
                    tax: 0
                });


            });
            routing.fromPriceInfos = fromPrice;


            //为行程航段信息节点中的为空的p节点
            var node_arr = [];
            $(this).find("label > .none").children().each(function (index, cell) {
                if ($(this).text().trim() != "") {
                    node_arr.push($(this));
                }
            });

            var i = 0;
            // 格式化行程详细信息节点，为省略的航班信息添加h4标签节点
            var temp_node = null;
            while (i <= node_arr.length) {

                if (node_arr[i][0].tagName != "H4") {
                    node_arr.splice(i, 0, temp_node);
                }

                temp_node = node_arr[i];

                i += 3;
            }

            var segments = [];

            i = 0;
            while (i < node_arr.length) {


                var segment = {
                    aircraftCode: "",  //机型
                    arrAirport: "", //机场3zima
                    arrCity: "",     //达到城市
                    arrTime: "",  //到达时间
                    cabin: "E", //舱位  默认为E
                    carrier: "", //航空公司
                    codeShare: false,   //默认false
                    depAirport: "",//出发机场 3字码
                    depCity: "",      //出发城市
                    depTime: "",
                    flightNumber: "", //航班号
                    flightTime: "",  //飞行时间
                    fromTerminal: "", //航站楼
                    marketingCarrier: "", //和行四一样
                    meal: "",
                    operatingCarrier: "",  //相同
                    operatingFlightNo: "", //增加返回承运航班号字段 - 2017-08-11 add by 周才樑
                    seatsRemain: "", //剩余座位数
                    stayTime: "",     //停留时间
                    stopCities: "", //现默认接收接口的stopAirports,默认以,或者/分隔 - 2017-07-21 by 周才樑 //经停 不换飞机
                    stopQuantity: "", //次数
                    toTerminal: "" // 到达的航站楼
                }

                //node_1 航班号数据节点   node_2 飞行时间数据节点   node_3  停留时间数据节点（默认存在）
                var node_1 = node_arr[i];
                var node_2 = node_arr[i + 1];
                var node_3 = node_arr[i + 2];

                var temp_line_1 = node_1.text().replace(/\n/g, "");
                var temp_arr = (temp_line_1.trim()).split(" ");

                var k = 0;
                var temp_arr_temp = [];
                while (k < temp_arr.length) {
                    if (temp_arr[k].trim() != "") {
                        temp_arr_temp.push(temp_arr[k].trim());
                    }
                    k += 1;
                }
                temp_arr = temp_arr_temp;
                var carrier = temp_arr[0];
                var aircraftCode = temp_arr[1];
                segment.carrier = carrier;
                segment.aircraftCode = aircraftCode;

                if (node_2[0].tagName == "P" && node_2.children().length != 0) {
                    var line = node_2.text();
                    line.replace(/\r\n/g, "");
                    var line_arr = line.split(" ");
                    var j = 0;
                    var line_arr_1 = [];
                    while (j < line_arr.length) {

                        if ((line_arr[j].trim()).search(/\n/) >= 0) {
                            var line_arr_2 = line_arr[j].trim().split(/\n/);
                            console.log(line_arr_2);
                            var l = 0;
                            while (l < line_arr_2.length) {
                                line_arr_1.push(line_arr_2[l].trim());
                                l += 1;
                            }
                        }

                        else
                            line_arr_1.push(line_arr[j]);

                        j += 1;
                    }

                    line_arr = line_arr_1;


                    j = 0;
                    var line_arr_temp = [];
                    while (j < line_arr.length) {
                        if (line_arr[j].trim() != "") {
                            line_arr_temp.push(line_arr[j].trim());
                        }
                        j += 1;
                    }
                    line_arr = line_arr_temp;
                    j = line_arr.length - 1;
                    var flag_index = 0;
                    while (j >= 0) {

                        if ((line_arr[j] + "").search(/\)/) >= 0) {
                            flag_index = j;
                            break;
                        }
                        j -= 1;
                    }

                    var line_1 = line_arr.slice(0, flag_index + 1);
                    var line_2 = line_arr.slice(flag_index + 1, line_arr.length);

                    var depTime = line_1[0];
                    var arrTime = line_1[3];
                    var data_info = formatTime([now_day, depTime, arrTime]);

                    now_day = data_info.now_day;

                    depTime = data_info.depTime;
                    arrTime = data_info.arrTime;

                    segment.arrTime = data_info.arrTime;
                    segment.depTime = data_info.depTime;

                    var depAirport = (line_1[1].replace(/\(/, "")).replace(/\)/, "");
                    var arrAirport = (line_1[4].replace(/\(/, "")).replace(/\)/, "");

                    segment.depAirport = depAirport;
                    segment.arrAirport = arrAirport;


                    //提取飞行飞行时间

                    j = 0;
                    while (j < line_2.length) {
                        if ((line_2[j] + "").search(/:/) >= 0) {
                            break;
                        }
                        j += 1;
                    }

                    var flight_time_arr = line_2.slice(j + 1, line_2.length);

                    segment.flightTime = formatTimeToMinute(flight_time_arr);

                }

                if (node_3 != null || node_3 != undefined) {

                    var stay_data_arr = ((($(node_3).text()).split(":"))[1]).split(" ");

                    var stay_time = formatTimeToMinute(stay_data_arr);

                    segment.stayTime = stay_time;
                }
                else {
                    segment.stayTime = 0;
                }

                //以上为segment的基础数据，下面为其他参数赋值
                segment = assignmentSegment(segment);

                segments.push(segment);
                routing.fromSegments = segments;
                i += 3;

            }

            plan_data_arr.push(routing);

        });
    }

    return plan_data_arr;
}

/**
 * 格式化routeCodes
 * @param plan_data
 * @returns {*}
 */
function formatRouteCodes(plan_data) {

    var i = 0;
    var j = 0;
    var airports = "";
    var cabins = ""; //还提取不了
    var carriers = "";
    var flightNumbers = "";
    var flightTimes = "";
    var marketingCarriers = ""; //默认和carriers相同
    var operatingCarriers = ""; //默认和carriers相同
    var temp_routing = plan_data.routings[i];

    while (i < plan_data.routings.length) {

        airports = "";
        cabins = ""; //还提取不了
        carriers = "";
        flightNumbers = "";
        flightTimes = "";
        marketingCarriers = ""; //默认和carriers相同
        operatingCarriers = ""; //默认和carriers相同
        temp_routing = plan_data.routings[i];

        //从fromSegments中遍历数据拼接airports|carriers|flightNumbers|flightTimes|marketingCarriers|operatingCarriers
        j = 0;
        while (j < temp_routing.fromSegments.length) {

            //设置城市三字码
            temp_routing.fromSegments[j].depCity = CITY_JSON[temp_routing.fromSegments[j].depAirport];
            temp_routing.fromSegments[j].arrCity = CITY_JSON[temp_routing.fromSegments[j].arrAirport];
            temp_routing.fromSegments[j].stopCities = CITY_JSON[temp_routing.fromSegments[j].arrAirport];
            //等于0时拼接规则(拼接airports|carriers|flightNumbers|flightTimes)
            if (j == 0) {
                airports = temp_routing.fromSegments[j].depAirport + "-" + temp_routing.fromSegments[j].arrAirport;
                carriers = temp_routing.fromSegments[j].carrier;
                flightNumbers = temp_routing.fromSegments[j].flightNumber;
                flightTimes = temp_routing.fromSegments[j].depTime + "/" + temp_routing.fromSegments[j].arrTime;
                cabins = temp_routing.fromSegments[j].cabin;
            }
            //不是的情况下直接拼接arrAirport
            else {
                airports += "," + temp_routing.fromSegments[j].depAirport + "-" + temp_routing.fromSegments[j].arrAirport;
                carriers += "," + temp_routing.fromSegments[j].carrier;
                flightNumbers += "," + temp_routing.fromSegments[j].flightNumber;
                flightTimes += "," + temp_routing.fromSegments[j].depTime + "/" + temp_routing.fromSegments[j].arrTime;
                cabins += "," + temp_routing.fromSegments[j].cabin;
            }
            j += 1;
        }

        //如果retSegment不为空则继续拼接,在等于0时加间隔符(_)
        if (temp_routing.retSegments != null) {
            j = 0;
            while (j < temp_routing.retSegments.length) {

                temp_routing.retSegments[j].depCity = CITY_JSON[temp_routing.retSegments[j].depAirport];
                temp_routing.retSegments[j].arrCity = CITY_JSON[temp_routing.retSegments[j].arrAirport];
                temp_routing.retSegments[j].stopCities = CITY_JSON[temp_routing.retSegments[j].arrAirport];

                //等于0时拼接规则(拼接airports|carriers|flightNumbers|flightTimes)
                if (j == 0) {
                    airports += "_" + temp_routing.retSegments[j].depAirport + "-" + temp_routing.retSegments[j].arrAirport;
                    carriers += "_" + temp_routing.retSegments[j].carrier;
                    flightNumbers += "_" + temp_routing.retSegments[j].flightNumber;
                    flightTimes += "_" + temp_routing.retSegments[j].depTime + "/" + temp_routing.retSegments[j].arrTime;
                    cabins += "_" + temp_routing.retSegments[j].cabin;
                }
                //不是的情况下直接拼接
                else {
                    airports += "," + temp_routing.retSegments[j].depAirport + "-" + temp_routing.retSegments[j].arrAirport;
                    carriers += "," + temp_routing.retSegments[j].carrier;
                    flightNumbers += "," + temp_routing.retSegments[j].flightNumber;
                    flightTimes += "," + temp_routing.retSegments[j].depTime + "/" + temp_routing.retSegments[j].arrTime;
                    cabins += "," + temp_routing.retSegments[j].cabin;
                }
                j += 1;
            }
        }

        //将拼接好的数据赋值给routing
        temp_routing.routeCodes.airports = airports;
        temp_routing.routeCodes.carriers = carriers;
        //注意:marketingCarriers|operatingCarriers和carriers数据相同,全用carriers赋值
        temp_routing.routeCodes.marketingCarriers = carriers;
        temp_routing.routeCodes.operatingCarriers = carriers;
        temp_routing.routeCodes.flightNumbers = flightNumbers;
        temp_routing.routeCodes.flightTimes = flightTimes;
        temp_routing.routeCodes.cabins = cabins;
        i += 1;
    }
    return plan_data;
}

function start() {

    var plan_data = {
        routings: []
    }

    var from_plan = getPlanInfo("from");
    var ret_plan = getPlanInfo("ret");

    // console.log(from_plan);
    // console.log(ret_plan);

    var i = 0;
    var j = 0;
    var plan_json_arr = {
        routings: [],
    };
    if (ret_plan.length > 0) {
        while (i < from_plan.length) {
            while (j < ret_plan.length) {
                var routing = {
                    fareType: "public",
                    flightClass: "Economy",
                    flightClassCode: "E", //舱等
                    flightOption: "roundTrip", // 飞行方案(往返/单程)
                    fromSegments: from_plan[i].fromSegments,
                    fromPriceInfos: from_plan[i].fromPriceInfos,
                    retSegments: ret_plan[j].fromSegments,
                    retPriceInfos: ret_plan[j].fromPriceInfos,
                    fromTo: "",
                    policy: "",
                    routeCodes: ret_plan[j].routeCodes
                };

                plan_json_arr.routings.push(routing);

                j += 1;
            }
            i += 1;
            j = 0;
        }

        //格式化segment中详细数据


        //格式化routeCodes
        plan_data = formatRouteCodes(plan_data.routings = plan_json_arr);


        return plan_data;
    }
    //格式化routeCodes
    plan_data.routings = from_plan
    plan_data = formatRouteCodes(plan_data);

    return plan_data;
}

return start();
"""