models = {
    'testpolygon' :{
        'provider': 'https://polygon-mumbai.g.alchemy.com/v2/preeNT1ZAP67R6hqiVAqbjyeibl--rtT',
        "gasPrice": 10,        
        'exchangOracleAddr': '0xeec575A29aeD1DD70f9785667063Cc628bD20A8D',
        'executorAddr': '0xA2c60875DC8d2053135F1EA237ab99147782b8eD',
        'routers': [
            {
                'name': 'QuickSwap',
                'address': '0x8954AfA98594b838bda56FE4C12a09D7739D179b',
                'r': 0.9970,
            },
            {
                'name': 'ApeSwap',
                'address': '0x8fCf4B197A9Df7ab4ed511932cA6c8E1a8fe2F1d',
                'r': 0.9980,
            },
        ],
        'bases': [
            {
                'name': 'myBTC',
                'address': '0x47FF7692217d941bD741E92a9A5dcFDe86E788AB',
                'decimals': 18,
            },
        ],
        'sides' : [
            {
                'name': 'myUSDT',
                'address': '0x02a52E76fA17Cc920d3EBac4aa8E97bca5876156',
                'decimals': 6,
                'minAmount': 100,
            },
        ],
    },
    'polygon': {
        'provider': 'http://localhost:8545',
        "gasPrice": 2000,        
        'exchangOracleAddr': '0xDc0aDF2c6bA9883D80cEa9695Da5E53943f679BA',
        'executorAddr': '0xAd213a8f2161beeA997159BF74e7Fdc450665d98',
        'routers': [
            {
                'name': 'QuickSwap',
                'address': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
                'r': 0.9970,
            },
            {
                'name': 'SushiSwap',
                'address': '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506',
                'r': 0.9970,
            },
            {
                'name': 'ApeSwap',
                'address': '0xC0788A3aD43d79aa53B09c2EaCc313A787d1d607',
                'r': 0.9980,
            },
            {
                'name': 'Polycat',
                'address': '0x94930a328162957FF1dd48900aF67B5439336cBD',
                'r': 0.9975,
            },
            {
                'name': 'Dfyn',
                'address': '0xA102072A4C07F06EC3B4900FDC4C7B80b6c57429',
                'r': 0.9970,
            },
            {
                'name': 'Jetswap',
                'address':'0x5C6EC38fb0e2609672BDf628B1fD605A523E5923',
                'r': 0.9970,
            },
            {
                'name': 'WaltSwap',
                'address':'0x3a1D87f206D12415f5b0A33E786967680AAb4f6d',
                'r': 0.9970,
            },
            
        ],
      
        'bases': [
            {
  'address': "0x001479933C26FeB43A410B3C935df2a0B49C48BC",
  'name': "AMIIBO",
  #'name'l: "Amiibo Token",
  'decimals': 18
},
{
  'address': "0x0074B9a846B5A3a2767aFE7E4d9A4e56191a5393",
  'name': "coal",
  #'name'l: "coal",
  'decimals': 0
},
{
  'address': "0x00d12c0288BFF7af3D8BfcC75CD1fB990aB66EA7",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x01079bDd1d42944C96EDb69B2514561433860F0A",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x0184316f58B9A44aCDD3e683257259dC0CF2202a",
  'name': "POLYGOLD",
  #'name'l: "PolyGold Token",
  'decimals': 18
},
{
  'address': "0x01D91Ca48333aff0EB62B78dC9cd93e60d2Dc91E",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x022bEe2EfAbEE77c04B63134218E08447aC71B0e",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x0249411013A0cc18e848E1dB3f8E992eD5fa1196",
  'name': "CTK",
  #'name'l: "CamiloToken",
  'decimals': 18
},
{
  'address': "0x0266cF816E214a5Bb0B95e97b8Ee917376b314E6",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x0361BdEAB89DF6BBcc52c43589FABba5143d19dD",
  'name': "dTOP",
  #'name'l: "dHEDGE Top Index (PoS)",
  'decimals': 18
},
{
  'address': "0x03Bc3f7AFfBE592E3F3502Cf818AAfB93b12334c",
  'name': "JUL",
  #'name'l: "JULSwap (PoS)",
  'decimals': 18
},
{
  'address': "0x049f12F5a27132d06DE128D48a914F6D82D33D23",
  'name': "JulD",
  #'name'l: "JulSwap (PoS)",
  'decimals': 18
},
{
  'address': "0x053D48C6cEc32346B5EAD0b65b99EDbE4F3B6221",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x05613bfe8e21B4064C6F5F0e967830Fb20428E8A",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x0621d647cecbFb64b79E44302c1933cB4f27054d",
  'name': "AMP",
  #'name'l: "Amp Token (PoS)",
  'decimals': 18
},
{
  'address': "0x06D0E50633790B23C3eE8570d59d7b2426539a64",
  'name': "YELD",
  #'name'l: "Polyyeld finance",
  'decimals': 18
},
{
  'address': "0x071FAb39F04f436dA2C94E6BEDe9D9C40816b722",
  'name': "BTRG",
  #'name'l: "BotRug",
  'decimals': 18
},
{
  'address': "0x074BB8E730C1F9853508D17C54478373fCF71b4D",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x075dFB346a51E73615fBfd8dd2F7949bEe5Dd872",
  'name': "azure bluet",
  #'name'l: "azure bluet",
  'decimals': 0
},
{
  'address': "0x07738Eb4ce8932CA961c815Cb12C9d4ab5Bd0Da4",
  'name': "ELET",
  #'name'l: "Elementeum (PoS)",
  'decimals': 18
},
{
  'address': "0x07ee4bB2750A897A5A7f0c3eF3b1f97F446F30ec",
  'name': "suicide",
  #'name'l: "suicide",
  'decimals': 18
},
{
  'address': "0x07F9eDAE4FB6422B09e82e9A700d90a6432F6cC5",
  'name': "PDUCK",
  #'name'l: "PolyDuck",
  'decimals': 18
},
{
  'address': "0x0833E165255E21a9e81f2D4D6bD10C43973c6526",
  'name': "CPTE",
  #'name'l: "Crypto puzzles (PoS)",
  'decimals': 18
},
{
  'address': "0x08c2526eE32A2F3902b5F225d09F3f9CEc4Ef02a",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x08e175A1eac9744a0F1cCaeb8F669af6a2BDa3Ce",
  'name': "E8",
  #'name'l: "Energy8",
  'decimals': 9
},
{
  'address': "0x08e4AF01d81E1d7bE0aeea814b9ac07A825f3e91",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x0a2eE6F68359f30Cc98E4C6aE54c1ffda645Af09",
  'name': "DT2",
  #'name'l: "DummyToken2",
  'decimals': 18
},
{
  'address': "0x0B0abbb41b5bC851e70C7ed21D259F136118D498",
  'name': "I♡U",
  #'name'l: "~♡♥ⓛⓞⓥⓔ♥♡~ (PoS)",
  'decimals': 18
},
{
  'address': "0x0b3F868E0BE5597D5DB7fEB59E1CADBb0fdDa50a",
  'name': "SUSHI",
  #'name'l: "SushiToken (PoS)",
  'decimals': 18
},
{
  'address': "0x0c28a2E81581BC924Df2520234315a2085e4E8e8",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x0c8C8Ae8bc3a69dC8482C01CEacfB588bb516B01",
  'name': "AURORA",
  #'name'l: "AuroraToken",
  'decimals': 18
},
{
  'address': "0x0cae44BFb0828B0B11dB587D1E1859206B4Ed403",
  'name': "FRO",
  #'name'l: "Froggy",
  'decimals': 18
},
{
  'address': "0x0D0ccc4FDE5a48d710cD821911d2aF1C58Eb7a1b",
  'name': "??",
  #'name'l: "Double Barrel",
  'decimals': 9
},
{
  'address': "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270",
  'name': "WMATIC",
  #'name'l: "Wrapped Matic",
  'decimals': 18
},
{
  'address': "0x0d962A1A2A27B402e4D84772dea65Ac8592Eb6bF",
  'name': "GMS",
  #'name'l: "Gemstones",
  'decimals': 18
},
{
  'address': "0x0E138198446818Ff5710e963a9e7F98eEf868C6F",
  'name': "TKN3",
  #'name'l: "ERC20 Test Token 3",
  'decimals': 18
},
{
  'address': "0x0e2499CB0f238a734463D79Da79606AAC8a103fd",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x0e2BE5729A37851D79F66B38BAC5fEe0353E65A3",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x0e59D50adD2d90f5111aca875baE0a72D95B4762",
  'name': "DB",
  #'name'l: "Dark.Build",
  'decimals': 18
},
{
  'address': "0x0e59eEDB3e852A3865457E8c3C735E5a47363F67",
  'name': "tHODL",
  #'name'l: "MegaTEST",
  'decimals': 9
},
{
  'address': "0x0e5A4b999807D1beda3be634097F246d13CC0103",
  'name': "XDO",
  #'name'l: "XDO",
  'decimals': 18
},
{
  'address': "0x0e6D04F74843214C7e00BAc8e7697C1a45574EE0",
  'name': "polyBUNNY",
  #'name'l: "Polygon BUNNY Token",
  'decimals': 18
},
{
  'address': "0x0EBB689C2Ca6B17bd98b29923802060bE3dc7c58",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x0F38dB64E04Bcd5373dCdF941Fd909d8436f4fdb",
  'name': "TNG",
  #'name'l: "TNodeGreen (PoS)",
  'decimals': 8
},
{
  'address': "0x0f4044F4475B7eC4bdE170146ad02A9cD3ad4853",
  'name': "FCAT",
  #'name'l: "Fortune Cat Coin (PoS)",
  'decimals': 18
},
{
  'address': "0x0F5CCF020db1834eFBe41192BBb45b767FDcE7A4",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x0fBff4691AE67eBC8B0ad95b3922AFc9493BC622",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x0FcaEfCd179261D02f8a8586cb33787898F9FC76",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x0feb4032F645210D1783Bf5A532B9653111661Df",
  'name': "dftest",
  #'name'l: "test1",
  'decimals': 18
},
{
  'address': "0x101A023270368c0D50BFfb62780F4aFd4ea79C35",
  'name': "ANKR",
  #'name'l: "Ankr (PoS)",
  'decimals': 18
},
{
  'address': "0x1028bd06bEDaA61De712e880E1D54EbeC981Ca88",
  'name': "normal minecart rail block",
  #'name'l: "normal minecart rail block",
  'decimals': 0
},
{
  'address': "0x104592a158490a9228070E0A8e5343B499e125D0",
  'name': "FRAX",
  #'name'l: "Frax (PoS)",
  'decimals': 18
},
{
  'address': "0x110b6Ffe819d3e826d13A26F8CF7Dff1D53c21b7",
  'name': "Grass",
  #'name'l: "PolyGrass",
  'decimals': 18
},
{
  'address': "0x1132f58810Ee9fF13E97aECCd8DDa688Cc5eb8F4",
  'name': "SRAT",
  #'name'l: "SpaceRat",
  'decimals': 9
},
{
  'address': "0x1142146FAf2c25D713bcDf72c7C68Ad78885ecd4",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x11602A402281974a70C2B4824d58ebeDe967E2bE",
  'name': "BYN",
  #'name'l: "Beyond Finance (PoS)",
  'decimals': 18
},
{
  'address': "0x1221591c1d77A9c334aBb0fe530ae6EE3aF51Af9",
  'name': "AXMATIC",
  #'name'l: "axMatic",
  'decimals': 18
},
{
  'address': "0x12d191209af9C3A91528738f2fc277F89e9fABE7",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x13436a3c5c2574C8145222260B0ed4C2Da31f760",
  'name': "TRZ",
  #'name'l: "PolyTreasure Token",
  'decimals': 18
},
{
  'address': "0x13748d548D95D78a3c83fe3F32604B4796CFfa23",
  'name': "KOGECOIN",
  #'name'l: "kogecoin.io",
  'decimals': 9
},
{
  'address': "0x1379E8886A944d2D9d440b3d88DF536Aea08d9F3",
  'name': "MYST",
  #'name'l: "Mysterium (PoS)",
  'decimals': 18
},
{
  'address': "0x137Ee749f0F8c2eD34cA00dE33BB59E3dafA494A",
  'name': "wCCX",
  #'name'l: "WrappedConceal",
  'decimals': 6
},
{
  'address': "0x14743E1c6f812154F7ecc980D890F0F5234103e7",
  'name': "APYS",
  #'name'l: "APYSwap",
  'decimals': 18
},
{
  'address': "0x1488C7Cdee1B8b534A1789E9da8B447C7999e04b",
  'name': "ET",
  #'name'l: "Ethlings Token",
  'decimals': 18
},
{
  'address': "0x149eaDE9b543779AE20562f7F1FcFEBF520F6A54",
  'name': "EGG",
  #'name'l: "Egg",
  'decimals': 18
},
{
  'address': "0x14ea7eC625A84491Ab0D4AC4475c90368613151B",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x15498F19e97Da374Dcd758cAFe53a3cDfdfebba6",
  'name': "YQTEST1",
  #'name'l: "YQTEST1",
  'decimals': 18
},
{
  'address': "0x15b1296c3858787bf00b627DF955a93bbE18D789",
  'name': "PNF",
  #'name'l: "PolyNFT",
  'decimals': 18
},
{
  'address': "0x161c0EcE60dCFcdC3e4BDd5F1cDe3eD2f68285A9",
  'name': "GEN",
  #'name'l: "Gen Token",
  'decimals': 18
},
{
  'address': "0x16247C17704eB706816162A25372B6Da70e275eE",
  'name': "YQTEST3",
  #'name'l: "YQTEST3",
  'decimals': 18
},
{
  'address': "0x172370d5Cd63279eFa6d502DAB29171933a610AF",
  'name': "CRV",
  #'name'l: "CRV (PoS)",
  'decimals': 18
},
{
  'address': "0x175Bdc4e52EECB675B86FC4C9A3Ea3f80adBb610",
  'name': "HXN",
  #'name'l: "Havens Nook (PoS)",
  'decimals': 18
},
{
  'address': "0x1783362A37F5205AA63Fc1d327543e2BE9649561",
  'name': "gravel block",
  #'name'l: "gravel block",
  'decimals': 0
},
{
  'address': "0x17D342b29F054030a455b4191f977C3b0aA62Fd9",
  'name': "KNG",
  #'name'l: "Kanga Exchange Token (PoS)",
  'decimals': 18
},
{
  'address': "0x18C4315847Cf73D5028c8A98EAd16e862450E618",
  'name': "pDAI",
  #'name'l: "Pod Dai Stablecoin (PoS)",
  'decimals': 18
},
{
  'address': "0x190c059a603FC7a6c97457C8fd31f8873a5BaCb2",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x194A6B2F3DeFF0f8fE8DA1A9B2c46BdfFC03d115",
  'name': "YQTEST2",
  #'name'l: "YQTEST2",
  'decimals': 18
},
{
  'address': "0x194e4341320CFFbfb4F011053C4f8DD4fE62b3AE",
  'name': "INS5",
  #'name'l: "Inspector5",
  'decimals': 18
},
{
  'address': "0x19A935CbAaa4099072479d521962588D7857D717",
  'name': "LitCoin",
  #'name'l: "LitCoin",
  'decimals': 18
},
{
  'address': "0x1a13F4Ca1d028320A707D99520AbFefca3998b7F",
  'name': "amUSDC",
  #'name'l: "Aave Matic Market USDC",
  'decimals': 6
},
{
  'address': "0x1A1A5D121D5EbEBD0761D95E332E7f57AC4462a9",
  'name': "MOCHA",
  #'name'l: "MOCHA",
  'decimals': 18
},
{
  'address': "0x1A83B5A84e496843C241fdC4CB90AE43894f1Cc7",
  'name': "PZK",
  #'name'l: "PolyZik",
  'decimals': 18
},
{
  'address': "0x1a9B17334e7f2EE399888cf855C726d77aA93E0A",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x1B30e875754aaD79A55929EcfC24f4bd1cd40C08",
  'name': "ANKR",
  #'name'l: "Ankr",
  'decimals': 18
},
{
  'address': "0x1B68CE222a64E96ADF6f40c87a201Eaa14f197cC",
  'name': "KODK",
  #'name'l: "Kodak Black Token",
  'decimals': 18
},
{
  'address': "0x1B815d120B3eF02039Ee11dC2d33DE7aA4a8C603",
  'name': "WOO",
  #'name'l: "Wootrade Network (PoS)",
  'decimals': 18
},
{
  'address': "0x1Ba3510A9ceEb72E5CdBa8bcdDe9647E1f20fB4b",
  'name': "DRAX",
  #'name'l: "Drax",
  'decimals': 18
},
{
  'address': "0x1baAf985B1B21a56CF5B78E9bFca9AF1e9b08905",
  'name': "Topia",
  #'name'l: "Polytopia Doge",
  'decimals': 18
},
{
  'address': "0x1BcC2d99D934b98CEBDF76A91db2C812B80F7590",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6",
  'name': "WBTC",
  #'name'l: "(PoS) Wrapped BTC",
  'decimals': 8
},
{
  'address': "0x1c40Ac03AacAF5F85808674E526E9c26309DB92F",
  'name': "MALT",
  #'name'l: "Malt Stablecoin",
  'decimals': 18
},
{
  'address': "0x1cC193c8c8f9F01fa90DE8A11FB9eFB865310F04",
  'name': "YQTEST2",
  #'name'l: "YQTEST2",
  'decimals': 18
},
{
  'address': "0x1Cd70232Ca5D2221628CFD46011e1FFBfc1e6c53",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x1d2a0E5EC8E5bBDCA5CB219e649B565d8e5c3360",
  'name': "amAAVE",
  #'name'l: "Aave Matic Market AAVE",
  'decimals': 18
},
{
  'address': "0x1d4D7804e0A63D7C496675A7dAE79855162e9961",
  'name': "VOLY",
  #'name'l: "Voly",
  'decimals': 18
},
{
  'address': "0x1D7fAB8A6741026D8FDBef52f90452b09bF582db",
  'name': "BONE",
  #'name'l: "Bone Token",
  'decimals': 18
},
{
  'address': "0x1E42EDbe5376e717C1B22904C59e406426E8173F",
  'name': "SURF",
  #'name'l: "SURF.Finance (PoS)",
  'decimals': 18
},
{
  'address': "0x1E75b69c447128d820f2C14DAD79041eDCe421E0",
  'name': "HBD21STJUNEI",
  #'name'l: "Junei21stYearOnEarth",
  'decimals': 18
},
{
  'address': "0x1f02fD6090D3975290bC3FB90eC8f68d57520568",
  'name': "POLYAPE",
  #'name'l: "PolyApe Token",
  'decimals': 18
},
{
  'address': "0x1faF10ECec8F59aa224bC2790507D03d8F037c16",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x1Ff1cd3b9a6e58675EDE956F3d6eB6f81EDf2913",
  'name': "PEURO",
  #'name'l: "PolyEuro",
  'decimals': 18
},
{
  'address': "0x203870159640BBE89717c8D837FDEE444717c388",
  'name': "BREW",
  #'name'l: "BREW",
  'decimals': 18
},
{
  'address': "0x204C4991D4E18EcE2e5d3E807431A06ef014c855",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x205e148bbd69cf9602B0caAEFd0D86BA47A6DC56",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x2086C6e9fA5a6DE0F49909a31FF563407bCecc52",
  'name': "FTW",
  #'name'l: "FuckTheWards",
  'decimals': 18
},
{
  'address': "0x20D3922b4a1A8560E1aC99FBA4faDe0c849e2142",
  'name': "maWETH",
  #'name'l: "Matic Aave interest bearing WETH",
  'decimals': 18
},
{
  'address': "0x21a20282Da8a76D8D21cc39CE11eB271B45Bf052",
  'name': "sugar cane",
  #'name'l: "sugar cane",
  'decimals': 0
},
{
  'address': "0x21f203DC627F838B683b6a297a54070CcCB09d62",
  'name': "TBO",
  #'name'l: "TBO Token",
  'decimals': 18
},
{
  'address': "0x2229611cFbB9F59F1224CF7E4f703C0347B1Ef0D",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x226f28b89f907c1B6D4c91a3d150669Aad4f5670",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x22Fa6143B3e8cd8c928F77A9326f1300ADc7b4d7",
  'name': "PUSSY",
  #'name'l: "Pussy",
  'decimals': 18
},
{
  'address': "0x235b952678e9C878623A5e8a166571C9225DC098",
  'name': "POLM",
  #'name'l: "PolyMoon",
  'decimals': 18
},
{
  'address': "0x237e67b2A36EC7Fdf326F6AA263214D5237142aF",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x23D29D30e35C5e8D321e1dc9A8a61BFD846D4C5C",
  'name': "HEX",
  #'name'l: "HEX (PoS)",
  'decimals': 8
},
{
  'address': "0x24328c46a0E00536Eb001c28E8ED28F9e20fC91A",
  'name': "RANGER",
  #'name'l: "Ranger Token",
  'decimals': 18
},
{
  'address': "0x24792302477Ec0e95dEE67ffD01549774ce55BF5",
  'name': "CRT",
  #'name'l: "CrypToads (PoS)",
  'decimals': 18
},
{
  'address': "0x24d30E9814FA87Dacf4E824F1D36d3bdD74CCa1D",
  'name': "MAMONA",
  #'name'l: "MAMONA",
  'decimals': 9
},
{
  'address': "0x2574eCE38AFE4F7a454f3842CF2c8e12016b873a",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x25788a1a171ec66Da6502f9975a15B609fF54CF6",
  'name': "POOL",
  #'name'l: "PoolTogether (PoS)",
  'decimals': 18
},
{
  'address': "0x25c99AFc8Fd2a4b34a9af10d00612C3f79622c88",
  'name': "GBE",
  #'name'l: "Goodbye",
  'decimals': 18
},
{
  'address': "0x25e843D1e42C07Ec4847AA449fAC41501f36f0dE",
  'name': "0XE",
  #'name'l: "0xUniverse Energy",
  'decimals': 9
},
{
  'address': "0x25Efa48558849710C39f8526e5caa9fcc9942Bd3",
  'name': "MOBIUS",
  #'name'l: "https://t.me/mobius_finance",
  'decimals': 9
},
{
  'address': "0x261Be0720d3874FE83D1320Fa33AF6859962E260",
  'name': "TestxUSD",
  #'name'l: "Test xUSD",
  'decimals': 18
},
{
  'address': "0x26d29C89AffB567592E0a04c882bc28D299126da",
  'name': "MEOWB",
  #'name'l: "MeowMeowfinance",
  'decimals': 18
},
{
  'address': "0x2727Ab1c2D22170ABc9b595177B2D5C6E1Ab7B7B",
  'name': "CTSI",
  #'name'l: "Cartesi Token (PoS)",
  'decimals': 18
},
{
  'address': "0x274089A95B8d82Ba7F11FDD661d8Ca4df899Ae0D",
  'name': "GODS",
  #'name'l: "PolyGods Token",
  'decimals': 9
},
{
  'address': "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  'name': "USDC",
  #'name'l: "USD Coin (PoS)",
  'decimals': 6
},
{
  'address': "0x27f795269406cdE4E1E7a0B619C0a50bd41b0D28",
  'name': "?",
  #'name'l: "Harvester DAO",
  'decimals': 18
},
{
  'address': "0x27F8D03b3a2196956ED754baDc28D73be8830A6e",
  'name': "amDAI",
  #'name'l: "Aave Matic Market DAI",
  'decimals': 18
},
{
  'address': "0x282D02D155657C95EC88AaD5A1D4413E646563Cf",
  'name': "PolySave",
  #'name'l: "PolySave",
  'decimals': 9
},
{
  'address': "0x28dD2A1a85A05A2e047759946f0A772d32e3B92b",
  'name': "xUSD",
  #'name'l: "xUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0x29d040b14710432ce07bAbc0C997c80DD64f2c9f",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x29Df98eC262aC614A7ceE6E16Ec698902c79FF78",
  'name': "ACDC",
  #'name'l: "Adept Camp Dog Coin",
  'decimals': 18
},
{
  'address': "0x29f4919a51C59f3e8dfc7fcFb2a3C5922Fb6a438",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x2A0Ec5e6977A8A343BD6E1D0fD6F0b5683fDa606",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x2A36Af6a4ac9518c1748722EE4c094DA2C1df66B",
  'name': "WATER",
  #'name'l: "WaterPoly",
  'decimals': 18
},
{
  'address': "0x2a93172c8DCCbfBC60a39d56183B7279a2F647b4",
  'name': "$DG",
  #'name'l: "decentral.games (PoS)",
  'decimals': 18
},
{
  'address': "0x2b08D397f86a8AE168493AeDC40CE9c8c200E2da",
  'name': "TEST",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0x2C57FC7dB9AA0e56027CdF433bbb0bf2614CCD36",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x2C9870Fa099AE4206b472575b06033E00957BA9D",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x2CbD327697aDC0d18A4AC1741075b60A230D8e01",
  'name': "DAR",
  #'name'l: "DiscovAR",
  'decimals': 18
},
{
  'address': "0x2DC6123A5c521Ccab4E191C9CEcde3df5814488f",
  'name': "?",
  #'name'l: "Polymoon",
  'decimals': 9
},
{
  'address': "0x2E2C78e5f7C7822B4664f61aC424c1cC4320C8a8",
  'name': "YQTEST3",
  #'name'l: "YQTEST3",
  'decimals': 18
},
{
  'address': "0x2e2DDe47952b9c7deFDE7424d00dD2341AD927Ca",
  'name': "CHUM",
  #'name'l: "ChumHum",
  'decimals': 18
},
{
  'address': "0x2e4b0Fb46a46C90CB410FE676f24E466753B469f",
  'name': "UMBR",
  #'name'l: "UmbriaToken (PoS)",
  'decimals': 18
},
{
  'address': "0x2E82608CAE06eA0922cc4bb5Afc4352112819EFC",
  'name': "PANINI",
  #'name'l: "Panini",
  'decimals': 18
},
{
  'address': "0x2F6714f7897F4C7BB176108098Ab145df7fE1899",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x3053ad3b31600074e9A90440770f78D5e8Fc5A54",
  'name': "WAULTx",
  #'name'l: "Wault",
  'decimals': 18
},
{
  'address': "0x30A8e1c256143AD440faa9042722929B0BC0Fc7D",
  'name': "bat",
  #'name'l: "bat token (PoS)",
  'decimals': 18
},
{
  'address': "0x310aC0ad148c2E9F4071f29cCfDF48a62B14327C",
  'name': "CHESS",
  #'name'l: "PolyChess Token",
  'decimals': 18
},
{
  'address': "0x311E0296CD0039C63974996c905352eB61FC2562",
  'name': "GAME",
  #'name'l: "PolyGamer Token",
  'decimals': 18
},
{
  'address': "0x316B4DB72EC7eacDB6E998257c4349C2B08fF27D",
  'name': "?",
  #'name'l: "Harvester DAO",
  'decimals': 18
},
{
  'address': "0x31a0D1A199631D244761EEba67e8501296d2E383",
  'name': "renZEC",
  #'name'l: "renZEC",
  'decimals': 8
},
{
  'address': "0x31aeCC5DFf1daF9ac8D315F84c1916c39464A659",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x31C362b577F0346318f258C7cF21C666Aa1F49e3",
  'name': "POP",
  #'name'l: "Poppins",
  'decimals': 18
},
{
  'address': "0x327Dc1Eb7d2eBfCd8492ac5Da4aC2e652cEa01E3",
  'name': "POLYRISE",
  #'name'l: "PolyRise",
  'decimals': 9
},
{
  'address': "0x32b85D4432DC49764C8fB4F227dcE4E5EA53A6ca",
  'name': "SPAM",
  #'name'l: "SPAM",
  'decimals': 18
},
{
  'address': "0x32Cd79c55eB2c55F532d9F9C893CB1F629bA8409",
  'name': "?",
  #'name'l: "Oil",
  'decimals': 9
},
{
  'address': "0x32F187a0888df63c0367C7793f7EED9DA1FE40F2",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x33441254a393B794842d0084e32469d0D77d2122",
  'name': "CAR",
  #'name'l: "PolyCar",
  'decimals': 8
},
{
  'address': "0x334D7Ae7F1D21CeB74537391558Ce57bbF3cCf73",
  'name': "AXS",
  #'name'l: "Axie Infinity Shard (PoS)",
  'decimals': 18
},
{
  'address': "0x34053687297673b2864F7086D65bD81aEe310CF4",
  'name': "XOXO",
  #'name'l: "Hugs n Kisses",
  'decimals': 9
},
{
  'address': "0x3459D8be27468A1e29F0885593cdfE50EcCDd708",
  'name': "carrot",
  #'name'l: "carrot",
  'decimals': 0
},
{
  'address': "0x349f520E9c64fedD84891E610929cB5F00664b17",
  'name': "JAVA",
  #'name'l: "JAVA",
  'decimals': 18
},
{
  'address': "0x34bcfa3835B159AB176dB1BE26d532b4369BCD15",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x34BDC06A7faD24E14D719BB7ab0E391cbc345d36",
  'name': "CUBAN",
  #'name'l: "CubanCoin",
  'decimals': 9
},
{
  'address': "0x34c41776FE94Ef35638C537776617bF179212f60",
  'name': "PINGU",
  #'name'l: "PolyPingu",
  'decimals': 18
},
{
  'address': "0x34E111E98DB3EeE694FB63D8e72DdBbCD5f42D0C",
  'name': "POMME",
  #'name'l: "POMME Token",
  'decimals': 18
},
{
  'address': "0x34Ee768f554d4d3249c81B42f6219f80d86380eb",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x35a5cEfbd9342D9F31be2654aDEdc8d755fbC217",
  'name': "MGC",
  #'name'l: "TestMGC",
  'decimals': 18
},
{
  'address': "0x35ebc8AbD1205e153b9f0fD16669eCFC31d3EF23",
  'name': "PPP",
  #'name'l: "PolyPump",
  'decimals': 18
},
{
  'address': "0x361d59565DdCEa2e9C2AFe98bbF4298984E1cBbe",
  'name': "DILLY",
  #'name'l: "Dilly",
  'decimals': 9
},
{
  'address': "0x36461570197d07c0431A53FbbC01529ed6ea747A",
  'name': "GMS",
  #'name'l: "Gemstones Token",
  'decimals': 9
},
{
  'address': "0x367438593610116eDF55Efc9f8035B6b6E906ec5",
  'name': "USDTEST3",
  #'name'l: "USDTEST3",
  'decimals': 18
},
{
  'address': "0x368899081A923260c8ecE2eB0c2d146D4a7C918E",
  'name': "SEM",
  #'name'l: "ShibaElonMars",
  'decimals': 18
},
{
  'address': "0x370c2154aAad8F3F7F47909Aa14758ea8E4C7003",
  'name': "CYO",
  #'name'l: "Cogoyaso",
  'decimals': 18
},
{
  'address': "0x3720B84e32C201eb864b8B92ba74C0a3476C2a43",
  'name': "FOX",
  #'name'l: "Fox Token",
  'decimals': 18
},
{
  'address': "0x37924E552e0471002a4AFF038717Df0468284676",
  'name': "mDOLLY",
  #'name'l: "Dolly Stable Coin on Matic",
  'decimals': 18
},
{
  'address': "0x37B5f741371ABf2207D236B6309d7D2015Bd64e9",
  'name': "OCTT",
  #'name'l: "Octett (PoS)",
  'decimals': 18
},
{
  'address': "0x37Ce06811dD156d72015870cdC0237d3FA2CF742",
  'name': "LOL",
  #'name'l: "LOL",
  'decimals': 8
},
{
  'address': "0x37e155D9BF75C6bB9e2d089a3865AB284B434352",
  'name': "ASHES",
  #'name'l: "Phoenix",
  'decimals': 18
},
{
  'address': "0x3809dcDd5dDe24B37AbE64A5a339784c3323c44F",
  'name': "SWAP",
  #'name'l: "TrustSwap Token (PoS)",
  'decimals': 18
},
{
  'address': "0x380A38C91c5C183E4e845861ff752142fd396264",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x385Eeac5cB85A38A9a07A70c73e0a3271CfB54A7",
  'name': "GHST",
  #'name'l: "Aavegotchi GHST Token (PoS)",
  'decimals': 18
},
{
  'address': "0x393B76729738a70F4Eaca61BD2734c3F83f3Ba48",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x3a3Df212b7AA91Aa0402B9035b098891d276572B",
  'name': "FISH",
  #'name'l: "Fish",
  'decimals': 18
},
{
  'address': "0x3A3e7650f8B9f667dA98F236010fBf44Ee4B2975",
  'name': "xUSD",
  #'name'l: "xDollar Stablecoin",
  'decimals': 18
},
{
  'address': "0x3a707448eA37785bC043931A5f51ae352B1c6C14",
  'name': "DUCKDO",
  #'name'l: "DUCKDO",
  'decimals': 18
},
{
  'address': "0x3aD3DadDcaF1fD8E59250d1e98F6aDb01BeD2A09",
  'name': "cobblestone block",
  #'name'l: "cobblestone block",
  'decimals': 0
},
{
  'address': "0x3AEF8512Fb6D4231beB786Ef75086951E3ae6362",
  'name': "PolyMoon",
  #'name'l: "PolyMoon",
  'decimals': 9
},
{
  'address': "0x3b00E8EB40fbF935088729a5967C22698F5Da117",
  'name': "WEED",
  #'name'l: "PolyWeed Token",
  'decimals': 18
},
{
  'address': "0x3b17EccCDF836a4a37b002293e0B0aE1B196ae96",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x3b5901A8DeD7F0E685742c26D8eEfeb5B0401Ea7",
  'name': "888",
  #'name'l: "Lucky888",
  'decimals': 18
},
{
  'address': "0x3b65A0830ed558e330c4E38529Eb586d96494689",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x3b9254964275f4A0FE0b4ccEB25DF298333524C2",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x3B9c4715959f8Ad2e0A84A86ED1B73e8D5097f9b",
  'name': "gold ingot",
  #'name'l: "gold ingot",
  'decimals': 0
},
{
  'address': "0x3C1D58c24D9a33bBa6d90E31e3AA828aF33f4F58",
  'name': "FUCK",
  #'name'l: "Finally Usable Crypto Karma (PoS)",
  'decimals': 4
},
{
  'address': "0x3Cef98bb43d732E2F285eE605a8158cDE967D219",
  'name': "BAT",
  #'name'l: "Basic Attention Token (PoS)",
  'decimals': 18
},
{
  'address': "0x3Dc7B06dD0B1f08ef9AcBbD2564f8605b4868EEA",
  'name': "XDO",
  #'name'l: "xDollar",
  'decimals': 18
},
{
  'address': "0x3e121107F6F22DA4911079845a470757aF4e1A1b",
  'name': "FXS",
  #'name'l: "Frax Share (PoS)",
  'decimals': 18
},
{
  'address': "0x3e1BCC93967E585d1B68A12028991D4B91C90028",
  'name': "xUSD",
  #'name'l: "xUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0x3e9d8D160b9E7b7c0FD34dE872671DBA88405313",
  'name': "BRSK",
  #'name'l: "BRSK Token",
  'decimals': 18
},
{
  'address': "0x3f59A4d20123Ac000465319075F3AbA21a9D4E24",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x3fD41b90f3daC0E38A6c4CF1153ff19c73594804",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x40105647e07DD01C1060De8EF9b5358e939e640c",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x40CCD55B789fdEE8D434915dC2Aa6Bd938506A92",
  'name': "RAGE",
  #'name'l: "RAGEMATIC (PoS)",
  'decimals': 18
},
{
  'address': "0x416d092E5A37BF324b55920825c0406f55234e38",
  'name': "EGG",
  #'name'l: "Goose Golden Egg",
  'decimals': 18
},
{
  'address': "0x4225582d127054382161a6499fdb98c8bBcD8aFF",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x4257c2aEEf8e755D45AbB0b6D1BdE56c20D5b313",
  'name': "LEGO",
  #'name'l: "Lego Token",
  'decimals': 18
},
{
  'address': "0x42B365a8c2E21534c520C0eB29ae604a4E82cbA1",
  'name': "TKN4",
  #'name'l: "ERC20 Test Token 4",
  'decimals': 18
},
{
  'address': "0x42CA2D9346148D06Cb9E9b5046963e4687fBF47a",
  'name': "EGO",
  #'name'l: "Ego",
  'decimals': 8
},
{
  'address': "0x43056301e3368F7Aa952b98b28e32380a62a7Ba2",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x43284543540a29De091F0A1526aC033DA423E0E6",
  'name': "SPOLY",
  #'name'l: "SafePoly Token",
  'decimals': 9
},
{
  'address': "0x44c22563730681AaD9c387672c1Ee5589B369180",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x4524a14808159Fd380Ad129dfb17E3d6692E505c",
  'name': "dont 5",
  #'name'l: "dont buy 5",
  'decimals': 18
},
{
  'address': "0x459317986245Db8d2a21dCb0750FAe79f2394240",
  'name': "WTF",
  #'name'l: "WhiteFog",
  'decimals': 18
},
{
  'address': "0x4597c8A59Ab28B36840B82B3A674994A279593D0",
  'name': "COVAL",
  #'name'l: "Circuits of Value V2",
  'decimals': 8
},
{
  'address': "0x459fCB9514747Df1fc46EA435C774B5c09679b55",
  'name': "FNG",
  #'name'l: "Finger",
  'decimals': 18
},
{
  'address': "0x462D8d82C2B2D2DDabf7f8a93928De09d47A5807",
  'name': "BzB",
  #'name'l: "BlazarBits (PoS)",
  'decimals': 18
},
{
  'address': "0x46946564de5A3155d7c053460D24c318303FaF38",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x46e639b0f250DAA920d13c0E679F7Cb90380722d",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x46F48FbdedAa6F5500993BEDE9539ef85F4BeE8e",
  'name': "ARIA20",
  #'name'l: "ARIANEE (PoS)",
  'decimals': 18
},
{
  'address': "0x4709A8f11BF913ecBf2Be53be6d78755dAdFed88",
  'name': "FXW",
  #'name'l: "Foow",
  'decimals': 18
},
{
  'address': "0x475258Fa7c29435223b0D856820acFC6C4E4B6EB",
  'name': "testq",
  #'name'l: "testq",
  'decimals': 9
},
{
  'address': "0x47536F17F4fF30e64A96a7555826b8f9e66ec468",
  'name': "BELUGA",
  #'name'l: "BelugaToken",
  'decimals': 18
},
{
  'address': "0x475DA76bfF2b16fD78D9564795c8Caf962229677",
  'name': "VST",
  #'name'l: "VerySimpleToken",
  'decimals': 9
},
{
  'address': "0x4785EC5823E1962BBa4FB2eEF25863CBCC1eAf9d",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x4878f691640254542A952F684F54d0f293e81Cd8",
  'name': "?",
  #'name'l: "Harvester DAO",
  'decimals': 18
},
{
  'address': "0x48Cc8bF5e8060B067d8AA783E95767FF54d7ba7F",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x48E1EeC032171F871890c86308147032BB246508",
  'name': "rChili",
  #'name'l: "Roasted Chili Token",
  'decimals': 18
},
{
  'address': "0x4950E46007340E82993A7afee26c73Fe2D129B23",
  'name': "TKN3",
  #'name'l: "ERC20 Test Token 3",
  'decimals': 18
},
{
  'address': "0x495f45379E748978E64605e3367dad700aB4d13b",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x4985E0B13554fB521840e893574D3848C10Fcc6f",
  'name': "NCT",
  #'name'l: "Nectar (PoS)",
  'decimals': 18
},
{
  'address': "0x49E4289B4FcB79d69D5d7bA460C7E8F378976d12",
  'name': "MGC",
  #'name'l: "TestMGC",
  'decimals': 18
},
{
  'address': "0x4B1df511d59F5c73a420217cE58a77b462151c9E",
  'name': "PLX",
  #'name'l: "PolyDEX.Fi 2.0",
  'decimals': 18
},
{
  'address': "0x4b56708BcA811ED5851B4E41E99d36bFccBACB9f",
  'name': "PLF",
  #'name'l: "Polyfck",
  'decimals': 18
},
{
  'address': "0x4BB0A0ceF106b0376A9320BE1cF9BCe2D9fC075E",
  'name': "PTC",
  #'name'l: "PeetyCoin (PoS)",
  'decimals': 18
},
{
  'address': "0x4Be4C530624FBB12dE01f935BE5803277484E390",
  'name': "HYN",
  #'name'l: "Hyene",
  'decimals': 18
},
{
  'address': "0x4BEcDD1704e16962053792fd0d6Baa533Daaa702",
  'name': "STONKX",
  #'name'l: "https://stonk.farm STONKX Token",
  'decimals': 18
},
{
  'address': "0x4C0a6D07Cc36e7503cC342556ccEBE3a379EB810",
  'name': "POLAR",
  #'name'l: "Polaris",
  'decimals': 18
},
{
  'address': "0x4C16f69302CcB511c5Fac682c7626B9eF0Dc126a",
  'name': "polyBUNNY",
  #'name'l: "Polygon BUNNY Token",
  'decimals': 18
},
{
  'address': "0x4c4BF319237D98a30A929A96112EfFa8DA3510EB",
  'name': "WEXpoly",
  #'name'l: "WaultSwap Polygon",
  'decimals': 18
},
{
  'address': "0x4d7199f4f3425946B5033652F24F718dc64063E2",
  'name': "USDTEST3",
  #'name'l: "USDTEST3",
  'decimals': 18
},
{
  'address': "0x4Db6764EE6Ade9032E85C20Aaa02DF9cb3cB4f88",
  'name': "ONE",
  #'name'l: "OneBillion",
  'decimals': 18
},
{
  'address': "0x4E6e977798Bc61F82A61c7F6F18cb1AFC35C4A68",
  'name': "MORDOR",
  #'name'l: "Mordor Token",
  'decimals': 18
},
{
  'address': "0x4E70856f091E41f135Eb3143070920e93Ad5f1A1",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x4EaC4c4e9050464067D673102F8E24b2FccEB350",
  'name': "ibBTC",
  #'name'l: "Interest-Bearing BTC",
  'decimals': 18
},
{
  'address': "0x4eB8DC0F7a0575A17F88388c3b5debD04ECd0af2",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x4EF08e36da5bf3Bd32BBA995e3E303712432011A",
  'name': "YOGA",
  #'name'l: "YOGA",
  'decimals': 18
},
{
  'address': "0x4F094C2228E8379d909647dAC521CCA77Ba08Da6",
  'name': "NUKO",
  #'name'l: "NUKO COIN",
  'decimals': 18
},
{
  'address': "0x4F92d29c2D1C101f66271303755925Feb73728E5",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x502a52617983A3d4A170A315DBdAa5764B041C5c",
  'name': "GTST",
  #'name'l: "GTestToken",
  'decimals': 18
},
{
  'address': "0x504E5231891Add3E369dEA0c4c9E373012496185",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x50B728D8D964fd00C2d0AAD81718b71311feF68a",
  'name': "SNX",
  #'name'l: "Synthetix Network Token (PoS)",
  'decimals': 18
},
{
  'address': "0x50e85c54754f3CD1A5b81377D0F57589936Ce5dc",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0x50EDe3FB8b847050D6A108a57D97234aeaE5ec3C",
  'name': "YEARN",
  #'name'l: "PolyYearn Token",
  'decimals': 18
},
{
  'address': "0x512BC507129E74a8BF653ea60774Fa4bf3c1e480",
  'name': "LOCO",
  #'name'l: "Loco Coin",
  'decimals': 18
},
{
  'address': "0x513D1F9DBBBbD0B493fd87b7b07dc17b8A0379f2",
  'name': "GMS",
  #'name'l: "Gemstones Token",
  'decimals': 9
},
{
  'address': "0x5142aaf9C0AD88834df7761B43f6747361B7A479",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0x516f6Cc604803872a5cE3Cd7695fA8D3fBFb520D",
  'name': "ROOSTER",
  #'name'l: "Rooster Token",
  'decimals': 18
},
{
  'address': "0x5173F0054981146D0F831A373E2f2989C5d327Ac",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x521CddC0CBa84F14c69C1E99249F781AA73Ee0BC",
  'name': "HH",
  #'name'l: "Holyheld (PoS)",
  'decimals': 18
},
{
  'address': "0x529A95b9177b782f256E345CeDA3bf0F1743bBbd",
  'name': "TESTFAC",
  #'name'l: "Token Factory Test",
  'decimals': 9
},
{
  'address': "0x52D35F8d328F18B181f680406dFCA482EbB53e9a",
  'name': "ULTM",
  #'name'l: "Ultim",
  'decimals': 18
},
{
  'address': "0x531E38B8d9E5abeA485b18f674A17a0f7086b454",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x5333f226e31A8A1EdC6CFbaAcA21eb403a6D89fe",
  'name': "CMN",
  #'name'l: "https://t.me/CoonMoon",
  'decimals': 18
},
{
  'address': "0x5351801EAcCc08Cbe7881C550ADa6C17dC0DdBe3",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x5357De35CF517e6CEcD91B269eA551caEE4D171C",
  'name': "SKITS",
  #'name'l: "superkittens (PoS)",
  'decimals': 18
},
{
  'address': "0x535BDfF1edED7d279e162e889B6687dCC00d2752",
  'name': "Floki",
  #'name'l: "Floki",
  'decimals': 18
},
{
  'address': "0x53a9b437ea271E11CA06d76D2E36affCCB4D5127",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x53E0bca35eC356BD5ddDFebbD1Fc0fD03FaBad39",
  'name': "LINK",
  #'name'l: "ChainLink Token",
  'decimals': 18
},
{
  'address': "0x541bc4eFbf90345d279E82ce314074A6D7cd36dC",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x541f3deD0B7b6Dcd5ac1F44ad2f2fD99ba8E667d",
  'name': "PIZZA",
  #'name'l: "pizza (PoS)",
  'decimals': 18
},
{
  'address': "0x5479eB1111692F76Ddc2fDDCC0C441d7714438d8",
  'name': "WARHOL20",
  #'name'l: "Wrapped Warhols",
  'decimals': 18
},
{
  'address': "0x556f501CF8a43216Df5bc9cC57Eb04D4FFAA9e6D",
  'name': "DUST",
  #'name'l: "Distant Universe Stardust Token",
  'decimals': 8
},
{
  'address': "0x55f83AD333dDD012Bd136Ecd56A8ed1E354215A5",
  'name': "BSF",
  #'name'l: "BSF Coin",
  'decimals': 18
},
{
  'address': "0x56404395854c6f182c6be3A3cDa354f37B4f185C",
  'name': "EZIOU",
  #'name'l: "EZIOU",
  'decimals': 18
},
{
  'address': "0x56a5e5D7aDd4a4C4464281dCd0dD999C80D06D38",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x570B7315CaCE7Cbe731FDeE4E62C9281bE8B5868",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x57398C6Fc5Fe01E68275b57Dc74e3a51Bd16ce46",
  'name': "Lite",
  #'name'l: "Lite",
  'decimals': 9
},
{
  'address': "0x57d54860Ff3873E1e3142A01ef5FC8EF7b967B5a",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x57ee99B828A2f41c9945efD614Dd370f8A1068f3",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x580A84C73811E1839F75d86d75d88cCa0c241fF4",
  'name': "QI",
  #'name'l: "Qi Dao",
  'decimals': 18
},
{
  'address': "0x581EAfbd81AB898b7086d969083F539F54d6b44B",
  'name': "BLSCN",
  #'name'l: "BerlusCoin",
  'decimals': 18
},
{
  'address': "0x5858CC20870564e7cE17b72caC88631456596126",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x59cffFb43d85CEb32a44C8DA106F88a65d8E9714",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x5A0177A12cDE798e1cEd5e857A23791A54A2237E",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x5a3064CbDCCF428ae907796cF6aD5a664CD7F3d8",
  'name': "PYQ",
  #'name'l: "PYQ",
  'decimals': 18
},
{
  'address': "0x5a30cD5d7471Ebf33fa0f4204aEfDbB47361d765",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x5B0c10270Ae2Ee3DC1003BB1E5Cb63E93306131C",
  'name': "RTRD",
  #'name'l: "Highly Regarded Token (PoS)",
  'decimals': 18
},
{
  'address': "0x5b6ab5078Bd2bbF1A215fFFBa16a94b7DF7F639d",
  'name': "DEFI++",
  #'name'l: "PieDAO DEFI++ (PoS)",
  'decimals': 18
},
{
  'address': "0x5B7C755894E4685eb5361da5A50331878203ce40",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x5Bd32f9C4c11CDa26509656e23EcEC4405c52D2d",
  'name': "oak wood planks",
  #'name'l: "oak wood planks",
  'decimals': 0
},
{
  'address': "0x5c24eA8ce83eFa995C431357790D645abac8C021",
  'name': "redstone item",
  #'name'l: "redstone item",
  'decimals': 0
},
{
  'address': "0x5C7F7Fe4766fE8f0fa9b41E2E4194d939488ff1C",
  'name': "DOKI",
  #'name'l: "DokiDokiFinance (PoS)",
  'decimals': 18
},
{
  'address': "0x5d47bAbA0d66083C52009271faF3F50DCc01023C",
  'name': "BANANA",
  #'name'l: "ApeSwapFinance Banana",
  'decimals': 18
},
{
  'address': "0x5E12f36bF1739A3A740D5916A8b22B0F5275F717",
  'name': "PIE",
  #'name'l: "DeFiPIE Token (PoS)",
  'decimals': 18
},
{
  'address': "0x5Ed1d4D5A6be574ceF49bcA359b881638b4A257D",
  'name': "KONG",
  #'name'l: "Ape Community Token",
  'decimals': 18
},
{
  'address': "0x5EF0eC434Ba786f7D8689552cb7A76110373606f",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x5f020313a18E44a1aB08108d7e58D42bbb5634D5",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x5fe2B58c013d7601147DcdD68C143A77499f5531",
  'name': "GRT",
  #'name'l: "Graph Token (PoS)",
  'decimals': 18
},
{
  'address': "0x6023535715997Fc85f87D321A55C6469e964cCB2",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x607090b0e33847B07d33BBd724a30C97cbb782FF",
  'name': "BM",
  #'name'l: "BlackMoon",
  'decimals': 8
},
{
  'address': "0x60AC2E84078Ce30CBC68e3d7b18bCF613271ce6B",
  'name': "ALOHA",
  #'name'l: "ALOHA",
  'decimals': 18
},
{
  'address': "0x60bB3D364B765C497C8cE50AE0Ae3f0882c5bD05",
  'name': "IMX",
  #'name'l: "Impermax (PoS)",
  'decimals': 18
},
{
  'address': "0x6142F62E7996fAeC5c5BB9D10669d60299D69Dfe",
  'name': "BuySpaceRat",
  #'name'l: "Go Buy SpaceRat at SpaceRat.Finance",
  'decimals': 18
},
{
  'address': "0x6181dEdD5D6aa117716cc385A0184C709b1263F3",
  'name': "wMBX",
  #'name'l: "wMBX Token (PoS)",
  'decimals': 18
},
{
  'address': "0x61c49F0c13e1791b71c32b729C0ff3F37c3B2e16",
  'name': "wUSD",
  #'name'l: "wUSD Stable Coin Poly ",
  'decimals': 18
},
{
  'address': "0x61dAECaB65EE2A1D5b6032df030f3fAA3d116Aa7",
  'name': "DMAGIC",
  #'name'l: "Dark Magic",
  'decimals': 18
},
{
  'address': "0x61Ed1C66239d29Cc93C8597c6167159e8F69a823",
  'name': "RSD",
  #'name'l: "Reference System for DeFi",
  'decimals': 18
},
{
  'address': "0x620390BB3f207CD895a992774c20da3Fa713b905",
  'name': "birch wood planks",
  #'name'l: "birch wood planks",
  'decimals': 0
},
{
  'address': "0x62c9B7442f2F4eDAB196Ce2adA7c1275C3508B52",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x62EF0D91DB70e4349796e87f044E95046CBa4E2E",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x63917A0AA22043c5A0f6ff54cF5D0e8Bc7E3A00e",
  'name': "rLeu",
  #'name'l: "RepescoLeu",
  'decimals': 18
},
{
  'address': "0x63BAAb7A12F4a02C168d078f7aCc37184B7b8B09",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x642F7511a68c57faE8AC0CAa618673a66166e4c7",
  'name': "XRGE",
  #'name'l: "RougeCoin (PoS)",
  'decimals': 18
},
{
  'address': "0x64465665C283bDCA163E8F9D4d759a67B42A747f",
  'name': "WIN",
  #'name'l: "WINDOWS",
  'decimals': 3
},
{
  'address': "0x64d3BB29dB58263B409Ef42B8672a970182FD990",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x656A94de9470DCddf6787d438218134A4709e9BD",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x6571F77c5aDcF257cDff577F97A378D8D6dF2cA4",
  'name': "YQTEST3",
  #'name'l: "YQTEST3",
  'decimals': 18
},
{
  'address': "0x6575202061d509D1ddF8F19EccA736889F01aF06",
  'name': "CNET",
  #'name'l: "Coraline-Network",
  'decimals': 18
},
{
  'address': "0x65d8a500e77513c02CF7F840649EF1b52aA38FaE",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x664ddCeD875f31002DAC4EC8e2e441F4B84c1dfF",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x664F1266D3C212E8b21c876efa2e750b93a4164f",
  'name': "?",
  #'name'l: "?‍?",
  'decimals': 18
},
{
  'address': "0x66768ad00746aC4d68ded9f64886d55d5243f5Ec",
  'name': "mRBAL",
  #'name'l: "Matic Rebalance Token",
  'decimals': 18
},
{
  'address': "0x667d1D397847b12cC24C351755AAaA7A4e3BcfCA",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x66821011617206F914dE76D9b9036de7732463e9",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x669e912F53cEF368fdB07774D7624B4DEbA45728",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x671A17f9CE500a76cD75d7C79268e681b14b4fa6",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x6742Cc2A8F5B9A6a4e49fcbF186937efCDb0eAe4",
  'name': "raw granite",
  #'name'l: "raw granite",
  'decimals': 0
},
{
  'address': "0x678A1037652350E1d1E04245faC0736e654d4cc6",
  'name': "MEOWB",
  #'name'l: "Meow Meow Coin",
  'decimals': 18
},
{
  'address': "0x678e5f70b6b582dfADB3dBD68AF17801d34555c5",
  'name': "REVO",
  #'name'l: "RevoNetwork",
  'decimals': 18
},
{
  'address': "0x67f287514281d8919f51c70C665fB80363D5ED53",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x682a4ea8A11e966ac307bB0A7D131C9B180357e4",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x6871B66eB20bB9743512A2DB7899F6a7caBb267a",
  'name': "?",
  #'name'l: "Moonshine",
  'decimals': 9
},
{
  'address': "0x68f044B59D96ec856aC72C29Df997348c8C1fFf3",
  'name': "BPUL",
  #'name'l: "BetaPulsarToken",
  'decimals': 18
},
{
  'address': "0x68Fd8313439ed23465aD53863AB74BeA232Cd91D",
  'name': "EGG",
  #'name'l: "Goose Golden Egg",
  'decimals': 18
},
{
  'address': "0x692597b009d13C4049a947CAB2239b7d6517875F",
  'name': "UST",
  #'name'l: "Wrapped UST Token (PoS)",
  'decimals': 18
},
{
  'address': "0x6929Cc1386fa07CF2F58DACfc9308F6CaB59974D",
  'name': "GCYAN",
  #'name'l: "Gandalf Cyan",
  'decimals': 18
},
{
  'address': "0x692ca411d82DeB4A96F8f89E173171b4Af83Badf",
  'name': "SWAN",
  #'name'l: "Swan Token",
  'decimals': 18
},
{
  'address': "0x692CEe1f68Fc8705c4f2FCe3CA22bD8Dec10652D",
  'name': "IBY",
  #'name'l: "IbetYou Token",
  'decimals': 18
},
{
  'address': "0x6991ED5D57848b7Ba22d0dEDCBd762eD1F25400B",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x69d3646C177aeB185E6987efE9BDef6cD7a744D9",
  'name': "oho",
  #'name'l: "oho",
  'decimals': 18
},
{
  'address': "0x6A174B728D8b7C0C1F239910BB90B3540e1Cc0Dd",
  'name': "gSAT",
  #'name'l: "GrumpySat",
  'decimals': 18
},
{
  'address': "0x6a28c1649B1D11838a45151F430aaB8950f5ce34",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x6A719Ff3B7333702aEcc954dE099b9Bf8BcD99a8",
  'name': "WIND",
  #'name'l: "WindPoly",
  'decimals': 18
},
{
  'address': "0x6A8024f1b449F7a5b25965eE656657ADdC570158",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x6aB6d61428fde76768D7b45D8BFeec19c6eF91A8",
  'name': "ANY",
  #'name'l: "Anyswap",
  'decimals': 18
},
{
  'address': "0x6aDbE5D10B17D9c1F0E1De4bB0E9Db120E384153",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x6AE7Dfc73E0dDE2aa99ac063DcF7e8A63265108c",
  'name': "JPYC",
  #'name'l: "JPY Coin (PoS)",
  'decimals': 18
},
{
  'address': "0x6aFB8e97E9628fa433bEa4e465af2358B5a0C160",
  'name': "???",
  #'name'l: "?? lucky dragon ?? (PoS)",
  'decimals': 18
},
{
  'address': "0x6b9D8c21828b47e92bbD552AA33534CF7Ecf2f17",
  'name': "OMN",
  #'name'l: "Ominous Coin",
  'decimals': 18
},
{
  'address': "0x6bb45cEAC714c52342Ef73ec663479da35934bf7",
  'name': "BONE",
  #'name'l: "Bone Token",
  'decimals': 18
},
{
  'address': "0x6bb9700058894774230431F7e1319Ed03f4Fe800",
  'name': "MAKI",
  #'name'l: "PolyMaki Token",
  'decimals': 18
},
{
  'address': "0x6c6bd7dE145005A2375fC85EdfE0b3eA013F3e95",
  'name': "NEU",
  #'name'l: "NeuCoin",
  'decimals': 0
},
{
  'address': "0x6c7Cae73C6061A897DD5F2c16AFc4b6dEf9f3734",
  'name': "TestxUSD",
  #'name'l: "Test xUSD",
  'decimals': 18
},
{
  'address': "0x6D01322986F0cA7ee964E4C105C08C30Eb11dc95",
  'name': "LUNY",
  #'name'l: "LunaYield.com",
  'decimals': 18
},
{
  'address': "0x6d0c966c8A09e354Df9C48b446A474CE3343D912",
  'name': "XVMC",
  #'name'l: "Mac&Cheese Token",
  'decimals': 18
},
{
  'address': "0x6d13311c659CaEaE274F83A2e875F8779F950bF0",
  'name': "MILK",
  #'name'l: "Milky Swap",
  'decimals': 9
},
{
  'address': "0x6E4c033Ca5CE35dB7E008E81B9d775e4D1A8B088",
  'name': "YQTEST2",
  #'name'l: "YQTEST2",
  'decimals': 18
},
{
  'address': "0x6e58A45f04E40284CD810D7507Cd02244034A000",
  'name': "RF",
  #'name'l: "Ri Finance",
  'decimals': 18
},
{
  'address': "0x6E9Cc1745042374509F5761ABc2f03b6d9a7a97E",
  'name': "DYOR",
  #'name'l: "DYOR",
  'decimals': 2
},
{
  'address': "0x6EB7D1bde3981E1863E7dC473Cc863BBe11356Ab",
  'name': "mDOP",
  #'name'l: "Dopple Token on Matic",
  'decimals': 18
},
{
  'address': "0x6F0f6018ecb46c69F27A57ccc3Ff0936072ff709",
  'name': "shibakiller",
  #'name'l: "safeshiba:shiba killer",
  'decimals': 18
},
{
  'address': "0x6f1e3dBff6EbFA53898027cfF2075d5222598186",
  'name': "SBC",
  #'name'l: "Sunsam Business Co",
  'decimals': 18
},
{
  'address': "0x6f57Ec3C983a04C9Bf9958C9E908c39a3cD0870d",
  'name': "AMIS",
  #'name'l: "AMIS (PoS)",
  'decimals': 9
},
{
  'address': "0x6F6E348e6561E1f48aC1a0063c238093110c36d2",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x6f80AdEFF95434FC5adf61CdcB612E86D25cfe6a",
  'name': "SAVE",
  #'name'l: "ANTI TITAN",
  'decimals': 18
},
{
  'address': "0x6f8721F935F600C795Bd8826e6c45101d585D069",
  'name': "Cafe",
  #'name'l: "Cuban Coffee",
  'decimals': 18
},
{
  'address': "0x6f8a06447Ff6FcF75d803135a7de15CE88C1d4ec",
  'name': "SHIB",
  #'name'l: "SHIBA INU (PoS)",
  'decimals': 18
},
{
  'address': "0x7007EC8fB210a48CB4eA05125D62d16b3BF6cc98",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x71B821aa52a49F32EEd535fCA6Eb5aa130085978",
  'name': "0xBTC",
  #'name'l: "0xBitcoin Token",
  'decimals': 8
},
{
  'address': "0x71c080EE56CC1851540662807F6A2212cDe58B19",
  'name': "MEOW",
  #'name'l: "PolyMeow",
  'decimals': 18
},
{
  'address': "0x721bb42293FDF2610C7936c883F69325D3E43114",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x72572CCf5208b59f4BcC14e6653d8c31Cd1fC5a0",
  'name': "VERT",
  #'name'l: "Vertex",
  'decimals': 18
},
{
  'address': "0x7278264D96813f2B22cff0F543e2A3973467D0EA",
  'name': "JEFF",
  #'name'l: "BEZOSDOGE",
  'decimals': 9
},
{
  'address': "0x72996c9090537Ed6737140C2D8CeAe4586E1cA0c",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x72bba3Aa59a1cCB1591D7CDDB714d8e4D5597E96",
  'name': "COMFI",
  #'name'l: "CompliFi (PoS)",
  'decimals': 18
},
{
  'address': "0x72c22654029764C9A7b3bB7E9B4b593046EfDdeE",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x7339A43Df10882e293b67bAa2E62c5333752998c",
  'name': "TESTxUSD",
  #'name'l: "TESTxDollar Stablecoin",
  'decimals': 18
},
{
  'address': "0x73B54aFe3484C424C5825c54568C3149C72CF2C5",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0x74457223D2a2860E7f857Dd1a709e0584d2Ea2E7",
  'name': "CORSO",
  #'name'l: "Corso",
  'decimals': 18
},
{
  'address': "0x748ff9576a8139B684c3067c5F2458c0C0fc36ad",
  'name': "KTN",
  #'name'l: "Kattana",
  'decimals': 0
},
{
  'address': "0x7555E6b6F5FE34BB7Ccdc8Db123DD97A69A9A43b",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x7584bF83998DEb33D4Dc5142FD642b336EBc0B93",
  'name': "POLB",
  #'name'l: "PolyBank",
  'decimals': 18
},
{
  'address': "0x76bF0C28e604CC3fE9967c83b3C3F31c213cfE64",
  'name': "CRYSTL",
  #'name'l: "CrystalToken",
  'decimals': 18
},
{
  'address': "0x76e63a3E7Ba1e2E61D3DA86a87479f983dE89a7E",
  'name': "OMEN",
  #'name'l: "Augury Finance",
  'decimals': 18
},
{
  'address': "0x7717f1EFA5E36205527A2374603004968aBb480a",
  'name': "BABY",
  #'name'l: "baby love (PoS)",
  'decimals': 18
},
{
  'address': "0x7734c8b0a8e25C8e804538EBa14b9ed3E52F16C7",
  'name': "STK",
  #'name'l: "SamyToken",
  'decimals': 18
},
{
  'address': "0x7808779bcFC03a75C7B4bEB0c9e73DF841DF2270",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x79251788a382a5e7c56396b1B779f759dC410760",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x79aa89D5922A91DAE346a3BAe73559B5492A7186",
  'name': "POLYTOKEN",
  #'name'l: "PolyToken",
  'decimals': 18
},
{
  'address': "0x7A20af0af69d6367Ef02ab9CC4A93226E1c34C63",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x7A5dc8A09c831251026302C93A778748dd48b4DF",
  'name': "PLX",
  #'name'l: "PolyDex.Fi",
  'decimals': 18
},
{
  'address': "0x7a7Dbe487FCF4e83954767cbE93b2E7023eCde9e",
  'name': "EGG",
  #'name'l: "Goose Golden Egg",
  'decimals': 18
},
{
  'address': "0x7aCE654eEA5b1459E3c7287Be21b4562cf8855B9",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x7b23943Cd31f3b3Bee3e76333a0AFdE80B0ED354",
  'name': "WOLF",
  #'name'l: "WolfSwap Token",
  'decimals': 18
},
{
  'address': "0x7b2F23f8939b241199f3aE809D1bcA69288A8b67",
  'name': "$",
  #'name'l: "DOLLAR",
  'decimals': 5
},
{
  'address': "0x7B354a313E705195f1e03014cD524Ab0CCEAB080",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x7B6896FeF1bDf8239E02c2BaFDbc468962Ec881c",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x7Ba612CEd3235414D1763eA49B00a0E77fC5e041",
  'name': "DOTO",
  #'name'l: "Donation Token",
  'decimals': 4
},
{
  'address': "0x7bc4784c012296b76d825888cdf39bF8DD781140",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x7C254df221993A8a2E703c3351c528f05E329595",
  'name': "NEWINU",
  #'name'l: "New Guinea Singing Dog Inu (PoS)",
  'decimals': 9
},
{
  'address': "0x7C4A54f5d20b4023D6746F1f765f4DFe7C39a7e6",
  'name': "renDOGE",
  #'name'l: "renDOGE (PoS)",
  'decimals': 8
},
{
  'address': "0x7CdC0421469398e0F3aA8890693d86c840Ac8931",
  'name': "AZUKI",
  #'name'l: "DokiDokiAzuki",
  'decimals': 18
},
{
  'address': "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
  'name': "WETH",
  #'name'l: "Wrapped Ether",
  'decimals': 18
},
{
  'address': "0x7dBfE09143cB2EEd4583cdeF6c6F7DFE0F190429",
  'name': "PolySave",
  #'name'l: "PolySave",
  'decimals': 9
},
{
  'address': "0x7dc0cb65EC6019330a6841e9c274f2EE57A6CA6C",
  'name': "PLU",
  #'name'l: "Pluton (PoS)",
  'decimals': 18
},
{
  'address': "0x7dc95DaE35aa4b0fCAD32120db7e6CAACd91f178",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0x7de5f380792DBA36500d4caB19CeEDaBEF7D7883",
  'name': "FUEL",
  #'name'l: "JetFuel",
  'decimals': 18
},
{
  'address': "0x7E6afEC8cf917976d11Fe65A34d3c17289fe3aE0",
  'name': "Pikachu",
  #'name'l: "Pikachu (PoS)",
  'decimals': 18
},
{
  'address': "0x7e9928aFe96FefB820b85B4CE6597B8F660Fe4F4",
  'name': "PBNB",
  #'name'l: "Orbit Bridge Polygon Binance Coin",
  'decimals': 18
},
{
  'address': "0x7f426F6Dc648e50464a0392E60E1BB465a67E9cf",
  'name': "PAUTO",
  #'name'l: "Orbit Bridge Polygon AUTOv2",
  'decimals': 18
},
{
  'address': "0x7FBc10850caE055B27039aF31bD258430e714c62",
  'name': "UBT",
  #'name'l: "Unibright (PoS)",
  'decimals': 8
},
{
  'address': "0x7FdC6069Ce9aA2862C4EfE44537B37D4bBf15d11",
  'name': "GREEN",
  #'name'l: "EverGreen",
  'decimals': 9
},
{
  'address': "0x80244C2441779361F35803b8C711C6c8fC6054a3",
  'name': "BONE",
  #'name'l: "Bone Token",
  'decimals': 18
},
{
  'address': "0x803318828d504492A32B2e381a16d684F5d7E6aB",
  'name': "NAG",
  #'name'l: "OneGate",
  'decimals': 18
},
{
  'address': "0x80385aDb23D35eF31E5EC35d3E19b19573856a65",
  'name': "ALJ",
  #'name'l: "AlejoToken",
  'decimals': 0
},
{
  'address': "0x803F27182E413273D679165EAb7b73747e027607",
  'name': "ETIT",
  #'name'l: "ETIT",
  'decimals': 9
},
{
  'address': "0x8096ac61db23291252574D49f036f0f9ed8ab390",
  'name': "crvUSDBTCETH",
  #'name'l: "Curve USD-BTC-ETH",
  'decimals': 18
},
{
  'address': "0x80f7E2ac9290DC22c57871C3c34f988ccA5E8977",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x81237De5672267A181100D0d02Aa748EedB354b3",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x814E81f635473b9EfB2C483D5D5E68b92feE2407",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x8160F33C2A5fD250eA12A1eAcFab62b9328F5d6E",
  'name': "BEN",
  #'name'l: "BenCoin",
  'decimals': 18
},
{
  'address': "0x823CD4264C1b951C9209aD0DeAea9988fE8429bF",
  'name': "maAAVE",
  #'name'l: "Matic Aave interest bearing AAVE",
  'decimals': 18
},
{
  'address': "0x8266a008ca99B7BbdB7C91C136F5B2714760CEbf",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x831753DD7087CaC61aB5644b308642cc1c33Dc13",
  'name': "QUICK",
  #'name'l: "Quickswap",
  'decimals': 18
},
{
  'address': "0x8346Ab8d5EA7A9Db0209aEd2d1806AFA0E2c4C21",
  'name': "MOD",
  #'name'l: "MODEFI  (PoS)",
  'decimals': 18
},
{
  'address': "0x835273d47A2a4Cc84693639f8D890af1CaeA611D",
  'name': "NDX",
  #'name'l: "Indexed (PoS)",
  'decimals': 18
},
{
  'address': "0x83749A528105a1AC9C36E67DC11b1fb5315Ce2a8",
  'name': "TPC",
  #'name'l: "Top Coin",
  'decimals': 18
},
{
  'address': "0x83Dfce0421477F37a344F6106A3Bc3b9Ff45d99A",
  'name': "XDO",
  #'name'l: "XDO",
  'decimals': 18
},
{
  'address': "0x840195888Db4D6A99ED9F73FcD3B225Bb3cB1A79",
  'name': "SX",
  #'name'l: "SportX (PoS)",
  'decimals': 18
},
{
  'address': "0x8422Ed20E891f6C56b4e5c106959EC32CA761fB5",
  'name': "\ufffd",
  #'name'l: "Moonshine",
  'decimals': 9
},
{
  'address': "0x84259e4c4207Ec8F2e6DB22Ba30d283180baCdB5",
  'name': "FOX",
  #'name'l: "PolyFox Token",
  'decimals': 18
},
{
  'address': "0x84e1670F61347CDaeD56dcc736FB990fBB47ddC1",
  'name': "LRC",
  #'name'l: "LoopringCoin V2 (PoS)",
  'decimals': 18
},
{
  'address': "0x8505b9d2254A7Ae468c0E9dd10Ccea3A837aef5c",
  'name': "COMP",
  #'name'l: "(PoS) Compound",
  'decimals': 18
},
{
  'address': "0x85301fA8A453e958c7208C9fA5c4D3AbBDaAe41D",
  'name': "YQTEST1",
  #'name'l: "YQTEST1",
  'decimals': 18
},
{
  'address': "0x854C3FC78174Ee918e66C335b72217deA887E293",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x855baEadfdc93e8647a491062Db2575DdD896220",
  'name': "TESTNOBUY",
  #'name'l: "TestNOBUY",
  'decimals': 18
},
{
  'address': "0x859287Ae7E623Ae842A3ff16839dF53Ab2258fcD",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0x85955046DF4668e1DD369D2DE9f3AEB98DD2A369",
  'name': "DPI",
  #'name'l: "DefiPulse Index (PoS)",
  'decimals': 18
},
{
  'address': "0x85eCa3374D7FEA1eCd79BB4D875CF9E220e9fbDB",
  'name': "DOGE2",
  #'name'l: "DOGE2",
  'decimals': 18
},
{
  'address': "0x85F20AfE9f16CBc9d26B8e8BE5c8A669cD8Fa70E",
  'name': "KING",
  #'name'l: "Slowking",
  'decimals': 18
},
{
  'address': "0x861B931e4D91b5B50A301df1E72Ef77192dE29d6",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x87c830b6d732C3209dB97f61B379F359570d6A49",
  'name': "SPCY",
  #'name'l: "Sapiency (PoS)",
  'decimals': 18
},
{
  'address': "0x87E5348BEF878aF0aA397Eac8d1B49Cc3B550De5",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x87ff96aba480f1813aF5c780387d8De7cf7D8261",
  'name': "WBUSD",
  #'name'l: "Wrapped BUSD",
  'decimals': 18
},
{
  'address': "0x8844cD0C0e23A4602987EFfc785beE04166fD44A",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x886156B9C25FD52698EF21eD439B3D62393947Bf",
  'name': "ABT",
  #'name'l: "ADNAN BASIC TOKEN",
  'decimals': 18
},
{
  'address': "0x89656Cc9567f89886F88caE333EbC55991AE978c",
  'name': "DFMUSK",
  #'name'l: "DefeatMUSK",
  'decimals': 0
},
{
  'address': "0x8a0B040F27407d7a603BcA701b857F8F81A1C7af",
  'name': "Buy Polydoge",
  #'name'l: "Go Buy Polydoge",
  'decimals': 18
},
{
  'address': "0x8A136F77B53166C7e4DAc59f686063ef88bC898F",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x8a2870fb69A90000D6439b7aDfB01d4bA383A415",
  'name': "DEGEN",
  #'name'l: "DEGEN Index (PoS)",
  'decimals': 18
},
{
  'address': "0x8A4001fD666BE272605c56BB956d11A46200Db81",
  'name': "GREEN",
  #'name'l: "Green Token (PoS)",
  'decimals': 8
},
{
  'address': "0x8a6fC0A8a6B5DB22B6d5a9DBedDFf00EeE6F0e8a",
  'name': "TESTxUSD",
  #'name'l: "TEST xDollar Stablecoin",
  'decimals': 18
},
{
  'address': "0x8A953CfE442c5E8855cc6c61b1293FA648BAE472",
  'name': "PolyDoge",
  #'name'l: "PolyDoge",
  'decimals': 18
},
{
  'address': "0x8Ab2Fec94d17ae69FB90E7c773f2C85Ed1802c01",
  'name': "LQTY",
  #'name'l: "LQTY (PoS)",
  'decimals': 18
},
{
  'address': "0x8B9190Ca706ad2DF23772B71DBDD263d0f85f209",
  'name': "ELECTRON",
  #'name'l: "Electron",
  'decimals': 18
},
{
  'address': "0x8bab80afDDb52F5B581C18324d985013Da49569a",
  'name': "CHILI",
  #'name'l: "The Chili Token",
  'decimals': 18
},
{
  'address': "0x8bB30E0e67b11b978a5040144c410e1ccDDcba30",
  'name': "ZCN",
  #'name'l: "0chain (PoS)",
  'decimals': 10
},
{
  'address': "0x8Bc56b1416B4A459Bd3C48B9451bE71211F7d5DD",
  'name': "diamond",
  #'name'l: "diamond",
  'decimals': 0
},
{
  'address': "0x8bF64Fd08B3Eb312B6B9CB8D272c0166DB6D6001",
  'name': "SWTCH",
  #'name'l: "SwitchToken",
  'decimals': 18
},
{
  'address': "0x8c8bdBe9CeE455732525086264a4Bf9Cf821C498",
  'name': "maUNI",
  #'name'l: "Matic Aave interest bearing UNI",
  'decimals': 18
},
{
  'address': "0x8C92e38eCA8210f4fcBf17F0951b198Dd7668292",
  'name': "DHT",
  #'name'l: "dHedge DAO Token (PoS)",
  'decimals': 18
},
{
  'address': "0x8CA5ed20346c5d8a21A849d59c64f0884a532882",
  'name': "OFT",
  #'name'l: "Orient (PoS)",
  'decimals': 18
},
{
  'address': "0x8Cc99Fd6a3A606f98A54a00E5EAb3Ff9372479De",
  'name': "MEOWB",
  #'name'l: "MeowMeowfinance",
  'decimals': 18
},
{
  'address': "0x8ccC1D2Af93cc1Bac25A77289303BEF044b1E30E",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x8D1B0e4eA19B1113d436960CE8d9B51ee4D4f375",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x8d6A339EdC24799265e5B3eCa8Ba8997FefDD7E4",
  'name': "TKN4",
  #'name'l: "ERC20 Test Token 4",
  'decimals': 18
},
{
  'address': "0x8D783d00C105199fE532828c32b93dC0b0A86808",
  'name': "xUSD",
  #'name'l: "xUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0x8da5E83DfB88719B389C4Fdd75352C4CeB685cA8",
  'name': "♥♥♥",
  #'name'l: "♥ LoveBot ♥ (PoS)",
  'decimals': 18
},
{
  'address': "0x8DCd2Fe229974546e83E25d23bD690e6ba61BEFE",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x8Dd15b60b69051dA1FA70A6d712a5Be04a115b57",
  'name': "POG",
  #'name'l: "Pogcoin",
  'decimals': 8
},
{
  'address': "0x8De755d4B198a1b1b79CE22239Bc83FfF7c73553",
  'name': "stackUSDC",
  #'name'l: "Stacker Ventures USDC v1",
  'decimals': 6
},
{
  'address': "0x8df23694bf341d4C94C35783F1D91FD38c434b93",
  'name': "MARSS",
  #'name'l: "Marss",
  'decimals': 18
},
{
  'address': "0x8dF3aad3a84da6b69A4DA8aeC3eA40d9091B2Ac4",
  'name': "amWMATIC",
  #'name'l: "Aave Matic Market WMATIC",
  'decimals': 18
},
{
  'address': "0x8E26576d29d460728F0C9f3559A1f8B874e862E5",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x8Eaec81876Fd29c26a2f869790CcEe0ba6485182",
  'name': "BULL",
  #'name'l: "BULL Token",
  'decimals': 18
},
{
  'address': "0x8f18dC399594b451EdA8c5da02d0563c0b2d0f16",
  'name': "WOLF",
  #'name'l: "moonwolf.io",
  'decimals': 9
},
{
  'address': "0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063",
  'name': "DAI",
  #'name'l: "(PoS) Dai Stablecoin",
  'decimals': 18
},
{
  'address': "0x8f5c98576F6E0Fae3F6A46A841DE87444A9C33a2",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x8f6196901a4a153d8eE8F3fa779A042F6092D908",
  'name': "SALE",
  #'name'l: "DxSale.Network (PoS)",
  'decimals': 18
},
{
  'address': "0x9122be17cc6967dce494F95AC3441e126f459472",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x91340BE956f9fe25cEc26B7BA3fce8774D611Ad4",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x9217bFA621636302f7B6EE5D2BD90d0B60eF4B26",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x925C31743FAc3bBa3a4Fdbcf314A9c7eB57F150C",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x9299D0995E7CF80dDD5F66F47EA9E114AD6525D4",
  'name': "RMX",
  #'name'l: "Redimix",
  'decimals': 18
},
{
  'address': "0x92aec2649051E04af4E4068d6e74cD51E1176840",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0x92e631Bb230E3C9245770A2fCc706ECBBa534e85",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0x940BDCb16629DbCc2387bF8eDa540652FBE42cDe",
  'name': "YQTEST3",
  #'name'l: "YQTEST3",
  'decimals': 18
},
{
  'address': "0x949E6A5A6df28834ae3867CFE4Fdc2b8eBc026E3",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x94c7d657f1c8Be06A4Dc009D2d475Bb559d858cb",
  'name': "SGAJ",
  #'name'l: "StableGaj Token",
  'decimals': 18
},
{
  'address': "0x94e397D8Dc8d532e1CDD189f7492b91595edD0ae",
  'name': "5S",
  #'name'l: "sssss",
  'decimals': 18
},
{
  'address': "0x957d1AD5214468332C5e6C00305a25116f9A46BB",
  'name': "NOIA",
  #'name'l: "NOIA Token (PoS)",
  'decimals': 18
},
{
  'address': "0x9610b01AAa57Ec026001F7Ec5CFace51BfEA0bA6",
  'name': "anyUSDC",
  #'name'l: "USDC",
  'decimals': 6
},
{
  'address': "0x9656cfbbdDc777f15341F4bd1733f5eEC6B5Feb4",
  'name': "SPACEFUNK",
  #'name'l: "funkyninja *❄✲❄* spacerobots (PoS)",
  'decimals': 18
},
{
  'address': "0x96837816715ca6b2f8223A06811c594081eB8F89",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x96B21093c2a33f15BB15CfA8412eF214ABe07FD4",
  'name': "DINOT Test Token",
  #'name'l: "DINOT",
  'decimals': 18
},
{
  'address': "0x96d161cbf38FACCeD333851A9cEf20936DDA88F4",
  'name': "pUSDC",
  #'name'l: "Pod USD Coin (PoS)",
  'decimals': 6
},
{
  'address': "0x96e7593E376a8f75fD52ae71B7b45358eF373AE8",
  'name': "Guru",
  #'name'l: "Guru",
  'decimals': 18
},
{
  'address': "0x9719d867A500Ef117cC201206B8ab51e794d3F82",
  'name': "maUSDC",
  #'name'l: "Matic Aave interest bearing USDC",
  'decimals': 6
},
{
  'address': "0x9737399FaB00754FDc8BEe48FCB0697CE85C7DE5",
  'name': "BLO",
  #'name'l: "Based Loans Ownership (PoS)",
  'decimals': 18
},
{
  'address': "0x979698F08836641858918955C7490fec5ce71E14",
  'name': "HAWK",
  #'name'l: "Hawk Token",
  'decimals': 18
},
{
  'address': "0x979B81fE607F957d84cB544Fe4dbC450874c5284",
  'name': "DZTN",
  #'name'l: "deztino",
  'decimals': 18
},
{
  'address': "0x97B14a709d1a1A455df2041b97040cba11A99914",
  'name': "red tulip",
  #'name'l: "red tulip",
  'decimals': 0
},
{
  'address': "0x981b008f3F8265c17260892C0539b9D83C4ae6B5",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0x98521344091028Cc8009a717B6B53992c697ae03",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x98AFb7289Cf1B745908a3152d560b7fbB9d6c415",
  'name': "ADAT",
  #'name'l: "ADA TOKEN",
  'decimals': 18
},
{
  'address': "0x98ea5fe852E45439909F0B133bD95a9dfE83272B",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x994049cDfCf7d55eaD6CE276D9026e98808DAdC2",
  'name': "xViking",
  #'name'l: "xViking",
  'decimals': 18
},
{
  'address': "0x9955D1ea71D01B53BDE6e631257245b2C98B8BBb",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0x998D334B051d1f1D94361d6170677DeB6e13D989",
  'name': "DEVX",
  #'name'l: "DEVX Token",
  'decimals': 18
},
{
  'address': "0x99dA82C5464C49962Cdda44fe30d352Bc5Da0580",
  'name': "QuickChart",
  #'name'l: "QuickChart",
  'decimals': 9
},
{
  'address': "0x9A702bf391D8a4279fd08e1e618513c2834bD8f3",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x9a71012B13CA4d3D0Cdc72A177DF3ef03b0E76A3",
  'name': "BAL",
  #'name'l: "Balancer (PoS)",
  'decimals': 18
},
{
  'address': "0x9Ad4CF2a2e6111F63EDaD2e05971E40791BA41f7",
  'name': "DT1",
  #'name'l: "DummyToken1",
  'decimals': 18
},
{
  'address': "0x9aF3b7DC29D3C4B1A5731408B6A9656fA7aC3b72",
  'name': "PUSD",
  #'name'l: "PUSD",
  'decimals': 18
},
{
  'address': "0x9b824c9B1f91ce2f8d062536658c010E1d64FE75",
  'name': "SAFEMOON",
  #'name'l: "SafeMoon",
  'decimals': 9
},
{
  'address': "0x9B8d69cFc265993e04b552f69B6A395681bD7BbB",
  'name': "HDK",
  #'name'l: "Hong D Kong",
  'decimals': 18
},
{
  'address': "0x9b8F17AC7fE0774BA3D122B3C9EC859DD2d527b6",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x9Bc9dB61f21a25cEA74De35753c2907C6594b984",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0x9C0595CDCF27CE3EF16ADd0a01fe02149317F144",
  'name': "TestMoon",
  #'name'l: "TestMoon",
  'decimals': 9
},
{
  'address': "0x9c49BA0212Bb5Db371e66b59D1565b7c06E4894e",
  'name': "CC10",
  #'name'l: "Cryptocurrency Top Tokens Index (PoS)",
  'decimals': 18
},
{
  'address': "0x9C5A447c8C1a35dC1EAad76c083FC9e7AcafD263",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x9C78EE466D6Cb57A4d01Fd887D2b5dFb2D46288f",
  'name': "MUST",
  #'name'l: "Must",
  'decimals': 18
},
{
  'address': "0x9C80eBCd0E291C5df5cfc92c4D999A5C5803d9B2",
  'name': "ZAKA",
  #'name'l: "Zaka",
  'decimals': 18
},
{
  'address': "0x9C9c3d859A4C0dD0505aE57714F3231FE8a07149",
  'name': "MOWL",
  #'name'l: "Moon Owl",
  'decimals': 9
},
{
  'address': "0x9e01e0A928588aE6E669b8d1F0f1fa4AB976f617",
  'name': "SHO",
  #'name'l: "Showcase Token (PoS)",
  'decimals': 18
},
{
  'address': "0x9Eb646a4Cd8a64c7B96ee3E990ff5FC8032a7D9C",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x9ecB26631098973834925eb453De1908Ea4bdD4e",
  'name': "pUSDT",
  #'name'l: "PT USDT Ticket",
  'decimals': 6
},
{
  'address': "0x9f5755D47fB80100E7ee65Bf7e136FCA85Dd9334",
  'name': "OM",
  #'name'l: "OM Token (PoS)",
  'decimals': 18
},
{
  'address': "0x9F92B1574E10Ed8D56c297Ca216E978444a71a64",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0x9fB83c0635De2E815fd1c21b3a292277540C2e8d",
  'name': "BUSD",
  #'name'l: "Binance-Peg BUSD Token",
  'decimals': 18
},
{
  'address': "0x9fEda6BA028392B3FF2dB25A4Dfb0654DB21eE91",
  'name': "ACORN",
  #'name'l: "Acorn Token",
  'decimals': 18
},
{
  'address': "0xA000D1674B983a7878B68294d5738794792D3D4F",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xa0e504482E24d8c9EB3A656174B6d35e135FF207",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xA1c57f48F0Deb89f569dFbE6E2B7f46D33606fD4",
  'name': "MANA",
  #'name'l: "(PoS) Decentraland MANA",
  'decimals': 18
},
{
  'address': "0xa207d6ADC10B3465eD4F9F2C464aEB84555beE9D",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xA2C095C1987E7A0A6c4AAC4E51A3aE1D411a183A",
  'name': "IRON",
  #'name'l: "IRON Stablecoin",
  'decimals': 18
},
{
  'address': "0xA31ea01c4C9dDe02FC374B3c394b106fE3756EF0",
  'name': "HTX",
  #'name'l: "Hashtrust",
  'decimals': 0
},
{
  'address': "0xA328Eb5E2fD147B528aac2f67896190a17724205",
  'name': "TESTxUSD",
  #'name'l: "TEST xDollar Stablecoin",
  'decimals': 18
},
{
  'address': "0xA36Ac77A789e2FC763cCf74EC0aa011556764f0E",
  'name': "axb",
  #'name'l: "axb",
  'decimals': 18
},
{
  'address': "0xA3D595823beeDE02cC755AB4e22AD009A70cB590",
  'name': "KISHU",
  #'name'l: "Kishu Inu (PoS)",
  'decimals': 9
},
{
  'address': "0xA3d8885825A843F040eb64A6a846b687cd07F072",
  'name': "SHUNG",
  #'name'l: "Shungite (PoS)",
  'decimals': 18
},
{
  'address': "0xa3F2E061F80ddEA8cB2f3AE961356fEFC96525cf",
  'name': "SAFEMOON",
  #'name'l: "SafeMoon",
  'decimals': 9
},
{
  'address': "0xa3F72eDCD353A745302e3F44a3E98be3B4BAcB79",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xa3Fa99A148fA48D14Ed51d610c367C61876997F1",
  'name': "miMATIC",
  #'name'l: "miMATIC",
  'decimals': 18
},
{
  'address': "0xA492F43D2eb21c40757d600f4cD08740F18DD83B",
  'name': "SAFEMOON",
  #'name'l: "SafeMoon",
  'decimals': 9
},
{
  'address': "0xA4a24e50811b1B9688253da59eeAcce3753FbfF7",
  'name': "FART",
  #'name'l: "FART",
  'decimals': 2
},
{
  'address': "0xa5Eb60CA85898f8b26e18fF7c7E43623ccbA772C",
  'name': "COSMIC",
  #'name'l: "CosmicSwap",
  'decimals': 18
},
{
  'address': "0xA5f7EA46EBDC3F192c19e900012B3c4a2D6E11a0",
  'name': "SVB",
  #'name'l: "super veggie burrito (PoS)",
  'decimals': 18
},
{
  'address': "0xa607a2f8aA5fc9C7c71576eEfe141A23C13963cb",
  'name': "YELD",
  #'name'l: "Polyyeld.finance",
  'decimals': 18
},
{
  'address': "0xa60c8bDB96EC4b0Bc93A0d20A8DCa2C180D37a3B",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xa74E622Cf87E07c7C62914098A3214c46CAa5465",
  'name': "raw andesite",
  #'name'l: "raw andesite",
  'decimals': 0
},
{
  'address': "0xA772B9Ac43E7A165Cac5582b27376020263189eb",
  'name': "USDT",
  #'name'l: "Tether USD",
  'decimals': 6
},
{
  'address': "0xA79983Daf2A92c2C902cD74217Efe3D8AF9Fba2a",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xA7d1447E497857559902586E161EC999A23226a8",
  'name': "APT",
  #'name'l: "APIDAE",
  'decimals': 18
},
{
  'address': "0xa8234c12051Db6161439EBcBbB060A48411805cC",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xA873f198E1c88Cdb1c8897B20f90F4648746e236",
  'name': "raw diorite",
  #'name'l: "raw diorite",
  'decimals': 0
},
{
  'address': "0xA88b4ce79c5814fB7df5cc53A46bDF8E485168f9",
  'name': "8BALL",
  #'name'l: "8Ball Token",
  'decimals': 18
},
{
  'address': "0xA8e9DbCCDed613B61F378414453d23Db8dD830DA",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xA97ED7Cb323B974750f5E657d5823F31352Bfdb6",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xaA08E208EDBdc99C9bF1872078A25b0700c48517",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xaAa5B9e6c589642f98a1cDA99B9D024B8407285A",
  'name': "TITAN",
  #'name'l: "IRON Titanium Token",
  'decimals': 18
},
{
  'address': "0xaB6F564394AD9E32FD4a92d35842a874BA4D7914",
  'name': "GAPE",
  #'name'l: "Gape Coin",
  'decimals': 9
},
{
  'address': "0xabf718D3863EB7D3448ebb908850d5C2b847d14b",
  'name': "USDTEST3",
  #'name'l: "USDTEST3",
  'decimals': 18
},
{
  'address': "0xAC8e5683fe3b0ff07f1C5A0c91adfe83AEF0331E",
  'name': "TEST",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0xAcD7B3D9c10e97d0efA418903C0c7669E702E4C0",
  'name': "ELE",
  #'name'l: "Eleven.finance",
  'decimals': 18
},
{
  'address': "0xAd230ec33ccf849C2bBd8D26C1706DB07b24Db95",
  'name': "LAND",
  #'name'l: "Land (PoS)",
  'decimals': 18
},
{
  'address': "0xAd3a44B57D0C205b997FBfC8db88FF13fd3d2aA2",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xaD7E3c3B6014b70227EDf0C1629601c475681624",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xad934Ab35fe63109F41aE36A9047C0905B0f6BFD",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xAe26440090f997c97b704F60ea206df648fe8Ea8",
  'name': "WINTOKEN",
  #'name'l: "Win Token",
  'decimals': 18
},
{
  'address': "0xaECeBfcF604AD245Eaf0D5BD68459C3a7A6399c2",
  'name': "RAMP",
  #'name'l: "RAMP (PoS)",
  'decimals': 18
},
{
  'address': "0xAF3D010744B3D4D76A73aFE4f7c01777abdCf3B6",
  'name': "YQTEST3",
  #'name'l: "YQTEST3",
  'decimals': 18
},
{
  'address': "0xaf5205cC7d95c1B8fD4ABD42fEA27f4fBe9e2e77",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xAf7fDD635D162Bef1283da5f5AdBbdb0A9a34d90",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xb072969BEfccBA697d87B2cB9CB00a1C78319E4D",
  'name': "Pory",
  #'name'l: "Porygon",
  'decimals': 9
},
{
  'address': "0xb0b20e10F25C52b5C85295f425d56EFCC761F0D9",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xB105FaC8abA7c015Cce3B9Dd68D08f4Dd8490745",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xb1B0142B577A2AbA8Ce72396A23Bb6B57ee37bf6",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xB1CB4aC6b1685DcbE691b9246406748805aa6FA8",
  'name': "POLYSAFE",
  #'name'l: "PolySafe",
  'decimals': 9
},
{
  'address': "0xB1f1025fa5Ecc34610f211b4a37A60Bd7c55E0cf",
  'name': "pBCK",
  #'name'l: "PolyBack",
  'decimals': 18
},
{
  'address': "0xB1f9D66426E2e006BAEB41D3d9B8FBc0d1f6008D",
  'name': "RDT",
  #'name'l: "Rediant Token",
  'decimals': 18
},
{
  'address': "0xb2C45a0a5AA5173c1432205E5e6a183d8D98168E",
  'name': "iBLUE0",
  #'name'l: "ironBLUEZero",
  'decimals': 0
},
{
  'address': "0xb2E9420ef61a51ed1a9EcEf8A84a98d73Ee0d339",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xB2F336CF37686CA3b70A9c10EdafC83161227891",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xb33EaAd8d922B1083446DC23f610c2567fB5180f",
  'name': "UNI",
  #'name'l: "Uniswap (PoS)",
  'decimals': 18
},
{
  'address': "0xb371248Dd0f9E4061ccf8850E9223Ca48Aa7CA4b",
  'name': "HNY",
  #'name'l: "Honey (PoS)",
  'decimals': 18
},
{
  'address': "0xb3C31CBF66cFD663C4B0DC689979d3C2eF938219",
  'name': "TestxUSD",
  #'name'l: "Test xUSD",
  'decimals': 18
},
{
  'address': "0xb3dF1D006088B95d29a97c3d167425f02567B1E0",
  'name': "JERM",
  #'name'l: "Jermcoin",
  'decimals': 18
},
{
  'address': "0xb4228798fF437ecD8fa43429664e9992256fe6Ac",
  'name': "KITTY",
  #'name'l: "Kitty Coin",
  'decimals': 18
},
{
  'address': "0xB48BBc0B1Dc347397313065DEdD239439026f352",
  'name': "?",
  #'name'l: "Moonshine",
  'decimals': 9
},
{
  'address': "0xB4aB9700B9287B682634d4534193669A32c06B90",
  'name': "HND",
  #'name'l: "Tokyo Token",
  'decimals': 18
},
{
  'address': "0xB4C2064d9C612e946C5a416Db5173788A6422523",
  'name': "WYZ",
  #'name'l: "WISECOIN",
  'decimals': 18
},
{
  'address': "0xb4c6FE90F91Bb8c77747d739A61D0F6B2AD9e957",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xb4cA879d4AC2eee3ae0f42488106f2b242cD0462",
  'name': "FRIENDS",
  #'name'l: "friends (PoS)",
  'decimals': 18
},
{
  'address': "0xB4F1c37C8DD9F28d4A75D3D349e97104AFF2Da4b",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xB5602e7345Cad4FcaA747fd23Af97f45c0aFaa9d",
  'name': "JW",
  #'name'l: "JimmyWalker ",
  'decimals': 18
},
{
  'address': "0xb5883A4Ad1D90f8Dad982Af93ae2fFA0Dfe0E0Fa",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xB5b91b33C4917ad0153a9295644C226be2F95982",
  'name': "wheat item",
  #'name'l: "wheat item",
  'decimals': 0
},
{
  'address': "0xb5bF4DC42f6103b3a7528Cc3DA0AdD3AdD6D7fAa",
  'name': "ROCK",
  #'name'l: "IRON Protocol Share",
  'decimals': 18
},
{
  'address': "0xB5C45517212E902aEAC2328EAb0178E9d735d6f7",
  'name': "MAGIC",
  #'name'l: "MagicMatic",
  'decimals': 9
},
{
  'address': "0xb5dFed73Dc3c68628fb1E2B6c9f33180EAC557cb",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xb5fcbBA2Bb2Ee4208358597844657CAE2bDCB94e",
  'name': "HUI",
  #'name'l: "HUI token",
  'decimals': 0
},
{
  'address': "0xB6040ACc4B81Ab95cE846923451791C05793e131",
  'name': "xUSD",
  #'name'l: "xUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0xb6689d4e9506195586FA1012547289a309FF714C",
  'name': "WYZ",
  #'name'l: "WISECOIN",
  'decimals': 18
},
{
  'address': "0xb67176655e7919a27aA34C279157124619aDFd4B",
  'name': "ZERO",
  #'name'l: "Zero.Exchange Token",
  'decimals': 18
},
{
  'address': "0xb68A02A5A988e1771c11C46877c1CA7429662c08",
  'name': "PRN",
  #'name'l: "PeronCoin",
  'decimals': 0
},
{
  'address': "0xB74F47A6Eff32831DA6F3e97916D384a2646a073",
  'name': "TEST PDUCK",
  #'name'l: "TEST PolyDuck",
  'decimals': 18
},
{
  'address': "0xb7518ED437FA7F078C087E0Ae8ff5961168c9761",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xB75D4F951d9bc7D93D45D78d43273ad41534e6DF",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xb77D1a6Bb2A9F41aE2F18f5D66498c02fd6f462F",
  'name': "BANANA",
  #'name'l: "BananaToken",
  'decimals': 18
},
{
  'address': "0xb77eEe32bE7684D3c06d8a18c4BfC4c33856dE35",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0xb7BCeAED243fFDCA3a213EeC66d51AcaC8Ae3F3c",
  'name': "FROG",
  #'name'l: "Frog Token",
  'decimals': 18
},
{
  'address': "0xb816d2Bd3FFEf8CA2E65E5F7E0695351b733C4f3",
  'name': "FAU",
  #'name'l: "FaucetToken",
  'decimals': 18
},
{
  'address': "0xb84D9e27714010b0641Fb712AB7dcEBb4cE4d975",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xb895569F11482737d189345D0393a833F4ac2934",
  'name': "USDTEST1",
  #'name'l: "USDTEST1",
  'decimals': 18
},
{
  'address': "0xb89aD6718e6D9E84f5375b153e5e226a3aA75C3d",
  'name': "FCT",
  #'name'l: "FuckCovid",
  'decimals': 18
},
{
  'address': "0xb91fBd847F62A7a917fEb522d20051659eb16406",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xB94519b34518C7756Ee8f1AC50e672297c1227D0",
  'name': "BabyDoge",
  #'name'l: "BabyDoge Token",
  'decimals': 18
},
{
  'address': "0xb9823443E1dd23a2D68782DCD711Ec5f23DA79B1",
  'name': "PTR",
  #'name'l: "Petroleo",
  'decimals': 18
},
{
  'address': "0xba4452217C59863ae2a332EC16bd7ed8c9A32C8B",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xbAe1b833cbA827BAFe783697A7d3D285a326233C",
  'name': "BAE",
  #'name'l: "BaeBay",
  'decimals': 18
},
{
  'address': "0xbb076A2eEfe1028B802aFC71efAD16033df16c26",
  'name': "POLYPOO",
  #'name'l: "polypoo",
  'decimals': 18
},
{
  'address': "0xbb7cfcDb1b7e2Bf082288237F56b35f54b8217E3",
  'name': "MTT",
  #'name'l: "MTTEST",
  'decimals': 9
},
{
  'address': "0xBb80F75a28f157A3a1dA36b43B6DcA00534ACD9D",
  'name': "YQTEST2",
  #'name'l: "YQTEST2",
  'decimals': 18
},
{
  'address': "0xBBaaC4F8C5916FaD25B2CA254419D066D8acA04A",
  'name': "MGMN",
  #'name'l: "MEGAMOON",
  'decimals': 10
},
{
  'address': "0xBc7b539638dcAF58b0760455344cBF64b00fD6DC",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xBcEa392142eb9c874b7f4263A336Ba0e37DAD083",
  'name': "SEELE",
  #'name'l: "Seele",
  'decimals': 18
},
{
  'address': "0xbdfB286EB39ad6f152597478360334A342b8f62D",
  'name': "MGC",
  #'name'l: "TestMGC",
  'decimals': 18
},
{
  'address': "0xbe9512e2754cb938dd69Bbb96c8a09Cb28a02D6D",
  'name': "GBTS",
  #'name'l: "GemBites",
  'decimals': 18
},
{
  'address': "0xBF753783f54E01FdBE5a0Bc243caCE6266e97db3",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xc0E1eB1F09699990Fd9AeB6Fda02bBb9ec97b751",
  'name': "WOLF",
  #'name'l: "PolyWolf Token",
  'decimals': 18
},
{
  'address': "0xC0fBA60AeCB863a3858dFaaA75D9d22A8D2Aa688",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xC10980e73AbA3f64BFC2d726A6F910a826AaF618",
  'name': "dirt block",
  #'name'l: "dirt block",
  'decimals': 0
},
{
  'address': "0xc1642422D9ea78AA064D72a1dC6536e2c41748a2",
  'name': "SOPHIE",
  #'name'l: "Sophie Dee",
  'decimals': 18
},
{
  'address': "0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
  'name': "USDT",
  #'name'l: "(PoS) Tether USD",
  'decimals': 6
},
{
  'address': "0xc22D189FF43868A347fda822842b67b1C8c57612",
  'name': "CASH",
  #'name'l: "PolyCash",
  'decimals': 18
},
{
  'address': "0xC2C850fba1541d1fe95eB54E1d414Be73C26103c",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xc34f24917c3Bfd94b87832B8EE8BcD5F5528bbe8",
  'name': "PTN",
  #'name'l: "PedicTOKEN",
  'decimals': 18
},
{
  'address': "0xc3FdbadC7c795EF1D6Ba111e06fF8F16A20Ea539",
  'name': "ADDY",
  #'name'l: "Adamant",
  'decimals': 18
},
{
  'address': "0xc3fEd6eB39178A541D274e6Fc748d48f0Ca01CC3",
  'name': "renBCH",
  #'name'l: "renBCH",
  'decimals': 8
},
{
  'address': "0xc440FFf040C904f49FE55806Df2037D2B850B037",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xC46479C19Fa10870FF4108841f3A82Efd15833F6",
  'name': "oxeye daisy",
  #'name'l: "oxeye daisy",
  'decimals': 0
},
{
  'address': "0xC467Dc2f2fA605ff590DbE56E7E71AbA90e15813",
  'name': "PPGv2",
  #'name'l: "PolyPigeon Token",
  'decimals': 18
},
{
  'address': "0xc4BCAa04918d8100353D468830c29d23A70E87d8",
  'name': "BRED",
  #'name'l: "BRED FINANCE",
  'decimals': 18
},
{
  'address': "0xC4e82BA0Fe6763cbE5E9CbCA0ba7cbD6F91C6018",
  'name': "aETH",
  #'name'l: "Ankr Eth2 Reward Bearing Bond (PoS)",
  'decimals': 18
},
{
  'address': "0xC515e8200df1699df0990f8440147102FDb06a60",
  'name': "PBIFI",
  #'name'l: "Orbit Bridge Polygon beefy.finance",
  'decimals': 18
},
{
  'address': "0xc55D5b3D8836116a675544B642e94Cc2D713c24d",
  'name': "?",
  #'name'l: "Polymoon",
  'decimals': 9
},
{
  'address': "0xc56d17dD519e5eB43a19C9759b5D5372115220BD",
  'name': "MOON",
  #'name'l: "Polywolf",
  'decimals': 18
},
{
  'address': "0xc5Dfa0A7E54f1dE1222C478313CF135a206F0125",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xC68e83a305b0FaD69E264A1769a0A070F190D2d6",
  'name': "ROLL",
  #'name'l: "Polyroll Token",
  'decimals': 18
},
{
  'address': "0xC698b8a1391F88F497A4EF169cA85b492860b502",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xC79358DE3868A7C751F52cFeECd650595AEE8B18",
  'name': "USDO",
  #'name'l: "pTokens USDO",
  'decimals': 18
},
{
  'address': "0xc816E22775E8A113d3A87885831B69728095E2Da",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0xc81c231A04fF6622cd3B308Ca06447114aBcD1Af",
  'name': "SAFEMOON",
  #'name'l: "SafeMoon",
  'decimals': 9
},
{
  'address': "0xc840B326E6aB36460aDB535a061342c66a6a9d07",
  'name': "?",
  #'name'l: "Hole",
  'decimals': 9
},
{
  'address': "0xc8B384090Bd6051f614759e9b56DEc27a5d2aA2d",
  'name': "MENTAL",
  #'name'l: "MENTAL",
  'decimals': 18
},
{
  'address': "0xC8c0b377f9f164bdB008c0e9fa57a3d9da2DaBCd",
  'name': "WP",
  #'name'l: "Warashibe Point",
  'decimals': 18
},
{
  'address': "0xc8D8a4F97e7d2d00185d9D61017899A40A3f247b",
  'name': "RAT",
  #'name'l: "Polyrat",
  'decimals': 18
},
{
  'address': "0xc8dD21FD1F855458D1D244840A13b8A9Ce3f31a5",
  'name': "SWAE",
  #'name'l: "Solar Wave",
  'decimals': 18
},
{
  'address': "0xc916896B1A8094D717d6E03fC5A71413Dd2A3b4f",
  'name': "xUSD",
  #'name'l: "xUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0xC95F5D57C482a9eE5bEd594e065ac0A2A81aAF6C",
  'name': "----------",
  #'name'l: "infinite peace protocol (PoS)",
  'decimals': 18
},
{
  'address': "0xc97D12255Cc6E60B7F8f26541B543Efb85172056",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0xc9B1A303dA2f94f3d482246693D5Ef27143a288f",
  'name': "iron ingot",
  #'name'l: "iron ingot",
  'decimals': 0
},
{
  'address': "0xc9D5918Eb7Aa36eDDc94511c460789B14680FD18",
  'name': "TALI",
  #'name'l: "TALI",
  'decimals': 18
},
{
  'address': "0xcA8FF28Af6dA3fb1ceB6b246e4C66eFe475A99a0",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xcB158282E5572e003953ead2C54E944867438449",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xcb29c8a02F3f9d3865A6B2819dD82C5FAD323fAE",
  'name': "POL",
  #'name'l: "Doge Polytopia",
  'decimals': 18
},
{
  'address': "0xCb83443b74Ff7ee2ECF1407Dbb73A67b1aDEcd9c",
  'name': "COP",
  #'name'l: "Pesos Colombianos",
  'decimals': 0
},
{
  'address': "0xCb8A3d96742BcF257cc3E7FF3c21aE2b2e37a160",
  'name': "YIELD",
  #'name'l: "PolyYield Token",
  'decimals': 18
},
{
  'address': "0xcBBcf31c593312B12882F3f5F6344fb9c8a0AFe2",
  'name': "JCT",
  #'name'l: "JPYC Contribution Token",
  'decimals': 18
},
{
  'address': "0xccBe9B810d6574701d324fD6DbE0A1b68f9d5bf7",
  'name': "STACK",
  #'name'l: "Stacker Ventures Token (PoS)",
  'decimals': 18
},
{
  'address': "0xCd1b5a07E53b7A5c9C08015270190469ca75c6B7",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xcd9C902e8131e4Da18eDA35b3F3084B4Bd741134",
  'name': "seed",
  #'name'l: "seed",
  'decimals': 0
},
{
  'address': "0xCDc2B9105c80F737F4FAEE7d3C86a9E18F3C0667",
  'name': "BUYSAFU",
  #'name'l: "GO BUY POLYSAFU https://t.me/polySAFU_official",
  'decimals': 18
},
{
  'address': "0xCE4e6DA9c509Cb33C23d748713c681C959f68658",
  'name': "YIELD",
  #'name'l: "PolyYield Token",
  'decimals': 18
},
{
  'address': "0xCe66aF0FcCe26Dce71395Cf030E9beb7ba1bDbbE",
  'name': "USDTEST1",
  #'name'l: "USDTEST1",
  'decimals': 18
},
{
  'address': "0xcE708afDb6decc43a300B81db667534bE902f89F",
  'name': "TestMoon",
  #'name'l: "TestMoon",
  'decimals': 9
},
{
  'address': "0xcE71eC00a61fcDCf1056D5076c2C0beF433a1DBC",
  'name': "egg",
  #'name'l: "egg",
  'decimals': 0
},
{
  'address': "0xcE829A89d4A55a63418bcC43F00145adef0eDB8E",
  'name': "renDOGE",
  #'name'l: "renDOGE",
  'decimals': 8
},
{
  'address': "0xcE899f26928a2B21c6a2Fddd393EF37c61dbA918",
  'name': "MOCA",
  #'name'l: "Museum of Crypto Art",
  'decimals': 18
},
{
  'address': "0xCe8eDac19f41A58F5255e3AA6d72cdbD2791Cc02",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xcEb23a3225cf2648A782C8DfF3601ACe0Cdc8e93",
  'name': "USDTEST3",
  #'name'l: "USDTEST3",
  'decimals': 18
},
{
  'address': "0xCf3616407E6FeEE346A55723801c62273E0050b0",
  'name': "axb",
  #'name'l: "axb",
  'decimals': 18
},
{
  'address': "0xcF51A734A2730700e18f54ccbAC0D116B0900305",
  'name': "PBR",
  #'name'l: "PoLyBOr",
  'decimals': 18
},
{
  'address': "0xCfD4D28Bb4dc9A90084b61c905E95834692fE2ec",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xcFe2cF35D2bDDE84967e67d00aD74237e234CE59",
  'name': "PUP",
  #'name'l: "Pup Token",
  'decimals': 18
},
{
  'address': "0xD00B0405C793e7ba3c73fbdd831f96D4e5797E70",
  'name': "GMS",
  #'name'l: "Gemstones Token",
  'decimals': 9
},
{
  'address': "0xD0130509E31Ab60aD990c3C1aB8170542F8B11bD",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xd030CE4321714E053eD4AdE93B08fbF876Cb54aE",
  'name': "YEN",
  #'name'l: "YenToken",
  'decimals': 18
},
{
  'address': "0xD05AB24d49b3463A4401Cd6b81ce02F4246202a6",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xD0660cD418a64a1d44E9214ad8e459324D8157f1",
  'name': "WOOFY",
  #'name'l: "Woofy",
  'decimals': 12
},
{
  'address': "0xd0f3121A190d85dE0AB6131f2bCEcdbfcfB38891",
  'name': "YELD",
  #'name'l: "PolyYeld Token",
  'decimals': 18
},
{
  'address': "0xD12DC5319808Bb31ba95AE5764def2627d5966CE",
  'name': "BOOTY",
  #'name'l: "PirateBooty",
  'decimals': 18
},
{
  'address': "0xd14813730b72D4dA08ADc730949AefF7F0D5B324",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xd16EA1831F1f5E732C50c9B02E7d73e540C4A57B",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xd185827117092ad10F77Bda1585b14910EE57a71",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xD1C7d902EbFA5bE9f06DD4D417f09AF68E0dBb66",
  'name': "ARABLE",
  #'name'l: "ARABLE TOKEN",
  'decimals': 4
},
{
  'address': "0xD201B8511aaB3E9b094b35ABcD5d7863c78D6d0e",
  'name': "Shark",
  #'name'l: "PolyShark Token",
  'decimals': 18
},
{
  'address': "0xd26a569468192dd82259Dc784dF4f9A73615dA42",
  'name': "MAXTOKEN",
  #'name'l: "Max Token",
  'decimals': 18
},
{
  'address': "0xD2757361c47123dB89e14988547ef5D985ED9d56",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xd2b4739392b151B84d368752173aB85c54cc8E9d",
  'name': "TKN3",
  #'name'l: "ERC20 Test Token 3",
  'decimals': 18
},
{
  'address': "0xD3A6eE9D0BE898d5F0872FBf3bAbA6354a808D77",
  'name': "BUG",
  #'name'l: "Bug Token",
  'decimals': 18
},
{
  'address': "0xd3F7CC7E18b91f0a8ECa2c594670fbe05cde2E2a",
  'name': "Copis",
  #'name'l: "CoviPinkSwap",
  'decimals': 18
},
{
  'address': "0xd418294b14B40f468241b0B39f31c2c674D91736",
  'name': "SUSHITEST",
  #'name'l: "Sushi Test",
  'decimals': 9
},
{
  'address': "0xd46df541148932690B81092f600f35208AFd4325",
  'name': "pPRISM",
  #'name'l: "Polygon Prism Network Token",
  'decimals': 18
},
{
  'address': "0xd490B87a339Fd0280cD4edD2F79560a1c69eD6Ad",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xd49E070cEc501A97D515295E5a140335B75c7571",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xD4ce462729c050b6E53817A8cb2dA4d135C1d634",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xd50dC82b44Ccb96Eb05919Faad54a704dF91daF0",
  'name': "SAILORMOON",
  #'name'l: "Sailor Moon",
  'decimals': 9
},
{
  'address': "0xD5A560EFEa1a64B4a8Dd9a4A1E285D329F7C4958",
  'name': "INFINITY",
  #'name'l: "PolyInfinity Token",
  'decimals': 18
},
{
  'address': "0xd5d84e75f48E75f01fb2EB6dFD8eA148eE3d0FEb",
  'name': "PGOV",
  #'name'l: "PGOV Token",
  'decimals': 18
},
{
  'address': "0xD6DF932A45C0f255f85145f286eA0b292B21C90B",
  'name': "AAVE",
  #'name'l: "Aave (PoS)",
  'decimals': 18
},
{
  'address': "0xD7241D0fb9EC0832B06f29d9169Ee2b5c4fA4FEe",
  'name': "SAFEMOON",
  #'name'l: "SafeMoon",
  'decimals': 9
},
{
  'address': "0xd78C475133731CD54daDCb430F7aAE4F03C1E660",
  'name': "HOPE",
  #'name'l: "Firebird.Finance",
  'decimals': 18
},
{
  'address': "0xd7a1bD68336855B36db5c458b0a9419Eb19DDebE",
  'name': "PTESTLP",
  #'name'l: "PTESTLP",
  'decimals': 9
},
{
  'address': "0xD7cD796a33b4D0E75eb71467f1Dfe9F71B74E0fB",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xD85d1e945766Fea5Eda9103F918Bd915FbCa63E6",
  'name': "CEL",
  #'name'l: "Celsius (PoS)",
  'decimals': 4
},
{
  'address': "0xD86b5923F3AD7b585eD81B448170ae026c65ae9a",
  'name': "IRON",
  #'name'l: "IRON Stablecoin",
  'decimals': 18
},
{
  'address': "0xD8D495c4619e967D44526E16C1499954C62574A5",
  'name': "?",
  #'name'l: "Bucks",
  'decimals': 9
},
{
  'address': "0xd96bB5096f5Dea315EDE4D0BA9e6Fc609623EE3A",
  'name': "JACK",
  #'name'l: "Jack Black Token",
  'decimals': 18
},
{
  'address': "0xd9a2C5C0Fb2F138C2B96582d29A648DF70F80465",
  'name': "PCAKE",
  #'name'l: "Polycake Token",
  'decimals': 18
},
{
  'address': "0xd9F748b03c06Eb2950E4f0f952E039E334D2F167",
  'name': "KKK",
  #'name'l: "KuKluxKoin",
  'decimals': 18
},
{
  'address': "0xDA537104D6A5edd53c6fBba9A898708E465260b6",
  'name': "YFI",
  #'name'l: "(PoS) yearn.finance",
  'decimals': 18
},
{
  'address': "0xDA6f726E2088F129D3Ecb2257206AdF7D8537Ba5",
  'name': "NCR",
  #'name'l: "Neos Credits (PoS)",
  'decimals': 18
},
{
  'address': "0xda8F20bf431d04a3661250F922D75e2bBE0B001C",
  'name': "Apple",
  #'name'l: "Apple Finance",
  'decimals': 18
},
{
  'address': "0xdaAd0665d6fae40F7Aa9cDd5F874BDBbeE1645A2",
  'name': "PolyRabbit",
  #'name'l: "PolyRabbit Token",
  'decimals': 18
},
{
  'address': "0xDaBE56AA2aBa9593dc3663D899FC3793c265e6b9",
  'name': "HONOR",
  #'name'l: "Honor",
  'decimals': 18
},
{
  'address': "0xdaDbb4681DeE476f2F4dEce54e6b53d9C824ed35",
  'name': "?",
  #'name'l: "Moonshine",
  'decimals': 9
},
{
  'address': "0xDAE5F1590db13E3B40423B5b5c5fbf175515910b",
  'name': "maUSDT",
  #'name'l: "Matic Aave interest bearing USDT",
  'decimals': 6
},
{
  'address': "0xDb14514A1A9C0D106DF1DB86d9adAD0eA0Cb7886",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xDb3b3b147A030F032633f6C4BEBf9a2fB5a882B5",
  'name': "EASY",
  #'name'l: "EASY",
  'decimals': 18
},
{
  'address': "0xDB57ce88D6fc04A18945412F6BC5B74D9026aDB8",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xDBf31dF14B66535aF65AaC99C32e9eA844e14501",
  'name': "renBTC",
  #'name'l: "renBTC",
  'decimals': 8
},
{
  'address': "0xDc1F2BFe60Bf4aE02C5FDeeCFc0528725031D47d",
  'name': "EQTY",
  #'name'l: "Equity",
  'decimals': 18
},
{
  'address': "0xDc88465D3Cf0D51f63ca2B51DA7D93Fc7a0EB833",
  'name': "PTK",
  #'name'l: "PolyTik",
  'decimals': 18
},
{
  'address': "0xDcBe578206e32801662c74bEd8437b2A3B1E0Cbe",
  'name': "SRK",
  #'name'l: "SHARK",
  'decimals': 18
},
{
  'address': "0xDd78b87C915Afb3e670682e9945D81cA1cA76020",
  'name': "USDTEST3",
  #'name'l: "USDTEST3",
  'decimals': 18
},
{
  'address': "0xdda9BbeB4f9cd44d4f532DF6F09E9cb0440333Bc",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xDe2Ce2A7F063c101fED6a7ADAE1413f82696661C",
  'name': "YQTEST2",
  #'name'l: "YQTEST2",
  'decimals': 18
},
{
  'address': "0xDf065D76EE3d0F1cAA3A1Ed5b36121c7b7BEf795",
  'name': "MICE",
  #'name'l: "Polymouse",
  'decimals': 18
},
{
  'address': "0xdF7837DE1F2Fa4631D716CF2502f8b230F1dcc32",
  'name': "TEL",
  #'name'l: "Telcoin (PoS)",
  'decimals': 2
},
{
  'address': "0xe0a39b2cf3365147CC98A70dC93d4fB253FF8c09",
  'name': "SPOLY",
  #'name'l: "SafePoly Token",
  'decimals': 9
},
{
  'address': "0xE0b22E0037B130A9F56bBb537684E6fA18192341",
  'name': "maDAI",
  #'name'l: "Matic Aave interest bearing DAI",
  'decimals': 18
},
{
  'address': "0xE0bd350D4d5AdE6e40aDF4B64875A05653E93C56",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0xE0Ee1D50C3020F16676C131c90f306E95D25668a",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xe1159B20ae213e33F9e4D10a2F88eb7Fc8eD4bfa",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xE13d7269bbB7c9269bbe357711a90332C8d56968",
  'name': "?",
  #'name'l: "Polymoon",
  'decimals': 9
},
{
  'address': "0xE1C8f3d529BEa8E3fA1FAC5B416335a2f998EE1C",
  'name': "ELK",
  #'name'l: "Elk",
  'decimals': 18
},
{
  'address': "0xe205F89828d68f2BAd2C43618AAE75C3b74146c0",
  'name': "PPG",
  #'name'l: "PolyPigeon",
  'decimals': 18
},
{
  'address': "0xE277eF1f3ebDF62071Edd662DBbdb7C97CF386c8",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xe2848E6d0590895754E2465254DE7Afde6130122",
  'name': "READ 'address'",
  #'name'l: "READ 'address'",
  'decimals': 9
},
{
  'address': "0xe2B282C8bbE72E63E128b61101d788B9417faf78",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xE2D20d7EeC09958F81C045cD1D3B47A1cf6450a2",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xE2dDce59dEe4e56ea8F5399c79eE358cDe778E4b",
  'name': "COMMUNITYMOON",
  #'name'l: "CommunityMoon",
  'decimals': 9
},
{
  'address': "0xE2F7441c55fdd2A4D961cC25CdbB9a6289CE7632",
  'name': "obsidian block",
  #'name'l: "obsidian block",
  'decimals': 0
},
{
  'address': "0xE329456b762a3888bbaFf6880036931D1399a417",
  'name': "LTI",
  #'name'l: "Layer 2 Index (PoS)",
  'decimals': 18
},
{
  'address': "0xe37745287d7A3A1e49143716cc93Ae92077a7cA2",
  'name': "CDTK",
  #'name'l: "CD_TOK",
  'decimals': 18
},
{
  'address': "0xe3BfD69f3385EcB2E0EAfF8EfE6c8fAE4d83a3cA",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0xe3c4006Ab7e02e91dF6016ACf238EbC85F8c42D4",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0xE4B8C5C3bd0db0079152640Ae51a5e8d7cFF840F",
  'name': "FMG",
  #'name'l: "Flamingo",
  'decimals': 18
},
{
  'address': "0xE4Dd8a8b06e44054B35385534adB1b93E4312bD0",
  'name': "TEST",
  #'name'l: "TEST",
  'decimals': 9
},
{
  'address': "0xE5bc5cc229cE7A2Af1eCE335cC48CC6b86F374C4",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xe5c08E74348fa9c11433ad2D04D83368f85070c6",
  'name': "TKN4",
  #'name'l: "ERC20 Test Token 4",
  'decimals': 18
},
{
  'address': "0xE622e9232C7627C0dfA181e6A9E10612627e6E7E",
  'name': "xUSD",
  #'name'l: "xUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0xe6456F72cB3F5c62b6A6F41AD4dD433Aa2041080",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xe68361E0f58D0C1e38A5392Dd7e0c6BB5CD66833",
  'name': "PolyGame",
  #'name'l: "PolyGameFinance",
  'decimals': 18
},
{
  'address': "0xe6FC6C7CB6d2c31b359A49A33eF08aB87F4dE7CE",
  'name': "IGG",
  #'name'l: "IG Gold (PoS)",
  'decimals': 6
},
{
  'address': "0xE72FEd7814C9b9fF6cC3dA1DD9ccdaA4Bb00bf38",
  'name': "TST",
  #'name'l: "TST",
  'decimals': 4
},
{
  'address': "0xE745F190A0085c4dDbF41A193BCfB3Dadf1401A1",
  'name': "LEEK",
  #'name'l: "Green Leek",
  'decimals': 18
},
{
  'address': "0xe7b8f0A9D00398bf44Ea59712A1870Ee5051226d",
  'name': "CRYSTAL",
  #'name'l: "Silver Crystal",
  'decimals': 18
},
{
  'address': "0xE840B73E5287865EEc17d250bFb1536704B43B21",
  'name': "mStable USD (Polygon PoS)",
  #'name'l: "mUSD",
  'decimals': 18
},
{
  'address': "0xE846f8cfDB902B79A6ecfed864825bB98E8DaB57",
  'name': "YQTEST3",
  #'name'l: "YQTEST3",
  'decimals': 18
},
{
  'address': "0xE8C43BCFe8677bf902468ec3D803D1D82e7E80fB",
  'name': "TKN3",
  #'name'l: "ERC20 Test Token 3",
  'decimals': 18
},
{
  'address': "0xe9545f78eF5c94ECcbe3BbF5bb0Ba9DF64408379",
  'name': "KNZ",
  #'name'l: "kenzo",
  'decimals': 18
},
{
  'address': "0xE9828045632b32E2aaC7f3a4C1511C0d8965576C",
  'name': "BORG",
  #'name'l: "TheBorg.Eth.Link",
  'decimals': 8
},
{
  'address': "0xe9ca49344228B7e6C4897A8a6E6C25d701F44042",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xe9d9018118B768a6172daFaf5A5b588ED41E7934",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0xe9F9a290A224627CC5075BE5e2401E8Dd972f154",
  'name': "EXP",
  #'name'l: "Experimental",
  'decimals': 18
},
{
  'address': "0xea255369b535E5A65aB4524420a9B4ec2c11Dfc9",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xeA927C743A4c4Ba826b399bC71FA3f8558f66629",
  'name': "GMS",
  #'name'l: "Gemstones Token",
  'decimals': 9
},
{
  'address': "0xea9306Bbe5fEE6D501282b34e9Db2C25415662DD",
  'name': "RPP",
  #'name'l: "rainbowpuffpuff (PoS)",
  'decimals': 18
},
{
  'address': "0xEAf547f3f24aBC2eD6fD96d39752d44AB1C91B13",
  'name': "stone block",
  #'name'l: "stone block",
  'decimals': 0
},
{
  'address': "0xeaf766e7eF51BaBe7be33b7169f5E27DBDdc6fC5",
  'name': "bary",
  #'name'l: "barry coin",
  'decimals': 18
},
{
  'address': "0xeB0b51aa20DFa8682C100fBE3c083D36642AB090",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xEB1bccE5009D158231C6F07A0e9c6Be2aB50197F",
  'name': "GMS",
  #'name'l: "Gemstones.finance",
  'decimals': 18
},
{
  'address': "0xeb2778f74E5ee038E67AA6c77f0F0451ABd748FD",
  'name': "PZAP",
  #'name'l: "PolyZap",
  'decimals': 18
},
{
  'address': "0xEb94A5e2C643403E29fa1d7197e7E0708B09aD84",
  'name': "ONX",
  #'name'l: "OnX.finance (PoS)",
  'decimals': 18
},
{
  'address': "0xEC1a0B35275494D4A0519ed4864Ac4FEA28B2Cba",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xec85E2A09a4242CF31d0A2D20980bDef67eb7761",
  'name': "GAME",
  #'name'l: "GAME Token",
  'decimals': 18
},
{
  'address': "0xec9fC958e2995bbfCd72abb00fBC8E08f96E657F",
  'name': "white tulip",
  #'name'l: "white tulip",
  'decimals': 0
},
{
  'address': "0xece151B5d01B07BD1104A2767ACF8F1770FcA13d",
  'name': "BABY",
  #'name'l: "BabySwap",
  'decimals': 18
},
{
  'address': "0xED06Ada906f5DdE290C082182cF3E28e55E512FB",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xedaf7c80b8a61Db945aD6b29c6b5efeD180A0E7F",
  'name': "ZMT",
  #'name'l: "ZOmbooT",
  'decimals': 18
},
{
  'address': "0xEdE0934e199caFA722F0620accB1f9ce62E1614E",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xEde1B77C0Ccc45BFa949636757cd2cA7eF30137F",
  'name': "WFIL",
  #'name'l: "Wrapped Filecoin (PoS)",
  'decimals': 18
},
{
  'address': "0xee7666aACAEFaa6efeeF62ea40176d3eB21953B9",
  'name': "MCHC",
  #'name'l: "MCHCoin (PoS)",
  'decimals': 18
},
{
  'address': "0xeEAC0eB93856b4ca60fB980bE45Ea29Dc0345260",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xEEeF80571f701B41D9da955A85A2b2Aa26B0714b",
  'name': "GMS",
  #'name'l: "Gemstones.finance Token",
  'decimals': 18
},
{
  'address': "0xeFb3009DdAc87E8144803d78E235E7fb4cd36e61",
  'name': "PolyMoon",
  #'name'l: "PolyMoon",
  'decimals': 9
},
{
  'address': "0xf0A229B97990817e2aC50fBb8eF2620684742B31",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xf0f38B0168E12b7Eb895084e36ce36EAF840f9C6",
  'name': "KFF",
  #'name'l: "Fried Chicken",
  'decimals': 18
},
{
  'address': "0xF14295026109CCD34bB12FA5e3734718C3855135",
  'name': "CBNSHRK",
  #'name'l: "CubanShark",
  'decimals': 9
},
{
  'address': "0xf1c1A3C2481A3a8A3f173A9ab5Ade275292A6fA3",
  'name': "VEE",
  #'name'l: "BLOCKv Token (PoS)",
  'decimals': 18
},
{
  'address': "0xf2b768fFB2d7513bBaF7256b2Fcb18213dafb865",
  'name': "SQUID",
  #'name'l: "PolyOrca",
  'decimals': 18
},
{
  'address': "0xF2fD98bDA7065fBA2733e91045240820baCC7E20",
  'name': "MEME",
  #'name'l: "PolyMemeV2",
  'decimals': 18
},
{
  'address': "0xF30aa10E63f40490161926E935CADe7b3B4bB8Db",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xF3ddd404d2596c62E81Cf7A5d0cC0582874F6760",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xf3E65d40D682BE2319a10FafCbb9437b6D121382",
  'name': "USDTEST3",
  #'name'l: "USDTEST3",
  'decimals': 18
},
{
  'address': "0xf4138CEF784D1dd3CF85cA93e28E8EEb9E83d923",
  'name': "?",
  #'name'l: "Polymoon",
  'decimals': 9
},
{
  'address': "0xf455f1097F8C7A2747DA12638e3B36a9Ae2041b6",
  'name': "allium",
  #'name'l: "allium",
  'decimals': 0
},
{
  'address': "0xf481507E1d833B76A68B73bE9F1F68EEcdCF265B",
  'name': "MEME",
  #'name'l: "PolyMeme",
  'decimals': 18
},
{
  'address': "0xF4B0903774532AEe5ee567C02aaB681a81539e92",
  'name': "GAJ",
  #'name'l: "PolyGaj Token",
  'decimals': 18
},
{
  'address': "0xF4b8888427b00d7caf21654408B7CBA2eCf4EbD9",
  'name': "maTUSD",
  #'name'l: "Matic Aave interest bearing TUSD",
  'decimals': 18
},
{
  'address': "0xf50D05A1402d0adAfA880D36050736f9f6ee7dee",
  'name': "INST",
  #'name'l: "Instadapp (PoS)",
  'decimals': 18
},
{
  'address': "0xf56856E3e71e7e7e567b4a6787569CCc1a7f3e87",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xF5801eeC8DED569Bd4BBf0d0638a4ebA590B3298",
  'name': "NEET",
  #'name'l: "Air Drop NEET COIN",
  'decimals': 18
},
{
  'address': "0xf5c39a7CEff5dA5BFB062389f62939A8C8396CB3",
  'name': "gNFT",
  #'name'l: "getNFT",
  'decimals': 18
},
{
  'address': "0xf613C467dCE6bad5cEe0875558133CB59D2605ed",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xf629712180bEF6F4c569B704e03d0AcbE276Eb6d",
  'name': "WSTA",
  #'name'l: "Wrapped STA (PoS)",
  'decimals': 18
},
{
  'address': "0xF84B92738Cb51d39Ec5a4EA03F19BfdAD545a8aE",
  'name': "TESTD",
  #'name'l: "TestDino",
  'decimals': 18
},
{
  'address': "0xf937b1751e273cB01A4E9c8bEdc7E6Ca74fA9188",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xf9a66b594905363967d43ECfA00d8331086074A3",
  'name': "WORMS",
  #'name'l: "Worms Token",
  'decimals': 18
},
{
  'address': "0xFA348e08b0b2FBBBc1AA4774c347A1E4789a0A2E",
  'name': "PLL",
  #'name'l: "PolyLala",
  'decimals': 18
},
{
  'address': "0xFa57dF7fFE9EA461E3411c2301C4e2319550936C",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xFA60804C74Ba841A695c3EBf7630CE73696e4983",
  'name': "axM",
  #'name'l: "Test ax",
  'decimals': 18
},
{
  'address': "0xFA6d4CaFe3C21Df630E454A855E2b09C22817890",
  'name': "dm",
  #'name'l: "TestDM",
  'decimals': 18
},
{
  'address': "0xfa72b07adE2Af7d41413850A1e8D5578b3490988",
  'name': "REGI",
  #'name'l: "RegiCoin (PoS)",
  'decimals': 18
},
{
  'address': "0xfaA4c6672c9396d427e1bEA251b765D30029AbFe",
  'name': "DG",
  #'name'l: "Dragon",
  'decimals': 18
},
{
  'address': "0xfab4877eb74526109F9e84614057ABe2888f99F8",
  'name': "TAPS",
  #'name'l: "TapSwap",
  'decimals': 18
},
{
  'address': "0xFac2EA9c7F0d9295D6Cd1Bab35b9C1de9dCCA7c0",
  'name': "?",
  #'name'l: "Harvester DAO",
  'decimals': 18
},
{
  'address': "0xfB83162266a4463299Dd681c1Fab88d7188c6944",
  'name': "CANNON",
  #'name'l: "Armaments",
  'decimals': 18
},
{
  'address': "0xFbdd194376de19a88118e84E279b977f165d01b8",
  'name': "BIFI",
  #'name'l: "beefy.finance",
  'decimals': 18
},
{
  'address': "0xfcb5DF42e06A39E233dc707bb3a80311eFD11576",
  'name': "METH",
  #'name'l: "www.METH.co.in",
  'decimals': 18
},
{
  'address': "0xfCe02B5936CaC182b56DA79894E1Ab8004afc873",
  'name': "YQTEST3",
  #'name'l: "YQTEST3",
  'decimals': 18
},
{
  'address': "0xFd07ee1F2f5d021aCE8F10f82CDe5F485F9a3Ad3",
  'name': "xUSD",
  #'name'l: "xUSD",
  'decimals': 18
},
{
  'address': "0xFd6cF3A1fcb42371fD7E69633d31303868b8171a",
  'name': "OMNIUNIT",
  #'name'l: "Omniunit (PoS)",
  'decimals': 18
},
{
  'address': "0xFdc26CDA2d2440d0E83CD1DeE8E8bE48405806DC",
  'name': "BTU",
  #'name'l: "BTU Protocol (PoS)",
  'decimals': 18
},
{
  'address': "0xfE1eE1409154557DbB43Cc060f615C27cD042c1F",
  'name': "MASK",
  #'name'l: "MetaMask",
  'decimals': 18
},
{
  'address': "0xfE68E9EfeA5f275C9FdF36a1B19c7A3C20DCB48E",
  'name': "NIOXV2",
  #'name'l: "SmartdexPair",
  'decimals': 18
},
{
  'address': "0xFe7FF8b5dfbA93A9EaB7Aee447C3c72990052d93",
  'name': "UBI",
  #'name'l: "Universal Basic Income (PoS)",
  'decimals': 18
},
{
  'address': "0xFeD16c746CB5BFeD009730f9E3e6A673006105c7",
  'name': "DRC",
  #'name'l: "Digital Reserve Currency (PoS)",
  'decimals': 0
},
{
  'address': "0xff30636B5B2d4497c65d08e8798D86987Fdc2F2E",
  'name': "WYZ",
  #'name'l: "WISECOIN",
  'decimals': 18
},
{
  'address': "0xFF39754755237b13441308DB986E97D599034AAC",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0xff88434E29d1E2333aD6baa08D358b436196da6b",
  'name': "BORING",
  #'name'l: "BoringDAO (PoS)",
  'decimals': 18
},
{
  'address': "0x98bA38AF9C0239D67B71661dBe1a4205499fbC5D",
  'name': "BONE",
  #'name'l: "Bone Token",
  'decimals': 18
},
{
  'address': "0x420A15cc477A394429E15E0EC677EB46e49FFCEA",
  'name': "MOVR",
  #'name'l: "Moonriver",
  'decimals': 18
},
{
  'address': "0x49d6eD49B1716598a5C17B57Fb703AFE2B3104a2",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x656AbeBBeB42413DcD711f4F529261398c2a5948",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x49677e90F3b521f7CD564E4138e63641e251daF8",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 11
},
{
  'address': "0x9114C9A9efd04f67dFf6b94B7d1E42Dbd4638F99",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 11
},
{
  'address': "0xa1212BD20A0926b4939f17D396521c439F48B81e",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 11
},
{
  'address': "0xDc15985340799F4b7e31812E20d68537b9DF25f4",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0xaC817e613A1cD679C78D720f5C4e485E750C2331",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0xeAC64482D11314219d1895b63FE9E560624aee6f",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x088dF2da7b8fA68538222DF007fDd519c9caa1dF",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x379f40E2a6a5d204885f437C29166D86Eb3762bE",
  'name': "HOUR",
  #'name'l: "Hourglass Token",
  'decimals': 18
},
{
  'address': "0xEebC70Fb7dE602e457DD759112d60Cf885f92Ac6",
  'name': "PSafe",
  #'name'l: "PolySafe",
  'decimals': 9
},
{
  'address': "0x0aFF058e91DC7c74C5E5f8Aeb6f209b53E3b4681",
  'name': "PMF",
  #'name'l: "PolyMath.Finance",
  'decimals': 18
},
{
  'address': "0xD2eBa21C2E0D6F996FDD063ae20aCA8264Ac1929",
  'name': "sUSDC",
  #'name'l: "Safe USDC",
  'decimals': 18
},
{
  'address': "0x1E368065177eCB78717b282dD6bE7cD80A8A04B8",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x4E77c61DA094E08E427CbaDD6b213ac2A44C4c54",
  'name': "POLYPIG",
  #'name'l: "POLYPIG",
  'decimals': 9
},
{
  'address': "0x76cc664E48Feb7B1368c13548c7328e17da9BfAC",
  'name': "CNE",
  #'name'l: "Chinese",
  'decimals': 18
},
{
  'address': "0xAbCE068858731724B831fdCC90A9DA5574A8c432",
  'name': "PLP",
  #'name'l: "PolyPig",
  'decimals': 18
},
{
  'address': "0x0a38F2774a92B6EE73f60820f2bd9283250D4434",
  'name': "BBC",
  #'name'l: "Babycoin",
  'decimals': 18
},
{
  'address': "0xC38e35B03657814F73Ce801aA7a0B35275B4182A",
  'name': "Babycoin",
  #'name'l: "Babycoin",
  'decimals': 18
},
{
  'address': "0x3112c1779813ceb0c8c8E5fB19bC75A1C2a16781",
  'name': "USA",
  #'name'l: "America",
  'decimals': 18
},
{
  'address': "0x0583dD3d49d618a2aE969496522A631392A0970B",
  'name': "MaticMoon",
  #'name'l: "Matic Moon",
  'decimals': 9
},
{
  'address': "0x6b140057F140e082B2501399915D9629751b011e",
  'name': "POLYTOKEN",
  #'name'l: "PolyToken",
  'decimals': 18
},
{
  'address': "0xD2C54753B3F0dc2a56A145636c755E0dCD48527C",
  'name': "RSA",
  #'name'l: "Russia",
  'decimals': 18
},
{
  'address': "0xd11BfA35686e8806456D0F3Ce8AED12914b50469",
  'name': "HTEST",
  #'name'l: "HTest Coin",
  'decimals': 9
},
{
  'address': "0x62AB1D0f332A03992E206784201bB848D34394F5",
  'name': "QUARK",
  #'name'l: "Quark Token",
  'decimals': 18
},
{
  'address': "0xa64e1096DAFC625Cefe30A315e52BeCBBAA06279",
  'name': "ABYSS",
  #'name'l: "Abyss Token",
  'decimals': 18
},
{
  'address': "0x3f37C4f5757806E82738800362A64743cC4B120f",
  'name': "MMP",
  #'name'l: "MaticMoneyPro",
  'decimals': 9
},
{
  'address': "0x31EF549476956d6901220B0Eb13dd3Ec957F59C2",
  'name': "MMP",
  #'name'l: "MaticMoneyPro",
  'decimals': 9
},
{
  'address': "0xE62Ec2e799305E0D367b0Cc3ee2CdA135bF89816",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x37Ff2a6cF0E8061CBD9a00919690F1B0A46eE674",
  'name': "FROGE",
  #'name'l: "froge.finance (PoS)",
  'decimals': 9
},
{
  'address': "0x04e6f0aAb19149a23170f94D309CF949e8B5241b",
  'name': "TEDD",
  #'name'l: "TEDD FINANCE",
  'decimals': 18
},
{
  'address': "0x04Dc2Da39759B272A6bEC64e6771EA0b87737151",
  'name': "HOUR",
  #'name'l: "Hourglass Token",
  'decimals': 18
},
{
  'address': "0x5Af1D52db428D50d01cA4e284Dc826d0c2596215",
  'name': "Bison",
  #'name'l: "Bison Token",
  'decimals': 18
},
{
  'address': "0xC0860a6f29C77BeE94f8726eAbAa337627a18514",
  'name': "BugattiV",
  #'name'l: "Bugatti Veyron",
  'decimals': 9
},
{
  'address': "0x609255414fF5289f87c99bAF9737a4EC85A18643",
  'name': "SONG",
  #'name'l: "Beatify (PoS)",
  'decimals': 18
},
{
  'address': "0x9CA6a77C8B38159fd2dA9Bd25bc3E259C33F5E39",
  'name': "SPORK",
  #'name'l: "The SporkDAO Token (PoS)",
  'decimals': 18
},
{
  'address': "0x34C1b299A74588D6Abdc1b85A53345A48428a521",
  'name': "EZ",
  #'name'l: "EASY V2",
  'decimals': 18
},
{
  'address': "0xC168E40227E4ebD8C1caE80F7a55a4F0e6D66C97",
  'name': "DFYN",
  #'name'l: "DFYN Token (PoS)",
  'decimals': 18
},
{
  'address': "0x16ECCfDbb4eE1A85A33f3A9B21175Cd7Ae753dB4",
  'name': "ROUTE (PoS)",
  #'name'l: "Route",
  'decimals': 18
},
{
  'address': "0x21D57A3e54f12e26Ba0AF0b9aF394537Af8b04c7",
  'name': "MiniDoge",
  #'name'l: "MiniDoge",
  'decimals': 9
},
{
  'address': "0xc2E93cC8E8EC96076D20f9d9d16f8d415D90CFb8",
  'name': "MiniDoge",
  #'name'l: "MiniDoge",
  'decimals': 9
},
{
  'address': "0x093b735dD3daEceDA74A4DC4352aF82EA54B806D",
  'name': "SHIBABY",
  #'name'l: "Shib Baby to the Moon",
  'decimals': 5
},
{
  'address': "0x9d47b3FAA5fF227D2BD404F572eF0ab0C8409161",
  'name': "VALX",
  #'name'l: "Validator (PoS)",
  'decimals': 18
},
{
  'address': "0x029F86fa657E25AE267B283312066cFd4ff136fA",
  'name': "EMOJI",
  #'name'l: "EMOJI",
  'decimals': 18
},
{
  'address': "0x91eE7D76599Fdc8da86FD291423139BF5D679CF0",
  'name': "LMOOSE",
  #'name'l: "Littlemoose",
  'decimals': 9
},
{
  'address': "0x4f5891E1db2173C1a630674B48b607Dd429dE0eB",
  'name': "MiniDoge",
  #'name'l: "MiniDoge",
  'decimals': 9
},
{
  'address': "0xb388A508E6ef30b1480e55356C2D57DEF5e04C54",
  'name': "PolyuDog_test",
  #'name'l: "PolyuDog_test",
  'decimals': 18
},
{
  'address': "0x5c6D6f5B8c0650e13A069080507Ae0A6bE7b36F4",
  'name': "PolyuDog",
  #'name'l: "PolyuDog",
  'decimals': 18
},
{
  'address': "0xdC3aCB92712D1D44fFE15d3A8D66d9d18C81e038",
  'name': "POLAR",
  #'name'l: "Polaris",
  'decimals': 18
},
{
  'address': "0xb6D721D80446B9884FF8A6082145d6411B657559",
  'name': "QI",
  #'name'l: "QiSwap (POS)",
  'decimals': 18
},
{
  'address': "0xD354D56DaE3588F1145dd664bc5094437b889d6F",
  'name': "ARTHX",
  #'name'l: "ARTH Shares",
  'decimals': 18
},
{
  'address': "0xE52509181FEb30EB4979E29EC70D50FD5C44D590",
  'name': "ARTH",
  #'name'l: "ARTH Valuecoin",
  'decimals': 18
},
{
  'address': "0x17e5457b6A5c3eFd9b8b4577630b3462abfa2831",
  'name': "MTK",
  #'name'l: "MyToken",
  'decimals': 9
},
{
  'address': "0x6214717EDEfA9e5a3C2A013CD30E5bF432cF76E9",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0x91b7479DB2d0e8A74Bdf223c3141ADB2A832ac3c",
  'name': "TKN3",
  #'name'l: "ERC20 Test Token 3",
  'decimals': 18
},
{
  'address': "0xcFFF1F8332b073983ca026e62CAAC04AA5C5D6C9",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0x01bCEC6175FA9366D14b8275e95D0fA45702f696",
  'name': "GORILLA",
  #'name'l: "PolyGorilla",
  'decimals': 18
},
{
  'address': "0x5dEC6FcEE448196AEA3C82baF22d0317a9080370",
  'name': "MiniDoge",
  #'name'l: "MiniDoge",
  'decimals': 9
},
{
  'address': "0x396d2865A89142F3912A83CeFC5CA1B634e8166B",
  'name': "MiniPig",
  #'name'l: "MiniPig",
  'decimals': 9
},
{
  'address': "0xB3747eFA81c42bae6D468EAfDbD2e027B6c9Ec6b",
  'name': "SWTCH2",
  #'name'l: "Switch Token",
  'decimals': 18
},
{
  'address': "0x29d2E93F8439b9c20d577011c47391c3B622D274",
  'name': "1INCH",
  #'name'l: "1INCH Token",
  'decimals': 18
},
{
  'address': "0x9482C9D634953fa764E71aA4eFc0F766E148FB87",
  'name': "MTK",
  #'name'l: "MyToken",
  'decimals': 9
},
{
  'address': "0x54c7ff21a565259A5b5c4e4583e745Bd0ad5f7a9",
  'name': "TENDIES",
  #'name'l: "TENDIES",
  'decimals': 18
},
{
  'address': "0x4D7a44D7c243BB2Db21dEF4FD5319c0EcA2E5F79",
  'name': "RADIO",
  #'name'l: "Radio Token",
  'decimals': 18
},
{
  'address': "0x9192f2EF62F308292a02918fB4d9C8B78fdb79Bf",
  'name': "LC10INCH",
  #'name'l: "Lous10inch",
  'decimals': 18
},
{
  'address': "0x87535D127904527B84a13d11c300Cd54300aC6FC",
  'name': "DMND",
  #'name'l: "Dmnd Token",
  'decimals': 18
},
{
  'address': "0xF391F574C63d9b8764B7a1F56D6383762E07B75B",
  'name': "FEG",
  #'name'l: "FEGtoken (PoS)",
  'decimals': 9
},
{
  'address': "0x3F22090f3Ea88EA1A2bD603557F700A8b6D7B1F0",
  'name': "MTK",
  #'name'l: "MyToken",
  'decimals': 9
},
{
  'address': "0x05615241c136B5142bB491bed60fd0152AB781bb",
  'name': "PCAKE",
  #'name'l: "Poly Cake",
  'decimals': 18
},
{
  'address': "0xF501dd45a1198C2E1b5aEF5314A68B9006D842E0",
  'name': "MTA",
  #'name'l: "Meta (PoS)",
  'decimals': 18
},
{
  'address': "0xF99d4a031AB410b5892a32068E636f83d7CD3F76",
  'name': "MTP",
  #'name'l: "SON TUNG MTPX100",
  'decimals': 18
},
{
  'address': "0xc594EE1c80992A0E3230b6eAa8CeD8Fe36B719B1",
  'name': "ISSv2",
  #'name'l: "IronSwap Token",
  'decimals': 18
},
{
  'address': "0x2b88aD57897A8b496595925F43048301C37615Da",
  'name': "PICKLE",
  #'name'l: "PickleToken (PoS)",
  'decimals': 18
},
{
  'address': "0x52054D7F4eCb33f56f8C27CdF66684032E63f24c",
  'name': "CARROT",
  #'name'l: "CarrotCake Finance",
  'decimals': 18
},
{
  'address': "0x276E47EEf8032518BF61bfA5F87b18A41C1f5825",
  'name': "PSAR",
  #'name'l: "Poolsar.Finance",
  'decimals': 18
},
{
  'address': "0xA4A137b4eae7f71ABA003e7d77954cBE832121F4",
  'name': "ORI",
  #'name'l: "Origami.Farm",
  'decimals': 18
},
{
  'address': "0xA2f9D01CeD64cfd9BfF9C4D62056d5f8B748Ba8c",
  'name': "EARN",
  #'name'l: "PolyEarn",
  'decimals': 18
},
{
  'address': "0x356Dc5C63E5a6424314e032f3BcD075555069cf0",
  'name': "TSX",
  #'name'l: "TestToken",
  'decimals': 18
},
{
  'address': "0xC21e75A5432521cCa6045F9211f21328ec7D4359",
  'name': "MNC",
  #'name'l: "Minecoin",
  'decimals': 18
},
{
  'address': "0x62E713DC9DE44Ba4E264cFA9732268e8554e72fD",
  'name': "Hasagi",
  #'name'l: "YasuoSwap",
  'decimals': 18
},
{
  'address': "0x9bEAcb549a3436Bd05D89fCF341d1f45e2b67447",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x26d326B1fc702260baeB62334d7c1Da6f1a2C386",
  'name': "GTPS",
  #'name'l: "GLOBAL TRANSACTION PAYMENT SOLUTION",
  'decimals': 18
},
{
  'address': "0x4Ee8135b058b8A6Bbd5Af8E9Ce387e051731e7B7",
  'name': "ILVA",
  #'name'l: "ILVA",
  'decimals': 18
},
{
  'address': "0xBC6B630B014e941A921CDc0967AAea2a8aB932B5",
  'name': "PCP",
  #'name'l: "PolyChain Protocol",
  'decimals': 9
},
{
  'address': "0x22734Bfa0bD1589BC283E78F672EdD5736503dfA",
  'name': "CRAB",
  #'name'l: "CRABSWAP",
  'decimals': 18
},
{
  'address': "0x77C5Aba9cD27Bf721d2a6426ED1DC6859C907412",
  'name': "ZED20",
  #'name'l: "ZED RUN",
  'decimals': 18
},
{
  'address': "0xe6F0306D638a2CD1f0b6700Eb01745CbD69D6E47",
  'name': "PolyTopia",
  #'name'l: "PolyTopia",
  'decimals': 18
},
{
  'address': "0x116Ff0d1Caa91a6b94276b3471f33dbeB52073E7",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x6e57020F08642E7934E03D6B0080d37c595fD6fE",
  'name': "MORPH",
  #'name'l: "PolyMorph.finance",
  'decimals': 9
},
{
  'address': "0xd79F527DaDA3818Aa8a606344565D7ac9F58A4b5",
  'name': "POLYPAD",
  #'name'l: "Polypad.network",
  'decimals': 9
},
{
  'address': "0xa4EB68622ea24512D2B3263D7E705AD418325260",
  'name': "Seal",
  #'name'l: "Poly Seal Defi",
  'decimals': 18
},
{
  'address': "0x7D41E0D59149F018D0D5B93F44B65f8ae0b90d6d",
  'name': "GOLD",
  #'name'l: "BullionGoldToken",
  'decimals': 18
},
{
  'address': "0xCB0bCBe3C0bD963f549480C2D052024db68aDEfB",
  'name': "CUPPA",
  #'name'l: "CUPPA",
  'decimals': 18
},
{
  'address': "0xE6a823862eE153168C772Cf494e9DfF77140C696",
  'name': "BBL",
  #'name'l: "Bailey Building & Loans (PoS)",
  'decimals': 18
},
{
  'address': "0xe70C59b2B919995a6c1919C549D0Bc14677d1B0D",
  'name': "FISH",
  #'name'l: "Fish",
  'decimals': 18
},
{
  'address': "0xa4c835a390aFFDafa9F6e8C4408A2970ce057683",
  'name': "MEW",
  #'name'l: "PolyMew",
  'decimals': 18
},
{
  'address': "0xc4e595acDD7d12feC385E5dA5D43160e8A0bAC0E",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x93510654DeD65481C952015AD6B59538EEeBb09B",
  'name': "TECH",
  #'name'l: "Tech.com",
  'decimals': 18
},
{
  'address': "0xC8204175E1bfeEB380E1A097d33335237D86d4B0",
  'name': "DINO",
  #'name'l: "DinoSwap",
  'decimals': 18
},
{
  'address': "0x2Ab4f9aC80F33071211729e45Cfc346C1f8446d5",
  'name': "CGG",
  #'name'l: "ChainGuardians Governance Token (PoS)",
  'decimals': 18
},
{
  'address': "0x44292d6dD3A00B9C0A80159a3aC0755Dc037B525",
  'name': "DPIE",
  #'name'l: "DreamPieSwap Token",
  'decimals': 18
},
{
  'address': "0xeb168C9D678dC34D64337F4eA12cf14ed6fbE34B",
  'name': "UNI-V2",
  #'name'l: "Uniswap V2",
  'decimals': 18
},
{
  'address': "0x6896e048C95dc3d52034A5D059E3C41908fCD5C0",
  'name': "aPOLAR",
  #'name'l: "aPolaris",
  'decimals': 18
},
{
  'address': "0x634EA08a2ca78ef73D2c5B79991fa438F4287c73",
  'name': "Taco",
  #'name'l: "Choco Taco",
  'decimals': 18
},
{
  'address': "0xbf3cEfe42C7142e04aE184Ade181370C55ffD14E",
  'name': "Squid",
  #'name'l: "Squid Swap",
  'decimals': 18
},
{
  'address': "0x4CEBdBCB286101A17D3eA1f7fe7bbDeD2B2053dd",
  'name': "YLD",
  #'name'l: "Yield (PoS)",
  'decimals': 18
},
{
  'address': "0x90867b06354c25F5c28c95ffBD506E53993C941E",
  'name': "Plankton",
  #'name'l: "Plankton Yield Farming",
  'decimals': 18
},
{
  'address': "0x9c21D96bB1b8cB5F655D6837823690d54aF9A566",
  'name': "Nezumi",
  #'name'l: "Nezumi Swap",
  'decimals': 18
},
{
  'address': "0xB3D7c2cF779F7d03A04f77a6ff98c4dcB5F2B48c",
  'name': "HATCHIE",
  #'name'l: "Hatchy Pocket",
  'decimals': 18
},
{
  'address': "0xf198f5f042cADA43750799a92C5CeFcaF4dC0208",
  'name': "SPMF",
  #'name'l: "Spiderman Finance",
  'decimals': 18
},
{
  'address': "0x34F4D0c5E515fafC8c6B9a4078635aF283923236",
  'name': "FUEL",
  #'name'l: "Fuel Token",
  'decimals': 18
},
{
  'address': "0x162f82379203Efaa4E1fAd25a742A40d96951a9F",
  'name': "PawPrints?",
  #'name'l: "PawPrints?",
  'decimals': 18
},
{
  'address': "0x9A6733163b2D839C4BA9A6893E70DBaEE3CC6583",
  'name': "CZM",
  #'name'l: "CZM Token",
  'decimals': 6
},
{
  'address': "0x284cd824d5317b3E84F892DEA99b3847B205814B",
  'name': "PST",
  #'name'l: "pumpstars.finance",
  'decimals': 18
},
{
  'address': "0xc28a9f4ff1f23770cf8D8301cF4fa3A25c263421",
  'name': "Ptest",
  #'name'l: "Polytest",
  'decimals': 18
},
{
  'address': "0x3c22fBd5383F0Cb5d97Af9c3Af42Ea18fda9b9F8",
  'name': "PONZI",
  #'name'l: "POLYPONZI FARM",
  'decimals': 18
},
{
  'address': "0xe1D6C07263022A6DdaB0c070c3861Cd1616ca102",
  'name': "ICE",
  #'name'l: "Iron Finance TITANv2 Token",
  'decimals': 18
},
{
  'address': "0x6eFb1d1D51A91c8f201C57B87Fe7f5cFf0237a9c",
  'name': "SPMF",
  #'name'l: "Spiderman.Finance",
  'decimals': 18
},
{
  'address': "0xea80aA3FcEc2f72c46A96c76e0d9970b71D6D9F4",
  'name': "POLYFARM",
  #'name'l: "PolyFarm finanace",
  'decimals': 18
},
{
  'address': "0x4035395969e615Dc1B75Cef626A0afE39697a7f1",
  'name': "GHOST",
  #'name'l: "PolyGhost",
  'decimals': 18
},
{
  'address': "0x709a12186f266b8a6EB82cF4dd128D95fA670E70",
  'name': "test",
  #'name'l: "testtoken1",
  'decimals': 18
},
{
  'address': "0x2F9Cb2bC064c9f816D9Fd481FEdF545F2cB4D31d",
  'name': "D",
  #'name'l: "D",
  'decimals': 6
},
{
  'address': "0xfB341688EbF3dDa9f95C2b916D98D47F47f95a44",
  'name': "A",
  #'name'l: "A",
  'decimals': 18
},
{
  'address': "0xe9Da9F31BeEfFD244a210C68c625eB889c6ceE4d",
  'name': "SHARKY",
  #'name'l: "SHARKY FINANCE",
  'decimals': 18
},
{
  'address': "0x65b79446Dd241a06caF96a70C07c8D32aA097CBa",
  'name': "OSFIN",
  #'name'l: "Ossas Finance",
  'decimals': 18
},
{
  'address': "0x845E76A8691423fbc4ECb8Dd77556Cb61c09eE25",
  'name': "pWINGS",
  #'name'l: "JetSwap Polygon Token",
  'decimals': 18
},
{
  'address': "0x9067df48d851A9cDb73015967C424528B941AC9f",
  'name': "pDEVX",
  #'name'l: "pDEVX Token",
  'decimals': 18
},
{
  'address': "0xFd98f2ba7b239479987Bba10CFb945158Fd6A82B",
  'name': "PONZI",
  #'name'l: "PolyPonzi Token",
  'decimals': 18
},
{
  'address': "0x9f227D0091babB76deF1abc7838e500FA25CA2A1",
  'name': "OCS",
  #'name'l: "Oreo Cake Swap",
  'decimals': 18
},
{
  'address': "0x3604C15E34E705da0Ff2196e16F46E979C1F69f5",
  'name': "HOBBIT",
  #'name'l: "HobbitSwap",
  'decimals': 18
},
{
  'address': "0x78A22c2aEA6721f503E97d9B5542CF89687c7900",
  'name': "JUNGLE",
  #'name'l: "PolyGorilla L2",
  'decimals': 18
},
{
  'address': "0xBeB4DbE7539e9D7d2Bdc45B5f2f56bE2C04fc34E",
  'name': "ICE",
  #'name'l: "IRON Titanium V2",
  'decimals': 18
},
{
  'address': "0xFe244B5f7F253f9899f305D8caf51E5472A8c31b",
  'name': "HYDRA",
  #'name'l: "HYDRA",
  'decimals': 18
},
{
  'address': "0xF3D65A3E39161dc77edC85E67beEC5E0831177E9",
  'name': "XC",
  #'name'l: "XCoin",
  'decimals': 18
},
{
  'address': "0x810507179264f26080b9bf7a4a2cf176E0F98Db2",
  'name': "SAN",
  #'name'l: "SAN SAN Swap",
  'decimals': 18
},
{
  'address': "0x4E657ECD27a5E6E50537a6B90da679d1AA2313cB",
  'name': "SOFIC",
  #'name'l: "SofinasCoin",
  'decimals': 18
},
{
  'address': "0x544e720271b1581F49f6e24963C6833CFc0AFEE0",
  'name': "SHEET",
  #'name'l: "Sheet Protocol",
  'decimals': 18
},
{
  'address': "0x2FA04d3605709efAA5191874a46B44286B911274",
  'name': "BabyLuckyTITAN",
  #'name'l: "BabyLuckyTITAN",
  'decimals': 9
},
{
  'address': "0x37666172262019DF537a0143Be3f66d7d8Bd1cDD",
  'name': "Minibabydoge",
  #'name'l: "Minibabydoge",
  'decimals': 18
},
{
  'address': "0x86BC05a6f65efdaDa08528Ec66603Aef175D967f",
  'name': "SDO",
  #'name'l: "SafeDollar.Fi",
  'decimals': 18
},
{
  'address': "0x95B8962D7FAF8459FF4D9d5032c827E803bE49F1",
  'name': "iDOG",
  #'name'l: "iDog",
  'decimals': 9
},
{
  'address': "0x1c779eC50d99e06f0cD34e894cC8Cc1dDB7AD160",
  'name': "RR",
  #'name'l: "MaticRR",
  'decimals': 18
},
{
  'address': "0x3680DbAc26b66cf185467FD6c3a5F01b6BdfF328",
  'name': "BabySpaceDog",
  #'name'l: "BabySpaceDog",
  'decimals': 9
},
{
  'address': "0x9537a798Ed613024Af2FE14C81aeccC89eFa71af",
  'name': "LuckyMatic",
  #'name'l: "Lucky Matic",
  'decimals': 9
},
{
  'address': "0xc6EdD0d7dd0aaB2cA31Aa3F9923d6A59eA570cf5",
  'name': "FreeBritney",
  #'name'l: "Free Britney Token",
  'decimals': 18
},
{
  'address': "0xC7eB49271028D813296707fE8945a7c4Fafa1cB4",
  'name': "PolyBartSimpson",
  #'name'l: "PolyBartSimpson",
  'decimals': 18
},
{
  'address': "0x3f5400F6fC06Bd838660532482132BE4cb67CeE4",
  'name': "BabyMatic",
  #'name'l: "BabyMatic",
  'decimals': 9
},
{
  'address': "0x90017E0952044806B2D4904165119aB40CD4B61f",
  'name': "6RUG",
  #'name'l: "6RUG",
  'decimals': 9
},
{
  'address': "0x9d59654271F3ED426E56594A00CcDd2431788107",
  'name': "Adddd",
  #'name'l: "Adddd",
  'decimals': 18
},
{
  'address': "0x3FB167508C74964aB5410B05a8fC6f297e311dBE",
  'name': "AQUA",
  #'name'l: "BabyAqua",
  'decimals': 9
},
{
  'address': "0x5326F8165c7D12058b89C79E3d2A9e62CFBa6644",
  'name': "BabySHIB",
  #'name'l: "BabyShib Inu",
  'decimals': 18
},
{
  'address': "0xC3843D386e3AA718f132Cd0424B90a018b497816",
  'name': "MPCat",
  #'name'l: "MPCat",
  'decimals': 9
},
{
  'address': "0x18f9bC5e42c15926eC706EfB221BfC0839cD87D7",
  'name': "BIUS",
  #'name'l: "Polybius-L1",
  'decimals': 18
},
{
  'address': "0xA93e68C0C649D3528B087A718104F5eCf1119176",
  'name': "BMT",
  #'name'l: "BullMatic",
  'decimals': 18
},
{
  'address': "0x823a3A5c95843d8ac5637083022252a786D43bFb",
  'name': "CCCBOBY",
  #'name'l: "CCCBOBY",
  'decimals': 9
},
{
  'address': "0xA74b3B02dc387D2FfB9573922d18Ac78f6b28422",
  'name': "DD1",
  #'name'l: "DD1",
  'decimals': 9
},
{
  'address': "0x2105f8a6DA79451F56227B74F72432C610e175EA",
  'name': "CANDY",
  #'name'l: "MaticCandy",
  'decimals': 9
},
{
  'address': "0x5F1C6F62E92ed4B82073a129A8342B8706F81B5F",
  'name': "behemoth",
  #'name'l: "behemoth",
  'decimals': 9
},
{
  'address': "0x72BE7dE407F7190581823a8470Bf3f0b5a502E86",
  'name': "BAT",
  #'name'l: "BATMATIC",
  'decimals': 18
},
{
  'address': "0x1518820879BC87d4dFeA5664bB1B6c240d20D4f2",
  'name': "DROP",
  #'name'l: "Drop",
  'decimals': 18
},
{
  'address': "0x85F02E9D4E1A3f52fa0Ad1Aa27A404Ab04295B1A",
  'name': "VolcanoMoney",
  #'name'l: "VolcanoMoney",
  'decimals': 18
},
{
  'address': "0x90c34f1e1F6E7E151A4eD0672B5D985A65477316",
  'name': "Tst",
  #'name'l: "Token",
  'decimals': 9
},
{
  'address': "0x36A775dd9905bE105d26D386751d8d237Ee0f4f7",
  'name': "SPSF",
  #'name'l: "Space Safe Finance",
  'decimals': 18
},
{
  'address': "0x5B76e7b501C706AEE77624440334B0d4f929ECd6",
  'name': "SRISE",
  #'name'l: "SpaceRise Token",
  'decimals': 9
},
{
  'address': "0xA8ebb24feEdF1c9e458f4aEF313D335677ABa096",
  'name': "SHIBAPLT",
  #'name'l: "SHIBA PLATINUM",
  'decimals': 16
},
{
  'address': "0x4956D7F64627d21380424e94A802099b14dAbA75",
  'name': "SCCMatic",
  #'name'l: "SCCMatic",
  'decimals': 18
},
{
  'address': "0x7aeb01b290511F92CD9DC6dBC47A8E23F8484C6b",
  'name': "Shibamoon",
  #'name'l: "Shibamoon",
  'decimals': 18
},
{
  'address': "0x90a5c6cAd799e8fcfaf6036678b14607B4Ed1415",
  'name': "Samoyed",
  #'name'l: "Samoyed Token",
  'decimals': 9
},
{
  'address': "0x07F6076023Be32D381815aF61813009467f3975D",
  'name': "RICH",
  #'name'l: "Rich",
  'decimals': 18
},
{
  'address': "0x2B21Ca040e745704A2B5ECA8AADA6B603D8A46FD",
  'name': "RTE",
  #'name'l: "RecepTayyipErdogan",
  'decimals': 18
},
{
  'address': "0x0c4101900644843aC77Af6f63A9C407e4D59CD05",
  'name': "POLYTOPIA",
  #'name'l: "POLYTOPIA Token",
  'decimals': 18
},
{
  'address': "0x9638Cd5feACa0834AF9c5158B93b12AAF737de42",
  'name': "REEF",
  #'name'l: "Coral Reef",
  'decimals': 18
},
{
  'address': "0x15d53ee80747c239aaF872E47f902006562931b6",
  'name': "POWER",
  #'name'l: "powerup Token",
  'decimals': 18
},
{
  'address': "0x2006906067A6c90fcE056505616540908e9ba1A4",
  'name': "R",
  #'name'l: "R",
  'decimals': 9
},
{
  'address': "0x6d802Ef189A68b5c19040c3928f1354BA065feEA",
  'name': "PTRR",
  #'name'l: "PolyTerrier",
  'decimals': 9
},
{
  'address': "0x03247a4368A280bEc8133300cD930A3a61d604f6",
  'name': "RBAL",
  #'name'l: "Rebalance Token (PoS)",
  'decimals': 18
},
{
  'address': "0x491663c18128627e0A7e0B45c818FB2D1dcd9B3f",
  'name': "POLYAKITA",
  #'name'l: "PolyAkita",
  'decimals': 18
},
{
  'address': "0xD448d7245cEBE7595F3167316FCBC728092F7E5c",
  'name': "polybabyfeg",
  #'name'l: "polybabyfeg",
  'decimals': 18
},
{
  'address': "0x2837695A9c9d163e9c265ECa720b575c9486C25E",
  'name': "POLYFLOKI",
  #'name'l: "POLY FLOKI",
  'decimals': 9
},
{
  'address': "0xD6394C613Ff6467855b53c895D840B2c4c7a3DEE",
  'name': "PolyPacMan",
  #'name'l: "PolyPacMan",
  'decimals': 18
},
{
  'address': "0x6cA4CD8873db45596C915268FC737994933D8a27",
  'name': "POLYSHIB",
  #'name'l: "POLYSHIBA INU",
  'decimals': 18
},
{
  'address': "0x6e25723BcE91090Ee94DCb6A74D7a1B82A70daf5",
  'name': "LuckyDog",
  #'name'l: "Lucky Dog",
  'decimals': 9
},
{
  'address': "0x472DB1061B5C78014Dcdf744648494DcA8197DA7",
  'name': "LGBBT",
  #'name'l: "LGBBT",
  'decimals': 9
},
{
  'address': "0xd95c600c2d6B5cbe6974E27c35ee83C069bA5E0C",
  'name': "Lucky akita",
  #'name'l: "Lucky akita",
  'decimals': 18
},
{
  'address': "0x1AD2B46bC07522b7ED73AAd90913449f1e4bEe69",
  'name': "HEXA",
  #'name'l: "Hexagon Token",
  'decimals': 9
},
{
  'address': "0x8405f3Cd6b71c888a7B974cb176853e6Cb554736",
  'name': "BULL",
  #'name'l: "PolyTerrier",
  'decimals': 9
},
{
  'address': "0xF6bb5d2FD0fD66bB05b72CfB950FC0d4924311f1",
  'name': "LuckyTitian",
  #'name'l: "LuckyTitian",
  'decimals': 9
},
{
  'address': "0x1E58a95F936D3a629D3Ee5124C2513015eEb8A24",
  'name': "QWERTY",
  #'name'l: "Qwerty Token",
  'decimals': 18
},
{
  'address': "0x64a54b880eD90d5F4aFA39452365Bf0F5975bBd3",
  'name': "MCT",
  #'name'l: "MetaChain Token",
  'decimals': 0
},
{
  'address': "0x70bE836E07138Cb468F67547d978c954c5aACe61",
  'name': "MaticShitzu",
  #'name'l: "MaticShitzu",
  'decimals': 18
},
{
  'address': "0x89c71681Bb91Ce79F935C2781a9021141c63272A",
  'name': "PBEE",
  #'name'l: "https://t.me/polybeeofficial",
  'decimals': 9
},
{
  'address': "0x9d808858e7aD0ddB00b3C97b1459eA81853440f9",
  'name': "PBTRFLY",
  #'name'l: "https://t.me/PolyButterfly",
  'decimals': 18
},
{
  'address': "0xE12d216E3681CAE1Eb9Ea52714BA85e5c04EEace",
  'name': "NAMCO",
  #'name'l: "Namco Games",
  'decimals': 18
},
{
  'address': "0x0d7F6f9e404aF9EA9C90dC2278bedeaee82106a5",
  'name': "PolyGoat",
  #'name'l: "PolyGoat",
  'decimals': 9
},
{
  'address': "0x48Fb37a3B9454e055C13E0959a3Af461024D8E90",
  'name': "PECHO",
  #'name'l: "https://t.me/tokenecho",
  'decimals': 9
},
{
  'address': "0xc5a60e0c8458b03f13FbCE99DB5E7d45C715cFB7",
  'name': "PolyDoggy",
  #'name'l: "PolyDoggy",
  'decimals': 9
},
{
  'address': "0xC9f4AEef342EF09857f5DeF348b4c6b73a5aC17d",
  'name': "HIPPO",
  #'name'l: "HIPPO Token",
  'decimals': 18
},
{
  'address': "0x201E9B3221e346abF0165751993F7b4189D1ef3b",
  'name': "BabyPig",
  #'name'l: "Poly Baby Pig",
  'decimals': 9
},
{
  'address': "0x2B3D3a67AB37220D3F92fe1fe570DFc4133D3784",
  'name': "DINO",
  #'name'l: "DinosaurFinance Token",
  'decimals': 18
},
{
  'address': "0x7E799240244f0b0a7d434bA2434de55c66b01DcE",
  'name': "PolyGoat",
  #'name'l: "PolyGoat",
  'decimals': 18
},
{
  'address': "0x8b4dFF0e17411820311005cB1F5fe6a0E3b43B3E",
  'name': "GHOST",
  #'name'l: "PolyGhost",
  'decimals': 18
},
{
  'address': "0x25D70A9C5E4EfC42905ce4df3086e9a8C3897BC6",
  'name': "PKC",
  #'name'l: "PolyPikachu Token",
  'decimals': 18
},
{
  'address': "0x7E20ca9Fb896a9d30699aBE27a24a2eC3EdA2BCF",
  'name': "ICE",
  #'name'l: "ICE (Iron Titan V2)",
  'decimals': 18
},
{
  'address': "0x116B6bea5589f851019F0Eeab19488D1Ae5a1fD6",
  'name': "CHAR",
  #'name'l: "POLY CHARMANDER",
  'decimals': 18
},
{
  'address': "0x2281881963a3CBC4c32A1F2870c3DE58C4A103BC",
  'name': "TBUSD",
  #'name'l: "Test BUSD",
  'decimals': 18
},
{
  'address': "0xA0B46A715b9732390fc12F17ec0E5996232A8eCF",
  'name': "RADIO",
  #'name'l: "Radio Token",
  'decimals': 18
},
{
  'address': "0x568AFFD0B6c82a4824Cb93890A212448971feE51",
  'name': "ICE",
  #'name'l: "ICE (TitanV2)",
  'decimals': 9
},
{
  'address': "0x4b54Bc363f5F9c6E0fcd82EaC6919aE213464Cc6",
  'name': "BTC2x-FLI",
  #'name'l: "BTC 2x Flexible Leverage Index (PoS)",
  'decimals': 18
},
{
  'address': "0x66d7FDCc7403f18cAE9b0e2e8385649D2AcBC12A",
  'name': "ETH2x-FLI",
  #'name'l: "ETH 2x Flexible Leverage Index (PoS)",
  'decimals': 18
},
{
  'address': "0x60D55F02A771d515e077c9C2403a1ef324885CeC",
  'name': "amUSDT",
  #'name'l: "Aave Matic Market USDT",
  'decimals': 6
},
{
  'address': "0x4d40C4C4f7Fc273Ec06735D8E837aa4045A4c12a",
  'name': "AUR",
  #'name'l: "Aurora Protocol",
  'decimals': 18
},
{
  'address': "0x5227f8773B9122310380b59E335cde26166910Df",
  'name': "IRON Finance Governance Token",
  #'name'l: "xICE",
  'decimals': 18
},
{
  'address': "0x723C9267F37cda496eE2BcCE1D5211A5712A7591",
  'name': "MARCO",
  #'name'l: "Marco token",
  'decimals': 18
},
{
  'address': "0xbA3608738BbD5D3F4Fd9694CDd482CE890806850",
  'name': "TONI",
  #'name'l: "Toni token",
  'decimals': 18
},
{
  'address': "0xBD31B590d7e13863C5c74B8573E7635fe915b883",
  'name': "REVVpoly",
  #'name'l: "REVV Polygon",
  'decimals': 18
},
{
  'address': "0xf5EA626334037a2cf0155D49eA6462fDdC6Eff19",
  'name': "SPADE",
  #'name'l: "PolygonFarm Finance",
  'decimals': 18
},
{
  'address': "0x78046515a6CED8e39F78e28c9844c729c42fb114",
  'name': "TKN1",
  #'name'l: "ERC20 Test Token 1",
  'decimals': 6
},
{
  'address': "0xBc453cfE84a8Beb569e53286bBccb48486a01CE5",
  'name': "TKN2",
  #'name'l: "ERC20 Test Token 2",
  'decimals': 18
},
{
  'address': "0x4A81f8796e0c6Ad4877A51C86693B0dE8093F2ef",
  'name': "ICE",
  #'name'l: "Iron Finance ICE Token",
  'decimals': 18
},
{
  'address': "0xd637CbBD0DAC848F281F159F704BF43E338bE2B8",
  'name': "RADIO",
  #'name'l: "Radio Token",
  'decimals': 18
},
{
  'address': "0xBB80aAE58575D41E34Ae0Bc34b2e9f484EA5F5Ed",
  'name': "PGC",
  #'name'l: "Poly Glactic",
  'decimals': 18
},
{
  'address': "0xfe712251173A2cd5F5bE2B46Bb528328EA3565E1",
  'name': "MVI",
  #'name'l: "Metaverse Index (PoS)",
  'decimals': 18
},
{
  'address': "0x2903D8a30327Ef9341A36c6d7206336Df3153470",
  'name': "FISH2",
  #'name'l: "Fish2",
  'decimals': 18
},
{
  'address': "0x908Af6019d0015Db7b4F7ee74e686b7238c5b445",
  'name': "BIBLE",
  #'name'l: "PolyHeaven Finance",
  'decimals': 18
},
{
  'address': "0xb758ece9A340A8DEF654D2a2252683B9b9aa1E7e",
  'name': "Popcorn",
  #'name'l: "Popcorn Swap",
  'decimals': 18
},
{
  'address': "0xdAb529f40E671A1D4bF91361c21bf9f0C9712ab7",
  'name': "BUSD",
  #'name'l: "(PoS) Binance USD",
  'decimals': 18
},
{
  'address': "0x652586A1306F4F946f940B762c0aea30917C0560",
  'name': "HARI",
  #'name'l: "Hari Coin",
  'decimals': 9
},
{
  'address': "0xc8aF7517227287638d1Cbf32398c5889577bd781",
  'name': "xPWINGS",
  #'name'l: "JetswapBar Polygon Token",
  'decimals': 18
},
{
  'address': "0x21a145EE2a93D9751e3A000Cf02860632f856934",
  'name': "Fluid",
  #'name'l: "Fluid Swap",
  'decimals': 18
},
{
  'address': "0xeCe4fF6d1E8A366E8C059823f60aD945Db5DcF56",
  'name': "STAR",
  #'name'l: "Star",
  'decimals': 18
},
{
  'address': "0x144572d46307955Fd8F6A45b1f8551624E75F04B",
  'name': "BFP",
  #'name'l: "Baby Farm Polygon",
  'decimals': 18
},
{
  'address': "0x70A1A98C5380582e94A615F63019eda102295A69",
  'name': "?PEACH",
  #'name'l: "Peachie Swap",
  'decimals': 18
},
{
  'address': "0x9B71b5511998e0798625b8Fa74e86D8192DE78C1",
  'name': "LPK",
  #'name'l: "Kripton",
  'decimals': 18
},
{
  'address': "0x4c7A9036C63db44946F4088Dadb15676bec91Fdd",
  'name': "CCTSwap",
  #'name'l: "Crypto Crocodiles Swap",
  'decimals': 18
},
{
  'address': "0xf508a6568a030973B83D8924Ef347ceF3b1538D2",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0xff3ee79CB4A7Fe0F78a3634cCfDbFc3CdCD65a64",
  'name': "CSTOP",
  #'name'l: "Common Sense Top10 Index",
  'decimals': 18
},
{
  'address': "0x00a7623e1172F9c755eF92efCdE90424F3465a80",
  'name': "PONZI",
  #'name'l: "Poly Ponzi",
  'decimals': 18
},
{
  'address': "0x8fA4dC2C4Ab7Aaae25CcA6430e61947EDD400ca4",
  'name': "PONZI",
  #'name'l: "Poly Ponzi",
  'decimals': 18
},
{
  'address': "0x2138620E399C2eBf73E2E5CFA330dACB15Ce2d9A",
  'name': "POKANA",
  #'name'l: "POKANA Token",
  'decimals': 18
},
{
  'address': "0xdDfE9FF7A6eC80d8eD566CD1AA0eA7E23BeA0764",
  'name': "MILK",
  #'name'l: "MILK",
  'decimals': 18
},
{
  'address': "0x50a6e53950E78036fe682f3a02b74d4a5827F92c",
  'name': "RADIO",
  #'name'l: "Radio Token",
  'decimals': 18
},
{
  'address': "0x2cf15C001A2A5dA76bf213D17763e5C856aE3632",
  'name': "TAR",
  #'name'l: "Tartarus (PoS)",
  'decimals': 8
},
{
  'address': "0xb8DD82E944354B7bf9e9E0744ba5fF786581d372",
  'name': "CID",
  #'name'l: "Cryptid (PoS)",
  'decimals': 18
},
{
  'address': "0xAa9654BECca45B5BDFA5ac646c939C62b527D394",
  'name': "DINO",
  #'name'l: "DinoSwap (PoS)",
  'decimals': 18
},
{
  'address': "0x5d4fe922AC03c00483eF669948d59B31aEF0AD42",
  'name': "CPRX",
  #'name'l: "Cryptoprx",
  'decimals': 18
},
{
  'address': "0xC5E34052dF9118334C24163763b52D7FC2944ad2",
  'name': "HEWO",
  #'name'l: "Hello World",
  'decimals': 18
},
{
  'address': "0x2e5f9B3C5fE71F31B9757d7789D55dA768EB4648",
  'name': "PUB",
  #'name'l: "PUB",
  'decimals': 18
},
{
  'address': "0x3454617d8D9B9DB01c0CDDcae98FeA978d7111b8",
  'name': "PUB",
  #'name'l: "PUB",
  'decimals': 18
},
{
  'address': "0xb2a7B32ce4ad45B65Ae93e205475818960b2739f",
  'name': "PUB",
  #'name'l: "PUB",
  'decimals': 18
},
{
  'address': "0xfd1a737C6cBdBEe9e8a388Ff4b2E617602A8139a",
  'name': "PUB",
  #'name'l: "PUB",
  'decimals': 18
},
{
  'address': "0x22a79288909731115420206015491549c71f8c43",
  'name': "PONZI",
  #'name'l: "PolyPonziFarm-L1",
  'decimals': 18
},
{
  'address': "0x9F7c54d384153d38397bbc0eCf696Bc6d60BeAe5",
  'name': "Cherry",
  #'name'l: "Cherry Finance",
  'decimals': 18
},
{
  'address': "0x12B6585cdC14D42527bf5a3Ec26C7d5fBBBFDdBa",
  'name': "TBULL",
  #'name'l: "TitanBull",
  'decimals': 18
},
{
  'address': "0xc66f5Cb6e920cBA2B9c5C343dEAEd2ea3096F1E5",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0x9ecE7249cD656e14E689B758DC9592e6E8075f91",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0xD0c45915ca544a55136A90690E00Aff658E3E0D3",
  'name': "PLYFI",
  #'name'l: "POLYTOPIAFinance",
  'decimals': 18
},
{
  'address': "0xcedd0d87E54c6766DE8cB431F2BEc59E131cD5b6",
  'name': "MOONTEST3",
  #'name'l: "MOONTEST3",
  'decimals': 9
},
{
  'address': "0xc2db4c131ADaF01c15a1DB654c040c8578929D55",
  'name': "WASABI",
  #'name'l: "Wasabi",
  'decimals': 18
},
{
  'address': "0xf153EfF70DC0bf3b085134928daeEA248d9B30d0",
  'name': "xMARK",
  #'name'l: "Standard (PoS)",
  'decimals': 9
},
{
  'address': "0x8f69D7a364E6616d55f1e0bF4fd5E7d868515A32",
  'name': "HUHU",
  #'name'l: "HUHUH token",
  'decimals': 18
},
{
  'address': "0xDA85a2773b5409A7ea4C470b8a551620613FebFe",
  'name': "JTKN4",
  #'name'l: "JToken4",
  'decimals': 18
},
{
  'address': "0xb2F423fFFB45c1560d44C77726c9BacE23d7bC5e",
  'name': "RADIO",
  #'name'l: "Radio Token",
  'decimals': 18
},
{
  'address': "0x9D2787591015326f45A2289BdC713879ED74C9e1",
  'name': "DINO",
  #'name'l: "DinoSwap (PoS)",
  'decimals': 18
},
{
  'address': "0x945A3bA4e422CaAD1d46B19A48636d59325324Ed",
  'name': "JTKN3",
  #'name'l: "JToken3",
  'decimals': 18
},
{
  'address': "0x20BABA5B09F53398E27647cC9ac1Ec8020A68Ee1",
  'name': "JTKN2",
  #'name'l: "JToken2",
  'decimals': 18
},
{
  'address': "0x19d2978839bEAE2e9f85340c1fA90a84eed5773c",
  'name': "JTKN5",
  #'name'l: "JToken5",
  'decimals': 18
},
{
  'address': "0xF2403dDd2E9c98760e1834F03f59157cd3f812Fe",
  'name': "SLGT",
  #'name'l: "SalesGovToken",
  'decimals': 18
},
{
  'address': "0x0325Bf6889Aa55F7D5F62619FDec3AA6D78308a8",
  'name': "SODA",
  #'name'l: "Soda",
  'decimals': 18
},
{
  'address': "0xB1Bf26c7B43D2485Fa07694583d2F17Df0DDe010",
  'name': "BlueICE",
  #'name'l: "Iron Finance BlueICE Gov Token",
  'decimals': 18
},
{
  'address': "0xaabFfA11D5B1fDDEE5121FF5ad0ad0c7155549e4",
  'name': "JTKN6",
  #'name'l: "JToken6",
  'decimals': 18
},
{
  'address': "0x684aF0dC99614F82bA567E639DD6846f01b93C4E",
  'name': "PIXEL",
  #'name'l: "Pixel",
  'decimals': 18
},
{
  'address': "0x94162cB84baDa965e4E3F572a4429Ec658dc5b70",
  'name': "PIXEL",
  #'name'l: "Pixel",
  'decimals': 18
},
{
  'address': "0x7E58274168232dbAC113E2c894677d2b787B3cE2",
  'name': "Pro",
  #'name'l: "PolyPro Token",
  'decimals': 18
},
{
  'address': "0x309088Beb628C0Bf8E8eAe9092A744E9875eA40c",
  'name': "TEST",
  #'name'l: "PolyTest Token",
  'decimals': 18
},
{
  'address': "0xD38EeE49B6ee7EE55F09da3D20C571993b5a655a",
  'name': "CRANE",
  #'name'l: "Origami.farm",
  'decimals': 18
},
{
  'address': "0xB72EceDE7b33d75883ebBF61a7452ff75626DbF7",
  'name': "DUB",
  #'name'l: "Massive Dub)",
  'decimals': 18
},
{
  'address': "0x28C388FB1F4fa9F9eB445f0579666849EE5eeb42",
  'name': "BEL",
  #'name'l: "Bella (PoS)",
  'decimals': 18
},
{
  'address': "0xfad70FD116559914240faB82b0078c4E82a6a1B8",
  'name': "CPIE",
  #'name'l: "CremePieSwap Token",
  'decimals': 18
},
{
  'address': "0xE358c82Ae464C5C691Fa26394148FA2B03339DA9",
  'name': "SSDoge",
  #'name'l: "SuperSonicDoge",
  'decimals': 18
},
{
  'address': "0x1c53052F275Aff00b2A8C2001Cd6fC50095Ad098",
  'name': "Club",
  #'name'l: "PolyClub Finance",
  'decimals': 18
},
{
  'address': "0x974d296973444986177b5bfCf565f8c60C481475",
  'name': "PAPR",
  #'name'l: "paprprintr.finance",
  'decimals': 18
},
{
  'address': "0xF73DCBa3Af0fB1Ae9fe1bC317B959d02631d470F",
  'name': "RUG",
  #'name'l: "RUGGERINO",
  'decimals': 5
},
{
  'address': "0xC122c74f4070EB9659eC8953b0EE069E97C7C2dC",
  'name': "SWP",
  #'name'l: "Swap.net Token",
  'decimals': 18
},
{
  'address': "0x4344460C2dfeF7262beCd2db40d04cB7721F1420",
  'name': "YDragon",
  #'name'l: "Yield Dragon",
  'decimals': 18
},
{
  'address': "0xbfe4793fcE9059055428Bfb86306244E6aa42428",
  'name': "secura",
  #'name'l: "securafinance",
  'decimals': 18
},
{
  'address': "0x4855eFb2F01ba2FAFfDa7fC040F2Bc6D7ee03CD4",
  'name': "VIB",
  #'name'l: "Vibranium Coin",
  'decimals': 18
},
{
  'address': "0x7254fd2C851F7a344776fe523C5fD36399436014",
  'name': "Hulala",
  #'name'l: "Hulala Finance",
  'decimals': 18
},
{
  'address': "0x5f1657896B38c4761dbc5484473c7A7C845910b6",
  'name': "pSWAMP",
  #'name'l: "pSwampy",
  'decimals': 18
},
{
  'address': "0xDe21CDbBC7f6f8E40aF8A7f372A86501f8BD7441",
  'name': "Stacy",
  #'name'l: "STACY",
  'decimals': 18
},
{
  'address': "0x8eb4dbf3e9af5c9660Bef7866aEC325DcBa1D261",
  'name': "HDS",
  #'name'l: "PolyHotDogs Finance",
  'decimals': 18
},
{
  'address': "0x3880257F51edDb32cE8239d720833f7d79Cb0a22",
  'name': "SOLJ",
  #'name'l: "SoljToken",
  'decimals': 18
},
{
  'address': "0x7878C87b4FeB75220320271E58Af3A9FA528F17C",
  'name': "DINO",
  #'name'l: "Dinoswap",
  'decimals': 18
},
{
  'address': "0xE4a92E926FC4F474f64EA72c83387f38295045a2",
  'name': "testcoin2",
  #'name'l: "testcoin2",
  'decimals': 18
},
{
  'address': "0xe6b8aCeb4b37e6086647fa19Fc616859F5152D62",
  'name': "HUHU",
  #'name'l: "HUHUH token",
  'decimals': 18
},
{
  'address': "0x04535ca1FFD227e7b8471c8e5e840E410cD9ADa2",
  'name': "TEST3",
  #'name'l: "PolyTest",
  'decimals': 9
},
{
  'address': "0xBFc72197B79Ee4CF8CA5d9602990345915D8b4E7",
  'name': "KCK",
  #'name'l: "Keccak",
  'decimals': 18
},
{
  'address': "0x70F8d407BD0b49ef9Bf404E5beCcdcf2074F5A27",
  'name': "IamG",
  #'name'l: "Iamgenerous",
  'decimals': 18
},
{
  'address': "0x04E9825d1f52f433f5b08EB696A3924D1f6d9A70",
  'name': "PHornet",
  #'name'l: "PolyHornet Token",
  'decimals': 18
},
{
  'address': "0xcD17911a0Dc913D621c6dE6a9e425F8065f275cD",
  'name': "BTK",
  #'name'l: "BitcoinKid",
  'decimals': 0
},
{
  'address': "0x61E9c2F3501889f6167921087Bd6EA306002904a",
  'name': "PIXEL",
  #'name'l: "Pixel",
  'decimals': 18
},
{
  'address': "0x129207AF07721E97BCe83395c02a2C8717e04324",
  'name': "PLANE",
  #'name'l: "PolyPlanes TOKEN",
  'decimals': 18
},
{
  'address': "0x14520807406DA50e6E7a1dAA58DA6775A2E0C992",
  'name': "KOR",
  #'name'l: "KOREA",
  'decimals': 18
},
{
  'address': "0xFC0c11aebE15E99832E00859f354713Da233D235",
  'name': "Star",
  #'name'l: "StarFinance",
  'decimals': 18
},
{
  'address': "0x2Fe9970E7d982Bf33e226799e0EEA7aB3Cafe240",
  'name': "Pegasus",
  #'name'l: "PegasusCoin",
  'decimals': 18
},
{
  'address': "0x19247Cc4dc01f1a159F211f799bCFbF83F93D70F",
  'name': "SCHOOL",
  #'name'l: "SchoolSwap Token",
  'decimals': 18
},
{
  'address': "0x90AC3fa9fCD997B168f218041de26eB01399Bb55",
  'name': "xYELD",
  #'name'l: "XYELD",
  'decimals': 18
},
{
  'address': "0x96B318Ab777E35C09D536a7274eBB9A6611480Df",
  'name': "CAP",
  #'name'l: "Capex",
  'decimals': 18
},
{
  'address': "0xda9463E80b9b8f7ea78993b25e7e62020cA3cba3",
  'name': "HAPPYBUNNY",
  #'name'l: "Happy Bunny",
  'decimals': 18
},
{
  'address': "0x64aFDF9e28946419E325d801Fb3053d8B8FFdC23",
  'name': "MEEB",
  #'name'l: "MeebMaster.com Token",
  'decimals': 18
},
{
  'address': "0xfD30189bD6de5503bB1db60cf1136123EdEA837A",
  'name': "PLITHIUM",
  #'name'l: "PRE-LITHIUM",
  'decimals': 18
},
{
  'address': "0xFaD2919e23091dcaBed4521c3609f6e253f665a1",
  'name': "testy",
  #'name'l: "testy",
  'decimals': 18
},
{
  'address': "0xa0e07B33AEb73804C59B14AbC54dc6B89D42228C",
  'name': "Fundi",
  #'name'l: "Fundi Finance",
  'decimals': 18
},
{
  'address': "0x61FE6d0Ee83A5614822bE14599Ee99c621190a60",
  'name': "PENNY",
  #'name'l: "penny (PoS)",
  'decimals': 18
},
{
  'address': "0x72e461DCfeEa8A592669573B55984cB154560F1F",
  'name': "DVtest",
  #'name'l: "DVtest Token",
  'decimals': 18
},
{
  'address': "0xb4A7a35aDF468b383e9AfBC236681234857513BF",
  'name': "EARNMATIC",
  #'name'l: "EARNMATIC",
  'decimals': 18
},
{
  'address': "0x9ADcF70b88b48C5aD39e1D72425F79440B5b5AC2",
  'name': "Duck",
  #'name'l: "Duck Finance",
  'decimals': 18
},
{
  'address': "0xa937941C8CC9A21d0c6B866Fd2eEaED78B8C2834",
  'name': "vBoneMatic",
  #'name'l: "BoneMaticvault",
  'decimals': 18
},
{
  'address': "0xC37899901ffDEf1b6Baf95FD4081D82942a0A85a",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x53FEab56AaD08E47ED03aD4eb996E9709f9F7CFd",
  'name': "BUM",
  #'name'l: "BUM Stablecoin",
  'decimals': 18
},
{
  'address': "0xd598Ca14eaff048bB98F8E56475cc6b1F3E5D319",
  'name': "GASS",
  #'name'l: "Shares.GasBack.Tech",
  'decimals': 9
},
{
  'address': "0x8940543528943ABa6d8A43f04B9485167886D8aF",
  'name': "BAKE",
  #'name'l: "Bake",
  'decimals': 18
},
{
  'address': "0x1a8Cd27a4ED1D0d9D566516156EF963c20DBE207",
  'name': "OMT",
  #'name'l: "Onion Mixer Token",
  'decimals': 18
},
{
  'address': "0xED1F90e4803954dcc1D5e584ab4689acC722e7C5",
  'name': "COQUI",
  #'name'l: "COQUI",
  'decimals': 18
},
{
  'address': "0x633a63ae13B95Ede70A601bBe270B46F537212c9",
  'name': "ONION",
  #'name'l: "ONION Token",
  'decimals': 18
},
{
  'address': "0x3066818837c5e6eD6601bd5a91B0762877A6B731",
  'name': "UMA",
  #'name'l: "UMA Voting Token v1 (PoS)",
  'decimals': 18
},
{
  'address': "0x6DdB31002abC64e1479Fc439692F7eA061e78165",
  'name': "COMBO",
  #'name'l: "Furucombo (PoS)",
  'decimals': 18
},
{
  'address': "0xA041544fe2BE56CCe31Ebb69102B965E06aacE80",
  'name': "BOND",
  #'name'l: "BarnBridge Governance Token (PoS)",
  'decimals': 18
},
{
  'address': "0xC6d54D2f624bc83815b49d9c2203b1330B841cA0",
  'name': "SAND",
  #'name'l: "SAND (PoS)",
  'decimals': 18
},
{
  'address': "0x8d1566569d5b695d44a9a234540f68D393cDC40D",
  'name': "GAME",
  #'name'l: "GAME Credits",
  'decimals': 18
},
{
  'address': "0x1cA45611A1bE800E02685D35b859e01cee9939de",
  'name': "TT",
  #'name'l: "Target Token",
  'decimals': 18
},
{
  'address': "0x3fE59889a6F5D325C90897cD434cfD0dc53DFaeA",
  'name': "FT",
  #'name'l: "Fund Token",
  'decimals': 18
},
{
  'address': "0x61217884784eD92Ca1630190bD9e8363B7EA4FA1",
  'name': "LAVA",
  #'name'l: "LAVA",
  'decimals': 18
},
{
  'address': "0xfE1a200637464FBC9B60Bc7AeCb9b86c0E1d486E",
  'name': "LITHIUM",
  #'name'l: "LITHIUM",
  'decimals': 18
},
{
  'address': "0x6987B151D2B34503B758a42FB1c036dAE4a8C385",
  'name': "ISSv2",
  #'name'l: "IronSwap Token",
  'decimals': 18
},
{
  'address': "0x931d905b0c76efbA6052dca17cF22Cd98207dBe1",
  'name': "ULTRAWOJAK",
  #'name'l: "Ultra Wojak",
  'decimals': 18
},
{
  'address': "0x3d244d67D680CaDcccf34F8F996CEA777B6d9FFE",
  'name': "waPUSD",
  #'name'l: "Wasabi PUSD",
  'decimals': 18
},
{
  'address': "0xde8da32f6d15d7b6A69F8DCf93680c6E191715a3",
  'name': "VISwap",
  #'name'l: "Value Internet Swap",
  'decimals': 18
},
{
  'address': "0xEF6B7E511c18B5fC0099e680f17AE5C3b7601d26",
  'name': "TIN",
  #'name'l: "Tyrannical (PoS)",
  'decimals': 8
},
{
  'address': "0x31Af84e6aeEA05D8494B4136224Dc9584c6c6166",
  'name': "ArableLands",
  #'name'l: "ArableLands",
  'decimals': 18
},
{
  'address': "0x851795f15bC0ce3fA58540D98201E117a4bDf41a",
  'name': "LAVA",
  #'name'l: "LAVA",
  'decimals': 18
},
{
  'address': "0x54cFe73f2c7d0c4b62Ab869B473F5512Dc0944D2",
  'name': "BZRX",
  #'name'l: "bZx Protocol Token (PoS)",
  'decimals': 18
},
{
  'address': "0x224BDbb6dfB2119073894cA8a9EBaAf6E04F462d",
  'name': "DogeShiba",
  #'name'l: "Doge Shiba Inu",
  'decimals': 9
},
{
  'address': "0x9Bbcda2606e616659b118399A2823E8a392f55DA",
  'name': "GIVE",
  #'name'l: "Give",
  'decimals': 18
},
{
  'address': "0xFDde616084427f0A231D0664a985E1F820E34693",
  'name': "bDIGG",
  #'name'l: "Badger Sett Digg (PoS)",
  'decimals': 18
},
{
  'address': "0x3324af8417844e70b81555A6D1568d78f4D4Bf1f",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xC004e2318722EA2b15499D6375905d75Ee5390B8",
  'name': "KOM",
  #'name'l: "Kommunitas",
  'decimals': 8
},
{
  'address': "0x9D4B26827e37030ca28A1a4039D381D6B4301A41",
  'name': "ALLSTARNFT",
  #'name'l: "All Star NFT",
  'decimals': 9
},
{
  'address': "0x5Ed16822c279019dEe31892990859ff013633068",
  'name': "WONSTER",
  #'name'l: "Wonster Token",
  'decimals': 18
},
{
  'address': "0xD66F2c70d9F706bf2f36FF0f7Bc83cD12315C8E4",
  'name': "BETH",
  #'name'l: "BabyEth",
  'decimals': 18
},
{
  'address': "0xa2CA40DBe72028D3Ac78B5250a8CB8c404e7Fb8C",
  'name': "FEAR",
  #'name'l: "Fear NFTs (PoS)",
  'decimals': 18
},
{
  'address': "0x9BE5f33F8Ac83c1E430410267dfC3eDa05d48917",
  'name': "PVT",
  #'name'l: "Pura Vida Token",
  'decimals': 18
},
{
  'address': "0x06E52DB46F1B1Bb3C3e0dB3D9686c38f8dFc5Db8",
  'name': "TAIL",
  #'name'l: "Tail Token",
  'decimals': 18
},
{
  'address': "0x3125CD2375A6Ae5833e307619e947C14f3e9702B",
  'name': "mSTABLEM",
  #'name'l: "Mock StableM Token",
  'decimals': 18
},
{
  'address': "0x08158A6b5d4018340387d1A302f882E98a8bC5b4",
  'name': "PPAY",
  #'name'l: "Plasma (PoS)",
  'decimals': 18
},
{
  'address': "0x19782D3Dc4701cEeeDcD90f0993f0A9126ed89d0",
  'name': "REN",
  #'name'l: "REN (PoS)",
  'decimals': 18
},
{
  'address': "0xe0A510CB670f5289Befd2A3591eC6c70F8e49CCD",
  'name': "mSTABLEM",
  #'name'l: "Mock StableM Token",
  'decimals': 18
},
{
  'address': "0x940aAE22d8Ea74C347Df8F057aec57A84a21ac46",
  'name': "SOBA",
  #'name'l: "Soba Token",
  'decimals': 18
},
{
  'address': "0xD3b71117E6C1558c1553305b44988cd944e97300",
  'name': "YEL",
  #'name'l: "YEL Token",
  'decimals': 18
},
{
  'address': "0x59E9261255644c411AfDd00bD89162d09D862e38",
  'name': "ETHA",
  #'name'l: "ETHA",
  'decimals': 18
},
{
  'address': "0x70b86450B2685F2A64Ed908Ab087C7ed5dFdba8e",
  'name': "PET",
  #'name'l: "Pet Token",
  'decimals': 18
},
{
  'address': "0x4237302A7db5dfD04d1FfF5Fd93a6F09bdE8F08C",
  'name': "EVO",
  #'name'l: "EVO (PoS)",
  'decimals': 18
},
{
  'address': "0x3656487b70AA1d24569C7370EeC01D1CDC41d391",
  'name': "FOR",
  #'name'l: "fortest",
  'decimals': 18
},
{
  'address': "0x19E0F8E570043Fa72D32D271440A38659cc1d326",
  'name': "sGHST",
  #'name'l: "Sushigotchi sGHST Token",
  'decimals': 18
},
{
  'address': "0xcCeEf1083791c4a9c85E4A8aeFbe54a9DEa6867b",
  'name': "uGHST",
  #'name'l: "Unigotchi uGHST Token",
  'decimals': 18
},
{
  'address': "0x021501bc836f63e610136969601A4e008B0B6064",
  'name': "DOGGOD",
  #'name'l: "DOGGOD",
  'decimals': 18
},
{
  'address': "0xd4A9a52040D154928F6d219a5c24D1aEdd8453fE",
  'name': "mSTM",
  #'name'l: "StakeMars Protocol on Polygon",
  'decimals': 18
},
{
  'address': "0x6Fd8aAe9f85A7Db14c45453daAB81aa3085E4bA3",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x6C0AB120dBd11BA701AFF6748568311668F63FE0",
  'name': "APW",
  #'name'l: "APWine Token (PoS)",
  'decimals': 18
},
{
  'address': "0x5316f8106d71362E40d0f01724ee6218007e620d",
  'name': "GASB",
  #'name'l: "GasBack.Tech",
  'decimals': 18
},
{
  'address': "0x53646df9851025A2cAd291864957174aF48a5477",
  'name': "GASF",
  #'name'l: "GasFuel",
  'decimals': 18
},
{
  'address': "0x1DA554D34027ca8dE74C5b1cd2FA53A8a1492C94",
  'name': "LION",
  #'name'l: "PolyLion Token",
  'decimals': 18
},
{
  'address': "0x7917FB62b993511320Eee5ad70E98D49356580C9",
  'name': "ELYSM",
  #'name'l: "PolyElysium Token",
  'decimals': 18
},
{
  'address': "0xEA4757420c0006cacd3fe70bd10f7496f8f81Af4",
  'name': "BUTTER",
  #'name'l: "Butter",
  'decimals': 18
},
{
  'address': "0xB77e62709e39aD1cbeEBE77cF493745AeC0F453a",
  'name': "WISE",
  #'name'l: "Wise Token (PoS)",
  'decimals': 18
},
{
  'address': "0x6971AcA589BbD367516d70c3d210E4906b090c96",
  'name': "PAW",
  #'name'l: "Paw",
  'decimals': 18
},
{
  'address': "0xF160969b3E49cbd93333c97E61b48d1644806939",
  'name': "YCG",
  #'name'l: "YayCubaGamer",
  'decimals': 18
},
{
  'address': "0x71d4cA971945cEB01E7ABCE3C2fa78E6619572cB",
  'name': "PST",
  #'name'l: "Pasar Seni Token",
  'decimals': 18
},
{
  'address': "0x03678f2c2c762DC63c2Bb738c3a837D366eDa560",
  'name': "XCASH",
  #'name'l: "X-Cash (PoS)",
  'decimals': 18
},
{
  'address': "0x1C954E8fe737F99f68Fa1CCda3e51ebDB291948C",
  'name': "KNC",
  #'name'l: "Kyber Network Crystal v2 (PoS)",
  'decimals': 18
},
{
  'address': "0x7b4C66b45a4DdfE321Da8e5F6a0dAEd4269AF97C",
  'name': "WMLN",
  #'name'l: "Watermelon Coin",
  'decimals': 18
},
{
  'address': "0x502EE8BCd3ebB4Ce19Da4587ba487Ab32Bf04780",
  'name': "CCER",
  #'name'l: "CCER",
  'decimals': 9
},
{
  'address': "0x9DFB228e6eEeD1667a044B7E1465Bd920822e501",
  'name': "AVENGERS",
  #'name'l: "Avengers Token",
  'decimals': 18
},
{
  'address': "0xfC40a4F89b410a1b855b5e205064a38fC29F5eb5",
  'name': "rUSD",
  #'name'l: "rUSD",
  'decimals': 18
},
{
  'address': "0x9b5d83cCb007958A69Fa786d623a4F0043eABC72",
  'name': "BEAN",
  #'name'l: "PolyBeans",
  'decimals': 18
},
{
  'address': "0x0f403f69053D0ED8F3e2d08046e4f41D58717249",
  'name': "Daca",
  #'name'l: "Dacacoin",
  'decimals': 18
},
{
  'address': "0xD66197f48a531Fe38A542f3e359728147980f3e9",
  'name': "BETA_SIM",
  #'name'l: "Simba Finance Token",
  'decimals': 18
},
{
  'address': "0xc8E3318FDE17C04C70B787Ee1218308b943f5cB6",
  'name': "MICE",
  #'name'l: "MockICE",
  'decimals': 18
},
{
  'address': "0x167F8C8A1AF9A4c851C8E541BA0f9939D395cCF1",
  'name': "WASABI",
  #'name'l: "Wasabi (PoS)",
  'decimals': 18
},
{
  'address': "0x4527D831ceFC76d0E5F8699f8fF4494611A6Bf31",
  'name': "NEPTUNE",
  #'name'l: "Neptune Token",
  'decimals': 18
},
{
  'address': "0xDb557f2DA723fDf1cA3E8fF643c0ae27458D8367",
  'name': "qBEAN",
  #'name'l: "LiquidBeans",
  'decimals': 18
},
{
  'address': "0x3d308d15FD6710e7464388BD295EFaC1d3d0001e",
  'name': "BOLT",
  #'name'l: "Bolt",
  'decimals': 18
},
{
  'address': "0x8aCec4Ab94e74FA19c01985950103158cce4a36B",
  'name': "FDN",
  #'name'l: "Free Data Network",
  'decimals': 18
},
{
  'address': "0x9CEA5845Fc56315C85BD63311B9cF5d603286D6A",
  'name': "CPT",
  #'name'l: "Coin Pasar",
  'decimals': 18
},
{
  'address': "0xd69b31c3225728CC57ddaf9be532a4ee1620Be51",
  'name': "anyUSDC",
  #'name'l: "USDC",
  'decimals': 6
},
{
  'address': "0xdF4f82B25C9D4FFbC7aBfc0dd07E43c64Fa18cc4",
  'name': "LEV",
  #'name'l: "CryptoLev",
  'decimals': 18
},
{
  'address': "0xb77cfaeDDBa3Ca32B34923028B24062CF91d4Be2",
  'name': "SMAY",
  #'name'l: "Smay",
  'decimals': 18
},
{
  'address': "0x44B141F04d15a17c3F00b4D8a9F7df8453818217",
  'name': "MIMA",
  #'name'l: "MIMA COin",
  'decimals': 18
},
{
  'address': "0xE969c00EF9CA2aa37d9872E1BAeF94d98BDd7993",
  'name': "AI",
  #'name'l: "AI Chain",
  'decimals': 18
},
{
  'address': "0x76177AA013a4E2D9266B0f0eCA202e063a088644",
  'name': "sMATIC",
  #'name'l: "semiautoMATIC",
  'decimals': 18
},
{
  'address': "0x74f4ccdaEdb13b73754cf7Bb8CbABE74E2DD4B70",
  'name': "GACHA",
  #'name'l: "Gacha Unit",
  'decimals': 18
},
{
  'address': "0x27c24A3aE5C81e449e3a64A844641f0b94539f10",
  'name': "DOLPH",
  #'name'l: "OceanFinance Dolphin Token",
  'decimals': 18
},
{
  'address': "0x2951A91C19C48E58d5006311DCFC83c652f354B5",
  'name': "faMATIC",
  #'name'l: "Fully AutoMATIC",
  'decimals': 18
},
{
  'address': "0xC9C0159644d3789EceB4f8cdfcF99C7605AE505c",
  'name': "PVI",
  #'name'l: "PolyVaults.fi",
  'decimals': 18
},
{
  'address': "0xC04FC68AA3AaAD65A3c56221Ac4a8a8274f3Ecf1",
  'name': "TEST",
  #'name'l: "TestToken",
  'decimals': 18
},
{
  'address': "0x61BDD9C7d4dF4Bf47A4508c0c8245505F2Af5b7b",
  'name': "AXS",
  #'name'l: "Axie Infinity Shard (PoS)",
  'decimals': 18
},
{
  'address': "0x7E4c577ca35913af564ee2a24d882a4946Ec492B",
  'name': "MOONED",
  #'name'l: "MoonEdge",
  'decimals': 18
},
{
  'address': "0xaC0dccF6a7D981baEd5b8b0fe70b4791082E439B",
  'name': "CLEAR",
  #'name'l: "Clear Token",
  'decimals': 8
},
{
  'address': "0xc49079e96cEaf20C9900f1B77aA09d2D5A011341",
  'name': "BLANK",
  #'name'l: "Blank Token (PoS)",
  'decimals': 18
},
{
  'address': "0x14595184579A3C2CC0661b59067BE91BDC57cAbc",
  'name': "STABLEM",
  #'name'l: "StableM Token",
  'decimals': 18
},
{
  'address': "0x24F63B282dBd2063F2d679c486A31680352EE520",
  'name': "FIRE",
  #'name'l: "Crypto FIRE Fund",
  'decimals': 18
},
{
  'address': "0xD11eF924C5190c6432508e4ba49319B2EB03C8C6",
  'name': "GTX5080",
  #'name'l: " GeForce GTX 5080",
  'decimals': 8
},
{
  'address': "0x55FF76BFFC3Cdd9D5FdbBC2ece4528ECcE45047e",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xfCCBA1395Bc9a814347D9Aa469FdebB7A4327200",
  'name': "XIII",
  #'name'l: "Thirteen",
  'decimals': 18
},
{
  'address': "0xC513048d342E880b082FD7CF01Fc93816BfF081A",
  'name': "FRENS",
  #'name'l: "Lion Frens",
  'decimals': 18
},
{
  'address': "0xc68131a34538a9005bd4D31BfF79F8d47FaC3e96",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xEE800B277A96B0f490a1A732e1D6395FAD960A26",
  'name': "ARPA",
  #'name'l: "ARPA Token (PoS)",
  'decimals': 18
},
{
  'address': "0x5cB9B05e162701949ac62DAD44feb5c0457cf2c0",
  'name': "RIVER",
  #'name'l: "PolyRiver Token",
  'decimals': 18
},
{
  'address': "0x197CfA65a1EbD6965Ea7Cd1223b984A90D22F3a9",
  'name': "POMB",
  #'name'l: "Polybomb",
  'decimals': 18
},
{
  'address': "0xB2910Ab614353b6cB70299e7ce2E85830BC77C10",
  'name': "KUNAI",
  #'name'l: "Kunai Token",
  'decimals': 18
},
{
  'address': "0x340fE1D898ECCAad394e2ba0fC1F93d27c7b717A",
  'name': "JDI",
  #'name'l: "JDIToken",
  'decimals': 18
},
{
  'address': "0x96f276345f2C1d1Dea8FD1dBEE58479729569075",
  'name': "MYSTIC",
  #'name'l: "Mystic Token",
  'decimals': 8
},
{
  'address': "0xE7a24EF0C5e95Ffb0f6684b813A78F2a3AD7D171",
  'name': "am3CRV",
  #'name'l: "Curve.fi amDAI/amUSDC/amUSDT",
  'decimals': 18
},
{
  'address': "0x650e280D1f03E684e3b888bb8E2799eB1a39De99",
  'name': "BETA_SIMT",
  #'name'l: "Simba Finance Ticket Token",
  'decimals': 18
},
{
  'address': "0xD664b8d8624750a4f945fe9efb1438e9e021cd56",
  'name': "KIWI",
  #'name'l: "KIWI",
  'decimals': 18
},
{
  'address': "0xfC5a11D0fe8B5AD23b8A643Df5EAE60b979CE1bF",
  'name': "WHIRL",
  #'name'l: "PolyWhirl",
  'decimals': 18
},
{
  'address': "0x8888fD4E918660Ea38950A49c9Da9A5Bf2971588",
  'name': "MDC",
  #'name'l: "MaticDollarCoin",
  'decimals': 18
},
{
  'address': "0x9FD4969573F9DEC7882409709C9B35F2dc3074ca",
  'name': "TAO",
  #'name'l: "TAO Coin",
  'decimals': 18
},
{
  'address': "0x288608979bB6F721fe7F24B6895AeD6Ee1012b39",
  'name': "SHIB",
  #'name'l: "SHIB",
  'decimals': 18
},
{
  'address': "0xA0826C84468D67e3F72621DE012DdA8558C3F833",
  'name': "SHIBA",
  #'name'l: "SHIBA",
  'decimals': 18
},
{
  'address': "0x0106c37106eBEe3C5eAF299B7d8622CaF491e6F3",
  'name': "PolyDash",
  #'name'l: "PolygonDash",
  'decimals': 18
},
{
  'address': "0xB0d77f0ec7deA7A564DA10Dc1Cb5d24aB066FeB8",
  'name': "ETHERROCK",
  #'name'l: "A Ether Rock",
  'decimals': 18
},
{
  'address': "0x98B1d7bA836a0a73d741735A309A18FeBEb6299c",
  'name': "YCORN",
  #'name'l: "Polycorn",
  'decimals': 18
},
{
  'address': "0x255707B70BF90aa112006E1b07B9AeA6De021424",
  'name': "TETU",
  #'name'l: "TETU Reward Token",
  'decimals': 18
},
{
  'address': "0xABe93454f00826555746e65422eE882fE5E4EE3C",
  'name': "DAIKI",
  #'name'l: "Daikiri Token",
  'decimals': 18
},
{
  'address': "0x18Cca3D7E2851693c2dc246E356eE9078a96E16B",
  'name': "FIAT",
  #'name'l: "Fiat Buster",
  'decimals': 0
},
{
  'address': "0x4c8634971Bc70a3597127b199d0386A515Bf504A",
  'name': "RASP",
  #'name'l: "BerryFarms Token",
  'decimals': 18
},
{
  'address': "0xc36c24BE28e9b28979fDf0bD8B8A00b766fb31a5",
  'name': "SPRK",
  #'name'l: "Space Rock Token",
  'decimals': 18
},
{
  'address': "0xEB330b45a28D95E7b0a13bD56d10A4Bb818d8940",
  'name': "BPUL",
  #'name'l: "BetaPulsarToken",
  'decimals': 18
},
{
  'address': "0x95b9Df02dD221ae75C30cE95340e05611d4dc357",
  'name': "SVTR",
  #'name'l: "SaveTrees",
  'decimals': 18
},
{
  'address': "0x4b7EeD479328f473eCE2f4627F8bea60f2feba7C",
  'name': "axb",
  #'name'l: "axb",
  'decimals': 18
},
{
  'address': "0xb0e63921B31073A34ece888c0F4b4C32f67A2cc8",
  'name': "tpip",
  #'name'l: "Testpip",
  'decimals': 18
},
{
  'address': "0xBDBc0612599B79298C81452951444Eb92C6359c8",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xfA26eD7123B7Db7528Ff7266a2682B0bBCC3A790",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x692260AEeb49158348201A5e645312014Db0a97e",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x17D78f20ad7dA368dA72aEf5D6042b37E019c7e6",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x4f922945809A73ABe0cbccD4600C181c4Bc21C41",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xDB19eF60FdDb31d06a1E35c2505f41Fb690Cbb90",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x9E8e1262b90bE9B55658D1bb4A2a9fb8BE9E6b04",
  'name': "PolyStake",
  #'name'l: "PolyStake(L1)",
  'decimals': 18
},
{
  'address': "0x2B9E7ccDF0F4e5B24757c1E1a80e311E34Cb10c7",
  'name': "MASK",
  #'name'l: "Mask Network (PoS)",
  'decimals': 18
},
{
  'address': "0x03943C3ef00d92e130185CeBC0bcc435Def2cC94",
  'name': "FM",
  #'name'l: "Follow Me",
  'decimals': 18
},
{
  'address': "0x2a6701d2B7bD4d3cDdCa1230d3E99AfC19A316E9",
  'name': "TEST-2",
  #'name'l: "TestyTesto",
  'decimals': 9
},
{
  'address': "0xABD1CbbF2a7F53C54946ce3d1557DB625c911126",
  'name': "AAPL",
  #'name'l: "Apple Finance V2",
  'decimals': 18
},
{
  'address': "0x7426242c37404B61570a22B87D53d7394bB78391",
  'name': "FED",
  #'name'l: "FedCoin",
  'decimals': 18
},
{
  'address': "0xC364fB242a3F690003251e6CedA540fC449430AD",
  'name': "SNK",
  #'name'l: "SNKCoin",
  'decimals': 18
},
{
  'address': "0xD662141a1562A02B8E888432eEfa52AA5791F661",
  'name': "GTQC",
  #'name'l: "QuetzalCoin",
  'decimals': 18
},
{
  'address': "0x10Bdc83682361F6C66D82273c0c989fd8c1CAbC3",
  'name': "DEMON",
  #'name'l: "Demon Token",
  'decimals': 18
},
{
  'address': "0x35b937583F04A24963eb685F728a542240f28Dd8",
  'name': "SFI",
  #'name'l: "Spice (PoS)",
  'decimals': 18
},
{
  'address': "0xEd644a452268957c833e7a2293D6d69c22413a46",
  'name': "USA",
  #'name'l: "AMERICAFIRST",
  'decimals': 18
},
{
  'address': "0xCaf870DaD882b00F4b20D714Bbf7fceADA5E4195",
  'name': "ZEFI",
  #'name'l: "ZCore Finance",
  'decimals': 18
},
{
  'address': "0x680dF64622Fa8bb61b5527e693c7039bBE4fa331",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x38E2F62C61E1223Ec1860E0B5aF09679101bf2DF",
  'name': "pb",
  #'name'l: "pb",
  'decimals': 18
},
{
  'address': "0xbBEf4337EE26389910CC4C00542Ee1daeED50Ddf",
  'name': "tpip",
  #'name'l: "Testpip",
  'decimals': 18
},
{
  'address': "0xc8355956059C3af1dce5e36ceCfd071267f6c3D6",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x5f64e2E83EeD7141912c96Dab6c5F13404B9e301",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xAB72EE159Ff70b64beEcBbB0FbBE58b372391C54",
  'name': "SDS",
  #'name'l: "SafeDollar.Fi Share 2.0",
  'decimals': 18
},
{
  'address': "0xF04e268F677A8739494E5F93C7d5f23087804F3A",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x8888888889953bdaa9a7273bA13c80918823ba71",
  'name': "SUISEI",
  #'name'l: "星街すいせい",
  'decimals': 18
},
{
  'address': "0xFBA769d1206C3038A210d6987D47b05A97d419C6",
  'name': "SPADEFARM",
  #'name'l: "SPADE FARM",
  'decimals': 18
},
{
  'address': "0x7a1FBC34247BdA01927E4089a686789602174fB0",
  'name': "Eggs",
  #'name'l: "SafeEggs",
  'decimals': 18
},
{
  'address': "0x7992fC76450C3f394821b4AE30c6D41ef998c39D",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x4257EA7637c355F81616050CbB6a9b709fd72683",
  'name': "CVX",
  #'name'l: "Convex Token (PoS)",
  'decimals': 18
},
{
  'address': "0x6f7C932e7684666C9fd1d44527765433e01fF61d",
  'name': "MKR",
  #'name'l: "MAKER (PoS)",
  'decimals': 18
},
{
  'address': "0x95c300e7740D2A88a44124B424bFC1cB2F9c3b89",
  'name': "ALCX",
  #'name'l: "Alchemix (PoS)",
  'decimals': 18
},
{
  'address': "0x3AE490db48d74B1bC626400135d4616377D0109f",
  'name': "ALPHA",
  #'name'l: "AlphaToken (PoS)",
  'decimals': 18
},
{
  'address': "0xc81278a52AD0e1485B7C3cDF79079220Ddd68b7D",
  'name': "BAO",
  #'name'l: "BaoToken (PoS)",
  'decimals': 18
},
{
  'address': "0x6f68fA254Db99315d5E34c0129F11de12e0bb482",
  'name': "test",
  #'name'l: "test",
  'decimals': 9
},
{
  'address': "0xf7235863883B440e85549F9F92F329DD9c79fa43",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x2596233fFa8AaA724613461595599E200E9728c8",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xB23E78d6a38092193878a5A30198C85800f38849",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xf55daE6dB40DC445476F672db12DBf2a4fE2b643",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xF9691165764eA5f01f01e0466AA63fB24D660eb8",
  'name': "DogeSushi",
  #'name'l: "DogeSushi",
  'decimals': 18
},
{
  'address': "0xeC5AE5A69045eCf74c5C864d2876826BE38e7846",
  'name': "CSWAP",
  #'name'l: "CSWAPToken",
  'decimals': 18
},
{
  'address': "0x8DdE105EdE886b2D943f3CAEf3ea4DBFb6558Ab6",
  'name': "GLCY",
  #'name'l: "Global currency",
  'decimals': 18
},
{
  'address': "0x474Ba20088174612427cf8440ac5712e98652AD2",
  'name': "MINTY",
  #'name'l: "Minty Art",
  'decimals': 18
},
{
  'address': "0x2993871A794480A87cc2E4CE6CEc50cC936bc631",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x26C94F81DDCE371C5a89dfa3a3Bb245553B0c050",
  'name': "BULB",
  #'name'l: "Bulbswap",
  'decimals': 18
},
{
  'address': "0x28b7C90d2CfA1E54bBaCd01c030E18a74AeECcF0",
  'name': "pb",
  #'name'l: "pb",
  'decimals': 18
},
{
  'address': "0x878534a571ad0f2d4F38bc8a8b2Cb393F472580d",
  'name': "tpip",
  #'name'l: "Testpip",
  'decimals': 18
},
{
  'address': "0xa1e9c15c92aF81416284e1acA1c497789863AbFC",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x9C76bc5a7e90248e387C6065638Bb3033806f3f0",
  'name': "MONSTER",
  #'name'l: "Monster Token",
  'decimals': 18
},
{
  'address': "0xfc90bDF42103519C4996839a78dd5D567889931E",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xb57e8d117eBE5393D9eD529516711852d243F98e",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x232eaB56c4fB3f84c6Fb0a50c087c74b7B43c6Ad",
  'name': "ZUZ",
  #'name'l: "Zeus (PoS)",
  'decimals': 18
},
{
  'address': "0xa124aFb74296DC03312E2170b917Dd9C7Fea9e17",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xc22489346e6F2d4507A0064b6e8342d22C735C9a",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xe37f31F16be5E3D20a7F096E1cfDaB94ECfc5342",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x9e725Cf7265D12fd5f59499AFf1258CA92CAc74d",
  'name': "CHICK",
  #'name'l: "loserchick",
  'decimals': 18
},
{
  'address': "0xeEE530048834e6cDf39978F9A8299ACf3c84E2d5",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xFA39033D3D7926242b4Ee708304f949A03AC8Cb0",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x823eE6743705253755a8E3eCD5d709f974241a44",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xdb23243183c73fAc6F80DE0ee9b57476FfFB93d3",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xA2d28b2e17367dbd643F50f7743561374cFd1425",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xaf965beB8C830aE5dc8280d1c7215B8F0aCC0CeA",
  'name': "maticDUCO",
  #'name'l: "Duino Coin on Polygon",
  'decimals': 18
},
{
  'address': "0x34d4ab47Bee066F361fA52d792e69AC7bD05ee23",
  'name': "AURUM",
  #'name'l: "RaiderAurum",
  'decimals': 18
},
{
  'address': "0xcd7361ac3307D1C5a46b63086a90742Ff44c63B3",
  'name': "RAIDER",
  #'name'l: "RaiderToken",
  'decimals': 18
},
{
  'address': "0xb7Bcb34180183C698C3F937a7DbC927f5722031b",
  'name': "STABLEM",
  #'name'l: "StableM Token",
  'decimals': 18
},
{
  'address': "0x3962F4A0A0051DccE0be73A7e09cEf5756736712",
  'name': "LPT",
  #'name'l: "Livepeer Token (PoS)",
  'decimals': 18
},
{
  'address': "0x74BACA77bc4EA498987c1a62f666eC5632d9BB0e",
  'name': "RAIDER",
  #'name'l: "CryptoRaiders",
  'decimals': 18
},
{
  'address': "0xECAB4f41Ef557cd1dE7524346bBb0F505cBB9b2e",
  'name': "PCAKE",
  #'name'l: "PCAKE",
  'decimals': 18
},
{
  'address': "0xee8827034D9406269043F2CD209e3288C8537067",
  'name': "_",
  #'name'l: "_",
  'decimals': 18
},
{
  'address': "0x4692b72B73Ea0Fb78894B895441309bEcEe44c13",
  'name': "_",
  #'name'l: "_",
  'decimals': 18
},
{
  'address': "0xc8bcb58caEf1bE972C0B638B1dD8B0748Fdc8A44",
  'name': "PEAR",
  #'name'l: "Pear Token",
  'decimals': 18
},
{
  'address': "0x2d3bfb602Dc06f201564e063450A2752a837C1a6",
  'name': "MBSTR",
  #'name'l: "Mobster Finance Token",
  'decimals': 18
},
{
  'address': "0x50fb6FcE76f5DabCe3Ada0e2847D99FfF2B2dDB4",
  'name': "AXSBACK",
  #'name'l: "AxieBack.finance",
  'decimals': 18
},
{
  'address': "0xfcc4Afb2A5fE0D4397B4A7BE7d85B4D56ca68652",
  'name': "PolyXT",
  #'name'l: "Polygon eXchange Token",
  'decimals': 18
},
{
  'address': "0x0B8e032d108416CdBc724DbAd670c8D75B85fAA8",
  'name': "BMB",
  #'name'l: "Bmboozle",
  'decimals': 18
},
{
  'address': "0xc4dB51115520D5eBFD2B1e8E52058d52253c4Ef1",
  'name': "FEGexGovernance",
  #'name'l: "FEGexGovernance",
  'decimals': 18
},
{
  'address': "0xB09a8DCA4Dc31F24018849ae7904901C27Ed323C",
  'name': "SH",
  #'name'l: "Shilling",
  'decimals': 18
},
{
  'address': "0xf7d9e281c5Cb4C6796284C5b663b3593D2037aF2",
  'name': "NFTP",
  #'name'l: "NFT Platform Index (PoS)",
  'decimals': 18
},
{
  'address': "0xC057446A89Cbcd827b642f933e5459f206B44872",
  'name': "XLS",
  #'name'l: "XLSkaterToken",
  'decimals': 18
},
{
  'address': "0x997f2E78e200d09B89dD2E7709C1CC0f231c59b9",
  'name': "test",
  #'name'l: "test",
  'decimals': 18
},
{
  'address': "0xF480f38C366dAaC4305dC484b2Ad7a496FF00CeA",
  'name': "GTON",
  #'name'l: "Graviton",
  'decimals': 18
},
{
  'address': "0x1B7654EF23b50Fa97840482D219f31221a54D655",
  'name': "NFH",
  #'name'l: "Non Fungible History",
  'decimals': 8
},
{
  'address': "0x82f905B73d3B25585656cBbA3c4518F276C9CD81",
  'name': "HVN",
  #'name'l: "Haven Support Coin",
  'decimals': 4
},
{
  'address': "0x8Fa4f7127e9FCaFee9F7cF7679dF5199c342B158",
  'name': "SBT",
  #'name'l: "SudoBOT",
  'decimals': 18
},
{
  'address': "0xfE31a87c001c7B0FcDF4c480621222d4FE793364",
  'name': "TOSHI",
  #'name'l: "Toshi Token (PoS)",
  'decimals': 18
},
{
  'address': "0x48879f08E7065ec3abFE22ad7Edd69AE452Ee20D",
  'name': "DUFF",
  #'name'l: "PolyDuff",
  'decimals': 18
},
{
  'address': "0xF1afb5674Bf946458BD1163163F62dE683B07D65",
  'name': "tEXO",
  #'name'l: "tEXO (POLY)",
  'decimals': 18
},
{
  'address': "0xfB6C595D1d98B19CeFe309cd0A8688fDC456e07C",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0x84bBF41B286059d77Fa046641f8dC9f485E5a027",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0x8BD19Ca78B700eBaD7Ece6381F391A805C2f3502",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0x5861e869285BEDE581B54771b68ED101F051135f",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0x546b4c391520E6652897c65153074088BFC0A909",
  'name': "FOR",
  #'name'l: "The Force Token (PoS)",
  'decimals': 18
},
{
  'address': "0x73f0F6aaB6cBC00817f7EfD4f76Da714067bFaAd",
  'name': "KING",
  #'name'l: "KingDefi Token",
  'decimals': 18
},
{
  'address': "0x91fe3f8F63EC903C90B399c200E89609bc445591",
  'name': "PDEGEN",
  #'name'l: "pDegen Finance",
  'decimals': 18
},
{
  'address': "0xAa40849abB7Ba1689cC1272f0D00Ccc04c9bAA04",
  'name': "FAANG",
  #'name'l: "FAANG Token",
  'decimals': 18
},
{
  'address': "0xE1f186285252FE4d3b0D5Aa161F58320Cb5057B8",
  'name': "KNAB",
  #'name'l: "Knab",
  'decimals': 18
},
{
  'address': "0x21274caDa499Ec241A3055c312132e75BE530522",
  'name': "pb",
  #'name'l: "pb",
  'decimals': 18
},
{
  'address': "0x88B7dF8Ab008f0085023f403ec72BE477Ca146aA",
  'name': "tpip",
  #'name'l: "Testpip",
  'decimals': 18
},
{
  'address': "0x4bc007Af0BDB99E58ED7CFAF1EFE37341282049f",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xBC5b59EA1b6f8Da8258615EE38D40e999EC5D74F",
  'name': "PAW",
  #'name'l: "Paw V2",
  'decimals': 18
},
{
  'address': "0x1F842Af93BE6C45F6a92883448aC9603c1F59a39",
  'name': "CYK4",
  #'name'l: "Vladmir Poutini",
  'decimals': 9
},
{
  'address': "0xADAC33f543267c4D59a8c299cF804c303BC3e4aC",
  'name': "MIMO",
  #'name'l: "MIMO Parallel Governance Token (PoS)",
  'decimals': 18
},
{
  'address': "0xA1AB4546FCb0167752c1b4b80646Af3ACFBB49f8",
  'name': "XMT",
  #'name'l: "Xircus Market Token",
  'decimals': 18
},
{
  'address': "0xcd7183b2D79B1DE0238618aEfd1eAc303413E1E1",
  'name': "PGF",
  #'name'l: "PokerGameFinance",
  'decimals': 18
},
{
  'address': "0xe03294f4ba8a709A5375a0f0cDD06fcdaa1d66c4",
  'name': "Emi",
  #'name'l: "EnvimarsFinance",
  'decimals': 18
},
{
  'address': "0xFe25d00ae5D9346250f2FfB49F7607B7491d3678",
  'name': "QUOKKAREST",
  #'name'l: "Quokka Token",
  'decimals': 18
},
{
  'address': "0x371b97c779E8C5197426215225dE0eEac7dD13AF",
  'name': "SEED",
  #'name'l: "SeedToken",
  'decimals': 0
},
{
  'address': "0x0cC89c4F4f6C19767b076ae6A6CA13dC1514bcba",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xEdb73FfE22F545Ff9683e3b63663E198e6843C19",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xda7bDacDD9a8E8ebE062b31F63b3f58CF480D09D",
  'name': "GWP",
  #'name'l: "Grow Protocol",
  'decimals': 9
},
{
  'address': "0x9f9808eB079544Aa27F4836B42461660388C366F",
  'name': "RICH",
  #'name'l: "RichToken",
  'decimals': 18
},
{
  'address': "0x888888d87d85Bc11549b17907E8f589214EB90c2",
  'name': "PLUT",
  #'name'l: "DePlutus Token",
  'decimals': 18
},
{
  'address': "0x01C1673D4a7a77d71A890f7BB452200CF9A28027",
  'name': "BBT",
  #'name'l: "BigBounty Farm Token",
  'decimals': 18
},
{
  'address': "0x3F374ed3C8e61A0d250f275609be2219005c021e",
  'name': "ARCADIUM",
  #'name'l: "ARCADIUM",
  'decimals': 18
},
{
  'address': "0xd0db099Cb0325Fc390dfc5DBB586c147e3D0B42a",
  'name': "HOUR",
  #'name'l: "Hourglass Token",
  'decimals': 18
},
{
  'address': "0x4e3Decbb3645551B8A19f0eA1678079FCB33fB4c",
  'name': "jEUR",
  #'name'l: "Jarvis Synthetic Euro",
  'decimals': 18
},
{
  'address': "0x79d00b7F228F8804827dE659109D72562d68cE4A",
  'name': "QUOKKA",
  #'name'l: "Quokka Token",
  'decimals': 18
},
{
  'address': "0xbD1463F02f61676d53fd183C2B19282BFF93D099",
  'name': "jCHF",
  #'name'l: "Jarvis Synthetic Swiss Franc",
  'decimals': 18
},
{
  'address': "0x767058F11800FBA6A682E73A6e79ec5eB74Fac8c",
  'name': "jGBP",
  #'name'l: "Jarvis Synthetic British Pound",
  'decimals': 18
},
{
  'address': "0xB5Ff4aBBd3719471851799dd7E6e61A26DB9d3AC",
  'name': "UNI-V2",
  #'name'l: "Uniswap V2",
  'decimals': 18
},
{
  'address': "0x141F4c6cD6a8a8517a92B9fB840d89d6333783FA",
  'name': "SDR",
  #'name'l: "System DeFi for Reference",
  'decimals': 18
},
{
  'address': "0x17BEA92fa8b6ba27591FFbcd94C0e6B9673A9Be8",
  'name': "LYNX",
  #'name'l: "LYNX",
  'decimals': 18
},
{
  'address': "0xE34BD2B5FC2357c01122E9510FA4F35621F358d1",
  'name': "API",
  #'name'l: "ApolloDefi",
  'decimals': 18
},
{
  'address': "0x1eC1b66FBEa4f305D4953e08A1C253adA114157D",
  'name': "QUOKKA",
  #'name'l: "Quokka Token",
  'decimals': 18
},
{
  'address': "0x7222D205AfF8D040CcE66DDDDA565e1EF7041E08",
  'name': "PElon",
  #'name'l: "PolyElon Token",
  'decimals': 9
},
{
  'address': "0x6C7850F2bCc786d9Dc1f24Be4fA207094d5abEE7",
  'name': "WINN",
  #'name'l: "Winn",
  'decimals': 18
},
{
  'address': "0xD6D1c897341Eb54BA9dd45A3378F37861baEB8e2",
  'name': "PolySex2",
  #'name'l: "PolySex2",
  'decimals': 18
},
{
  'address': "0x409d1CE864f10837621F24052AaCeEF560dA7269",
  'name': "PLOW",
  #'name'l: "Plow Token",
  'decimals': 18
},
{
  'address': "0x32c0A8eb7913b1706Eedf20a4551D82f2C7Ced03",
  'name': "PLOP",
  #'name'l: "Plop Token",
  'decimals': 18
},
{
  'address': "0xCf8bd4733A98ad794b9626B213004c8d3caD5F12",
  'name': "SHRN",
  #'name'l: "Shrine",
  'decimals': 18
},
{
  'address': "0xAd8B6fDfACB845755461B533EDd62dA5772349fC",
  'name': "MATIC FARM",
  #'name'l: "MATIC FARM",
  'decimals': 18
},
{
  'address': "0xD148018551Abf22Db85Df49c25363C4E0aFEbD13",
  'name': "TAOTEST",
  #'name'l: "TAO TEST TOKEN",
  'decimals': 18
},
{
  'address': "0x6Bfb803a4c458ED4Cf7Eb96CF8CE6bcAa9CE1624",
  'name': "test",
  #'name'l: "testToken",
  'decimals': 18
},
{
  'address': "0x468041079d9d99c87F5a17b44Be6D6a529B5F597",
  'name': "CLV",
  #'name'l: "Clover (PoS)",
  'decimals': 6
},
{
  'address': "0x1fd6cF265fd3428F655378a803658942095b4C4e",
  'name': "YELD V2",
  #'name'l: "PolyYeld V2",
  'decimals': 18
},
{
  'address': "0xEf47e6365eEd530570E03Fa2f4c0fFB7Cdd60c8D",
  'name': "YELD V2",
  #'name'l: "PolyYeld V2",
  'decimals': 18
},
{
  'address': "0x4f094c9E6B73cC6dE98619c605B17Cd41B99A61F",
  'name': "TL",
  #'name'l: "TURKLIRASI",
  'decimals': 18
},
{
  'address': "0xe8B6dDfc778d4B43b48fa933b864B1Ac5077218C",
  'name': "OnePunch",
  #'name'l: "OnePunch token",
  'decimals': 14
},
{
  'address': "0x9cb8aE7193ed21e7ee078128dfd145c84Fe83b37",
  'name': "JORB",
  #'name'l: "Jorb Token",
  'decimals': 18
},
{
  'address': "0x11f82635DCcEB4D5FaC332b13b62C1d32310c6eC",
  'name': "CSI",
  #'name'l: "Cannabis Science Coin",
  'decimals': 18
},
{
  'address': "0xa32148ee25c60678d701FdF47F2FAbE8B385270B",
  'name': "GOLDPIG",
  #'name'l: "Golden Pig Moon",
  'decimals': 18
},
{
  'address': "0x34f380a4e3389e99C0369264453523Bbe5aF7faB",
  'name': "KANGAL",
  #'name'l: "Kangal",
  'decimals': 18
},
{
  'address': "0xe1C411348354A33a4082Aa67921B649EB2C55ced",
  'name': "SAFEPOLYMOON",
  #'name'l: "Safe Poly Moon",
  'decimals': 18
},
{
  'address': "0x6f0CAd28165121Ab60d3D5504A702e77d644E367",
  'name': "renZEC",
  #'name'l: "renZEC (PoS)",
  'decimals': 8
},
{
  'address': "0x7583FEDDbceFA813dc18259940F76a02710A8905",
  'name': "FET",
  #'name'l: "Fetch (PoS)",
  'decimals': 18
},
{
  'address': "0x0b962A2061B59d0191f3bC30247aAF51849154e5",
  'name': "WSX",
  #'name'l: "Wise-XEarn",
  'decimals': 5
},
{
  'address': "0x7DfF46370e9eA5f0Bad3C4E29711aD50062EA7A4",
  'name': "SOL",
  #'name'l: "SOL",
  'decimals': 18
},
{
  'address': "0x0B220b82F3eA3B7F6d9A1D8ab58930C064A2b5Bf",
  'name': "GLM",
  #'name'l: "Golem Network Token (PoS)",
  'decimals': 18
},
{
  'address': "0x596eBE76e2DB4470966ea395B0d063aC6197A8C5",
  'name': "JRT",
  #'name'l: "Jarvis Reward Token (PoS)",
  'decimals': 18
},
{
  'address': "0xF23B0f42dEE73d1DE547Aa65554Ca959f68b0045",
  'name': "POLYDOGE",
  #'name'l: "Poly Doge Token",
  'decimals': 18
},
{
  'address': "0xf80274F4D68087A72B5dFe8c434222b21E379727",
  'name': "fmn",
  #'name'l: "polyFamin",
  'decimals': 18
},
{
  'address': "0x3DC03399a35DB8c8ede87E30278e38Aa11b3C207",
  'name': "xYELD V2",
  #'name'l: "XYELD V2",
  'decimals': 18
},
{
  'address': "0x8714C59Ce0D6c3672d8D0543358261c8e2EDDc9b",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0x913aEB4B83Afda46228587356b08958F5860c109",
  'name': "BAD",
  #'name'l: "Badaboum",
  'decimals': 18
},
{
  'address': "0xF3f7754d1859809435c10c10bDAD1d7036A01799",
  'name': "SLGi",
  #'name'l: "SloughiINU",
  'decimals': 8
},
{
  'address': "0x6f46E4c5D0D5fb4B562C46804B5Bd30d58e3578a",
  'name': "nDEFI",
  #'name'l: "Scarlet Macaw",
  'decimals': 18
},
{
  'address': "0xc5Bb36d4Eeed36100ad84f8305a75fC3d065dB9c",
  'name': "A3rd",
  #'name'l: "A3rd",
  'decimals': 18
},
{
  'address': "0x387404d8D51954ca52daf3cAd9689aDf5f7a568C",
  'name': "A3rd",
  #'name'l: "A3rd",
  'decimals': 18
},
{
  'address': "0x49897B33fFA71b0136Bf46D947F7384C24E0C1Cb",
  'name': "A4th",
  #'name'l: "A4th",
  'decimals': 18
},
{
  'address': "0x62F32ee7d77273c6ecd55e510881B512f02A4577",
  'name': "kmLINK/USDC-LINK",
  #'name'l: "Kashi Medium Risk ChainLink Token/USD Coin (PoS)-Chainlink",
  'decimals': 6
},
{
  'address': "0x6c70e2DEEB8b6CBaC171e46fa926bB5757cB1681",
  'name': "BLOW",
  #'name'l: "Blow Token",
  'decimals': 18
},
{
  'address': "0x711c3D57C6D51CfBE758615Cf3B98DDf2CE6191e",
  'name': "kmDAI/USDT-LINK",
  #'name'l: "Kashi Medium Risk (PoS) Dai Stablecoin/(PoS) Tether USD-Chainlink",
  'decimals': 6
},
{
  'address': "0xfe59fc69Df196aB90D7179aD9B779F692136e591",
  'name': "kmUSDT/DAI-LINK",
  #'name'l: "Kashi Medium Risk (PoS) Tether USD/(PoS) Dai Stablecoin-Chainlink",
  'decimals': 18
},
{
  'address': "0xa8316D5091AE2C152C1F74c8159F890E9f3967de",
  'name': "Z1",
  #'name'l: "Z1",
  'decimals': 8
},
{
  'address': "0x61986EA1969b8cD3AdDE63Cdd104687df3d6bbB4",
  'name': "US9763991",
  #'name'l: "Utility Coin CSi CBN US 9763991 B2 Patent Drug Development",
  'decimals': 18
},
{
  'address': "0x9A022637a6c17Ca6ca6D6dE342C83A13bA84113F",
  'name': "taz",
  #'name'l: "tiraxtur Coin",
  'decimals': 2
},
{
  'address': "0xCe2cB67b11ec0399E39AF20433927424f9033233",
  'name': "FLP",
  #'name'l: "FireBird Liquidity Provider",
  'decimals': 18
},
{
  'address': "0x93810fe228Fa8C69B08C2D8df3Ec05357C00C625",
  'name': "ARABELLA",
  #'name'l: "ARABELLA Token",
  'decimals': 18
},
{
  'address': "0x190Eb8a183D22a4bdf278c6791b152228857c033",
  'name': "AGIX",
  #'name'l: "SingularityNET Token (PoS)",
  'decimals': 8
},
{
  'address': "0x18bE51f132753A0c23dD0216476FC076b80a74Bf",
  'name': "SPUD2",
  #'name'l: "It is a Potato",
  'decimals': 18
},
{
  'address': "0xCB898b0eFb084Df14dd8E018dA37B4d0f06aB26D",
  'name': "SING",
  #'name'l: "Sing Token",
  'decimals': 18
},
{
  'address': "0x2fe8733dcb25BFbbA79292294347415417510067",
  'name': "XED",
  #'name'l: "Exeedme (PoS)",
  'decimals': 18
},
{
  'address': "0x61532F17452D6C8759aE2cA5Ab6d134dED776C22",
  'name': "RGEM",
  #'name'l: "RGEM",
  'decimals': 18
},
{
  'address': "0x70784d8A360491562342B4F3d3D039AaAcAf8F5D",
  'name': "SIM",
  #'name'l: "Simba Empire",
  'decimals': 18
},
{
  'address': "0x9469603F3Efbcf17e4A5868d81C701BDbD222555",
  'name': "QUOKK",
  #'name'l: "PolyQuokka Finance Token",
  'decimals': 18
},
{
  'address': "0x008670418c4D2D857Bf62671722B8c6a17529628",
  'name': "$PTA",
  #'name'l: "Polygon Test Alongside",
  'decimals': 18
},
{
  'address': "0xE2Aa7db6dA1dAE97C5f5C6914d285fBfCC32A128",
  'name': "PAR",
  #'name'l: "PAR Stablecoin",
  'decimals': 18
},
{
  'address': "0xC91c06DB0f7bFFba61e2A5645CC15686F0a8c828",
  'name': "RAZOR",
  #'name'l: "RAZOR (PoS)",
  'decimals': 18
},
{
  'address': "0x365AE1c67b3efA55C624c9705Ad1Df2072D3d254",
  'name': "Che",
  #'name'l: "CheGuevara (PoS)",
  'decimals': 18
},
{
  'address': "0xF1bd521984b4b46176ef4E77f3de01B9FBbe5191",
  'name': "CARDS",
  #'name'l: "CARD.STARTER (PoS)",
  'decimals': 18
},
{
  'address': "0x9eb1F7bc4875A09DfF51B1fb2f80f6B8E0b4EB81",
  'name': "SC",
  #'name'l: "SiriCoin",
  'decimals': 18
},
{
  'address': "0xBbC3Fc97ae51E67D8BC5de8FF02b0904faC53844",
  'name': "XPIN",
  #'name'l: "xpin.finance Token",
  'decimals': 18
},
{
  'address': "0x1Aa3D70E5006695cd9B5463021ba7Bde01A37539",
  'name': "DRC",
  #'name'l: "DARACOIN",
  'decimals': 9
},
{
  'address': "0x8AE127d224094CB1B27e1b28a472e588cbcc7620",
  'name': "AAX",
  #'name'l: "aaxexchange.org",
  'decimals': 18
},
{
  'address': "0x844cdc97CFDF0Cd55a195b7D7D80172f2435EF5b",
  'name': "testing",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0xE64fBfA5FdAFad4C3642B71c33b0Da0597516c30",
  'name': "Honeybee",
  #'name'l: "Honeyfinance",
  'decimals': 18
},
{
  'address': "0x895fa841553D1561b3278b580a93F2bCd9687D2a",
  'name': "test2108",
  #'name'l: "test2108",
  'decimals': 18
},
{
  'address': "0xED4343Fa131DDFdea822Ed5610b17FdD5c65bd65",
  'name': "haUSD",
  #'name'l: "hawalaUSD",
  'decimals': 6
},
{
  'address': "0x8cB96E95C714E0996e6D299F617F518D965E352E",
  'name': "GTF",
  #'name'l: "GLOBALTRUSTFUND TOKEN (PoS)",
  'decimals': 8
},
{
  'address': "0xBB816b9556f171FbD73746759FD7dDE7d8f54337",
  'name': "PYRO",
  #'name'l: "Pyro 2.0",
  'decimals': 18
},
{
  'address': "0x7719758dF93eEDD66C8722A702F4D517D71A881c",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xcb3dC163A1e8e50297aEa07A1dbE7DD8132FF010",
  'name': "PIXEL",
  #'name'l: "Polypixel Token",
  'decimals': 18
},
{
  'address': "0xB1289f48E8d8Ad1532e83A8961f6E8b5a134661D",
  'name': "SIRIUS",
  #'name'l: "Sirius Token",
  'decimals': 18
},
{
  'address': "0xE9f2e81894D34aefE7b6bBc89898fF92C39Db320",
  'name': "UTOPIA",
  #'name'l: "PolyTopia Token",
  'decimals': 18
},
{
  'address': "0xcbEF7a4B4385Db4747362b900b6f6f8051B152c0",
  'name': "INF",
  #'name'l: "Infinity Diamond (PoS)",
  'decimals': 18
},
{
  'address': "0x370E18906797E8AFC4d419A76B949D7fc4C7154b",
  'name': "MUT",
  #'name'l: "MiniUtopia.co",
  'decimals': 18
},
{
  'address': "0x2C89bbc92BD86F8075d1DEcc58C7F4E0107f286b",
  'name': "AVAX",
  #'name'l: "Avalanche Token",
  'decimals': 18
},
{
  'address': "0x5B0a0CD03e9Df1829E00128ebE277Cc3247da346",
  'name': "BFLY",
  #'name'l: "Butterfly Protocol (PoS)",
  'decimals': 18
},
{
  'address': "0x199070E35B4AaF6198CaB425E93D4f08532e9B6E",
  'name': "DMTR",
  #'name'l: "Demetris",
  'decimals': 18
},
{
  'address': "0xbBF7C961B51D65A2011ECEb2AfEd35f0FbefdAD7",
  'name': "FRDY",
  #'name'l: "Farraday",
  'decimals': 18
},
{
  'address': "0x9caC2D9Ad8642DDC94e1a976075B58B7e4033205",
  'name': "TESTCG",
  #'name'l: "TestCG Token",
  'decimals': 18
},
{
  'address': "0x9043Ed7aFD928c6120Dd1eb1b09296Dc72D4352C",
  'name': "DGO",
  #'name'l: "DogeOre",
  'decimals': 18
},
{
  'address': "0xaaC249333F739866DF136C8BbE11E90E9DBb5574",
  'name': "4ORCE",
  #'name'l: "4orceToken",
  'decimals': 18
},
{
  'address': "0xCA9e68E8F9C5601A12128BEC34Af2375FE5735C2",
  'name': "PDC",
  #'name'l: "PANDACOIN",
  'decimals': 9
},
{
  'address': "0xf4AF83D306F2decbB7A8af3723b7C2e4D27332be",
  'name': "PUMA",
  #'name'l: "PolyPuma Token",
  'decimals': 18
},
{
  'address': "0x3865BbB2568338f4EDf0F539a9C010836A86bE40",
  'name': "HOUR",
  #'name'l: "Hourglass Token",
  'decimals': 18
},
{
  'address': "0xC2b5C5517B9DcEf90bc5683Cb6D8bFbEbBFf81C0",
  'name': "MILLENNIA",
  #'name'l: "Millennia",
  'decimals': 0
},
{
  'address': "0x3cEbBd199507735bbfC1250aA8ad375F50137F52",
  'name': "ZEX",
  #'name'l: "Geonzex",
  'decimals': 18
},
{
  'address': "0xE56f260e160A26E6Ace16b3B4D8673573876e33F",
  'name': "PAPU",
  #'name'l: "Elpapu",
  'decimals': 18
},
{
  'address': "0xEDaF280EF69bcE2D3F0D94A857Bd6Cba9376c93e",
  'name': "nDEFI",
  #'name'l: "Polly nDefi Index",
  'decimals': 18
},
{
  'address': "0x874e178A2f3f3F9d34db862453Cd756E7eAb0381",
  'name': "GFI",
  #'name'l: "Gravity Finance",
  'decimals': 18
},
{
  'address': "0x6fCaD66A7DA50e913b63E1Cf619C3E8E3C41E93C",
  'name': "BCT",
  #'name'l: "Best Crypto DAO Token Ever",
  'decimals': 9
},
{
  'address': "0x065f4e71A09D060f349C2840a792189B431945D9",
  'name': "Polly",
  #'name'l: "Polly Finance",
  'decimals': 18
},
{
  'address': "0x69801796A01da2450F31919F9F3A77B90651f428",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x100A947f51fA3F1dcdF97f3aE507A72603cAE63C",
  'name': "HAIR",
  #'name'l: "Hair Token",
  'decimals': 18
},
{
  'address': "0x02650994B5243465205835E94eC0B23374D15fe0",
  'name': "GARI",
  #'name'l: "GARI",
  'decimals': 18
},
{
  'address': "0x0f3A19835C34135E8846b989cF0717AA10fB1Fd1",
  'name': "polycattest",
  #'name'l: "polycattest",
  'decimals': 18
},
{
  'address': "0xe37a8ec2f962446b97b1E1B94c73825B7f588D59",
  'name': "TBK",
  #'name'l: "THAIBANKAEW",
  'decimals': 8
},
{
  'address': "0xA6A0Ed3EF084B1628f1036D15bB10241c1627f65",
  'name': "COLLAR",
  #'name'l: "PolyPup Collar Token",
  'decimals': 18
},
{
  'address': "0x3da858682E52C93032CDeEF8DBed9ADe3278de3C",
  'name': "FGNEWS",
  #'name'l: "FootGunsNews",
  'decimals': 18
},
{
  'address': "0x4583955E607577510A828195954868B8C98D90d0",
  'name': "KIWI",
  #'name'l: "KIWI",
  'decimals': 18
},
{
  'address': "0x3020E0DB586ba099dd63810dd315d501865BBCeb",
  'name': "TECH",
  #'name'l: "Cryptomeda",
  'decimals': 18
},
{
  'address': "0x99a1ed9D82a5FfA5Ff3B12C23268455c569f9411",
  'name': "DINO",
  #'name'l: "CryptoDinos",
  'decimals': 18
},
{
  'address': "0x904371845Bc56dCbBcf0225ef84a669b2fD6bd0d",
  'name': "RELAY",
  #'name'l: "Relay Token",
  'decimals': 18
},
{
  'address': "0x28cC94Cf01A8f29668368687e409d7E3DAC17bFE",
  'name': "nDEFI",
  #'name'l: "Polly nDefi Index",
  'decimals': 18
},
{
  'address': "0x144E2005C25EA92254c24Ac6303a6d74AA4F5ec0",
  'name': "POLY",
  #'name'l: "Polymetric",
  'decimals': 18
},
{
  'address': "0x1cE4A2C355F0DcC24E32A9Af19F1836D6F4f98ae",
  'name': "CPD",
  #'name'l: "Coinspaid (PoS)",
  'decimals': 18
},
{
  'address': "0x42AEb84241A4A0B90F9Da6f76E11fe1d9083FD14",
  'name': "GECKOCON21 TICKET",
  #'name'l: "CoinGecko GeckoCon 2021 NFTTicket",
  'decimals': 0
},
{
  'address': "0xf4Dc2fb8A329E2Edf8b4D423b6eF31B94Bb612d0",
  'name': "D&G",
  #'name'l: "Dolcegabbana",
  'decimals': 18
},
{
  'address': "0x0df0f72EE0e5c9B7ca761ECec42754992B2Da5BF",
  'name': "ATA",
  #'name'l: "Automata (PoS)",
  'decimals': 18
},
{
  'address': "0x8B0063dbB53a822f2BF3a50EBE8d2c365392ac5b",
  'name': "waMUSD",
  #'name'l: "Wasabi mUSD",
  'decimals': 18
},
{
  'address': "0x9942BdDc30F5B4D543477EfEf3A1f441bEfd7297",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xF239E69ce434c7Fb408b05a0Da416b14917d934e",
  'name': "SHI3LD",
  #'name'l: "PolyShield",
  'decimals': 18
},
{
  'address': "0xB24dFE49342f39F8AfC2211A44102ffdad0582F5",
  'name': "s",
  #'name'l: "s",
  'decimals': 18
},
{
  'address': "0xa509Da749745Ac07E9Ae47E7a092eAd2648B47f2",
  'name': "MYFRIENDS",
  #'name'l: "MYFRIENDS",
  'decimals': 18
},
{
  'address': "0x2628568509E87c4429fBb5c664Ed11391BE1BD29",
  'name': "renDGB",
  #'name'l: "renDGB",
  'decimals': 8
},
{
  'address': "0x479D3214079C38eD9ab296D96b88bFe23EEd0002",
  'name': "BRL",
  #'name'l: "Brilliant",
  'decimals': 18
},
{
  'address': "0xE7b631F9657f716302498418B2F580DE7ac8B080",
  'name': "PDOGE7",
  #'name'l: "PDOGE7",
  'decimals': 18
},
{
  'address': "0x9776f7635B2b8d83A44745c2BB80F766E5578355",
  'name': "COLLAR",
  #'name'l: "PolyPup Collar Token",
  'decimals': 18
},
{
  'address': "0xA731349fa468614c1698fc46ebf06Da6F380239e",
  'name': "HT",
  #'name'l: "Huobi Token",
  'decimals': 18
},
{
  'address': "0x8edeFEbAC5276EF7Ae1E4620b7E18FCcf0450cf6",
  'name': "T",
  #'name'l: "test",
  'decimals': 18
},
{
  'address': "0x08BE454de533509e8832B257116C5506E55b0b64",
  'name': "STND",
  #'name'l: "Standard",
  'decimals': 18
},
{
  'address': "0xd3f07EA86DDf7BAebEfd49731D7Bbd207FedC53B",
  'name': "nDEFI",
  #'name'l: "Polly nDefi Nest",
  'decimals': 18
},
{
  'address': "0x8D354E27DA71481aa87a27BAa6A065Cb030b4F2B",
  'name': "VELEN",
  #'name'l: "Diva",
  'decimals': 18
},
{
  'address': "0xFbaE8e2D04a67C10047D83ee9B8AeFFE7F6EA3f4",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x6Ad07819171b8841404f3Bd3A4B2aa2282c2eC88",
  'name': "TEST",
  #'name'l: "TestToken",
  'decimals': 18
},
{
  'address': "0x876E80943BadF1f46A3322754F5ad32448913771",
  'name': "MVO",
  #'name'l: "MVO",
  'decimals': 18
},
{
  'address': "0x866a680d43Cb17F2B65F7cCC3471146A560AfADa",
  'name': "PENDLETEST",
  #'name'l: "Pendle Test",
  'decimals': 18
},
{
  'address': "0x0130E62c6a220B1940bCcA9f481b7447a6aFbE8C",
  'name': "NAT",
  #'name'l: "native",
  'decimals': 18
},
{
  'address': "0x53736299c3294D0e8aa002FC36Df7627048b573A",
  'name': "tpip",
  #'name'l: "Testpip",
  'decimals': 18
},
{
  'address': "0x79cfc419a4870FC176A4aB8c81FcFD4073a972c1",
  'name': "BETA",
  #'name'l: "PolyBeta",
  'decimals': 18
},
{
  'address': "0x1FcbE5937B0cc2adf69772D228fA4205aCF4D9b2",
  'name': "BADGER",
  #'name'l: "Badger (PoS)",
  'decimals': 18
},
{
  'address': "0xfd0cbdDec28a93bB86B9db4A62258F5EF25fEfdE",
  'name': "BITT",
  #'name'l: "BITTOKEN (PoS)",
  'decimals': 18
},
{
  'address': "0x42ED4D26a0f3d1BcB88efFc13a51ed0E9Cbd4E45",
  'name': "SLIPS",
  #'name'l: "SafeLips",
  'decimals': 9
},
{
  'address': "0x5686C84cACcbDc97d3eB9184189DBA40C9d07a6A",
  'name': "tpip",
  #'name'l: "Testpip",
  'decimals': 18
},
{
  'address': "0xCad2fd1CDd6F2d62744320BaDC8C0EdE4bc29c5e",
  'name': "000",
  #'name'l: "THE PIGGY INDEX [000]",
  'decimals': 18
},
{
  'address': "0x712F0cf37Bdb8299D0666727F73a5cAbA7c1c24c",
  'name': "hMATIC",
  #'name'l: "Matic Token Hop Token",
  'decimals': 18
},
{
  'address': "0x3aD736904E9e65189c3000c7DD2c8AC8bB7cD4e3",
  'name': "MATICx",
  #'name'l: "Super MATIC",
  'decimals': 18
},
{
  'address': "0x01a811638D1979cfd3bd14F9c103d2d83872AeD1",
  'name': "UX",
  #'name'l: "\"the user experience\"
  'decimals': 18
},
{
  'address': "0x8c8E698F0fe1C88309788ce3fC0582f46d977b87",
  'name': "PKN",
  #'name'l: "Plankton",
  'decimals': 18
},
{
  'address': "0x122b2D5298a964d43d6eE883036cA5777873cf06",
  'name': "DOGIRA",
  #'name'l: "Dogira",
  'decimals': 9
},
{
  'address': "0xE877c22E13Df38A718D002A12379CdD97C814174",
  'name': "CAMIS",
  #'name'l: "CamiloCoin",
  'decimals': 18
},
{
  'address': "0x00e5646f60AC6Fb446f621d146B6E1886f002905",
  'name': "RAI",
  #'name'l: "Rai Reflex Index (PoS)",
  'decimals': 18
},
{
  'address': "0xf647AFa0da0E99f887D07Da8d1A2DB433cd5E1e7",
  'name': "PORVOS",
  #'name'l: "Porvos con la Lola",
  'decimals': 18
},
{
  'address': "0x3e67aF60f168B9B2adaDb57164d6726764ffaF0A",
  'name': "PDARK",
  #'name'l: "PDARKCOIN",
  'decimals': 18
},
{
  'address': "0xde4c826179aeA9DE46a7ed0E103848FA7373ca45",
  'name': "PCZDIAMOND",
  #'name'l: "PCZDIAMOND",
  'decimals': 18
},
{
  'address': "0x30DA0876615E1A9c8127068C3552CA0EF8299DC5",
  'name': "NEXUS",
  #'name'l: "Nexus Finance",
  'decimals': 5
},
{
  'address': "0x8a0e8b4b0903929f47C3ea30973940D4a9702067",
  'name': "INSUR",
  #'name'l: "InsurAce (PoS)",
  'decimals': 18
},
{
  'address': "0xb480A6af0Fc32D2DDa91E66862C621d5De356d6F",
  'name': "TorNetwork",
  #'name'l: "TorNetwork",
  'decimals': 18
},
{
  'address': "0xCbf93Accff63EE371421f0395Ee10dCb72b7c747",
  'name': "TESTCG",
  #'name'l: "TestCG Token",
  'decimals': 18
},
{
  'address': "0x01fA5b3A5d77BcF705DD505bBcBb34bce310E7FE",
  'name': "AXI",
  #'name'l: "Axioms (PoS)",
  'decimals': 18
},
{
  'address': "0xbc7cB585346f4F59d07121Bb9Ed7358076243539",
  'name': "SILVER",
  #'name'l: "Silver",
  'decimals': 18
},
{
  'address': "0xefaF0b4c3c1184774F35dae71462E1CB5da16667",
  'name': "AGL",
  #'name'l: "Agile",
  'decimals': 18
},
{
  'address': "0xebCbDd997d09C2282e257aA37b5234695B40dB5D",
  'name': "TEST",
  #'name'l: "Test token",
  'decimals': 9
},
{
  'address': "0x55943AD562C2f5535EF8eB8984848BF52c831c92",
  'name': "Mdc",
  #'name'l: "Mad Dick",
  'decimals': 18
},
{
  'address': "0xcE00240DC9aF622e7C71dA69969F8da8c591F785",
  'name': "HETUN",
  #'name'l: "hetunToken",
  'decimals': 18
},
{
  'address': "0x39D0FAFCaC447dB2BD8Bb6Df83445A4DA9943c16",
  'name': "POORYA",
  #'name'l: "poorya",
  'decimals': 8
},
{
  'address': "0x9D6BB85155087a0c28271BB7db4FC6f60059474E",
  'name': "USD",
  #'name'l: "UNITED STATES DOLLAR",
  'decimals': 18
},
{
  'address': "0x4166BBFd54C9c02F4EEDBc2978a646c7A93AE92E",
  'name': "MSI",
  #'name'l: "MiniSushi",
  'decimals': 9
},
{
  'address': "0x0B048D6e01a6b9002C291060bF2179938fd8264c",
  'name': "ALPHA",
  #'name'l: "PolyAlpha Finance",
  'decimals': 18
},
{
  'address': "0x309a47D5b799a5AD834e445Dc202Db7e231E9924",
  'name': "GCoin",
  #'name'l: "Gakuen Loot Coin",
  'decimals': 18
},
{
  'address': "0x9a95149B9341d87Adb4B1ebE95fc3f8dB9c46359",
  'name': "COLLAR",
  #'name'l: "PolyPup Collar Token",
  'decimals': 18
},
{
  'address': "0x8DF26a1BD9bD98e2eC506fc9d8009954716A05DC",
  'name': "COLLAR",
  #'name'l: "PolyPup Collar Token",
  'decimals': 18
},
{
  'address': "0x43308565C0204C8076A291F0726f914c3133CE34",
  'name': "TET",
  #'name'l: "Tetcoin",
  'decimals': 18
},
{
  'address': "0xCd9c7397B0ef2E9b2a9440d61B0e1E3351a38A28",
  'name': "XLT",
  #'name'l: "Litetokens",
  'decimals': 18
},
{
  'address': "0x689f8e5913C158fFB5Ac5aeb83b3C875F5d20309",
  'name': "SNK",
  #'name'l: "Snook",
  'decimals': 18
},
{
  'address': "0xd422089785ada2762343B209b43bC48dd7ad4AE9",
  'name': "CZR",
  #'name'l: "Czarcoin",
  'decimals': 18
},
{
  'address': "0x991aeafbe1B1C7ac8348DC623AE350768d0C65b3",
  'name': "BED",
  #'name'l: "Comfy",
  'decimals': 18
},
{
  'address': "0x18e7bDB379928A651f093ef1bC328889b33A560c",
  'name': "wRNBW",
  #'name'l: "Wrapped Rainbow Token",
  'decimals': 18
},
{
  'address': "0xc104e54803abA12f7a171a49DDC333Da39f47193",
  'name': "wXRNBW",
  #'name'l: "Wrapped Vesting Rainbow Token",
  'decimals': 18
},
{
  'address': "0x047fD3B3D2366F9babe105ade4598E263d6c699c",
  'name': "COUGAR",
  #'name'l: "Cougar Token",
  'decimals': 18
},
{
  'address': "0x28424507fefb6f7f8E9D3860F56504E4e5f5f390",
  'name': "amWETH",
  #'name'l: "Aave Matic Market WETH",
  'decimals': 18
},
{
  'address': "0x2e1AD108fF1D8C782fcBbB89AAd783aC49586756",
  'name': "TUSD",
  #'name'l: "TrueUSD (PoS)",
  'decimals': 18
},
{
  'address': "0x18961f2BaC390751aABe5B843c57A8573bfA3950",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x3D8E1141a52466607A8aa489084D3871de0bb6CD",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x6af96896cDf72361CDd7c2f839480d3D4503BE7f",
  'name': "DARK",
  #'name'l: "Darkcoin",
  'decimals': 18
},
{
  'address': "0xa44Fc6A9F98E3Bf32a5167675513d9E9E8002eb4",
  'name': "CZDIAMOND",
  #'name'l: "CZDiamond",
  'decimals': 18
},
{
  'address': "0x0eFc380f71bcc8F2C6aFDAdbe54E42A7C6162391",
  'name': "DARK",
  #'name'l: "Darkcoin",
  'decimals': 18
},
{
  'address': "0x885f2ec2520b67408Aaf8700dB0D56E7beF93820",
  'name': "CZDIAMOND",
  #'name'l: "CZDiamond",
  'decimals': 18
},
{
  'address': "0x8BFb23F6CFfd36C818E41E46A5f35716e1b8FA82",
  'name': "DARK",
  #'name'l: "Darkcoin",
  'decimals': 18
},
{
  'address': "0xDBc9CBF2a289966c1bc1Bb43D8d0213fE9E7D791",
  'name': "CZDIAMOND",
  #'name'l: "CZDiamond",
  'decimals': 18
},
{
  'address': "0x1942b8262a0683B54f4f91D0c08dDD92ed6E8FE6",
  'name': "DARK",
  #'name'l: "Darkcoin",
  'decimals': 18
},
{
  'address': "0x6664C64C8582e62dA861Fcac33a627b0f92fF0F8",
  'name': "CZDIAMOND",
  #'name'l: "CZDiamond",
  'decimals': 18
},
{
  'address': "0xaa20bBae3B4D6D890a2FA44B8d55ED6b74eC098B",
  'name': "Poly1",
  #'name'l: "Poly1",
  'decimals': 18
},
{
  'address': "0xeA1733E638170843e2c104162cCc951331043114",
  'name': "PICHI",
  #'name'l: "PolyCityToken",
  'decimals': 18
},
{
  'address': "0x0249536FDa5c5D379Dc70D50236Dd9F3a414bB3B",
  'name': "TST",
  #'name'l: "Test",
  'decimals': 18
},
{
  'address': "0x86756DF8D53f85d042Bda0a733bd1E55132F40f3",
  'name': "TST",
  #'name'l: "Test2",
  'decimals': 18
},
{
  'address': "0x6a5FCC167f277f7DdEEa87CfF3D86b834010f0F7",
  'name': "TGA",
  #'name'l: "TGA Metaverse Collection",
  'decimals': 18
},
{
  'address': "0xc30215aAeefb174686Edb378896cd2aCd7E200DD",
  'name': "ELABS",
  #'name'l: "ecosis Labs",
  'decimals': 18
},
{
  'address': "0x5c2ed810328349100A66B82b78a1791B101C9D61",
  'name': "amWBTC",
  #'name'l: "Aave Matic Market WBTC",
  'decimals': 8
},
{
  'address': "0x883aBe4168705d2e5dA925d28538B7a6AA9d8419",
  'name': "BALL",
  #'name'l: "Ball Token",
  'decimals': 18
},
{
  'address': "0xe15A9C1183DfeEcD9e159c5397f9e367901ff482",
  'name': "PAP1",
  #'name'l: "PApu1",
  'decimals': 18
},
{
  'address': "0x49B4D34eDCC985fEa2A8fBCC11Ec575283D10D87",
  'name': "UPmatic",
  #'name'l: "UPmatic",
  'decimals': 18
},
{
  'address': "0xb8ab048D6744a276b2772dC81e406a4b769A5c3D",
  'name': "WUSD",
  #'name'l: "Wault USD",
  'decimals': 18
},
{
  'address': "0x24834BBEc7E39ef42f4a75EAF8E5B6486d3F0e57",
  'name': "LUNA",
  #'name'l: "Wrapped LUNA Token (PoS)",
  'decimals': 18
},
{
  'address': "0x7Ef750829137926675CD8d568d4988e0Fa29ddb6",
  'name': "TYFU",
  #'name'l: "TyrantFund",
  'decimals': 18
},
{
  'address': "0x3f717919deF69f81d17b80839bf8af35697ccbFa",
  'name': "DTX",
  #'name'l: "DaTa eXchange Token (PoS)",
  'decimals': 18
},
{
  'address': "0x4C392822D4bE8494B798cEA17B43d48B2308109C",
  'name': "Polly",
  #'name'l: "Polly Finance",
  'decimals': 18
},
{
  'address': "0xe20B9e246db5a0d21BF9209E4858Bc9A3ff7A034",
  'name': "wBAN",
  #'name'l: "Wrapped Banano",
  'decimals': 18
},
{
  'address': "0xC9c1c1c20B3658F8787CC2FD702267791f224Ce1",
  'name': "FTM",
  #'name'l: "Fantom Token (PoS)",
  'decimals': 18
},
{
  'address': "0xCe742d3dca61276F03014d4Ebc5B595a503648c4",
  'name': "TEST",
  #'name'l: "Testing token",
  'decimals': 18
},
{
  'address': "0x4C3bF0a3DE9524aF68327d1D2558a3B70d17D42a",
  'name': "DYDX",
  #'name'l: "dYdX (PoS)",
  'decimals': 18
},
{
  'address': "0x3B5F1E212De0036f943188a1721d43BA194A12ba",
  'name': "",
  #'name'l: ".eth (PoS",
  'decimals': 18
},
{
  'address': "0x42C3d84e4E465263C85dFcf304ec3571b4332c46",
  'name': "UNIQ",
  #'name'l: "Unicorn",
  'decimals': 18
},
{
  'address': "0x0eF2603Cd156E1934E19D0B07Cd64F415e1E7940",
  'name': "PIGX",
  #'name'l: "PIGX (PoS)",
  'decimals': 18
},
{
  'address': "0x782bEa4e957E8C17444a374FB27c0b2921F87181",
  'name': "NOR",
  #'name'l: "NORNET",
  'decimals': 18
},
{
  'address': "0x59fE965a8355B20BC6B87c0473F2845098A2b281",
  'name': "mCYNS",
  #'name'l: "mCYNS Token",
  'decimals': 18
},
{
  'address': "0x92117C2AAceC7780f05c00f96277e600b62fC5E6",
  'name': "mCYN",
  #'name'l: "Matic CYN Token",
  'decimals': 18
},
{
  'address': "0xa9Ee51B3ECd466E5c340635216AF7298b3533122",
  'name': "mELP",
  #'name'l: "Matic ELP Token",
  'decimals': 18
},
{
  'address': "0xFEE0A6289298CD7d6E376191DA00FD95B3584Dcf",
  'name': "mELPS",
  #'name'l: "mELPS Token",
  'decimals': 18
},
{
  'address': "0x4AAabD886A44D0600C7A87584Eede816f76DfF99",
  'name': "mHIPS",
  #'name'l: "mHIPS Token",
  'decimals': 18
},
{
  'address': "0x6B8bCe6E4EF035A7d8E40FBEC2184E3B649Df4dE",
  'name': "mHIP",
  #'name'l: "Matic Hippo Token",
  'decimals': 18
},
{
  'address': "0x65A05DB8322701724c197AF82C9CaE41195B0aA8",
  'name': "FOX",
  #'name'l: "FOX (PoS)",
  'decimals': 18
},
{
  'address': "0x59e792a9C8CF4A5e5ab219aB2565Fb893e4f98d7",
  'name': "ADDYFORK",
  #'name'l: "AdamantFork",
  'decimals': 18
},
{
  'address': "0xE7c507f42D0C0A5047147f34439F7138Fc6050C6",
  'name': "BELA",
  #'name'l: "Bela Farm Token",
  'decimals': 18
},
{
  'address': "0x0C0AcC27E77c17559C43B47BE2C6aCc6b879fE73",
  'name': "mers",
  #'name'l: "mers.finance",
  'decimals': 18
},
{
  'address': "0xc47033074e21d18673b99540889EaFBc6870a21C",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x0a9Fe090cF2c912A460b8dd3a0f647F3780248D1",
  'name': "Cls",
  #'name'l: "Cls",
  'decimals': 18
},
{
  'address': "0xb459409d3d5008B88804697Be1075B98b876Cb87",
  'name': "RAI",
  #'name'l: "RAI",
  'decimals': 18
},
{
  'address': "0xf8a57c1d3b9629b77b6726a042ca48990A84Fb49",
  'name': "btcCRV",
  #'name'l: "Curve.fi amWBTC/renBTC",
  'decimals': 18
},
{
  'address': "0xc4ACD115F1CeeBD4A88273423D6CF77C4A1c7559",
  'name': "AD2",
  #'name'l: "Asian Dragon",
  'decimals': 8
},
{
  'address': "0x40ed0565eCFB14eBCdFE972624ff2364933a8cE3",
  'name': "GPUL",
  #'name'l: "GammaPulsarToken",
  'decimals': 18
},
{
  'address': "0xe0Ce60AF0850bF54072635e66E79Df17082A1109",
  'name': "PROPEL",
  #'name'l: "Propel",
  'decimals': 18
},
{
  'address': "0x4347C7084Ab565ef1C3929106756B85295796cE2",
  'name': "Toc",
  #'name'l: "Type1coin",
  'decimals': 18
},
{
  'address': "0x76d787410067DB8b444038BC17E6Fb5870d1040D",
  'name': "DON",
  #'name'l: "DoubleOrNothingToken",
  'decimals': 0
},
{
  'address': "0xB44cf912E9D0341e92f64f4a0642393B7f3526C4",
  'name': "PULL",
  #'name'l: "Rug Pull, For Sure",
  'decimals': 18
},
{
  'address': "0x0279eee698ABC84ADA3126BE6441ED82f2460865",
  'name': "CIA",
  #'name'l: "CryptoInvestor.ca DBA the CIA",
  'decimals': 18
},
{
  'address': "0x9C1Df8Ffd7b49a795BdbB85Eb39D4ae371994E30",
  'name': "GOOG",
  #'name'l: "Google",
  'decimals': 18
},
{
  'address': "0x0000000000004946c0e9F43F4Dee607b0eF1fA1c",
  'name': "CHI",
  #'name'l: "Chi Gastoken by 1inch",
  'decimals': 0
},
{
  'address': "0x74305d519F93C4A39eE41CfCA8b9C2B7b1C3853d",
  'name': "API",
  #'name'l: "APIPIRO",
  'decimals': 18
},
{
  'address': "0x0B6afe834dab840335F87d99b45C2a4bd81A93c7",
  'name': "ANGEL",
  #'name'l: "Angel (PoS)",
  'decimals': 18
},
{
  'address': "0xf911D2e1df43110DCe59443988A37517aF62D380",
  'name': "BET",
  #'name'l: "BabyEth",
  'decimals': 9
},
{
  'address': "0x69701c9A3539dDA8A47A18ef039Dae1da5078C6D",
  'name': "P2P",
  #'name'l: "P2PCOIN",
  'decimals': 18
},
{
  'address': "0x24540f2a963e9962Fc0C10B88BD10D43E75dA0ed",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x9e1c0A912fB0D97b4eF876C3E3b064416475DACE",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xeF0AD8Ff8E942265B203778db2490cb1417933Ad",
  'name': "PUSS",
  #'name'l: "Pussy Coin",
  'decimals': 18
},
{
  'address': "0xdD8d37d91c84F2c243bCc7Ba871824Dda837928F",
  'name': "HLM",
  #'name'l: "Helm",
  'decimals': 18
},
{
  'address': "0x2713Bbd13e4da5b90217Ff3403d04fb95581Cc16",
  'name': "HOR",
  #'name'l: "FTX_Horizon",
  'decimals': 18
},
{
  'address': "0xee41942A1042fA3201CC617FDf4BD77A270BeDDf",
  'name': "ARB",
  #'name'l: "ArbToken",
  'decimals': 18
},
{
  'address': "0x1d5f9ce8c0a5f7f8a7A72Eb8752AEf348A884Ca9",
  'name': "TE",
  #'name'l: "TurboEther",
  'decimals': 18
},
{
  'address': "0x826B5Ca9277A57bc8bd71c6219E5b61d0862288f",
  'name': "P2P",
  #'name'l: "P2PCOIN",
  'decimals': 18
},
{
  'address': "0x6d7b72169da3a8FcD2746FaD26167D1bc50dCFD4",
  'name': "ARB",
  #'name'l: "ArbToken",
  'decimals': 18
},
{
  'address': "0xbFb99BACCC25410D25eC750855Fe66ad0141978a",
  'name': "UE",
  #'name'l: "UltraEther",
  'decimals': 18
},
{
  'address': "0xADF79dB1147e831158F08b13356D69Ccf6649d2b",
  'name': "UNI-V2",
  #'name'l: "Uniswap V2",
  'decimals': 18
},
{
  'address': "0x30DE46509Dbc3a491128F97be0aAf70dc7Ff33cB",
  'name': "XZAR",
  #'name'l: "South African Tether (PoS)",
  'decimals': 18
},
{
  'address': "0xc811553c09e472eb4516f69413F164eF4cAAFb02",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xDc78c06Fa5bb24a01DB85868B44F2Ed92eDD8d75",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x71547808A7ccDb8469958a1dce9d23874d519812",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xc69Fc55d467EC02606eD11c63DDd7C89e24F5D84",
  'name': "GAMEFI",
  #'name'l: "GameFi",
  'decimals': 18
},
{
  'address': "0xe3E2108220433635a6097FCc0815B6d6A8B90351",
  'name': "FST",
  #'name'l: "FIRSTTOKEN",
  'decimals': 18
},
{
  'address': "0x1386e8BA65dfAD31F51B285Ede77ED526Dd0581e",
  'name': "?PUNK",
  #'name'l: "?Punk.eth (PoS)",
  'decimals': 18
},
{
  'address': "0x5dBbDf87f9C49338E99A00c6ceb669f86DF984Bc",
  'name': "?PUNK",
  #'name'l: "?Punk.eth (PoS)",
  'decimals': 18
},
{
  'address': "0x259617d6c9B8ca547883ee115AeeC222a8fEBBe9",
  'name': "BRK",
  #'name'l: "Burak",
  'decimals': 12
},
{
  'address': "0x94860B8BDaeB0Fb35D115Ec5F9Ee47FaF7E4722c",
  'name': "DWSK",
  #'name'l: "Dorian Wandoskin",
  'decimals': 18
},
{
  'address': "0x24e0801a4fADF2Ee800b7d0Efc0FC52685CEE079",
  'name': "Draco",
  #'name'l: "Draconeum",
  'decimals': 3
},
{
  'address': "0xC63F5466325f475D4b86e80bc241911C8b773E61",
  'name': "KUJI",
  #'name'l: "KUJI",
  'decimals': 18
},
{
  'address': "0xC7d5a5df6aE030520366EF8A300543941B99e843",
  'name': "BMG",
  #'name'l: "Black Market Gaming",
  'decimals': 18
},
{
  'address': "0xA9316E1909eDF3eD33B0Dd1c6631c50B82c6e142",
  'name': "NFT Sprites",
  #'name'l: "A NFTSprites.com",
  'decimals': 18
},
{
  'address': "0xc7553307eD737dcE132aE7915E6496864617B261",
  'name': "OWL",
  #'name'l: "Owl Token",
  'decimals': 18
},
{
  'address': "0x209bc5c788cDD15dF9afb9a66e94a9E9a4090ac4",
  'name': "DTN",
  #'name'l: "DonToken",
  'decimals': 18
},
{
  'address': "0x9CDAE334aA149042654D865B961aeE9ACF496162",
  'name': "?COIN",
  #'name'l: "?coin.eth (PoS)",
  'decimals': 18
},
{
  'address': "0x0527c8C43250279D6Eb74dA1078193f5316fc9a0",
  'name': "PYD",
  #'name'l: "PolyQuity Dollar",
  'decimals': 18
},
{
  'address': "0xf00eCE8EDF75Db1aD4c8640EA44537fCCDF6E7a4",
  'name': "OKNA",
  #'name'l: "Tokenart (PoS)",
  'decimals': 18
},
{
  'address': "0x0000000059678E962Fd104ED8B378B328D40494a",
  'name': "Draco",
  #'name'l: "Draconeum",
  'decimals': 18
},
{
  'address': "0xdaB35042e63E93Cc8556c9bAE482E5415B5Ac4B1",
  'name': "IRIS",
  #'name'l: "Iris",
  'decimals': 18
},
{
  'address': "0xb5fC2B6b70f940207ef4260Ae3cBB7714926f7e5",
  'name': "EN",
  #'name'l: "EcoNyan",
  'decimals': 18
},
{
  'address': "0x3d0b79E297E419F58851C1a8DC5304E99aede65b",
  'name': "PBR",
  #'name'l: "PBlogger",
  'decimals': 12
},
{
  'address': "0x59B8E1EF875336949673dB6365B8364aE954addC",
  'name': "ALCX",
  #'name'l: "Alchemix",
  'decimals': 18
},
{
  'address': "0x564a96B6A3b718C856Dd5d51C94aCffdDaf1A006",
  'name': "E1",
  #'name'l: "TurboEcoNyan",
  'decimals': 18
},
{
  'address': "0x5214723413e076409F642F9FeDf657B12E5EF0a4",
  'name': "STUT",
  #'name'l: "SuperTurboUltraToken",
  'decimals': 18
},
{
  'address': "0x18E18939eDBB043E847d55476Dd6c9C5aB0d982c",
  'name': "UD",
  #'name'l: "UpsideDown",
  'decimals': 18
},
{
  'address': "0x9C23d92B5188CF4F69a71668445F3A69bE343CA0",
  'name': "TH",
  #'name'l: "Trash",
  'decimals': 18
},
{
  'address': "0xa353dEb6Fb81dF3844D8bd614D33d040fDBb8188",
  'name': "MST",
  #'name'l: "MagicStone",
  'decimals': 18
},
{
  'address': "0xE7804D91dfCDE7F776c90043E03eAa6Df87E6395",
  'name': "DFX",
  #'name'l: "DFX Token (PoS)",
  'decimals': 18
},
{
  'address': "0xdDa40cdfe4A0090f42Ff49f264A831402ADB801A",
  'name': "DOGIRA",
  #'name'l: "Dogira",
  'decimals': 9
},
{
  'address': "0x50BC0CBC314F1c51DcE4D9175aB87DBE4C1e49df",
  'name': "POLx",
  #'name'l: "Proof of liquidity token",
  'decimals': 18
},
{
  'address': "0x5508752f55f4ac7B7AC22542cFAFECB343Ee78f7",
  'name': "WBT",
  #'name'l: "WBTToken",
  'decimals': 18
},
{
  'address': "0xCBf4AB00b6Aa19B4d5D29C7c3508B393a1C01Fe3",
  'name': "MegaDoge",
  #'name'l: "MegaDoge.Org",
  'decimals': 18
},
{
  'address': "0x5757E6379c987a1FF08b31181EF4f69F57bb9155",
  'name': "YAF",
  #'name'l: "YAF Token",
  'decimals': 5
},
{
  'address': "0x1B9D40715E757Bdb9bdEC3215B898E46d8a3b71a",
  'name': "Metis",
  #'name'l: "Metis Token (PoS)",
  'decimals': 18
},
{
  'address': "0x1257A41a839cc99Be556B77eF99ef063Cf259803",
  'name': "CLICK",
  #'name'l: "Crypto Clicker",
  'decimals': 18
},
{
  'address': "0x52AD2f2a3a5B5C0Ae4253Cd5444050600bdcc356",
  'name': "PUSS",
  #'name'l: "Pussy Coin",
  'decimals': 18
},
{
  'address': "0x14100fD6E927B22EC6a036e85ee881b2c45b0b6F",
  'name': "XSP1",
  #'name'l: "XSoundProtocol1",
  'decimals': 0
},
{
  'address': "0xCD966B72CFF52Dc349089b6b6f5865B5743b4E08",
  'name': "TOMI",
  #'name'l: "TOMI",
  'decimals': 18
},
{
  'address': "0x1a3acf6D19267E2d3e7f898f42803e90C9219062",
  'name': "FXS",
  #'name'l: "Frax Share",
  'decimals': 18
},
{
  'address': "0x45c32fA6DF82ead1e2EF74d17b76547EDdFaFF89",
  'name': "FRAX",
  #'name'l: "Frax",
  'decimals': 18
},
{
  'address': "0x6002410dDA2Fb88b4D0dc3c1D562F7761191eA80",
  'name': "WORK",
  #'name'l: "The Employment Commons Work Token (PoS)",
  'decimals': 18
},
{
  'address': "0xf80F93350b18E5F896e7189533462D39E599416C",
  'name': "superbit",
  #'name'l: "superbit",
  'decimals': 18
},
{
  'address': "0x2058A9D7613eEE744279e3856Ef0eAda5FCbaA7e",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xcd353F79d9FADe311fC3119B841e1f456b54e858",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xcBF6f78981e63Ef813cb71852d72A060b583EECF",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x597A9bc3b24C2A578CCb3aa2c2C62C39427c6a49",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x2aF5Fdcbb712019cF84567Eef673722b6B13645c",
  'name': "ZXS1",
  #'name'l: "0xSound Protocol1",
  'decimals': 0
},
{
  'address': "0xF524d21316c69f50B46623a9773300B86FBe2e10",
  'name': "GRID",
  #'name'l: "GRID",
  'decimals': 18
},
{
  'address': "0xCdf59DE1d771E265aD8A1571532181e137258f44",
  'name': "CAT-LP",
  #'name'l: "PolyCat LP",
  'decimals': 18
},
{
  'address': "0xf8F9efC0db77d8881500bb06FF5D6ABc3070E695",
  'name': "SYN",
  #'name'l: "Synapse",
  'decimals': 18
},
{
  'address': "0x48cBc913dE09317dF2365e6827Df50dA083701D5",
  'name': "FOUR",
  #'name'l: "The 4th Pillar Token (PoS)",
  'decimals': 18
},
{
  'address': "0x0b502860B730BfAf5FA5566EC9996C53810Dfe08",
  'name': "DGold",
  #'name'l: "Dragon Gold Token",
  'decimals': 18
},
{
  'address': "0x5647Fe4281F8F6F01E84BCE775AD4b828A7b8927",
  'name': "MM",
  #'name'l: "Million (PoS)",
  'decimals': 18
},
{
  'address': "0x50204178a0b157653D86373a6a6fdb3563a8c6Fe",
  'name': "ANV",
  #'name'l: "Animvs Coin",
  'decimals': 18
},
{
  'address': "0x656E569983B74A76B9aEaA442F0650165F95997F",
  'name': "SHUN",
  #'name'l: "Shun Kakinoki",
  'decimals': 18
},
{
  'address': "0x152f4592d4Ac2A2791A16334fEa01f6543e858e5",
  'name': "blockgamer.net",
  #'name'l: "blockgamer",
  'decimals': 18
},
{
  'address': "0x16e0e254C56CdC9750bFcfca018a66Ff6cEf2D21",
  'name': "blockgamer.net",
  #'name'l: "blockgamer",
  'decimals': 18
},
{
  'address': "0x16eD7f0bBC2Fd950D12512f0b087905f1cBc831B",
  'name': "blockgamer.net",
  #'name'l: "blockgamer",
  'decimals': 18
},
{
  'address': "0x7EBD3636110FF4aE1A66204f04Ec596f95E797F1",
  'name': "Mayn",
  #'name'l: "MAYN",
  'decimals': 18
},
{
  'address': "0xA7305Ae84519fF8Be02484CdA45834C4E7D13Dd6",
  'name': "UFARM",
  #'name'l: "UNIFARM Token (PoS)",
  'decimals': 18
},
{
  'address': "0x1BD6FfDd7B3697C80B22262dA91C9fbed53924F7",
  'name': "TOI",
  #'name'l: "Toilet",
  'decimals': 18
},
{
  'address': "0x74da9ec8dA4d85Cd5341dBC3600A68525a07872c",
  'name': "BabyEth",
  #'name'l: "BabyEth",
  'decimals': 18
},
{
  'address': "0x2721bF55168E37C9E8298e18B4097cF5E5891238",
  'name': "GEM",
  #'name'l: "Moon Gem",
  'decimals': 18
},
{
  'address': "0x01080746938F2a63767730382e8b78551f111fFA",
  'name': "GEM",
  #'name'l: "Moon Gem",
  'decimals': 18
},
{
  'address': "0x0775d7C64fcB6DA6Fd855620dC3cB881461676Ba",
  'name': "GEM",
  #'name'l: "Moon Gem",
  'decimals': 18
},
{
  'address': "0xb3C5e27A79E9B21E1100eF5DB33a1B97a6A35825",
  'name': "GEM",
  #'name'l: "Moon Gem",
  'decimals': 18
},
{
  'address': "0xfad2f593cDF0d4197dd273DC67CAb34916136dBD",
  'name': "GEM",
  #'name'l: "Moon Gem",
  'decimals': 18
},
{
  'address': "0x24D270FB8d71aBE7bB160C7E849B516E56f84a09",
  'name': "NDG",
  #'name'l: "New DeFi Governance",
  'decimals': 18
},
{
  'address': "0xC2B6200a9ced47B12f95587f3e1E2640893a26D6",
  'name': "XWIN",
  #'name'l: "xWIN Token from BSC (PoS)",
  'decimals': 18
},
{
  'address': "0x9d8fc48620d4E6D26eDb09f38d0F0E8C6e41dfB6",
  'name': "polyFEG",
  #'name'l: "PolyFEG",
  'decimals': 18
},
{
  'address': "0xdAD97F7713Ae9437fa9249920eC8507e5FbB23d3",
  'name': "crvUSDBTCETH",
  #'name'l: "Curve USD-BTC-ETH",
  'decimals': 18
},
{
  'address': "0xE10f9Ee1c1a1d989214B777D2291719b69EF4a16",
  'name': "blockgamer.co",
  #'name'l: "BGT",
  'decimals': 18
},
{
  'address': "0x73DA7F257f6b306aE5A14E85b60FB36b5518A840",
  'name': "PUSD.USDC",
  #'name'l: "PUSD.USDC",
  'decimals': 18
},
{
  'address': "0x27170dD4a934985E5EeBA5b8d03Dda222fA75F60",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xc71819eEd89Dc2f667d4Ab3D2A8403bcD7667cec",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x6c3B2f402CD7d22AE2C319B9d2f16f57927a4A17",
  'name': "KRW",
  #'name'l: "KROWN",
  'decimals': 18
},
{
  'address': "0x95f91c82EdBa4D2B985f9435E3791191a4289F45",
  'name': "IPT",
  #'name'l: "Issuaa Protocol Token",
  'decimals': 18
},
{
  'address': "0x46D502Fac9aEA7c5bC7B13C8Ec9D02378C33D36F",
  'name': "WSPP",
  #'name'l: "WolfSafePoorPeople",
  'decimals': 18
},
{
  'address': "0x5617604BA0a30E0ff1d2163aB94E50d8b6D0B0Df",
  'name': "AX",
  #'name'l: "AthleteX",
  'decimals': 18
},
{
  'address': "0x581bc5a33ccD295571753F04353f0C6837600CC7",
  'name': "MAGIC",
  #'name'l: "MagicMatic",
  'decimals': 9
},
{
  'address': "0x8929D3FEa77398F64448c85015633c2d6472fB29",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xD4D2AF6d5aD25e0e228AffeFE583545667d95070",
  'name': "Enot",
  #'name'l: "EnotPoloskun",
  'decimals': 18
},
{
  'address': "0xb5106A3277718eCaD2F20aB6b86Ce0Fee7A21F09",
  'name': "pBREW",
  #'name'l: "CafeSwap Token",
  'decimals': 18
},
{
  'address': "0x0644558069A68C5f44FFC71768593503B7DccA02",
  'name': "PBNK",
  #'name'l: "Piggy Bank Rocket",
  'decimals': 18
},
{
  'address': "0xb7e47f973a4e9121421412B6258E7437892558aC",
  'name': "CYBEAR",
  #'name'l: "cybear.finance",
  'decimals': 18
},
{
  'address': "0xd9E838dd60c8ea1e7dD4E670913323bB87DB112c",
  'name': "EWT",
  #'name'l: "Ecowatt Token",
  'decimals': 4
},
{
  'address': "0xFcA32D718188F2d28E2B899534D2B29C95AF2AFb",
  'name': "sTOI",
  #'name'l: "USD Toilet",
  'decimals': 6
},
{
  'address': "0x2f535aE1A9f6405E9e6E2Ff10FdEd846358a5C39",
  'name': "LIBRA",
  #'name'l: "LIBRA Token",
  'decimals': 18
},
{
  'address': "0xa0b20DecBc557E3f68E140eD5a0c69bc865F865A",
  'name': "BREW",
  #'name'l: "CafeSwap Token",
  'decimals': 18
},
{
  'address': "0xFe28cF189764901A0A817b54F55fe2E47Df711Bb",
  'name': "REX",
  #'name'l: "REX",
  'decimals': 18
},
{
  'address': "0x013F9c3fAc3e2759d7e90AcA4F9540F75194A0d7",
  'name': "USDN",
  #'name'l: "Neutrino USD",
  'decimals': 18
},
{
  'address': "0x62a872d9977Db171d9e213A5dc2b782e72ca0033",
  'name': "NEUY",
  #'name'l: "NEUY (PoS)",
  'decimals': 18
},
{
  'address': "0xb0E98db756BE23CfBf65F2cAd063596429498E7E",
  'name': "XGCR",
  #'name'l: "X Galaxy Credit",
  'decimals': 18
},
{
  'address': "0x4fA83eD2140a07c75234f1433e7B165FBab76E35",
  'name': "CCLY",
  #'name'l: "CloudyCloud",
  'decimals': 18
},
{
  'address': "0xfd5962484BE2c3574D70131BF5D452CcC7C69F67",
  'name': "UCT",
  #'name'l: "Universal Community Trust (PoS)",
  'decimals': 18
},
{
  'address': "0xD4b42287F1EE04aF246aD792153C39D62733f826",
  'name': "UCTC",
  #'name'l: "UCT Cash (PoS)",
  'decimals': 18
},
{
  'address': "0x7aB857ae7D1495A4b8C07B1f02ef9e747460E9e2",
  'name': "DexCoin",
  #'name'l: "DexCoin",
  'decimals': 18
},
{
  'address': "0x33a394Bc15127D201A8942c82D2971c1e62d0296",
  'name': "crm",
  #'name'l: "CryptoMafia",
  'decimals': 18
},
{
  'address': "0x1cA31Da9D3d9b8E8F58572a47Ca87E83cf4C6fAD",
  'name': "SLM",
  #'name'l: "Solar Moon",
  'decimals': 18
},
{
  'address': "0xE79feAAA457ad7899357E8E2065a3267aC9eE601",
  'name': "WCHI",
  #'name'l: "Wrapped CHI (PoS)",
  'decimals': 8
},
{
  'address': "0x72DCE0e4d5467a4721e04ad9841c64c464b8B0c5",
  'name': "INFLUCOIN",
  #'name'l: "InfluCoin",
  'decimals': 18
},
{
  'address': "0x3AdD09F8A07216E1F389C145F2b725649c39bf90",
  'name': "TAX",
  #'name'l: "Tax Token",
  'decimals': 18
},
{
  'address': "0xaC3090B7042FCA2cDBF233022e4a9823a032600c",
  'name': "BETA",
  #'name'l: "PolyBeta Finance",
  'decimals': 18
},
{
  'address': "0xC8E616A6189FD5519e91968fb33CB66a45dbCBeB",
  'name': "HAKON",
  #'name'l: "Hakon",
  'decimals': 18
},
{
  'address': "0xF6a09deadF5A10aA7822d95e3228b2315De8f6fa",
  'name': "MM",
  #'name'l: "Mintopoly Money",
  'decimals': 8
},
{
  'address': "0xdc23Fa74A5434c55738D06EfEcF4E36ad02a058d",
  'name': "R1",
  #'name'l: "ER",
  'decimals': 9
},
{
  'address': "0x3B1A0c9252ee7403093fF55b4a5886d49a3d837a",
  'name': "UM",
  #'name'l: "Continuum",
  'decimals': 18
},
{
  'address': "0x7b910C6EF8C5C0370914198d93B36d9246B9F881",
  'name': "ZEUS",
  #'name'l: "Zeus",
  'decimals': 18
},
{
  'address': "0x34b3b039a2576136e27D525c58baBe637a409d9f",
  'name': "DELPHI",
  #'name'l: "Delphi Protocol",
  'decimals': 18
},
{
  'address': "0x31BBf2AFEe1F8D1e3C2e0D9C20Ed20E10ec8001c",
  'name': "HBG",
  #'name'l: "HarborBcg",
  'decimals': 18
},
{
  'address': "0x5b56A425F8b45D82EBB57dcA4F02528409ae763B",
  'name': "JustForFun",
  #'name'l: "JustForFun",
  'decimals': 4
},
{
  'address': "0x647a337036b448Bed2fF75f27789A73f6Ff56f3f",
  'name': "BuyItUp",
  #'name'l: "BuyItUp",
  'decimals': 4
},
{
  'address': "0xba2EB61a5D424d2E04E125A0A55d0D0D0b3bFE5D",
  'name': "ROCKET",
  #'name'l: "SOLANA ROCKET",
  'decimals': 18
},
{
  'address': "0xa561766078A1b7705b428025f4786B6D1E6410DE",
  'name': "AE",
  #'name'l: "AEUPHORAE.COM",
  'decimals': 18
},
{
  'address': "0x98689Df2a96dE1810e2CCeB8Bd8405ed7172B43E",
  'name': "KAI",
  #'name'l: "KAWAII",
  'decimals': 18
},
{
  'address': "0xDb982a636807B3ACD9FD28a99410B68c2159Fb32",
  'name': "THEOS",
  #'name'l: "THEOS (PoS)",
  'decimals': 18
},
{
  'address': "0x1258f64c4b7355B22876Bb3253b37d0c49615D1E",
  'name': "LOR",
  #'name'l: "Lord Finance LOR token",
  'decimals': 18
},
{
  'address': "0x70c006878a5A50Ed185ac4C87d837633923De296",
  'name': "REVV",
  #'name'l: "REVV",
  'decimals': 18
},
{
  'address': "0x84B71eb498D227A5Db2461e8cCC482c14Af37942",
  'name': "SOLR",
  #'name'l: "SolRazr",
  'decimals': 18
},
{
  'address': "0x8174b243559BB4A2742B6c9b4c4f2070FFfCC467",
  'name': "THEOS",
  #'name'l: "Theos",
  'decimals': 18
},
{
  'address': "0xbD2472EC2Cc4D9d37353CeAA840889a6B0c4BDe9",
  'name': "TPT",
  #'name'l: "Test Pool Token",
  'decimals': 18
},
{
  'address': "0xcBEA63B905d62bAd6506e2C47b1Ea00C56D8f93d",
  'name': "ARTM",
  #'name'l: "ARTM (PoS)",
  'decimals': 18
},
{
  'address': "0xcFB7d0825a5e91487c33Ff55B31EA1B099e3Ba60",
  'name': "MCK",
  #'name'l: "MarketCapKiller",
  'decimals': 18
},
{
  'address': "0x45A0e7bDE7702F650E8b9765D9148c4b9eda2994",
  'name': "D20",
  #'name'l: "D20Token",
  'decimals': 18
},
{
  'address': "0xAdC3D75c188FAAEAF46dE77cEc876354343D3c5b",
  'name': "GMF",
  #'name'l: "Gamefic",
  'decimals': 18
},
{
  'address': "0xba482e736B89e80Da1b66342BBC9dB9a380658b6",
  'name': "FUDX",
  #'name'l: "FUDX_Token",
  'decimals': 2
},
{
  'address': "0xE670FcF33C615dF18b78921c1C5fe930D42B31F4",
  'name': "AED",
  #'name'l: "Minima quidem nostru",
  'decimals': 18
},
{
  'address': "0x01B4da99B55a1e7D4747D01336FeB79462fB54FC",
  'name': "AED",
  #'name'l: "Harum dolor odit por",
  'decimals': 18
},
{
  'address': "0xF3a814c3C1B7DBE108eeF4bDB29c0266a2448a61",
  'name': "FJB",
  #'name'l: "FUCK JOE BIDEN",
  'decimals': 18
},
{
  'address': "0xa7051C5a22d963b81D71C2BA64D46a877fBc1821",
  'name': "EROWAN",
  #'name'l: "SifChain (erowan) (PoS)",
  'decimals': 18
},
{
  'address': "0xBAe01B1947D0B23C67E8D9572672d4b56D07b62D",
  'name': "TWETH",
  #'name'l: "Tokenised WETH",
  'decimals': 18
},
{
  'address': "0x21702FcfDEDa7826B4441214B6d45a40f44B6395",
  'name': "SBK",
  #'name'l: "Schrute Bucks",
  'decimals': 18
},
{
  'address': "0x5e1aE306ab94e83669d02bE3902820d8d99FCd41",
  'name': "SNK",
  #'name'l: "Stanley Nickels",
  'decimals': 18
},
{
  'address': "0x36FF415d0BcEdF976d60E85c72E01D19230FBd29",
  'name': "HOBO",
  #'name'l: "HoboNickels (PoS)",
  'decimals': 8
},
{
  'address': "0x07257926FFB64631F8FA303f217A52655b53Fd32",
  'name': "IMN",
  #'name'l: "Iman",
  'decimals': 18
},
{
  'address': "0x12f3aF493fF321A97E75648CF2cab5006735FFb0",
  'name': "TDOGE",
  #'name'l: "TestDoge#'name'",
  'decimals': 18
},
{
  'address': "0x229b1b6C23ff8953D663C4cBB519717e323a0a84",
  'name': "BLOK",
  #'name'l: "BLOK",
  'decimals': 18
},
{
  'address': "0x80789391b4028c23c7175ccB70DfdD6727cD0D4f",
  'name': "BEEBOOP",
  #'name'l: "Beeboop Token",
  'decimals': 18
},
{
  'address': "0x9929e0D059C12a0E9999461563da26270f209024",
  'name': "ASDD",
  #'name'l: "Vladimir Mooney",
  'decimals': 18
},
{
  'address': "0x06F41DDFF2f084DE0eAA78f89110ec69057ffDf7",
  'name': "TRT",
  #'name'l: "Kennedy Gardner",
  'decimals': 18
},
{
  'address': "0x300211Def2a644b036A9bdd3e58159bb2074d388",
  'name': "CIOTX",
  #'name'l: "Crosschain IOTX",
  'decimals': 18
},
{
  'address': "0x361A5a4993493cE00f61C32d4EcCA5512b82CE90",
  'name': "SDT",
  #'name'l: "Stake DAO Token (PoS)",
  'decimals': 18
},
{
  'address': "0x88a3aCAc5C48F93121d4d7771A068A1FCDE078BC",
  'name': "IVORY",
  #'name'l: "Ivory Token",
  'decimals': 18
},
{
  'address': "0xC4Df0E37e4ad3e5C6D1dF12d3Ca7Feb9d2B67104",
  'name': "KAVIAN",
  #'name'l: "KAVIAN Token",
  'decimals': 18
},
{
  'address': "0xe7c15C988528baE6E2C6961E394f0ad663e52CB5",
  'name': "GS50",
  #'name'l: "The-Eighty-Twenty",
  'decimals': 18
},
{
  'address': "0x46eF1DCDA4EeE8118D880adCb38a91d785dF2c1d",
  'name': "MIOU",
  #'name'l: "Minou",
  'decimals': 18
},
{
  'address': "0xC8a152B4f5F5921fe06699544952035ECc366544",
  'name': "PTK",
  #'name'l: "PoToken",
  'decimals': 18
},
{
  'address': "0x6d1f762cE9a613688eAF10e3687A9b6f103de0E2",
  'name': "EDD",
  #'name'l: "EDD",
  'decimals': 18
},
{
  'address': "0x4A63e2E882A436D01B0Fbc252dc081785c52c28c",
  'name': "polyGAS",
  #'name'l: "polyGAS",
  'decimals': 18
},
{
  'address': "0x544E6EcD77a7cEA194D806b6d624E6AA01e4821e",
  'name': "testGAS",
  #'name'l: "testGAS",
  'decimals': 18
},
{
  'address': "0x5fcb390B4422f4FF7940c23618A62BF5f69658A8",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x840B5FC8C6deE2b1140174a3ABdC215190426CCf",
  'name': "polyGAS",
  #'name'l: "polyGAS",
  'decimals': 18
},
{
  'address': "0xF9FFfb046CF17e78918bfEB2aee463e69FC1ab9a",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xcCBBA38E41d5428FD82cf42efE5385AEF6f80826",
  'name': "CQTF",
  #'name'l: "CryptoQuantumTradingFund (PoS)",
  'decimals': 18
},
{
  'address': "0xd8a2432946ffFe7FA33Ba69edd65874Bc9671771",
  'name': "DKBIT",
  #'name'l: "DARKBIT",
  'decimals': 0
},
{
  'address': "0xa0BadC7f4292B3745aee868964449926CCEcD567",
  'name': "NYAN",
  #'name'l: "PolyNYAN",
  'decimals': 18
},
{
  'address': "0x9EFF0AA8d3eE901fa71840AcA6a22e4Eca8Db67A",
  'name': "HEX",
  #'name'l: "Hexagon",
  'decimals': 18
},
{
  'address': "0xd2Bc8E8bE0Ded018FEB6c59c67D81bbF8B92AefE",
  'name': "OPQ",
  #'name'l: "OPAQUE",
  'decimals': 12
},
{
  'address': "0x6b7a87899490EcE95443e979cA9485CBE7E71522",
  'name': "ONE",
  #'name'l: "ONE",
  'decimals': 18
},
{
  'address': "0xEb935614447185eeea0aBC756Ff2ddC99FBB9047",
  'name': "aKLIMA",
  #'name'l: "AlphaKlima (PoS)",
  'decimals': 18
},
{
  'address': "0xa7608cC47Fb65811B030A1782E7D639BAe69F36C",
  'name': " BakeNomics",
  #'name'l: "The Bakery Nomics",
  'decimals': 10
},
{
  'address': "0x15eF8287DFe3993ec644eDD8Be7731F00b25f4f6",
  'name': "ESHIP",
  #'name'l: "ELONSHIP",
  'decimals': 8
},
{
  'address': "0x8403E89377FD2739b962098CC8a78f21c7315365",
  'name': "nesto od tri slova",
  #'name'l: "bilo sta",
  'decimals': 18
},
{
  'address': "0xB80419F2a9d3f4596D79E03711Fc37F8eE27a02F",
  'name': "SurgeInu",
  #'name'l: "Surge Inu",
  'decimals': 18
},
{
  'address': "0x30066Be0231F8B3929dE597B25DD47A251dBdFcf",
  'name': "JUICE",
  #'name'l: "Juice Token",
  'decimals': 18
},
{
  'address': "0x0d9D668c4AE1D64b859930dDCd8cD9539a80ac93",
  'name': "GANNIUM",
  #'name'l: "Gannium",
  'decimals': 18
},
{
  'address': "0xd50EC6360f560a59926216Eafb98395AC430C9fD",
  'name': "alKLIMA",
  #'name'l: "AlchemistKlima (PoS)",
  'decimals': 18
},
{
  'address': "0x7c28F627eA3aEc8B882b51eb1935f66e5b875714",
  'name': "PAINT",
  #'name'l: "Paint",
  'decimals': 18
},
{
  'address': "0x71e06EFC48bCd97f797294E05469E028c7a4967c",
  'name': "SPJ",
  #'name'l: "sultanproject",
  'decimals': 18
},
{
  'address': "0x314eE137b637AD72cfd800C1d17639EC5Df364d5",
  'name': "TFC",
  #'name'l: "Trust Finance Coin",
  'decimals': 8
},
{
  'address': "0x8201532917e55bA29674Ef4E88FFe0b775f1BaE8",
  'name': "TOWER",
  #'name'l: "Tower Stablecoin",
  'decimals': 18
},
{
  'address': "0x83D1fa6C5F6c60e6e4376914f2A30969a43B4540",
  'name': "imxB",
  #'name'l: "Impermax Borrowable",
  'decimals': 18
},
{
  'address': "0x487cb12b5F9a5f9ee87146700e9A7025b565f34a",
  'name': "ABC",
  #'name'l: "ABCToken",
  'decimals': 18
},
{
  'address': "0xa71399EBCeEFAb0bBFe446C07fF1aa514214d711",
  'name': "TP1",
  #'name'l: "TestPool1",
  'decimals': 18
},
{
  'address': "0xe031A5fA7C7da4aF92C8a077aBD85E6F0D08C0a1",
  'name': "TP0",
  #'name'l: "TestPool0",
  'decimals': 18
},
{
  'address': "0x54fF5918AE037fb1Cc73fcB0d4dd8c505f4AbFCF",
  'name': "ERV",
  #'name'l: "Doloribus fugit ani",
  'decimals': 18
},
{
  'address': "0x414639C2A8cE0F42d417E49FdEde6F355Cf42E42",
  'name': "TP2",
  #'name'l: "TestPool2",
  'decimals': 18
},
{
  'address': "0x6D7B10EB6a7376bD1f491807040C06704cdA0218",
  'name': "TP1",
  #'name'l: "TestPool1",
  'decimals': 18
},
{
  'address': "0x04387d8bADe6e08ea9644847736b6110350C45a1",
  'name': "TKN1",
  #'name'l: "Token1",
  'decimals': 18
},
{
  'address': "0x28A19e15536e0396319409D84dC65e097db4f649",
  'name': "TKN2",
  #'name'l: "Token2",
  'decimals': 18
},
{
  'address': "0x8fa31A802067c19E179803c42f7736e60BC9Aae8",
  'name': "TKN11",
  #'name'l: "Token11",
  'decimals': 18
},
{
  'address': "0xe67e5C17989Ba02F012b51f0C763814eC12A99EC",
  'name': "TKN22",
  #'name'l: "Token22",
  'decimals': 18
},
{
  'address': "0x2447603CB3eB35AE5e07B085813a71ba35CB131d",
  'name': "ALIENO",
  #'name'l: "ALIENO",
  'decimals': 18
},
{
  'address': "0x8cbb4D7310CA667ceDeCAfe4CFeE97c4b92e4a61",
  'name': "TKN111",
  #'name'l: "token111",
  'decimals': 18
},
{
  'address': "0x43C7E373C5c9B2f1334b9c518b4fc52ccc82528E",
  'name': "Test1234",
  #'name'l: "Test1234",
  'decimals': 18
},
{
  'address': "0xce4f7FC9f29B663087060BB3131E9171eFD2c806",
  'name': "TKN222",
  #'name'l: "Token222",
  'decimals': 18
},
{
  'address': "0x22D5dF224348321B65DCb14ff2bED72d4B6e5634",
  'name': "ELCT",
  #'name'l: "Electron Token",
  'decimals': 18
},
{
  'address': "0xC7B15937e06Ce7E09C58203c73FE3bA1ba2ec143",
  'name': "AFRT",
  #'name'l: "Functionality Rewards Token",
  'decimals': 18
},
{
  'address': "0x5118aeC3AfCca3f1e21733eE9C88BB800AFE6F7b",
  'name': "FLDG",
  #'name'l: "FledgeCoin",
  'decimals': 18
},
{
  'address': "0xB66eEA4f7541A54184F8c0b6BaAd780295C40a1e",
  'name': "BGT",
  #'name'l: "Cillum",
  'decimals': 18
},
{
  'address': "0x4479992fD2e4aB89b99A0eD12Bf8745a39fB602D",
  'name': "VFR",
  #'name'l: "Sit harum",
  'decimals': 18
},
{
  'address': "0x12a34A6759c871C4C1E8A0A42CFc97e4D7Aaf68d",
  'name': "TUT",
  #'name'l: "Tutellus token",
  'decimals': 18
},
{
  'address': "0x6500beaF1e846ce6f9d022dA3838570410C8CEEf",
  'name': "LGT",
  #'name'l: "Legendary Token",
  'decimals': 18
},
{
  'address': "0xb6d25D35ab5e0Ef3A93D64bEaD065FDEfA0bBdeB",
  'name': "$MATICX",
  #'name'l: "MATICX",
  'decimals': 4
},
{
  'address': "0x216F4fBbFdd1c40DFFa464d047231822Be21247f",
  'name': "CDE",
  #'name'l: "Explicabo",
  'decimals': 18
},
{
  'address': "0xC657Fa714069C36649e8F82aFb3eDEd89d8026d9",
  'name': "MTC",
  #'name'l: "matic clasic",
  'decimals': 18
},
{
  'address': "0xA41faE1b6224C2666C7aF632d85546Aef7754E2A",
  'name': "$MATICX",
  #'name'l: "MATICX",
  'decimals': 4
},
{
  'address': "0xc5666D43F06C073E869bce02407569f578B2072D",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xEe0B6f9d849007534c72Be3b15b734C356186262",
  'name': "SHIRO",
  #'name'l: "SHIRO",
  'decimals': 8
},
{
  'address': "0x596EF766472F1dA611726a49e8870dA4c29C794d",
  'name': "BBC",
  #'name'l: "BibouneCoin",
  'decimals': 18
},
{
  'address': "0xea69a42Fb203b5a501A072D3A33278c8D1C0CBdB",
  'name': "ZETC",
  #'name'l: "Zetuber Cred",
  'decimals': 18
},
{
  'address': "0x4A5bd73C00fafdcB9787DA75a4b6Cbf59735c6aC",
  'name': "MITTO",
  #'name'l: "mitto",
  'decimals': 9
},
{
  'address': "0x4EB033a22ee1D173EFcd808d5ea6152792814ecd",
  'name': "TACO",
  #'name'l: "TacoParty",
  'decimals': 18
},
{
  'address': "0xbAB63b0a21473Fb8E73f5E95dF5AE0BA530C6E6E",
  'name': "TWEET",
  #'name'l: "Tweet Coin",
  'decimals': 9
},
{
  'address': "0xFEc89b108DA58CC7259994b2655A1d1Fd228125E",
  'name': "KUBE",
  #'name'l: "Tetrakube",
  'decimals': 18
},
{
  'address': "0x9E349fD9D1b8f94069d58e5F7b0c6338BbA03F40",
  'name': "Dogma",
  #'name'l: "Dogmatic Token",
  'decimals': 18
},
{
  'address': "0xBe9Ab22B02b88a1e7C61DCFc2bC4A2d62A71B79C",
  'name': "wang",
  #'name'l: "wang",
  'decimals': 18
},
{
  'address': "0x6866BADbF6b25dfAdf40BDad00e73a84c9752e35",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0xC399F9311072FcA138AC748BA960AAdB356fb217",
  'name': "BCT",
  #'name'l: "BCT",
  'decimals': 18
},
{
  'address': "0x82f55cA7d7aAA521569AF34233e4724c21d1d609",
  'name': "5CNF",
  #'name'l: "CNFCNFY",
  'decimals': 9
},
{
  'address': "0xF99726A056d4b110983D456F28364F7194E362fE",
  'name': "ARASEL",
  #'name'l: "ARASEL",
  'decimals': 18
},
{
  'address': "0xb5846453B67d0B4b4Ce655930Cf6E4129F4416D7",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xF687A32AAF022c5fd8B2ad624C94969D41cF929F",
  'name': "SYR",
  #'name'l: "Syrian Gold",
  'decimals': 18
},
{
  'address': "0x9a05D1FF699ea187Dc8523E333eD63503f0d82db",
  'name': "BABYQUICK",
  #'name'l: "BABYQUICK",
  'decimals': 18
},
{
  'address': "0xc10358f062663448a3489fC258139944534592ac",
  'name': "BCMC",
  #'name'l: "Blockchain Monster Coin",
  'decimals': 18
},
{
  'address': "0x1B43b97094Aa3c6Cc678eDb9e28Ac67dAaa7Cc64",
  'name': "LICP",
  #'name'l: "Liquid ICP",
  'decimals': 18
},
{
  'address': "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0x374f333Afeb01eeE41A82101ed8c851E86932086",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x90e4cA67282DB86C416b5C763E403640c7E785F0",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xc3413C949D89Eb624Ae40Ad71935BaE268c4678f",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x6DBE2d55a1084467d5857EB3C4ce192b4ED146CA",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0xBdC4595b275cf72c722296CB789Bddc6d02A341F",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xcB858161Da3A680801859dF4d4Fd57Ad73C99470",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0xFBFBb4BDb471629a2eAE545f278B31F681b3CeE9",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x33d6EafBE9995956379B3cFfac5B704Fed98856B",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xce48D936cBD889f1C0529687d0494a5025cA1e91",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x36e601E7467f786210E206c37B8B577cd0ADB6EF",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xEd9C478adf6bF0367919B88A21Fe965F4DFA9EaE",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x4Fce68bf7F59383Fa7d31119d740E673e344e26a",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x90feCB74837ed715D1b58881a1e7b0091DfDf7d2",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x4aC458227494471914df5340ca9417A7F18f1E09",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xB1A300b35f4555851d950Ff398F6161bA5997342",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x2523d0Ff3B269e570A290b76eD1bF3D3ffEe824c",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xa8d4332cDEb9a6508E6e1e0141a0a2511f168EDd",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x5D695691Db7B8b396f01D9C4D940dC8Aca8F4C64",
  'name': "KGDLC",
  #'name'l: "davecoin",
  'decimals': 18
},
{
  'address': "0x67dA532D10A4292D82C5d2E5c0D4aB9C97a052e7",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xDCC511D907fF950296ceb3fEB598bE2aaf14292b",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x025087b4Dc77e0F976B6941329a7E83F62406709",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x08f5d1B426FC0810A4e9496C4f7F60abdDD19A79",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x5375c8f1012d8Ac37d5A230ba8Bfd0495616c3d1",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xAa1d3b7DA5Ea612696E22a96EeB6096d46794F4F",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x319907aA2Db2e41A6c879AA5055E508CDDa4cc2b",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x3F6721208a8013228a423072CbfC63a6ADcf703C",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0xb8e349D82Af62d782e177064589007d722621823",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0xe7B9394f61C290d559c40B29cD971E3341bAE3f0",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0xDbf3F13f1211b100Ac88C8603705822511e5E9c0",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0x2F800Db0fdb5223b3C3f354886d907A671414A7F",
  'name': "BCT",
  #'name'l: "Toucan Protocol: Base Carbon Tonne",
  'decimals': 18
},
{
  'address': "0x4e78011Ce80ee02d2c3e649Fb657E45898257815",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0x6e0fEDd1196fe11Bf7fC1d3BFb293118C0d9105b",
  'name': "$PKT",
  #'name'l: "PolyKiwi",
  'decimals': 18
},
{
  'address': "0xaAa3C00D6D768FBb4059a0C4C6fD7b8baf89f062",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0xFf7D71e753A7fF48003177972D648841ACFad55E",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x648199CC93539A87e18dCa92Fcd268E093D8E483",
  'name': "TOB",
  #'name'l: "TokenBomb",
  'decimals': 18
},
{
  'address': "0xcB8BCDb991B45bF5D78000a0b5C0A6686cE43790",
  'name': "WEIRD",
  #'name'l: "Weird (PoS)",
  'decimals': 18
},
{
  'address': "0x5187816A80A61B67b9879AEA87eA0890A493396b",
  'name': "CORIS",
  #'name'l: "CorgiSwap",
  'decimals': 18
},
{
  'address': "0x2bBB98FB2a0D9D86b79506Ef7A1EEA456345F97f",
  'name': "imxB",
  #'name'l: "Impermax Borrowable",
  'decimals': 18
},
{
  'address': "0x827ad315960F5a0f5280D6936C8E52A5878bBa04",
  'name': "B-50QI-50BAL",
  #'name'l: "Balancer 50 QI 50 BAL",
  'decimals': 18
},
{
  'address': "0x95EC757F837b44f4f412660F0722f443a567f4ff",
  'name': "GAS",
  #'name'l: "GasToken",
  'decimals': 2
},
{
  'address': "0x83C92e1a4a824CD42F94012B7b50AFf372E4d25f",
  'name': "CMI",
  #'name'l: "Cryptocurrency Market Index",
  'decimals': 18
},
{
  'address': "0x0d5B7Df582f22bCa58702e1a414D29886554896B",
  'name': "K1",
  #'name'l: "K1",
  'decimals': 9
},
{
  'address': "0x5dC39530B3C04a7c2DcB88fE7Ca71611Cd916a6b",
  'name': "B1",
  #'name'l: "B1",
  'decimals': 18
},
{
  'address': "0x373f9453b67BF371BBab84CE3B59D0Cf9f31D721",
  'name': "K2",
  #'name'l: "K2",
  'decimals': 9
},
{
  'address': "0xfCC6B89a91fE73E18DCaA1Bac01C9ab1bB197E28",
  'name': "B2",
  #'name'l: "B2",
  'decimals': 18
},
{
  'address': "0x883C80B52E574df443D797EE222eCCd730054a6C",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0xa1428174F516F527fafdD146b883bB4428682737",
  'name': "SUPER",
  #'name'l: "SuperFarm (PoS)",
  'decimals': 18
},
{
  'address': "0x4767da4eEf50C354785Ac87f6Cc39D68749044Bc",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x580a27b4d5a63C608e56665e6c1Cd06224854B47",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x77453eAfC58E715ab5AB3f884048Eaf976922D42",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x83fA348C5368649AD019b848B734bEF32f4351e4",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x163D1300eB0f089393FC58c1EF26aC4482CEC6C7",
  'name': "SELL",
  #'name'l: "Sell Token",
  'decimals': 18
},
{
  'address': "0x807771ecF7ae17c23a7A57B484DE7cF1F6d231c2",
  'name': "BUY",
  #'name'l: "Buy Token",
  'decimals': 18
},
{
  'address': "0x14643e422Ba977FE24308fEBCE567FE861891711",
  'name': "TKN",
  #'name'l: "Token",
  'decimals': 18
},
{
  'address': "0x62De998c9FCC824Ac6Fd9bCaFB43eEb91C52C5A6",
  'name': "CS",
  #'name'l: "Coin-Storage ",
  'decimals': 8
},
{
  'address': "0xF9DAeBc34E2C0e937fc9ac431E550B9e3b63fAA8",
  'name': "6DG",
  #'name'l: "Six",
  'decimals': 6
},
{
  'address': "0xA063dc00e7a8626bA66bc256fADab7e336c68622",
  'name': "FIN",
  #'name'l: "Final",
  'decimals': 18
},
{
  'address': "0xE530ECfA005F61B2b98666aED976378f25EF4BA3",
  'name': "MDM",
  #'name'l: "MEDIUM",
  'decimals': 18
},
{
  'address': "0xc609EbC5b5E27F66A233709b55ff80FBfb008B49",
  'name': "EDG",
  #'name'l: "SD",
  'decimals': 6
},
{
  'address': "0x989080019F0eeA6492Af6232231873Cc60cf5696",
  'name': "FIN",
  #'name'l: "Final",
  'decimals': 18
},
{
  'address': "0xEA5BD5f1046aE0C3A38a75aA1636F0800847E6Aa",
  'name': "MDM",
  #'name'l: "Medium",
  'decimals': 18
},
{
  'address': "0x9842470655DeC5558B09B08afa214DcAB71C2CD1",
  'name': "token1",
  #'name'l: "token1",
  'decimals': 18
},
{
  'address': "0xbFe8C642A19B5fF6A6098829fe0f1d006B85cd0b",
  'name': "token2",
  #'name'l: "token2",
  'decimals': 9
},
{
  'address': "0x8a72fEc7d1a8275e68027107e113dB23Ab6522a9",
  'name': "ICE",
  #'name'l: "ICE (Iron Titan V2)",
  'decimals': 18
},
{
  'address': "0x3d00CF331b04E5b8b69deb0644C756DF5C180359",
  'name': "token1",
  #'name'l: "token1",
  'decimals': 18
},
{
  'address': "0xDaa7B0d19e35c3E7b5080ffA6D28afb8137F0f24",
  'name': "token2",
  #'name'l: "token2",
  'decimals': 9
},
{
  'address': "0x040a96e3a789D3CAE523415B3F6213D3a7dD8753",
  'name': "MDM",
  #'name'l: "Medium",
  'decimals': 18
},
{
  'address': "0x39f737cFC6c0fB5D70Fe7977565674734F4430e3",
  'name': "FIN",
  #'name'l: "Final",
  'decimals': 18
},
{
  'address': "0x316f7e305334eFE9aD6c7161B9CF74C0e19C260d",
  'name': "TEST",
  #'name'l: "Tester",
  'decimals': 18
},
{
  'address': "0x71E38F1829ca127CfA6fc1be4858DEB650412035",
  'name': "TEST2",
  #'name'l: "Tester2",
  'decimals': 18
},
{
  'address': "0x852F6bE1f8808A5e6Fb68d72593E5B6e5aD2D663",
  'name': "DMT",
  #'name'l: "Demo Token",
  'decimals': 18
},
{
  'address': "0x08A74AEBFb4860C8b479b44265d3b81209675A47",
  'name': "MYTOK",
  #'name'l: "MyToken",
  'decimals': 18
},
{
  'address': "0xd10852DF03Ea8b8Af0CC0B09cAc3f7dbB15e0433",
  'name': "FLUX",
  #'name'l: "Flux Protocol",
  'decimals': 18
},
{
  'address': "0xef3aF9dFEA19Dd9892ae6C57BE973FB390991530",
  'name': "XIAZ2",
  #'name'l: "Xiazfinance2",
  'decimals': 18
},
{
  'address': "0x5F5454a575e35318647A8EEC4667E57Cc064a60C",
  'name': "testOne",
  #'name'l: "testOne",
  'decimals': 18
},
{
  'address': "0x69Fa0458aFC20a1407b71f846B37e75fc0bF9C4a",
  'name': "Nonari",
  #'name'l: "Nonari Token",
  'decimals': 18
},
{
  'address': "0x273945e8e56C01C8689fa7F1f2878DE9B6FD62d5",
  'name': "K3",
  #'name'l: "K3",
  'decimals': 9
},
{
  'address': "0xBD59D80F636F202964Df7E72B3e997D6ac6C176e",
  'name': "B3",
  #'name'l: "B3",
  'decimals': 18
},
{
  'address': "0x2CF374cDe24177F78748AD5fD31af07C9258a100",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x81fD22e36f2784a913A633Ef0C4545A43D5B357B",
  'name': "YPT",
  #'name'l: "yptest",
  'decimals': 18
},
{
  'address': "0x335882721129DDd058d5d1733691c6757EB83709",
  'name': "YPA",
  #'name'l: "yptest",
  'decimals': 18
},
{
  'address': "0x430705A284fBeC14f4B3c48a2dB7Faa90fC85f6A",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0xA71B42ea89e0D735B59b9099ae8983Eb903764C6",
  'name': "BCT",
  #'name'l: "BCT Test",
  'decimals': 18
},
{
  'address': "0xb34a61dd00883eC224415B80F409435f25c03341",
  'name': "SHMUPI",
  #'name'l: "Shmupi Coin",
  'decimals': 18
},
{
  'address': "0xbB32e503338b38BF9485cFf60A4794C496e7A35A",
  'name': "B5",
  #'name'l: "B5",
  'decimals': 18
},
{
  'address': "0xf32d7543b91525d2A47424E4d7A460F9Dd358293",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xF9B065f0B6e467da7FE3Ca166c6029fA0e264079",
  'name': "K5",
  #'name'l: "K5",
  'decimals': 9
},
{
  'address': "0x8FaD0da05bFaC68bb50c1bEAF876A53d8C24A816",
  'name': "B6",
  #'name'l: "B6",
  'decimals': 18
},
{
  'address': "0xE95c57Ae66a787Be863DE52751b4126078BEAe22",
  'name': "K6",
  #'name'l: "K6",
  'decimals': 9
},
{
  'address': "0x51421cdE59283Eb59958167A1d4d90AFb018d896",
  'name': "SOAPKLIMA",
  #'name'l: "SoapKlima",
  'decimals': 18
},
{
  'address': "0xcDe6e773A11F76A12bF89697bFE753D803e3cEB2",
  'name': "SOAPKLIMA",
  #'name'l: "SoapKlima",
  'decimals': 18
},
{
  'address': "0xc14F8d18aFd1DdD7AE309be5CAC723297FAB18F7",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0x6Ad8E4A96d11f1f28b8131bC238cC4312e72Abf6",
  'name': "SOAPKLIMA",
  #'name'l: "SoapKlima",
  'decimals': 18
},
{
  'address': "0xe258ACEa1C667c72498247ac75cE2B8a67950f53",
  'name': "",
  #'name'l: "",
  'decimals': 18
},
{
  'address': "0x85467E24870d04deb9507A520034e071B6047283",
  'name': "SOAPKLIMA2",
  #'name'l: "SoapKlima",
  'decimals': 18
},
{
  'address': "0x9E443800AA0F56Fc9864E369e3Bd80202b28da33",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x6B0845DCEB6CaabE382736Bd6c5E9a423bA7B000",
  'name': "ZUBI",
  #'name'l: "ZUBI Coin",
  'decimals': 18
},
{
  'address': "0xc7Fbb6DeCE6De00Ec04743ddAE55168ce571e414",
  'name': "",
  #'name'l: "",
  'decimals': 18
},
{
  'address': "0x127b511F1e9e3595fF555a9356908d93268591A0",
  'name': "",
  #'name'l: "",
  'decimals': 18
},
{
  'address': "0x4cE8485608F78921Fbc0F96e63c0566B1b176Db0",
  'name': "LARK",
  #'name'l: "Lark Token",
  'decimals': 18
},
{
  'address': "0xf257d9da5FbA029020Df0FAFeCd61Be4FfcE776D",
  'name': "tcoin2",
  #'name'l: "tcoin2",
  'decimals': 18
},
{
  'address': "0xF8c10504bcfc9733330e7FcB70d9fE0D1BB3083F",
  'name': "tcoin1",
  #'name'l: "tcoin1",
  'decimals': 18
},
{
  'address': "0x109Bf9e09D9e13e05b2D6411cAF559623Cc5148f",
  'name': "tcoin3",
  #'name'l: "tcoin3",
  'decimals': 18
},
{
  'address': "0x88808296CB0FA67679DA69621CCFDd9F530a11b5",
  'name': "tcoin4",
  #'name'l: "tcoin4",
  'decimals': 18
},
{
  'address': "0x554f074d9cCda8F483d1812d4874cBebD682644E",
  'name': "$ANRX",
  #'name'l: "AnRKey X (PoS)",
  'decimals': 18
},
{
  'address': "0x0ae11155765ABF28136046d5c8091aEc3C891318",
  'name': "eighteen",
  #'name'l: "eighteen",
  'decimals': 18
},
{
  'address': "0xA16dce5D6FECB27ca43E234cf9799bA000953732",
  'name': "six",
  #'name'l: "six",
  'decimals': 6
},
{
  'address': "0x2918E2CD30AE1b0fA4DDAe093B79bc7E96aaB3b5",
  'name': "nine",
  #'name'l: "nine",
  'decimals': 9
},
{
  'address': "0xeA42Cc4002841c4D9a6fb0E89d342aFf2Dfc6F9E",
  'name': "BT",
  #'name'l: "BIII Token",
  'decimals': 18
},
{
  'address': "0x6EFb5F9d28FACACdCb39E8B7AD87668b3496BB42",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0xb68E1Db2675516e5fBF11f03563e9A9DF0d9B2b3",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0xe455Eca0C2E172B0cDE8282c63F3f9df516C1ff7",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 9
},
{
  'address': "0xfE40bE28b837883647e14d9Cc7dbB5456eA55BEC",
  'name': "BCT",
  #'name'l: "Toucan Protocol: Base Carbon Tonne",
  'decimals': 9
},
{
  'address': "0xfa014Ea4D4eE0a92f1dB0D58DFE01858C10fFdf1",
  'name': "TESTKLIMA",
  #'name'l: "TestKlima",
  'decimals': 18
},
{
  'address': "0xA76715f5Da7974036F62b695cf3092224c3b30E9",
  'name': "KLIMA",
  #'name'l: "KLIMA",
  'decimals': 18
},
{
  'address': "0x7861Ea4E33A50302aAE8726DeeD5f1D3774ef840",
  'name': "KLIMA",
  #'name'l: "KLIMA",
  'decimals': 18
},
{
  'address': "0x6EC07416938B359533820b5b37aA05F32Cb5532B",
  'name': "BCT",
  #'name'l: "Toucan Protocol: Base Carbon Tonne",
  'decimals': 18
},
{
  'address': "0xb81a417b4382c941541232D6739D450F1FB988cE",
  'name': "KLIMA",
  #'name'l: "KDAO",
  'decimals': 18
},
{
  'address': "0xD561030476F3e338E4f82a1c3c1C32054ABc6be5",
  'name': "BCT",
  #'name'l: "BCT",
  'decimals': 18
},
{
  'address': "0x6A3aCa82e78f20B11aa55A706c0266bfc5F7Ff35",
  'name': "BCT",
  #'name'l: "BCT",
  'decimals': 18
},
{
  'address': "0xb101EaE6694b6F35703552Ee43158b8E8296d67b",
  'name': "KLIMA",
  #'name'l: "Klima DAO",
  'decimals': 18
},
{
  'address': "0xe9e051957470E0499eb4577C5B8E961D822C7513",
  'name': "",
  #'name'l: "",
  'decimals': 18
},
{
  'address': "0xf81A07d962c8Bc972FD8a3bB771E8C4B2ed6f8B2",
  'name': "Ax",
  #'name'l: "AxTest",
  'decimals': 18
},
{
  'address': "0xe9993763E0B7f7d915A62A5f22A6E151F91d98A8",
  'name': "TORG",
  #'name'l: "TORG (PoS)",
  'decimals': 18
},
{
  'address': "0x211331A95DAA2899B9076e9D4f762840A40d0dE9",
  'name': "QAZ",
  #'name'l: "Coffee time",
  'decimals': 18
},
{
  'address': "0x95C4bECfD3a55909116b5835dccceD520De7EB34",
  'name': "tCYN Token",
  #'name'l: "tCYN",
  'decimals': 18
},
{
  'address': "0xDAA8bbA9Cfdb35238CBfEA428177f61818C4f500",
  'name': "tUSDT Token",
  #'name'l: "tUSDT",
  'decimals': 18
},
{
  'address': "0xfC1F944DC80D13072d41975445ca80A8160cF776",
  'name': "ttELC",
  #'name'l: "Everlasting Cash Test",
  'decimals': 18
},
{
  'address': "0x22b9E25aae9980666924019279763e66f9fC6689",
  'name': "BLK",
  #'name'l: "Black",
  'decimals': 18
},
{
  'address': "0x839F1a22A59eAAf26c85958712aB32F80FEA23d9",
  'name': "AXN",
  #'name'l: "Axion",
  'decimals': 18
},
{
  'address': "0x6811079E3c63ED96Eb005384d7E7ec8810E3D521",
  'name': "xSUSHI",
  #'name'l: "SushiBar (PoS)",
  'decimals': 18
},
{
  'address': "0x0bd54539fBDD584CCBa3a255142f1e607C8b4f7a",
  'name': "DYP",
  #'name'l: "Decryptocol",
  'decimals': 18
},
{
  'address': "0x1607fC872e20692b9E51fA73eBc836C1608D6E9c",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x98d0274895a6187e095859D80B6A1248a7FEFB98",
  'name': "XMN",
  #'name'l: "Metronotes",
  'decimals': 9
},
{
  'address': "0x7596745BaCD9743B69e9F04b577588019a39107A",
  'name': "WOAH",
  #'name'l: "Woahbit",
  'decimals': 18
},
{
  'address': "0xE04c20C176cE8be0E2231A0D28d6558EFD9396FA",
  'name': "DSK",
  #'name'l: "Desk",
  'decimals': 18
},
{
  'address': "0xa351Dae051ba08c2FDb7fAf88DC0582AEED289C8",
  'name': "ttELC",
  #'name'l: "Everlasting Cash Test",
  'decimals': 18
},
{
  'address': "0xd63568e4bcb3d32C928E243E2bdB9E272d748A06",
  'name': "ICP-20",
  #'name'l: "Wrapped ICP",
  'decimals': 18
},
{
  'address': "0xA9536B9c75A9E0faE3B56a96AC8EdF76AbC91978",
  'name': "PECO",
  #'name'l: "Polygon Ecosystem Index",
  'decimals': 18
},
{
  'address': "0x34965ba0ac2451A34a0471F04CCa3F990b8dea27",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x56F483CF2f1F6cf224656647CA0a0D11BFB0404E",
  'name': "WRVL",
  #'name'l: "Wrapped RavenCoin Lite",
  'decimals': 18
},
{
  'address': "0x78D056FCd0ae4613406ffA51E4BA40175C00E551",
  'name': "TRE",
  #'name'l: "TRE",
  'decimals': 18
},
{
  'address': "0x10a716E0D771356A25dcA180F27d2a48dAFb80Fd",
  'name': "ROF",
  #'name'l: "RoseFinance",
  'decimals': 10
},
{
  'address': "0xC957A20B3d9580Ead5a08DF1dC25802122027EF1",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xC177Ea5fE7B53B86B76F1ceB758aDc3b0f5757C4",
  'name': "99VB",
  #'name'l: "99Vitaliks",
  'decimals': 0
},
{
  'address': "0x77f18fA1bb7FaC839575eF71e8E322ef0784331d",
  'name': "TEST2",
  #'name'l: "ImpermaxTest2",
  'decimals': 18
},
{
  'address': "0x9dA1F82C6D158Ec39d11F6bd74232B60B47f869c",
  'name': "TEST1",
  #'name'l: "ImpermaxTest1",
  'decimals': 18
},
{
  'address': "0x353a52787CFcdcB5358ea5155612E263Be992f49",
  'name': "Stoken",
  #'name'l: "SToken",
  'decimals': 18
},
{
  'address': "0xf01650FE5e8e852E8a82C908D705346A174B48C9",
  'name': "CT8",
  #'name'l: "CHTEST468",
  'decimals': 18
},
{
  'address': "0xEe9801669C6138E84bD50dEB500827b776777d28",
  'name': "O3",
  #'name'l: "O3 Swap Token",
  'decimals': 18
},
{
  'address': "0x848ac25A632143E0D5cb52A538dE965155c72201",
  'name': "WRP",
  #'name'l: "Warp",
  'decimals': 18
},
{
  'address': "0xC25351811983818c9Fe6D8c580531819c8ADe90f",
  'name': "IDLE",
  #'name'l: "Idle (PoS)",
  'decimals': 18
},
{
  'address': "0xf9DbC7E0435B24600c57E9e605248AB54b5467e2",
  'name': "BNZ",
  #'name'l: "Beanz",
  'decimals': 18
},
{
  'address': "0x7A6Da55fa0620Ecb3B5dF20f4b73D1526BCDCDF8",
  'name': "PRF",
  #'name'l: "Portafilter",
  'decimals': 18
},
{
  'address': "0x8fD4715236702EBA9E5A4Ee41257334809ECEd4A",
  'name': "CLB",
  #'name'l: "Cold Brew",
  'decimals': 18
},
{
  'address': "0xdb986Dc13E1023d02E7cb582Ef53034f8Fc8B378",
  'name': "CIA",
  #'name'l: "Crypto Investor Agency",
  'decimals': 18
},
{
  'address': "0xb89fd55ef1EA71560469d55637Ef9c2770d4830D",
  'name': "FLAG",
  #'name'l: "For Loot And Glory",
  'decimals': 18
},
{
  'address': "0x86995070BE5EcfA2850cc42Ba0358D98966f3203",
  'name': "mELC",
  #'name'l: "(Matic) Everlasting Cash",
  'decimals': 18
},
{
  'address': "0xc8b6Af292136591A7Cb795cf30752BD7EF100Ff2",
  'name': "BKYC",
  #'name'l: "BluekeyCash",
  'decimals': 18
},
{
  'address': "0xD2e1cD904D1903C3746fA4BdF02e3dCD01c4548c",
  'name': "EKARTINU",
  #'name'l: "eKart Inu",
  'decimals': 9
},
{
  'address': "0x481882fc2F9ED02D3d23C822042657F52924F3a5",
  'name': "IMT",
  #'name'l: "Idle Mystic",
  'decimals': 9
},
{
  'address': "0x24239bBC3e0E09999e67B1194830De479829D2db",
  'name': "IMT",
  #'name'l: "Idle Mystic",
  'decimals': 18
},
{
  'address': "0x10FEaE6eC36752acAB8c391cA65a900a49aeFa75",
  'name': "RGH",
  #'name'l: "Rughoo",
  'decimals': 18
},
{
  'address': "0xf93fFB0831192C12333F7880761a89aAAa65703A",
  'name': "LUDR",
  #'name'l: "LuckyDragon",
  'decimals': 18
},
{
  'address': "0xE97a60f5D34dA4f68bc1f1b9CE2C19Ec1A33E928",
  'name': "HGH",
  #'name'l: "Matic Mike Juice",
  'decimals': 18
},
{
  'address': "0x16B690166e8794da396D9fefCA5A5D0334C1E3DB",
  'name': "ASW",
  #'name'l: "Autumn Davidson",
  'decimals': 18
},
{
  'address': "0x63DCF0F818d0969AE28eBF4e4afF70326541f47f",
  'name': "CMVE",
  #'name'l: "Certification Membership Value Element",
  'decimals': 8
},
{
  'address': "0x4D0B3893009807Ec88Ec0737c6658f6148597778",
  'name': "WBB",
  #'name'l: "Wrapped Bitblocks",
  'decimals': 8
},
{
  'address': "0x396EF6350C02D19c08774b05A4F7652F01734fb8",
  'name': "HAVEN",
  #'name'l: "Havencoin",
  'decimals': 18
},
{
  'address': "0x8b8E89fdB1Ec4696c604FCFEbeD2740E4c727900",
  'name': "KTEST",
  #'name'l: "KTEST",
  'decimals': 18
},
{
  'address': "0xA334CB72E228a8eC1d3A4eDE7E80f34c7aDf861b",
  'name': "JTEST",
  #'name'l: "JTEST",
  'decimals': 18
},
{
  'address': "0xb93c7F7Ae99799B95Aabd702251d37D0Ae42d5EC",
  'name': "JTEST2",
  #'name'l: "JTEST2",
  'decimals': 18
},
{
  'address': "0xB1b901793B5B702835d6975B0C94004c794824D7",
  'name': "HD",
  #'name'l: "Hroapye Demo",
  'decimals': 18
},
{
  'address': "0xa64551dd4f4202131e9261573956915749025DF9",
  'name': "HUCK",
  #'name'l: "Huckstermoon",
  'decimals': 9
},
{
  'address': "0x2a70bC8F3DC23b98FC105aA0f34803D9C94B6909",
  'name': "IPT",
  #'name'l: "Index Pool Token",
  'decimals': 18
},
{
  'address': "0x6fEd28D59C3957Ced3eBfb76989f0cb6fafE77fF",
  'name': "FLT",
  #'name'l: "Filter",
  'decimals': 18
},
{
  'address': "0x61F344492cbbDF28057EF7e0D8EF2DC420fd481B",
  'name': "CFR",
  #'name'l: "Coffee Fire",
  'decimals': 18
},
{
  'address': "0x9BbeE7aEC9DBbF4249A3a7B3806d07d7935D0251",
  'name': "AAA",
  #'name'l: "Macy Drake",
  'decimals': 18
},
{
  'address': "0x0802d874aE67C7e2EdD17dA716d4c5495be8E53A",
  'name': "FBR",
  #'name'l: "Fuzzy Bunny Radio",
  'decimals': 18
},
{
  'address': "0x1309Fea39E1f959B6323a1283aD18F7766Bd181d",
  'name': "TEST",
  #'name'l: "-------",
  'decimals': 18
},
{
  'address': "0x7F85c5912017B3cA506a57dc577946C2cF22d2cA",
  'name': "TEST",
  #'name'l: "-------",
  'decimals': 18
},
{
  'address': "0x13D866772e5E14B787773c5E04C59d73bd9dfB03",
  'name': "CLXN",
  #'name'l: "Colexion",
  'decimals': 18
},
{
  'address': "0x76df17E2Ac56ba739Ce374dd23eCcFa863fB4902",
  'name': "ZEE",
  #'name'l: "Zee Coin",
  'decimals': 18
},
{
  'address': "0xCf557Cdb4f8AA2Ae99bF545b78d61BD50ef8A0B8",
  'name': "TEST",
  #'name'l: "-------",
  'decimals': 18
},
{
  'address': "0x76502d5FB8698Ae5387cFfda2DB3B6B69D7bf976",
  'name': "BDCL",
  #'name'l: "BirdCastle",
  'decimals': 18
},
{
  'address': "0x3232b3E785aAEa5493Fb587558be3eBeE6153512",
  'name': "TST",
  #'name'l: "--------",
  'decimals': 18
},
{
  'address': "0xDE4567BcE0bc89027ee3e58F2d2eA2c388979fEF",
  'name': "TST",
  #'name'l: "--------",
  'decimals': 18
},
{
  'address': "0xB1F72bfaD7221e570Cc89c13C9CC1f5173BD608b",
  'name': "TST",
  #'name'l: "--------",
  'decimals': 18
},
{
  'address': "0x7485Db7d8AF6aEC7cAba737C46E7AF3458027d12",
  'name': "TST",
  #'name'l: "--------",
  'decimals': 18
},
{
  'address': "0xbF6a7180d6E59e2fA87bC83CF6531e365Be9a1B2",
  'name': "TST",
  #'name'l: "--------",
  'decimals': 18
},
{
  'address': "0x76D9984F9437c26810CDaEad81CBC6bE21Fc5139",
  'name': "TST",
  #'name'l: "--------",
  'decimals': 18
},
{
  'address': "0x3a874e6fE844B0Bf48d796e26B07AE59FF1c7C89",
  'name': "oct2",
  #'name'l: "27oct2",
  'decimals': 18
},
{
  'address': "0x6aAeb1E5e1D8BE82dAA518B0e7697B535Ac0f27d",
  'name': "123Q",
  #'name'l: "1234Q",
  'decimals': 18
},
{
  'address': "0x93f5C42dad0E4b0c82279a9BAfbC5d6d5567FA0A",
  'name': "oiu",
  #'name'l: "oiu",
  'decimals': 18
},
{
  'address': "0x9dED3117008251F66714743Df461b24a6c30ACAe",
  'name': "PPP",
  #'name'l: "Hayley Valenzuela",
  'decimals': 18
},
{
  'address': "0xf96010Ef1f6F1E41e3505F3ca0d9b05F225F41Ad",
  'name': "rew",
  #'name'l: "rew",
  'decimals': 18
},
{
  'address': "0x4163Ea7C612585D3b669ef7eCcEB713A6E02C5A4",
  'name': "TEST",
  #'name'l: "-------",
  'decimals': 18
},
{
  'address': "0x0d08960051aE9DC6667E5dD4A5436dDCB1AAF891",
  'name': "ASD",
  #'name'l: "Tamekah Randolph",
  'decimals': 18
},
{
  'address': "0x99bC02451830abD90316269Db2e929A93BBCe6dB",
  'name': "PLP",
  #'name'l: "Cara Lawrence",
  'decimals': 18
},
{
  'address': "0x41A5903dCCF9C3C6329dc50109C902B513F46B82",
  'name': "TEST",
  #'name'l: "TEST Token",
  'decimals': 18
},
{
  'address': "0x9b230644ED4F12B52f52B709741E477D70545d2D",
  'name': "TEST1",
  #'name'l: "TEST Token",
  'decimals': 18
},
{
  'address': "0x529A824025083fd08A7D52d0bB3e17c60396939f",
  'name': "BabyDoge",
  #'name'l: "Baby Doge Coin",
  'decimals': 9
},
{
  'address': "0xCC73A0a9dcDa525f054bd53E2b08d408890f0A8D",
  'name': "TEST1",
  #'name'l: "TEST Token",
  'decimals': 18
},
{
  'address': "0x0b3006F5a3B3822Fd1713D30f4f3dB5e930F00c0",
  'name': "TEST",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0x4fA43A983466DDA2FcA21dd19c4456A2B1C1b857",
  'name': "Burner",
  #'name'l: "Burner Project",
  'decimals': 18
},
{
  'address': "0xC4Ff66070Ca8A750D7dF350C48Eed46559fFb1d8",
  'name': "TEST22",
  #'name'l: "TEST22 Token",
  'decimals': 18
},
{
  'address': "0x9e7d09C2183D0D3d6072E394600dAF22b4B26bD6",
  'name': "TTT",
  #'name'l: "TTT",
  'decimals': 18
},
{
  'address': "0xCb5e0207CfcC22f2a479EDB52F28e6d119D85D27",
  'name': "TTT",
  #'name'l: "TTT",
  'decimals': 18
},
{
  'address': "0xC6B43A306462d4a2bB5fD1D05246A5F615395183",
  'name': "TTT",
  #'name'l: "TTT",
  'decimals': 18
},
{
  'address': "0xb5f7DFca98788256569BdCEC6a413b4F2D819737",
  'name': "TEST22",
  #'name'l: "TEST22 Token",
  'decimals': 18
},
{
  'address': "0x39361BCc613Fee3a564515c440Da3A6D4AFE05Ae",
  'name': "VDI",
  #'name'l: "Volcano DeFi INDEX",
  'decimals': 18
},
{
  'address': "0x8917b0360A46bBD09cca71e3DB78268437db2f34",
  'name': "SAND",
  #'name'l: "SAND",
  'decimals': 18
},
{
  'address': "0x182f1d39dF9460D7AEf29afBc80bBD68ED0A41d5",
  'name': "RUUF",
  #'name'l: "RuufCoin",
  'decimals': 18
},
{
  'address': "0x64Bc251b0EB9200948C9155573Cd459C5E17C6a4",
  'name': "SIPLEAN",
  #'name'l: "Leancoin",
  'decimals': 18
},
{
  'address': "0x8f9E8e833A69Aa467E42c46cCA640da84DD4585f",
  'name': "CHAMP",
  #'name'l: "NFT Champions",
  'decimals': 8
},
{
  'address': "0x6eC7061775Da542a5eDcb2699Ee7f11B0FF8F205",
  'name': "RUGINU",
  #'name'l: "The One Inu",
  'decimals': 18
},
{
  'address': "0x50e4DA8fdb40FAD433222D6eE64A7A07c7F7eF32",
  'name': "SPINU",
  #'name'l: "Spooky Inu",
  'decimals': 18
},
{
  'address': "0x92A9C92C215092720C731c96D4Ff508c831a714f",
  'name': "RAILPOLY",
  #'name'l: "RAIL Polygon",
  'decimals': 18
},
{
  'address': "0x21364671fD823BBda8Ba1f40a24171DeCBdB3D54",
  'name': "TREATS",
  #'name'l: "Shibies Treats",
  'decimals': 18
},
{
  'address': "0xe7946921c619F5D9E8f28E3A5B4d218e9520dD11",
  'name': "st-ICP",
  #'name'l: "Staked ICP",
  'decimals': 18
},
{
  'address': "0xb0C22d8D350C67420f06F48936654f567C73E8C8",
  'name': "sKLIMA",
  #'name'l: "Staked Klima",
  'decimals': 9
},
{
  'address': "0xa751193E645e2c94a142243Ce05e5b5e825B918a",
  'name': "BabyDoge",
  #'name'l: "BabyDoge",
  'decimals': 9
},
{
  'address': "0x3096eD4607619e5845419C6036fDb6FBc98c6BD3",
  'name': "BabyDoge",
  #'name'l: "BabyDoge",
  'decimals': 9
},
{
  'address': "0x8f3c8E9a04d0029f48720d604996093d96e5361e",
  'name': "BabyDoge",
  #'name'l: "BabyDoge",
  'decimals': 9
},
{
  'address': "0x159478459cE7F554Db1a3D499Bd31479Dc9cE9df",
  'name': "BabyDoge",
  #'name'l: "BabyDoge",
  'decimals': 9
},
{
  'address': "0x323BA6a606928785a0d0368ed9DdB455413c8788",
  'name': "ASA",
  #'name'l: "Mira Vinson",
  'decimals': 18
},
{
  'address': "0x4Cb58E92a26bb40284E8d5D70cFE1dC8EB75aC31",
  'name': "ALGB",
  #'name'l: "Algebra Token",
  'decimals': 18
},
{
  'address': "0xad2C1f065923B66030009CE9A32505e6e7E2ad2E",
  'name': "ADS",
  #'name'l: "Maggie Steele",
  'decimals': 18
},
{
  'address': "0x7e80BA2Ad217bC85c5A671A883E4Ed14673D763A",
  'name': "ALGB",
  #'name'l: "Algebra",
  'decimals': 18
},
{
  'address': "0xfeFeDdeF6e8c05561195710a4B78682DB482A53C",
  'name': "AAS",
  #'name'l: "Roth Whitaker",
  'decimals': 18
},
{
  'address': "0x3040D67d5a4F06a04332Ec8300e469217c5FE0ED",
  'name': "AVA",
  #'name'l: "Deanna Butler",
  'decimals': 18
},
{
  'address': "0x6506AAED329c5ba3ac1aF2c9F24471d69B323DfE",
  'name': "ASA",
  #'name'l: "Latifah Slater",
  'decimals': 18
},
{
  'address': "0xB26aEE3f23F740db776Ab02505c3ed7B5243b3B1",
  'name': "PIS",
  #'name'l: "Pamela Pollard",
  'decimals': 18
},
{
  'address': "0xf275BF779e6629ecc47E5e0F5C60ec1034800478",
  'name': "LOLCAT",
  #'name'l: "LOLCAT Token",
  'decimals': 18
},
{
  'address': "0x0169eC1f8f639B32Eec6D923e24C2A2ff45B9DD6",
  'name': "ALGB",
  #'name'l: "Algebra",
  'decimals': 18
},
{
  'address': "0x003dE7C042585Ee1450F5a8b14E416c207f44FEb",
  'name': "TAG",
  #'name'l: "Xandra Keith",
  'decimals': 18
},
{
  'address': "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
  'name': "unknown",
  #'name'l: "unknown",
  'decimals': 0
},
{
  'address': "0xe7102f60E8328CEC3Cc4EeFC8FE857f0Fd0404f1",
  'name': "GZ",
  #'name'l: "GodZilla",
  'decimals': 9
},
{
  'address': "0xaF8950CdF6a8de31dda0Ceeaae118cBB386aD95D",
  'name': "GZ",
  #'name'l: "GodZilla",
  'decimals': 9
},
{
  'address': "0xcaCc59E28df7811a8AC83a49F124B76ee95e70C6",
  'name': "CONGO",
  #'name'l: "CONGOCOIN",
  'decimals': 12
},
{
  'address': "0x97c3C801B21Dc4D53CB99Fc3f3Bf8dC08977Cd48",
  'name': "VSF",
  #'name'l: "Amir Lucas",
  'decimals': 18
},
{
  'address': "0x3d36e5914C87EFE0C02EF7BAf14fcd4ca4f94602",
  'name': "987",
  #'name'l: "29oct-2",
  'decimals': 18
},
{
  'address': "0xc48F61a288A08F1B80c2edd74652e1276B6A168c",
  'name': "GYSR",
  #'name'l: "Geyser (PoS)",
  'decimals': 18
},
{
  'address': "0xaE3B1643C5ef861568dc0F4BFb573c908813F1D1",
  'name': "uhf",
  #'name'l: "oct29-8",
  'decimals': 18
},
{
  'address': "0x7Bf1E8E529390b5692Ac1058A60A321c0Aa4Ba7e",
  'name': "Prae",
  #'name'l: "Nora Gates",
  'decimals': 18
},
{
  'address': "0xA988BF725e30Fd2B8ffD8732C307816a1D068E74",
  'name': "ujf",
  #'name'l: "oct29-9",
  'decimals': 18
},
{
  'address': "0x0E0fFD047A4c0795c5a849dB75aBd367Bb92aEB5",
  'name': "bjo",
  #'name'l: "29oct-10",
  'decimals': 18
},
{
  'address': "0xF854225cAAef5a722884a68a23215dFa5386751E",
  'name': "wXLM",
  #'name'l: "Wrapped Stellar Lumens",
  'decimals': 18
},
{
  'address': "0x10Dd3DdD92bB5484F77d496860a4Cb4c1A49e838",
  'name': "SDS",
  #'name'l: "Hermione Lyons",
  'decimals': 18
},
{
  'address': "0xC72827bf75df95FF1c2d48A9C092b5aa4CFD3D6c",
  'name': "TB/Year",
  #'name'l: "DeNet Storage Payments",
  'decimals': 18
},
{
  'address': "0x627F699300A9D693FBB84F9Be0118D17A1387D4e",
  'name': "ZTEST",
  #'name'l: "ZTEST",
  'decimals': 18
},
{
  'address': "0xB1F1287e8A10dfbF48607D0b55eb91b69F250284",
  'name': "CSV",
  #'name'l: "Signe Calhoun",
  'decimals': 18
},
{
  'address': "0x6DDd1cc0a0eBc635A4169D010d75bE510469BAce",
  'name': "BDH",
  #'name'l: "Leandra Rodriguez",
  'decimals': 18
},
{
  'address': "0x40D03a16fD11e03eCaEBD7C81FE3D5285A826153",
  'name': "P3N",
  #'name'l: "Poin Tok3n",
  'decimals': 18
},
{
  'address': "0x3cd35BE361007D12290F0cF0d4D68a635918666A",
  'name': "VDV",
  #'name'l: "Virginia Pratt",
  'decimals': 18
},
{
  'address': "0xA99cf31b7f04EE76C27BbD30C9770703D0F5C3af",
  'name': "PON",
  #'name'l: "POLYGON Beplay",
  'decimals': 18
},
{
  'address': "0xe4e8d9CfD123699a040219165E22Fa912D47147b",
  'name': "PONA",
  #'name'l: "POLYGON Beplay PONA",
  'decimals': 18
},
{
  'address': "0xc48AE82ca34C63887b975F20ABA91a38f2a900B8",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x855D4248672a1fCE482165e8DBE1207b94b1968a",
  'name': "WOW",
  #'name'l: "WOWswap",
  'decimals': 18
},
{
  'address': "0xa115066c6d305aE60D06dFDed4661a44B0BB01F5",
  'name': "PAYT",
  #'name'l: "PAy Token",
  'decimals': 18
},
{
  'address': "0xb9b4F753336e85EDF5205b392d0ea3E4902bf23b",
  'name': "META AGE? ",
  #'name'l: "Meta Age",
  'decimals': 9
},
{
  'address': "0xC0A003db55D0888D7e0ecc189196d0E369A838D9",
  'name': "GZL",
  #'name'l: "GODZILA",
  'decimals': 18
},
{
  'address': "0x3D5D79a0adE77d10D0Eb993624a89F126DE6e30B",
  'name': "SAT",
  #'name'l: "Satoshi",
  'decimals': 18
},
{
  'address': "0xcE62CD6279E8eDf254025ced6DbA7fd30dabca22",
  'name': "MATRIX",
  #'name'l: "PolyMatrix",
  'decimals': 18
},
{
  'address': "0xC8614bEAB1Fb6e93FF56C36A960b03d93CdF205b",
  'name': "ddd",
  #'name'l: "Donny",
  'decimals': 18
},
{
  'address': "0xE8EBfBD31ACF4BAD293c44e2D260227F245b4153",
  'name': "bch5",
  #'name'l: "Oliver Rasmussen",
  'decimals': 18
},
{
  'address': "0xdDE1607262Ec88a25E218B7BC907a02Da79B2cD2",
  'name': "MTC",
  #'name'l: "MATIC CLASIC",
  'decimals': 18
},
{
  'address': "0x6393c0a63712601e3Dda577dc5Bfaf0189e89169",
  'name': "$BANANA",
  #'name'l: "Bored Banana Token (PoS)",
  'decimals': 0
},
{
  'address': "0x3Abfdb2C164F2fBA1C58B4D3714e7D9Ccd04EA2b",
  'name': "Norm",
  #'name'l: "Clinton Russell",
  'decimals': 18
},
{
  'address': "0xf0059CC2b3E980065A906940fbce5f9Db7ae40A7",
  'name': "ULT",
  #'name'l: "Shardus (PoS)",
  'decimals': 18
},
{
  'address': "0x9626240D53D329Ce837e607e320E8262B2Df2953",
  'name': "SHIT",
  #'name'l: "Shit Coin",
  'decimals': 6
},
{
  'address': "0xeA2746bE6cf47f376e9B9D6b78A47707559C3A8E",
  'name': "FLOF",
  #'name'l: "Floflis",
  'decimals': 18
},
{
  'address': "0x8eEF5a82E6Aa222a60F009ac18c24EE12dBf4b41",
  'name': "TXL",
  #'name'l: "Tixl Token",
  'decimals': 18
},
{
  'address': "0x92868A5255C628dA08F550a858A802f5351C5223",
  'name': "BRIDGE",
  #'name'l: "Cross-Chain Bridge Token",
  'decimals': 18
},
{
  'address': "0x5f0197Ba06860DaC7e31258BdF749F92b6a636d4",
  'name': "1FLR",
  #'name'l: "Flare Token",
  'decimals': 18
},
{
  'address': "0x20D6d0a7Ae3F4337D0d64fAb71820d9Bf69728AA",
  'name': "POLYSHIB",
  #'name'l: "POLYSHIBA INU",
  'decimals': 18
},
{
  'address': "0x604d917178EE0Fbf54A7bE78cc03370848244e92",
  'name': "Biz",
  #'name'l: "Biz",
  'decimals': 18
},
{
  'address': "0x2Bb2eF50c53E406c80875663C2A2e5592F8a3ccc",
  'name': "nSTABLE",
  #'name'l: "Polly nStable Nest",
  'decimals': 18
},
{
  'address': "0x337d063E74EdaA0B8A21F948575fE00B3363a138",
  'name': "DYFI",
  #'name'l: "DYnamicDeFi",
  'decimals': 9
},
{
  'address': "0xb82b16b767dFE5417e3c1199ECd02cADF74aC214",
  'name': "$GGWT",
  #'name'l: "Gigawatt",
  'decimals': 18
},
{
  'address': "0xFe8AE2A8fC4517fcA01aA2e2A660E400360b94Ed",
  'name': "$GGWT",
  #'name'l: "Gigawatt",
  'decimals': 18
},
{
  'address': "0x6571253Daf919232058e4d8a28E3C462e22315aD",
  'name': "IMT",
  #'name'l: "IdleMystic",
  'decimals': 9
},
{
  'address': "0xc08e94e12ca1357DF36F3c16c3A1df5F84c7B801",
  'name': "$GGWTT",
  #'name'l: "Gigawatt Token",
  'decimals': 18
},
{
  'address': "0xDa5949544aAf6124D06F398BFdE4C86Cc33B0Ee7",
  'name': "CYFM",
  #'name'l: "CyberFM Radio",
  'decimals': 18
},
{
  'address': "0x8b90aAfEBcca131e2bED2B0562A0BC4456B6e373",
  'name': "BILU",
  #'name'l: "Billu Coin",
  'decimals': 18
},
{
  'address': "0x4259Abc22981480D81075b0E8C4Bb0b142be8EF8",
  'name': "FRUIT",
  #'name'l: "FRUITARIAN",
  'decimals': 18
},
{
  'address': "0xf62E61bAd5EB0aDbDE048CAF5036a82FDCA6B331",
  'name': "wRUNES",
  #'name'l: "Wrapped Runes",
  'decimals': 18
},
{
  'address': "0x17757dcE604899699b79462a63dAd925B82FE221",
  'name': "GRAPE",
  #'name'l: "Grape Token",
  'decimals': 18
},
{
  'address': "0x8Ee3cADB135487a987774f69B4782860809E4d45",
  'name': "MML_TEST",
  #'name'l: "memos.live",
  'decimals': 18
},
{
  'address': "0x15A7347C7b0cE900f05C457b3C6add18cc9E486C",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0xF953975b3d959614588EcEAab5A3Db462aA93FFC",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x8c9aAcA6e712e2193acCCbAC1a024e09Fb226E51",
  'name': "GBNT",
  #'name'l: "GammaBountyToken",
  'decimals': 18
},
{
  'address': "0x20e787875e49BB829bDE42A87899bc2737aebae6",
  'name': "CATGIRL",
  #'name'l: "Cat Girl",
  'decimals': 9
},
{
  'address': "0xe82808eaA78339b06a691fd92E1Be79671cAd8D3",
  'name': "PLOT",
  #'name'l: "PlotX",
  'decimals': 18
},
{
  'address': "0x8b1f836491903743fE51ACd13f2CC8Ab95b270f6",
  'name': "ACY",
  #'name'l: "ACY (PoS)",
  'decimals': 18
},
{
  'address': "0xb2dB86EAbf950AdE945FA742986a3d8943d362FA",
  'name': "BITORB",
  #'name'l: "Bitorbit",
  'decimals': 18
},
{
  'address': "0x9aFe6f40401509FbEc3ac261416052e9d416a3F2",
  'name': "PCZZ",
  #'name'l: "polygon-czz",
  'decimals': 8
},
{
  'address': "0x1FA720d686A3F7A12Bc1Ea3cf4a10Da78Fb0bb4B",
  'name': "SRGD",
  #'name'l: "Studio Releasing Gold",
  'decimals': 1
},
{
  'address': "0x3b6dF03C777a9A549021b4F91b142B2c19a27944",
  'name': "Nequ",
  #'name'l: "Drake Atkins",
  'decimals': 18
},
{
  'address': "0x416289c5337F77DA763f1a8a83Cf76437B4239B7",
  'name': "ETS",
  #'name'l: "Eternals",
  'decimals': 18
},
{
  'address': "0x723B17718289A91AF252D616DE2C77944962d122",
  'name': "GAIA",
  #'name'l: "GAIA Everworld",
  'decimals': 18
},
{
  'address': "0xE9d5f7df8Ff1f7c509B3D9BCBb1F41EFFB3100a0",
  'name': "plka",
  #'name'l: "poolka",
  'decimals': 18
},
{
  'address': "0x14b0deFa66f1E0E072c5944c8CB3CC06896558f2",
  'name': "SSC",
  #'name'l: "StarStock Coin",
  'decimals': 18
},
{
  'address': "0xbD553E8adDb835dA97Bc84Ba2AA391F8001D01dC",
  'name': "cr7",
  #'name'l: "CR7",
  'decimals': 8
},
{
  'address': "0x43caf166bBA355a69A051efc4D01235757265460",
  'name': "ICE",
  #'name'l: "Trae Young PSA 10",
  'decimals': 18
},
{
  'address': "0x726f339349DD48b8a27dF9dcE337c24Dc92b32EE",
  'name': "DONSOU",
  #'name'l: "DONSOU Token",
  'decimals': 4
},
{
  'address': "0xab40Be25545B7BA0957E114BF18f233B0198Aa18",
  'name': "DogeDorah",
  #'name'l: "DogeDorah",
  'decimals': 9
},
{
  'address': "0x297b1B6f4308855B9937122766020fd449Dcb8B2",
  'name': "METROCHI",
  #'name'l: "METROCHI",
  'decimals': 18
},
{
  'address': "0xc3A32D7A1EaB69c146742ecb309B4fcD422F58B3",
  'name': "METROQUICK",
  #'name'l: "METROQUICK",
  'decimals': 18
},
{
  'address': "0x37c33D87796B8D88e8DC2E23AaD99A0F2cb2bfe5",
  'name': "Quo",
  #'name'l: "Tasha Gibbs",
  'decimals': 18
},
{
  'address': "0x945370078b33aFA9278DD309d343F6fd52550188",
  'name': "Sed",
  #'name'l: "Sade Owen",
  'decimals': 18
},
{
  'address': "0xf9c1F70f9bF57FAD5f63c6E1E25C2e895f04c0A6",
  'name': "DHC",
  #'name'l: "DeltaHub Community",
  'decimals': 18
},
{
  'address': "0xD501E2d348a53003951A87cA3e135357bE753538",
  'name': "WEN",
  #'name'l: "Wen Lambo",
  'decimals': 18
},
{
  'address': "0x2D78680fD510711549838Da691D80934b7De1352",
  'name': "Volu",
  #'name'l: "Chastity Collins",
  'decimals': 18
},
{
  'address': "0xd9180afA2FAEDf2335498ECf1a0b902B0c7dD07C",
  'name': "Et a",
  #'name'l: "Jacob Burch",
  'decimals': 18
},
{
  'address': "0x400a1f342175a6FCF2345b2f695326BA38e02e00",
  'name': "234",
  #'name'l: "Holly Oneil",
  'decimals': 18
},
{
  'address': "0xFB9591F6570a128E0E48b0e38bbbC9F9cD20Ce08",
  'name': "DDD",
  #'name'l: "Jorden Juarez",
  'decimals': 18
},
{
  'address': "0x76AE10DAe9f12B68fBdDf5cf0b7C03f7633BCE73",
  'name': "Susc",
  #'name'l: "Xenos Briggs",
  'decimals': 18
},
{
  'address': "0x1796ae0b0fa4862485106a0de9b654eFE301D0b2",
  'name': "PMON",
  #'name'l: "Polychain Monsters",
  'decimals': 18
},
{
  'address': "0xD3EEDa0A1A99213a56701dAf4B0377c70bec9589",
  'name': "ALKEMA",
  #'name'l: "Alkema Token",
  'decimals': 18
},
{
  'address': "0x8DF24859ea9e85bec4cb2E065b4550D9B84473C9",
  'name': "GEM",
  #'name'l: "Moon Gem",
  'decimals': 18
},
{
  'address': "0x32dCE20dB785EFC3C58085986941D366EF6a497b",
  'name': "fGEM",
  #'name'l: "fake - Moon Gem",
  'decimals': 18
},
{
  'address': "0x8b42Bc396cE039f29d9Fa41A415b2b87Da64b049",
  'name': "fGEM",
  #'name'l: "fake - Moon Gem",
  'decimals': 18
},
{
  'address': "0xee5Dcd70825cDE536Dcd0817552D9E459217D357",
  'name': "fGEM",
  #'name'l: "fake - Moon Gem",
  'decimals': 18
},
{
  'address': "0xdE6815308909bc3d8d6Aa9C937Dd6Ba906f8DC5D",
  'name': "fGEM",
  #'name'l: "fake - Moon Gem",
  'decimals': 18
},
{
  'address': "0x0F53Dae34fB237dFaa28CE5946A11FF2409a444D",
  'name': "fGEM",
  #'name'l: "fake - Moon Gem",
  'decimals': 18
},
{
  'address': "0x19060Debf62343eA2B641ca7f69aEaebFdCdD9A9",
  'name': "ZUPTA",
  #'name'l: "ZUPTA",
  'decimals': 18
},
{
  'address': "0x6e348eB38867173E641692Cd92276207563F9335",
  'name': "S&C",
  #'name'l: "Sina",
  'decimals': 18
},
{
  'address': "0xc5Ccd27F14826faca78C88D36e355eCc79229Aac",
  'name': "LUX",
  #'name'l: "Lux Coin",
  'decimals': 18
},
{
  'address': "0x893039Ed96EE53c87221d27346561273a90e25f9",
  'name': "WoW_sina",
  #'name'l: "Sina",
  'decimals': 18
},
{
  'address': "0xc9CD4D820c5a2B5ee40AEA77a5744290C4BD964D",
  'name': "WoW_sina",
  #'name'l: "Sina",
  'decimals': 18
},
{
  'address': "0x4C2C04E6f0ec30EbD60b2fFbE11814C3d59910f7",
  'name': "NGN",
  #'name'l: "Crypto Nijigen",
  'decimals': 10
},
{
  'address': "0xDB66d51505a09403a242F3F99747Fe9606E26131",
  'name': "INS",
  #'name'l: "InsaneNet",
  'decimals': 18
},
{
  'address': "0x61054426e16883Aa7A00Da604E7561E7521D1B96",
  'name': "USV",
  #'name'l: "Universal Store of Value",
  'decimals': 9
},
{
  'address': "0x98599248e05930Fbe17E004c3BEA2AF91abcCA80",
  'name': "Cons",
  #'name'l: "Stuart Barlow",
  'decimals': 18
},
{
  'address': "0x102F4CD0Bf6e9c608c49d76eA373D1a7542f910a",
  'name': "TGD",
  #'name'l: "Gabriel Cain",
  'decimals': 18
},
{
  'address': "0x1221a875ea2Af00e7b919A2e51CFc6b6B805a780",
  'name': "Omn",
  #'name'l: "Palmer Sargent",
  'decimals': 18
},
{
  'address': "0x011Ca6e693fDB81B79cd3c6844a59c155C4C8C07",
  'name': "RICO",
  #'name'l: "RICO CORP",
  'decimals': 18
},
{
  'address': "0x36aAEd85555d5525CCE76760E394041f8B43dC83",
  'name': "FT",
  #'name'l: "FerrariToken",
  'decimals': 18
},
{
  'address': "0x4dF071FB2D145bE595b767f997C91818694A6CE1",
  'name': "MRCH",
  #'name'l: "MerchDAO (PoS)",
  'decimals': 18
},
{
  'address': "0x0Fc7353934025a564c993b8623308Db92c01A99F",
  'name': "Quig",
  #'name'l: "Oleg Rowe",
  'decimals': 18
},
{
  'address': "0x57c7583dBbf2eD1fc26B819531C814Fd8db8cC9F",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x4F6cbacA3151f7746273004Fd7295933a9b70E69",
  'name': "WHIRL",
  #'name'l: "OmniWhirl",
  'decimals': 18
},
{
  'address': "0xd97803C320c30090845c21eBB6218a2985385a12",
  'name': "JeffCoin",
  #'name'l: "JeffCoin",
  'decimals': 18
},
{
  'address': "0x0A5926027d407222F8fe20f24cB16e103f617046",
  'name': "NFD",
  #'name'l: "Feisty Doge NFT (PoS)",
  'decimals': 18
},
{
  'address': "0x0168373fC1d72158b7032c9029298cF4C790748C",
  'name': "GUMMY",
  #'name'l: "Grape-up Yummy",
  'decimals': 18
},
{
  'address': "0x76fC20573e3D9EE3a71eD4083940290eD1f418bB",
  'name': "GU2TASTY",
  #'name'l: "Grape-up Double Tasty",
  'decimals': 18
},
{
  'address': "0x4A0279BEb59bB7Aa4D7B82994857A8400912646F",
  'name': "GUICEPOP",
  #'name'l: "Grape-up Ice Pop",
  'decimals': 18
},
{
  'address': "0xB4dD79877D63F701132907a7515086d72eC25720",
  'name': "GUMMY",
  #'name'l: "Grape-up Yummy",
  'decimals': 18
},
{
  'address': "0xA93C437090662AAbee4B1A7b2f903c852D3D6E74",
  'name': "GU2TASTY",
  #'name'l: "Grape-up Double Tasty",
  'decimals': 18
},
{
  'address': "0x1c144b730BE17D89c35291F7Dab557fCDf4b536D",
  'name': "GUICEPOP",
  #'name'l: "Grape-up Ice Pop",
  'decimals': 18
},
{
  'address': "0xCe3a42Db43096Bd5D6908E76C7857eD51bdEd024",
  'name': "GUFEST",
  #'name'l: "Grape-up Festival",
  'decimals': 18
},
{
  'address': "0x60dA560d481006fb9A3845499897F028622a9aE4",
  'name': "GUJET",
  #'name'l: "Grape-up Turbo Jet",
  'decimals': 18
},
{
  'address': "0x959CfdE6C6A3b815a0bFD039C6b34E362517b5F9",
  'name': "GUFORT",
  #'name'l: "Grape-up Fortress",
  'decimals': 18
},
{
  'address': "0xf2437ea99D3893807c0318dC3c08A69C92b087A3",
  'name': "GUIMP",
  #'name'l: "Grape-up Imperial",
  'decimals': 18
},
{
  'address': "0x9403af92611411A7Af207f482Dc4Ba4030bC663f",
  'name': "GUDMD",
  #'name'l: "Grape-up Diamond",
  'decimals': 18
},
{
  'address': "0xdE2409f81F0053e18557729145E7C777905c0C5a",
  'name': "GURUBY",
  #'name'l: "Grape-up Ruby",
  'decimals': 18
},
{
  'address': "0x655212E4514b28bCCd5B4f2785B5b791Dc4f86Bf",
  'name': "HYPERTET",
  #'name'l: "HYPERTET",
  'decimals': 18
},
{
  'address': "0x51869836681BcE74a514625c856aFb697a013797",
  'name': "GENESIS",
  #'name'l: "Genesis",
  'decimals': 18
},
{
  'address': "0x1Ba9457401579e7cf28eFc5062F34564E27204bC",
  'name': "Com",
  #'name'l: "Idona Conley",
  'decimals': 18
},
{
  'address': "0x0bD820aD2d7Ab7305b5C9538ba824C9b9bEb0561",
  'name': "ROYA",
  #'name'l: "Royale (PoS)",
  'decimals': 18
},
{
  'address': "0xE8B1e9b12b5fa9E249f1D57FA92bacA2E7bc0B61",
  'name': "CFC",
  #'name'l: "CSi Founders Coin Series",
  'decimals': 18
},
{
  'address': "0x6276BcE3B7313Bc6D7aE795A8Eae365075b25acf",
  'name': "SHELTR",
  #'name'l: "Shelter",
  'decimals': 6
},
{
  'address': "0x06eD7375C33499967cc436FDbcDA874f294838A2",
  'name': "taotest5",
  #'name'l: "taotest5",
  'decimals': 18
},
{
  'address': "0xE0339c80fFDE91F3e20494Df88d4206D86024cdF",
  'name': "ELON",
  #'name'l: "Dogelon (PoS)",
  'decimals': 18
},
{
  'address': "0xC82857E4571Fe5799ab664576DD8c94f64c521f6",
  'name': "Aliq",
  #'name'l: "Talon Hudson",
  'decimals': 18
},
{
  'address': "0xcc04408489834459C692A4BB256a5F8083ff876f",
  'name': "DON",
  #'name'l: "Donnie",
  'decimals': 18
},
{
  'address': "0xfE8CA33f7eB02b70def3fa4C34e632Ab8e059AFb",
  'name': "DON",
  #'name'l: "Donnie",
  'decimals': 18
},
{
  'address': "0x050c0B20eEE7F1268A3C915B89B46BA6c52E36dC",
  'name': "CSL",
  #'name'l: "CSi Lab series",
  'decimals': 18
},
{
  'address': "0x8FEE55071515a40d8f7885E36874EeEa83FDb59c",
  'name': "IPT",
  #'name'l: "Index Pool Token",
  'decimals': 18
},
{
  'address': "0x385c2a99678178bBa7eaE3ec4f64AeD702F44CaF",
  'name': "Corp",
  #'name'l: "Ayanna Klein",
  'decimals': 18
},
{
  'address': "0xaEe7F88ef1356b48F2E160E4e008214ce9295647",
  'name': "Veli",
  #'name'l: "Hillary Cantrell",
  'decimals': 18
},
{
  'address': "0x9e29FB7F906F576451439546133Bb67Ef44573a0",
  'name': "Quis",
  #'name'l: "Connor Bentley",
  'decimals': 18
},
{
  'address': "0x6641eB633656640BA16628fbC343F50Db364e6e1",
  'name': "IMX",
  #'name'l: "Immutable X (PoS)",
  'decimals': 18
},
{
  'address': "0x0853FFEfE6b939371FCB624ace9976A7C93f5028",
  'name': "wee",
  #'name'l: "we",
  'decimals': 18
},
{
  'address': "0xeCABd61ce65Cb3c1C7c1457FceC23d4eCe879263",
  'name': "gr0",
  #'name'l: "gr0und",
  'decimals': 18
},
{
  'address': "0x24d678E740E8b9b6F6544FC088A97655f2fD2743",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x0d368AA355aa80A1a0277dB4Afece2E921d62c12",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0xc76F83036E00c196E2ddB9587B7f3F785b40AD30",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x9Bf320bd1796a7495BB6187f9EB4Db2679b74eD3",
  'name': "nSTBL",
  #'name'l: "Polly nStable Nest",
  'decimals': 18
},
{
  'address': "0x2c4d614eA315617599a1070E4e8b82890D9040E0",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0xB41EC2c036f8a42DA384DDE6ADA79884F8b84b26",
  'name': "TIDAL",
  #'name'l: "Tidal Token",
  'decimals': 18
},
{
  'address': "0x8C67ef2a3FcBeEA9317B1ab6d48B03A526226f29",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x85699e6dDf946E30DddbD3CF60443283D4D5e24A",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x364Fa2a92e0DC8DF778220E2E814DeCeC4365EeB",
  'name': "nmn",
  #'name'l: ",,,,,",
  'decimals': 18
},
{
  'address': "0xc5A2237B0f4bB6A2E15FF0299eE49ac5c9acc1c0",
  'name': "ANTZ",
  #'name'l: "Peace Antz",
  'decimals': 18
},
{
  'address': "0x22bce38C62fE4D58139dbaF04d1BEa158CB16982",
  'name': "Bridge-LP",
  #'name'l: "Cross-Chain Bridge LPs",
  'decimals': 18
},
{
  'address': "0xDEfa10Dc800Dd3fb33cE6295EE936587A7188cC5",
  'name': "⚫?⬜",
  #'name'l: "Squid Game",
  'decimals': 9
},
{
  'address': "0x9CBc5D2a2690E3035948AE677F4462d1BdBd4024",
  'name': "YFW",
  #'name'l: "Yearn Finance World",
  'decimals': 18
},
{
  'address': "0xdb95f9188479575F3F718a245EcA1B3BF74567EC",
  'name': "GTC",
  #'name'l: "Gitcoin (PoS)",
  'decimals': 18
},
{
  'address': "0xCe99eFa912255E49D0e6F15C1a62e0b3b05234AE",
  'name': "HYPERFANTOM",
  #'name'l: "HYPERFANTOM",
  'decimals': 18
},
{
  'address': "0xB85517b87BF64942adf3A0B9E4c71E4Bc5Caa4e5",
  'name': "FTM",
  #'name'l: "Fantom Token",
  'decimals': 18
},
{
  'address': "0xb730F49aA75320e73d5ce6256fe7fE3F74Db598c",
  'name': "wer",
  #'name'l: "poolka",
  'decimals': 18
},
{
  'address': "0x3f2A47033d622D007F41235Aa636Bd97e4Cc307b",
  'name': "TDD",
  #'name'l: "Lareina Gaines",
  'decimals': 18
},
{
  'address': "0x8E8Fbd2F45eea4d079b1c581a93d5497dfA44e16",
  'name': "Nost",
  #'name'l: "Ezekiel Floyd",
  'decimals': 18
},
{
  'address': "0xada82fcF5C873B8FAEA1986af3E88ECbe9533AD7",
  'name': "TDS",
  #'name'l: "Kasper Craft",
  'decimals': 18
},
{
  'address': "0x427F1336F3D399B122E9c2D6Db135d5B6B0BC12B",
  'name': "AVA",
  #'name'l: "Nehru Morton",
  'decimals': 18
},
{
  'address': "0x4124172B0FBE6c577c8D534c71b8072A637c345d",
  'name': "AVS",
  #'name'l: "Colt Wells",
  'decimals': 18
},
{
  'address': "0xA91FE5a535967F52D3abEBDFFb3B306D964ace13",
  'name': "QUARTZ",
  #'name'l: "Sandclock",
  'decimals': 18
},
{
  'address': "0x322557CE3CCD2827AF502996D69b1600Ac8AD386",
  'name': "DON2",
  #'name'l: "Donnie2",
  'decimals': 18
},
{
  'address': "0x45b79dDd55790f94f71979f42A9e63d9E5a8309D",
  'name': "EMATIC",
  #'name'l: "Elon Matic",
  'decimals': 9
},
{
  'address': "0xd1f3f1C3FE407141e4f0a866Ea919C49990A6c2c",
  'name': "SOURAB",
  #'name'l: "SOURAB",
  'decimals': 18
},
{
  'address': "0xAe532050bFd23Bb243264945B2cb1a13A5f7eD3F",
  'name': "Volu",
  #'name'l: "Chava Drake",
  'decimals': 18
},
{
  'address': "0x8E248Cfcb00c022597D191a881Ea365BedF4a269",
  'name': "Sint",
  #'name'l: "Gavin Wolf",
  'decimals': 18
},
{
  'address': "0x5E2370a767C690de397845CaE1866D659Ac053Ee",
  'name': "MINICZAR",
  #'name'l: "MINICZAR",
  'decimals': 18
},
{
  'address': "0x749c9946E6741E6c0d5c9B050aeCC2075D8b46D6",
  'name': "RETRI",
  #'name'l: "Retriever Inu",
  'decimals': 18
},
{
  'address': "0xfd37d5306A30fD5211A55401a3a1af0F680c9282",
  'name': "nug",
  #'name'l: "nugget",
  'decimals': 18
},
{
  'address': "0xA407E0AeF26D6283740aB34af20448823f32c0B4",
  'name': "VRV",
  #'name'l: "VVerse",
  'decimals': 9
},
{
  'address': "0xDf281C774D37553d1033cBc5FBD4D67635c7fE60",
  'name': "?",
  #'name'l: "Roll",
  'decimals': 9
},
{
  'address': "0x7e2F0DCF40886972e17c8B1A1b28868DF07dd895",
  'name': "tara",
  #'name'l: "tara",
  'decimals': 18
},
{
  'address': "0xAe8aA15bcea95d2D63aa39Cb9B77EF7fc17E708D",
  'name': "Illu",
  #'name'l: "Ann Melendez",
  'decimals': 18
},
{
  'address': "0xd131650151A1F7C3A464Dc57fb2ea2Aec7D6e500",
  'name': "KIM",
  #'name'l: "KISHU INU MICRO ",
  'decimals': 18
},
{
  'address': "0x54c66aFd1D37107b1eA1894C6d03Ee4b2A1543ff",
  'name': "SQUID",
  #'name'l: "Squid Token",
  'decimals': 18
},
{
  'address': "0xeE13f4Ca15EDE6E3284632a819802196E792B2F4",
  'name': "SQUIDGAME",
  #'name'l: "⭘△▢",
  'decimals': 9
},
{
  'address': "0xa78A4cA148E5471F7Bb3354809cd97bFAe7aaE83",
  'name': "cav",
  #'name'l: "Cave",
  'decimals': 18
},
{
  'address': "0xC1e2ca002E03207F933d358DbDEcBaD108C4191a",
  'name': "ODDZ",
  #'name'l: "OddzToken (PoS)",
  'decimals': 18
},
{
  'address': "0x5518a3aF961EEe8771657050c5Cb23D2B3e2F6eE",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xC53bc671dd5a376107470a62A259f586F164Ea98",
  'name': "PEP",
  #'name'l: "Polygon Earning Platform",
  'decimals': 18
},
{
  'address': "0x84DA9aE031f9E5ea3e14A6D869D5171F12f23633",
  'name': "BELI",
  #'name'l: "Beli Token",
  'decimals': 18
},
{
  'address': "0x7C040131af4b90Ac9ef7523c126d3cA187324052",
  'name': "BELI",
  #'name'l: "Beli Token",
  'decimals': 18
},
{
  'address': "0xE6537cb12F1C2A91adc20a0889202D2B0cc1E4D7",
  'name': "MEG",
  #'name'l: "MEG",
  'decimals': 18
},
{
  'address': "0xb705255eEBa0890648B5a09ae3077D45D123D94A",
  'name': "SQUIDSGAME",
  #'name'l: "SQUIDSGAME",
  'decimals': 18
},
{
  'address': "0x71D6a6752D1ED91EB5DBB918fb8E4F3B2257ED63",
  'name': "NUM",
  #'name'l: "Number",
  'decimals': 18
},
{
  'address': "0xeaA76708822e3F92cB28A6C5790adc4FE4dc95Dd",
  'name': "IPT",
  #'name'l: "Index Pool Token",
  'decimals': 18
},
{
  'address': "0xD19f56F0353f44Fe6a643B7606478235FC3f12Ff",
  'name': "CCC",
  #'name'l: "Avye Workman",
  'decimals': 18
},
{
  'address': "0x38Bb9ba086c625aE202C1bF4D91950558F252179",
  'name': "VSG",
  #'name'l: "Fredericka Bishop",
  'decimals': 18
},
{
  'address': "0x7309Df6CDA8f618a2edD11c313d11Da9Fbff5197",
  'name': "NRG",
  #'name'l: "Energify",
  'decimals': 18
},
{
  'address': "0x8B27FA42Cb7Ca5BE307d6155D14133bf33e77711",
  'name': "CON",
  #'name'l: "Con",
  'decimals': 18
},
{
  'address': "0x9b4a185fF79a213b8B73b053f377D38890F487C8",
  'name': "BELI",
  #'name'l: "Beli Token",
  'decimals': 18
},
{
  'address': "0x0a489c8C0e69442499220D0bd181ba3f23E7195B",
  'name': "mond",
  #'name'l: "monay",
  'decimals': 18
},
{
  'address': "0x42335aF34AE08D78Ecf32893Ae51728241a9416d",
  'name': "SAVE",
  #'name'l: "Save",
  'decimals': 18
},
{
  'address': "0xCEc974B72997B921F629daE516b890B72Aa0bECa",
  'name': "Wavy",
  #'name'l: "Wavy",
  'decimals': 18
},
{
  'address': "0x700481409de3f632F61a2AC9BFd76138357714da",
  'name': "GOL",
  #'name'l: "GOL (PoS)",
  'decimals': 8
},
{
  'address': "0xCbA79495a4Ad7bd200b141BF3984697CDCA97Dd5",
  'name': "Uta",
  #'name'l: "Baxter Houston",
  'decimals': 18
},
{
  'address': "0x7EdaBe12993Be629F7B6469C46Fe3b2bEe6C87c0",
  'name': "Alia",
  #'name'l: "Odette Mack",
  'decimals': 18
},
{
  'address': "0xD0F12376179ebC04cc861DDD2fa5D958aCE6aa1F",
  'name': "Fac",
  #'name'l: "Buffy Good",
  'decimals': 18
},
{
  'address': "0xa295e8C3e134B64a798EC46239A368419cfbba64",
  'name': "SAVE",
  #'name'l: "Save",
  'decimals': 18
},
{
  'address': "0xDa8aBA84C195C4FEa3477330e33e30CFCd4b7315",
  'name': "CUB",
  #'name'l: "Cube",
  'decimals': 18
},
{
  'address': "0xFc1A01F5D1538d003154d3ebB87aA21Da48BCB2B",
  'name': "FLSH",
  #'name'l: "FlashPolygon",
  'decimals': 18
},
{
  'address': "0x841cf01c0a1c6998FeEfe8D20e7E8aee8E05befc",
  'name': "MSCN",
  #'name'l: "MUSICIANS",
  'decimals': 18
},
{
  'address': "0x26611cFe066f8be4ab7EF459940D885E160Be3D1",
  'name': "BARRI",
  #'name'l: "Barricoin",
  'decimals': 18
},
{
  'address': "0xF4Ab459A686FCFc06c201fB1738411d7529156e3",
  'name': "HAP",
  #'name'l: "Happy",
  'decimals': 18
},
{
  'address': "0x32052fF4c391115148E7b714E337cd23E8084D99",
  'name': "Labo",
  #'name'l: "Nadine Mclaughlin sadad ad ad ad ad a",
  'decimals': 18
},
{
  'address': "0x467b3e813c57E8049b3e21415613E284816574B0",
  'name': "sdfs",
  #'name'l: "Minerva Hendricks",
  'decimals': 18
},
{
  'address': "0x452FEb6fCD0D1A786B031f6e19FfE0870f3D97a6",
  'name': "123",
  #'name'l: "Cole Tate",
  'decimals': 18
},
{
  'address': "0x73b42958eA0fC03afcd6660fD1cB616c8df9D258",
  'name': "gfhn",
  #'name'l: "Leandra Ryan",
  'decimals': 18
},
{
  'address': "0xEc8178F8f3DFA6F545b131FF6B359f30D9f2a82A",
  'name': "SLY",
  #'name'l: "Sly",
  'decimals': 18
},
{
  'address': "0x654D8F69A5A44586C25aFe3160Bd93C7458CE30b",
  'name': "PRB",
  #'name'l: "PROBAT",
  'decimals': 18
},
{
  'address': "0xfF8ad0D47dD9328ECF4FCd44911Fd288E34A44fB",
  'name': "GRN",
  #'name'l: "GREEN",
  'decimals': 18
},
{
  'address': "0xE8e96dc55573F308074569521E37f3bd532D2e9D",
  'name': "HYPERMATIC",
  #'name'l: "HYPERMATIC",
  'decimals': 18
},
{
  'address': "0xAdde8d31415394C9fBDdfc1e145D0D36fAE84Cf0",
  'name': "TPC",
  #'name'l: "The Penguin Coin",
  'decimals': 2
},
{
  'address': "0xfAbfb07b6a738D4B9FbDd28C6843017bDe24Ac82",
  'name': "PP",
  #'name'l: "Profit Pay",
  'decimals': 9
},
{
  'address': "0xe64f652d490C7324b46815203f6b9b3c5179965D",
  'name': "Q",
  #'name'l: "Network Q",
  'decimals': 10
},
{
  'address': "0x0c56aCF0013F187AA543d806E3E8Dc0B12a9C295",
  'name': "GNS",
  #'name'l: "Genesis",
  'decimals': 18
},
{
  'address': "0x67eD879bf30FED6E1A935970DE1b5850D56F8f46",
  'name': "SCARG",
  #'name'l: "Scarred Entertainment",
  'decimals': 18
},
{
  'address': "0x2C2C70d5d52F001284dC0C6935f1aFA6eD7a294f",
  'name': "USV",
  #'name'l: "Universal Store of Value",
  'decimals': 9
},
{
  'address': "0x3370C17c0411D2Ce90A59162e3b3ec348c84768d",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x7fc850Ae958037504876eBf7B9B8eEC1510EB5eb",
  'name': "LOND",
  #'name'l: "LONG DEFI",
  'decimals': 18
},
{
  'address': "0x2f82C5E183dC165115DA32D6b46b88FE411f22F7",
  'name': "EBC",
  #'name'l: "EBCToken",
  'decimals': 18
},
{
  'address': "0xdeAF4eb2b1C6D4Aa3806F582a2b80A0AE770F6Bf",
  'name': "IPT",
  #'name'l: "Index Pool Token",
  'decimals': 18
},
{
  'address': "0x6a152Cb7CF2E1bb246278beE122Ae4d464bc173A",
  'name': "TARSIER",
  #'name'l: "Tarsier Oddity",
  'decimals': 14
},
{
  'address': "0x6877547e5C7323183a337f8fe7b836a22D0cC54B",
  'name': "SRT",
  #'name'l: "Snrat Token",
  'decimals': 18
},
{
  'address': "0x18411D3560177B3be9bA2D96D37dd1970461F425",
  'name': "Volu",
  #'name'l: "Audra Collier",
  'decimals': 18
},
{
  'address': "0x4DdC0977788CB60c7b2e6EC9e761b546f13975C2",
  'name': "Accu",
  #'name'l: "Ruby Thomas",
  'decimals': 18
},
{
  'address': "0xC8c34b6Ae5fd094350aED7B029299b1bAAeB07c3",
  'name': "jujh",
  #'name'l: "Isaac Nash",
  'decimals': 18
},
{
  'address': "0x6f37d76bda0682749c13C913472E4027dF584820",
  'name': "vcf",
  #'name'l: "Hasad Paul",
  'decimals': 18
},
{
  'address': "0xCE514e46e24Eafa8141bB61Dab7367948dC839fE",
  'name': "Vit",
  #'name'l: "Allegra Garrett",
  'decimals': 18
},
{
  'address': "0xBDb2A0Fb7922546141C12a9259fc18D815010b7f",
  'name': "In2",
  #'name'l: "Aurelia Beard",
  'decimals': 18
},
{
  'address': "0xc36C817e58233DD9771a56a4B97499d1b7f84C9d",
  'name': "ALTD",
  #'name'l: "Altairian dollar",
  'decimals': 0
},
{
  'address': "0xB2A1F431Dc0A16e8D7a7Edf2A418D667975da103",
  'name': "DBG",
  #'name'l: "Lana Weeks",
  'decimals': 18
},
{
  'address': "0x8Caa0cF3AfDC978eB410031C113057f8b078390e",
  'name': "Quae",
  #'name'l: "Ezekiel Sloan",
  'decimals': 18
},
{
  'address': "0xc9A6181cA196Ec59A2938e49F64bA5C31802Ae5D",
  'name': "jhh",
  #'name'l: "Kaye Pickett",
  'decimals': 18
},
{
  'address': "0x569342365a06397647F6b27bBe4A4a4986F8e810",
  'name': "ror",
  #'name'l: "new ror",
  'decimals': 18
},
{
  'address': "0x1f7bfE45a23898aFE1d1b65B9469652c572B7340",
  'name': "Maxi",
  #'name'l: "Boris Haynes",
  'decimals': 18
},
{
  'address': "0xD9d2106ad47a8ccA6ca4DE9BfCcC78351A1262B5",
  'name': "HUGG",
  #'name'l: "HuggCoin",
  'decimals': 8
},
{
  'address': "0x5E7478D0D538C27dc4956dde3310168caBD58B24",
  'name': "USV",
  #'name'l: "Universal Store of Value",
  'decimals': 9
},
{
  'address': "0xbD7A5Cf51d22930B8B3Df6d834F9BCEf90EE7c4f",
  'name': "ENS",
  #'name'l: "Ethereum #'name' Service (PoS)",
  'decimals': 18
},
{
  'address': "0xa0E6D0c9F1292d6959BBe380783B1d6896844C66",
  'name': "BEN",
  #'name'l: "Bean",
  'decimals': 18
},
{
  'address': "0xa2c1a430DD5c59b42e88dfCfdC777D9d7FDfd92e",
  'name': "MockDAI",
  #'name'l: "MockDai Stablecoin",
  'decimals': 18
},
{
  'address': "0x20efd251560fAf484b2Cc8818AA70A9cab63aF0a",
  'name': "USV",
  #'name'l: "Universal Store of Value",
  'decimals': 9
},
{
  'address': "0x868720B75Cf8ec0e41452B4615225600A1eAb095",
  'name': "SLY",
  #'name'l: "Slayer",
  'decimals': 18
},
{
  'address': "0x576Cf361711cd940CD9C397BB98C4C896cBd38De",
  'name': "USDC",
  #'name'l: "USD Coin (Wormhole)",
  'decimals': 6
},
{
  'address': "0x30072398a6DA623A6B12aFb7F3eE48D3273512D4",
  'name': "BJUMP",
  #'name'l: "BeaverJump",
  'decimals': 18
},
{
  'address': "0x93b441B5F8296526efb56Ae9baFf6B8f283D0efE",
  'name': "POLYSHEEB",
  #'name'l: "PolySheeba",
  'decimals': 18
},
{
  'address': "0x5034077B88879177989558C22AbF6f4253B39177",
  'name': "HAUFO T",
  #'name'l: "HA UFO",
  'decimals': 18
},
{
  'address': "0x34E946Fca70F4035a18148dF49f73A5171dF94c2",
  'name': "ERUPEE",
  #'name'l: "INR",
  'decimals': 18
},
{
  'address': "0x1D607Faa0A51518a7728580C238d912747e71F7a",
  'name': "DATA",
  #'name'l: "DATA Economy Index (PoS)",
  'decimals': 18
},
{
  'address': "0xd9B064E78199598e9435F9158bE1f28b4db422a3",
  'name': "XDCK",
  #'name'l: "Duck",
  'decimals': 18
},
{
  'address': "0x752DC265EAf6Da2Db0F8e4a32D5596D3f18e8701",
  'name': "WAVN",
  #'name'l: "Wrapped Avian",
  'decimals': 18
},
{
  'address': "0x960dB99f77E4DA9dD7F2d263f6a31f9Db1056B81",
  'name': "BLACKTBOYS",
  #'name'l: "BLACKTBOYS",
  'decimals': 18
},
{
  'address': "0xAcbB3015565bAE7e82D2DAaF0B2362DC2ff9803F",
  'name': "MUR",
  #'name'l: "Meta universe rich",
  'decimals': 18
},
{
  'address': "0x2040E4893C5547a89386c1F16a52BC18fE38d8B7",
  'name': "MUR",
  #'name'l: "Meta universe rich",
  'decimals': 18
},
{
  'address': "0x3cb511bFD3D18E348CA0Eb0F5bf600E6007BbdB0",
  'name': "TRN",
  #'name'l: "Train",
  'decimals': 18
},
{
  'address': "0x165736d5bBfC168f9F8B93802f56B40806879518",
  'name': "2021LFG",
  #'name'l: "2021LFG",
  'decimals': 18
},
{
  'address': "0x337Bbd8e004C635d4B09f3e783742F2A8DC896e3",
  'name': "NTTC",
  #'name'l: "Navigator",
  'decimals': 9
},
{
  'address': "0x5e90276eA8d7095b513C12E002c1B43C496427b3",
  'name': "Tem2",
  #'name'l: "Ursa Drake",
  'decimals': 18
},
{
  'address': "0x19AEc38aCa1f2Bf21E10d52B574bAf9B90082E19",
  'name': "SHEESH",
  #'name'l: "Sheesh Coin",
  'decimals': 18
},
{
  'address': "0xA3B3C6BC66C2cf819C35834Dd8ff05dEAF415CB2",
  'name': "cal",
  #'name'l: "call",
  'decimals': 18
},
{
  'address': "0xBFcE46480958A8C09C4Df1C9c0eC43c882f66A27",
  'name': "vaca",
  #'name'l: "ovaca",
  'decimals': 18
},
{
  'address': "0x6a1cD375A424ec6cE4493fD3a5070b53771576dC",
  'name': "IPT",
  #'name'l: "Index Pool Token",
  'decimals': 18
},
{
  'address': "0x82bD579e3680d10D169c802aE4E2D7B4d95b0284",
  'name': "ALVS",
  #'name'l: "ALVS_Coin",
  'decimals': 2
},
{
  'address': "0x3f6b3595ecF70735D3f48D69b09C4E4506DB3F47",
  'name': "GAMER",
  #'name'l: "GameStation",
  'decimals': 18
},
{
  'address': "0xA0274ED49BEb80cC944E1163546D16c31f6aE4Da",
  'name': "SOKJANCHI",
  #'name'l: "Sokjanchi",
  'decimals': 18
},
{
  'address': "0x29522c65bCA0F1cC1BB2C912Ca47B1aE3De8F40f",
  'name': "egos",
  #'name'l: "egos avatars",
  'decimals': 18
},
{
  'address': "0xE8A003A96eD41177679b37d496Ae5336522C7731",
  'name': "cat",
  #'name'l: "FatCat",
  'decimals': 18
},
{
  'address': "0xf7EDDBf3Bf849d6db1f068E75B5bD5cac7634C8f",
  'name': "BACH",
  #'name'l: "Bachini 60/40 Portfolio",
  'decimals': 18
},
{
  'address': "0x97aE367ed1D93A40762412a7B7975F7113ec38c6",
  'name': "Ita",
  #'name'l: "Galena Wilkerson",
  'decimals': 18
},
{
  'address': "0x6c95DDda21eF64dD8cc2296FA21B1fCf0Ea52206",
  'name': "Aute",
  #'name'l: "Shay Norton",
  'decimals': 18
},
{
  'address': "0x81e3C55f612ed68cDaCe2d0DDf50570e1740A8CC",
  'name': "SFF",
  #'name'l: "Darrel Washington",
  'decimals': 18
},
{
  'address': "0x49d0579886876CC2ce6D36D4089d22c7ae62FA66",
  'name': "SHIBM",
  #'name'l: "SHIBA MATIC",
  'decimals': 18
},
{
  'address': "0x2809845698dF7f76782d893AAaC8BA46b1ade800",
  'name': "T321",
  #'name'l: "TestPool321Token",
  'decimals': 18
},
{
  'address': "0x39d7130eA6cBB87eB92d53dD01e1a22d83DA9402",
  'name': "Sed",
  #'name'l: "Sarah Dennis",
  'decimals': 18
},
{
  'address': "0xC23e2c3EA734D9FBcb2B49F8AB7755d61E5A8cf5",
  'name': "frid",
  #'name'l: "friday",
  'decimals': 18
},
{
  'address': "0x767FC449DcD7fF08a79A9Bf30Db0DF0dde04885B",
  'name': "COR7",
  #'name'l: "Ocean Cortez",
  'decimals': 18
},
{
  'address': "0xf1a7932a3bf68d6fcF44837B3240B6674E351a54",
  'name': "CRS",
  #'name'l: "Crypto Shark",
  'decimals': 18
},
{
  'address': "0xAEE46a42883Bd82094434afa0a20c06293F08Cdd",
  'name': "BRM",
  #'name'l: "Beramcoin",
  'decimals': 18
},
{
  'address': "0x77F6223D58F0E20d546c446447ED3A164E1e7306",
  'name': "SHITE",
  #'name'l: "SHITE.IO",
  'decimals': 9
},
{
  'address': "0xDC5F49d8a2944b32256f05C062c85CfB5ceDe33b",
  'name': "QUEBEC",
  #'name'l: "Crypto Quebec",
  'decimals': 8
},
{
  'address': "0x734fAf359c65BdA0675aDFb791B7175a89d18c9c",
  'name': "Soontoshi WenSama",
  #'name'l: "Rinku",
  'decimals': 18
},
{
  'address': "0xC05C25D1a11006Fdfcf885e27B307CA62D5da04b",
  'name': "NGMI",
  #'name'l: "Not Gonna Make It",
  'decimals': 18
},
{
  'address': "0x29d1b639F366754179e1452EF590bFdCe3f9DC44",
  'name': "WEN",
  #'name'l: "Rinku",
  'decimals': 18
},
{
  'address': "0xA3A107684C58f99983F9bad77272fa11095B1054",
  'name': "WAT",
  #'name'l: "WAT",
  'decimals': 18
},
{
  'address': "0x93dA8f92e89Dde30C27CD2Ef965bD9e91BcFb174",
  'name': "RP",
  #'name'l: "Runway Points (prePO Acquisition Royale)",
  'decimals': 18
},
{
  'address': "0x02180d251eeE44F9d9182c7308f9774F61eD172C",
  'name': "SKY",
  #'name'l: "SKY",
  'decimals': 18
},
{
  'address': "0xdb725f82818De83e99F1dAc22A9b5B51d3d04DD4",
  'name': "GET",
  #'name'l: "GET Protocol (PoS)",
  'decimals': 18
},
{
  'address': "0x3981Ca8F23cCD17236b5868b6C45f6D2837fea40",
  'name': "POST",
  #'name'l: "Space time",
  'decimals': 18
},
{
  'address': "0x3E68Ea16543C599f9F1d5D73E720D048FBd46AB3",
  'name': "PUMP",
  #'name'l: "Pump and Dump",
  'decimals': 18
},
{
  'address': "0x26dbC587F789D5511f9359ea47fAFb40f06b96b4",
  'name': "EVST",
  #'name'l: "Everest Protocol",
  'decimals': 18
},
{
  'address': "0xB5D762ed1365E471A3E618bf4707C501954D6AD6",
  'name': "USV",
  #'name'l: "Universal Store of Value",
  'decimals': 9
},
{
  'address': "0x5fbDa31a2bE6af41329aca9F18E8959aA89B372B",
  'name': "TOP50",
  #'name'l: "Top 50 index",
  'decimals': 18
},
{
  'address': "0x57f869b8F27f2a79a0597e5a7141Ad2925819CD0",
  'name': "GoHuT",
  #'name'l: "God And Humans Token",
  'decimals': 18
},
{
  'address': "0x16A801E521a9366C1Fee3048E9198bd6E7AEd40a",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xf2C9650Fd759f93e59D2ae8F42A97C0600150F0e",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x3582Ec775c6046dB51B4D680211c722D9b77Aa59",
  'name': "Bankless",
  #'name'l: "BanklessToken",
  'decimals': 18
},
{
  'address': "0xfbc22D81dAfA8C841EB6e6396073D64cbF5bE2f2",
  'name': "HNS",
  #'name'l: "HoneySwap",
  'decimals': 18
},
{
  'address': "0x4d6A30EFBE2e9D7A9C143Fce1C5Bb30d9312A465",
  'name': "CLAM",
  #'name'l: "Otter Clam",
  'decimals': 9
},
{
  'address': "0x7c64aD5F9804458B8c9F93f7300c15D55956Ac2a",
  'name': "cUSD",
  #'name'l: "Celo Dollar",
  'decimals': 18
},
{
  'address': "0xfD4B0d04CF5194961Fa73c6E0d80e5cE21FE001e",
  'name': "USV",
  #'name'l: "Universal Store of Value",
  'decimals': 9
},
{
  'address': "0x756eceaE1BA2E683b794bE52d1f15706d10DDf78",
  'name': "LFG",
  #'name'l: "Lets Fucking GO",
  'decimals': 18
},
{
  'address': "0x9A4Eb698e5DE3D3Df0a68F681789072DE1E50222",
  'name': "FID",
  #'name'l: "Fidira",
  'decimals': 18
},
{
  'address': "0x9fFcf6a70C01D1E5dd6dB55f1b63D84B3a863Cfb",
  'name': "HAS ",
  #'name'l: "Hoodie Aliens Socks",
  'decimals': 18
},
{
  'address': "0x0007b5E2BCE942CCEa519E3956292C0e92C9a2aa",
  'name': "HASOCKS ",
  #'name'l: "Hoodie Aliens Socks",
  'decimals': 18
},
{
  'address': "0x7d580D7055Df2EF60bE562791E1B679306f52786",
  'name': "SARCO",
  #'name'l: "Sarcophagus from Mainnet (Wormhole)",
  'decimals': 18
},
{
  'address': "0xD56Fd957027CEF9e3FD122d99dF0b250F066a31f",
  'name': "PHI",
  #'name'l: "PHI",
  'decimals': 18
},
{
  'address': "0x6733C4a40916BC2c340b1de3Ea2500FBA92ffF54",
  'name': "Inv",
  #'name'l: "Lisandra Fry",
  'decimals': 18
},
{
  'address': "0xEFFf34b4c01693a9577382a04AaA5cdB9a5FC3Cc",
  'name': "PAPR",
  #'name'l: "Paper",
  'decimals': 18
},
{
  'address': "0x0049E136c72F39fe36169c879D02B865796D0C55",
  'name': "new",
  #'name'l: "new one",
  'decimals': 18
},
{
  'address': "0xA7A1D7715520fD99Cb3a28d720Be5e0E34c0AA48",
  'name': "JEJ",
  #'name'l: "JEJ",
  'decimals': 18
},
{
  'address': "0x7E108699CeD91A73d1A8887A49888F86bDeED8d1",
  'name': "JRTO",
  #'name'l: "JULIEN ROMAN",
  'decimals': 4
},
{
  'address': "0x50bCBC40306230713239Ae1BdDD5eefEEaa273Dc",
  'name': "ASIA",
  #'name'l: "ASIA COIN (PoS)",
  'decimals': 18
},
{
  'address': "0xc9C1DaD6554b193e1e7b7930e0B83acfcedA5aD7",
  'name': "DEB",
  #'name'l: "Digital exchange bank",
  'decimals': 18
},
{
  'address': "0x12724aA0838361ca209f05D84FC187964d395a89",
  'name': "HALO",
  #'name'l: "Halo",
  'decimals': 18
},
{
  'address': "0x2fE0f38C041AB2eb1aBe074C46Dfe106Cf21cf21",
  'name': "cat",
  #'name'l: "CatToken",
  'decimals': 18
},
{
  'address': "0x91C67C1178f025a732bE847b2896F06ae5E326dc",
  'name': "Quo",
  #'name'l: "Channing Davidson",
  'decimals': 18
},
{
  'address': "0xc115683555e65DFE26783c640115B3Cf999c3dCd",
  'name': "Qui",
  #'name'l: "Asher Glover Pool",
  'decimals': 18
},
{
  'address': "0xAC929757f5738316431b91b4557aD8C77fbCDE02",
  'name': "Nos",
  #'name'l: "Caesar England",
  'decimals': 18
},
{
  'address': "0xcA7266c9F9CBEcB141CD2592688a8cd844a0C5b8",
  'name': "STI",
  #'name'l: "Stimulus",
  'decimals': 18
},
{
  'address': "0x5A35d30c8b23e571e4F7eFc25F353c91fD12F8E8",
  'name': "xPOP",
  #'name'l: "Popcorn.Network (Redeemable POP)",
  'decimals': 18
},
{
  'address': "0x0E2e4158dD99B49d79B5Fa2a04f2023360DA0266",
  'name': "LTE",
  #'name'l: "Last Token Ever",
  'decimals': 9
},
{
  'address': "0x2189C9Eb3E1ef9d14b29eeF0c27AeBba5FA9Ad7A",
  'name': "SBG",
  #'name'l: "shiba gold",
  'decimals': 18
},
{
  'address': "0x6FDacb3848b0350992110215A9Cd241B8954bF57",
  'name': "?",
  #'name'l: "Castle",
  'decimals': 18
},
{
  'address': "0x10635bF5c17F5E4c0Ed9012aEf7C12f96a57a4Dd",
  'name': "TAP",
  #'name'l: "Tapmydata (PoS)",
  'decimals': 18
},
{
  'address': "0x200e169B6a4798987A88Cc9769807248423C1f55",
  'name': "ooo",
  #'name'l: "ooo",
  'decimals': 18
},
{
  'address': "0xef74eF81A12ab19ABb5c74542c61738B0D19A3B6",
  'name': "Sunt",
  #'name'l: "Marsden Harrell",
  'decimals': 18
},
{
  'address': "0x0E0ffc562d72316b783E887bbAAe1FD794ADb530",
  'name': "DOV",
  #'name'l: "DOVU (PoS)",
  'decimals': 18
},
{
  'address': "0x6601199E317a0AdD0168A64277917BBEa8c627B4",
  'name': "LOL",
  #'name'l: "LOL",
  'decimals': 18
},
{
  'address': "0xfF1CC0aC6594cD4057c5719C8cb764f3D8Eac7aC",
  'name': "COF",
  #'name'l: "coffee",
  'decimals': 18
},
{
  'address': "0x2413A0670623312decad2B935b0c48857C108668",
  'name': "UUU",
  #'name'l: "UUU",
  'decimals': 18
},
{
  'address': "0x80Ae3B3847E4e8Bd27A389f7686486CAC9C3f3e8",
  'name': "SARCO",
  #'name'l: "Sarcophagus (PoS)",
  'decimals': 18
},
{
  'address': "0x2984227844a163623F490C10992e239aB25b3E18",
  'name': "KIK",
  #'name'l: "KIK",
  'decimals': 18
},
{
  'address': "0x1441729568ab2A9871677edfeb13fBFCc7157a26",
  'name': "PRXY",
  #'name'l: "Proxy",
  'decimals': 18
},
{
  'address': "0x53677D896B16a1D109E38CB1421ea099264dCD34",
  'name': "WKF",
  #'name'l: "WKF Coin",
  'decimals': 18
},
{
  'address': "0x76b6BF6381EE6fe683D7F509F4BCd6E250533680",
  'name': "COW",
  #'name'l: "COBW",
  'decimals': 18
},
{
  'address': "0x0eFFCEc1cE49bc589142Fd28A2cc30796b685dd9",
  'name': "RIBI",
  #'name'l: "Ribeye",
  'decimals': 18
},
{
  'address': "0x82868099caDE6872a6417E514c23a6e63c5DCa46",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x3212aFa98b212d6A435009c4BF560018c43A58A2",
  'name': "SCC",
  #'name'l: "SpaceCatCoin",
  'decimals': 18
},
{
  'address': "0x2A6f69709ca73a4Ac31Ec724dd8A385420E92b1F",
  'name': "NVR",
  #'name'l: "NVRToken",
  'decimals': 18
},
{
  'address': "0xA4FD85b0Fe137b3ae651ecCE2b09ca108f695242",
  'name': "HYPERBNB",
  #'name'l: "HYPERBNB",
  'decimals': 18
},
{
  'address': "0x852590BE65C09Caa72244aa2764dfD68d6E6b869",
  'name': "PMT",
  #'name'l: "Polygon Maker Token",
  'decimals': 18
},
{
  'address': "0x416D9deF117B15Ec1a7f01A7F47F795eE9bA48C8",
  'name': "REGEN",
  #'name'l: "Regenerative",
  'decimals': 18
},
{
  'address': "0xF3CcDC6904361bBc19f4aed006552da520BD24bd",
  'name': "TITAN2",
  #'name'l: "Titan v2",
  'decimals': 9
},
{
  'address': "0x1D81b6fc85D0F116d2EE66D1ebAECe8d0211980E",
  'name': "CVC",
  #'name'l: "CvLiveCoin",
  'decimals': 18
},
{
  'address': "0xcEF9343B5f3B838252bc1B2bc228218344fc9239",
  'name': "liqd",
  #'name'l: "liquidity",
  'decimals': 18
},
{
  'address': "0xA300ddB6c763211316D397d7A6A70464b90E801e",
  'name': "noon",
  #'name'l: "no 1:1",
  'decimals': 18
},
{
  'address': "0xFF6f3e2e0eBe18e44e9f690f0Ea6136EF356E054",
  'name': "jij",
  #'name'l: "jij",
  'decimals': 18
},
{
  'address': "0x38BBd5aAFF8A8bA7Df2d646AdDA996b23640Eb59",
  'name': "Ella",
  #'name'l: "Ella Jefferson",
  'decimals': 18
},
{
  'address': "0x142780677E331bC8f721823825B1DB024314B04c",
  'name': "ill1",
  #'name'l: "illum",
  'decimals': 18
},
{
  'address': "0x7c070A4f7A6A00Ea33b2130d5AD4C9d0FfB3Eb0a",
  'name': "CB",
  #'name'l: "CryptoBridge",
  'decimals': 18
},
{
  'address': "0xBbba073C31bF03b8ACf7c28EF0738DeCF3695683",
  'name': "SAND",
  #'name'l: "SAND",
  'decimals': 18
},
{
  'address': "0xE778796965CeA8095FAd2D907F88D06B668fac91",
  'name': "ASTRO",
  #'name'l: "Astro",
  'decimals': 18
},
{
  'address': "0xc17b109E146934D36c33E55FADE9cBDa791b0366",
  'name': "KRL",
  #'name'l: "Kart Racing League",
  'decimals': 18
},
{
  'address': "0xDB7Cb471dd0b49b29CAB4a1C14d070f27216a0Ab",
  'name': "BANK",
  #'name'l: "Bankless Token (PoS)",
  'decimals': 18
},
{
  'address': "0x3a16bC62e7140179E8e878fe74a09D72AD51b0B0",
  'name': "SEA",
  #'name'l: "Seatail",
  'decimals': 18
},
{
  'address': "0xFbd25F0E7943F7b0d101e59e37337CdF37ec9676",
  'name': "TST1",
  #'name'l: "TEST1",
  'decimals': 18
},
{
  'address': "0x45753ff1B112C47a0A7b20D78BB6E64a4082BC0c",
  'name': "TST3",
  #'name'l: "TEST3",
  'decimals': 18
},
{
  'address': "0xe48796A92DCB303D56d4Eecb626456db132242ea",
  'name': "GOLD",
  #'name'l: "GOLDERION",
  'decimals': 8
},
{
  'address': "0xC00B07bAbF61afbf8fe1C696db1150b17cE0A4D0",
  'name': "GM",
  #'name'l: "Good Morning",
  'decimals': 9
},
{
  'address': "0x07e62d7cf5FED7e171945772a5e5aBaE8b1A312F",
  'name': "AIR",
  #'name'l: "Moon Air",
  'decimals': 18
},
{
  'address': "0xc4610FBe17fA87a553B1f24f4EA40c739a3E843b",
  'name': "DUMB",
  #'name'l: "Dumb Apes",
  'decimals': 0
},
{
  'address': "0x82C23dc3506A93dc5B31b0f164e361f7E2Ec80B0",
  'name': "HYPERBNB",
  #'name'l: "HYPERBNB",
  'decimals': 18
},
{
  'address': "0xdF93a8Be0000e4f78421AE9484D77D944d0C3393",
  'name': "AMRD",
  #'name'l: "ARGAN MEGA RIANSYAH DEFI",
  'decimals': 18
},
{
  'address': "0xC4d673d12056439FeA9a1235A35735241e412d9F",
  'name': "SHIBGON",
  #'name'l: "SHIBAgon",
  'decimals': 9
},
{
  'address': "0x7d88D931504D04BFBEE6F9745297A93063CAb24c",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x81CFFe797B3fd4A9e3F040Da89381b351921132d",
  'name': "HYPERETH",
  #'name'l: "HYPERETH",
  'decimals': 18
},
{
  'address': "0x51CAf35a274afcc395a80E6399C3e1169586b27F",
  'name': "HYPERBTC",
  #'name'l: "HYPERBTC",
  'decimals': 18
},
{
  'address': "0xE6669b05bE3A526b36A7eB9249a77769aB446B77",
  'name': "SAITAMA",
  #'name'l: "Saitama Inu",
  'decimals': 9
},
{
  'address': "0x82dC7D8EaEb2B70B5456dC07C0f9eD90B0416136",
  'name': "SAP",
  #'name'l: "Shiba Army Polygon",
  'decimals': 18
},
{
  'address': "0xD365dc174539cdc274f09eC3eb7a58B524a49445",
  'name': "HYPERBTC",
  #'name'l: "HYPERBTC",
  'decimals': 18
},
{
  'address': "0x873DDc01B20117B5B85742675506E90542a9c538",
  'name': "TEST",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0x084a2E1F2C86e4Bc42883B6a434cd974eB6CEe51",
  'name': "YFT",
  #'name'l: "yearn finance ",
  'decimals': 18
},
{
  'address': "0x1061ef4C9579fA01Be0D20E424030d7f486A57bD",
  'name': "XBL",
  #'name'l: "Blackhole Finance",
  'decimals': 18
},
{
  'address': "0x29549697603203CAFe8BA4aF4A338C2441FA2909",
  'name': "shawn",
  #'name'l: "shawn",
  'decimals': 18
},
{
  'address': "0x264ca46ae09043e1c29b8ee88f9A81822866A36D",
  'name': "GST",
  #'name'l: "GreenSwap Token",
  'decimals': 8
},
{
  'address': "0x033d942A6b495C4071083f4CDe1f17e986FE856c",
  'name': "AGA",
  #'name'l: "AGA Token (PoS)",
  'decimals': 4
},
{
  'address': "0xced8abb6456948feb687Ec5aA7d2EF6c7243AD75",
  'name': "WOAH",
  #'name'l: "Woahbit",
  'decimals': 18
},
{
  'address': "0x7892146AC0C5c09bcF82173C8bF9BA0E3c5DEDc6",
  'name': "213",
  #'name'l: "Germane Bruce",
  'decimals': 18
},
{
  'address': "0x3223Aef09D1f6eD1778B76ab06e2bD611839A03B",
  'name': "IPT",
  #'name'l: "Index Pool Token",
  'decimals': 18
},
{
  'address': "0xC88F05482bd35Ea7CCE99a8688b02280e765D282",
  'name': "BLV",
  #'name'l: "BlackVerse",
  'decimals': 18
},
{
  'address': "0x60A9Dd64D1dCeeC7469F9b9cfB9fdC58f84cfbc6",
  'name': "MNV",
  #'name'l: "MoonVerse",
  'decimals': 18
},
{
  'address': "0x60b3C569F1D58D0790775827646DC62De5E6c975",
  'name': "Dol2",
  #'name'l: "Blaine Parrish",
  'decimals': 18
},
{
  'address': "0x7B883D6eF5312f4F31eFDA6E8b81aB3D9321AeBf",
  'name': "Ex2",
  #'name'l: "Sonia Wagner",
  'decimals': 18
},
{
  'address': "0xCE3BE69F36d9e545509877A38892d2C9883bc418",
  'name': "Sin2",
  #'name'l: "Kasimir Fry",
  'decimals': 18
},
{
  'address': "0xbfFFE59d8227ee587271A8c01B7F6e04775059f3",
  'name': "ETH",
  #'name'l: "etherium - ",
  'decimals': 9
},
{
  'address': "0x92134Ed58Ddf88307FcD3B10fC87D0f1416768a7",
  'name': "ADOGE",
  #'name'l: "0x@ALX Doge",
  'decimals': 18
},
{
  'address': "0xbC7fb72986B866b6bB179820a8f559381bA9Daec",
  'name': "MKTK",
  #'name'l: "Meenkeea Project Token",
  'decimals': 18
},
{
  'address': "0xD71d02EA0bf7565C1Ac39f09Dc8ECF950D4830AA",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x901eb48A8394eA3a135c6Ac611030D297DA9dC8b",
  'name': "HNY",
  #'name'l: "Honey",
  'decimals': 18
},
{
  'address': "0x7cD5c5F50bA2862229abe41A516329Bb7dDc7E1e",
  'name': "GDN",
  #'name'l: "Garden",
  'decimals': 18
},
{
  'address': "0x8DA02454e483fd75f39E15Ee0AD0c6704250670A",
  'name': "BLOK",
  #'name'l: "BLOK",
  'decimals': 18
},
{
  'address': "0xeaC34a5425Fe41574396FEDbCDdc11A53025E750",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x5dD175A4242afE19e5c1051d8cd13Fc8979f2329",
  'name': "RVRS",
  #'name'l: "REVERSE",
  'decimals': 9
},
{
  'address': "0xCb327BE7Fb95b58c74dd7F57b88630cf7b6449E4",
  'name': "1USD",
  #'name'l: "1USD",
  'decimals': 18
},
{
  'address': "0x716bcE7e6807c16E0955a87F0BA1879595D976d8",
  'name': "TitanDAI",
  #'name'l: "TitanDai Stablecoin",
  'decimals': 18
},
{
  'address': "0xCA02aEf9E954e97eFDbBb5A8a372Cc308b656C40",
  'name': "DAI",
  #'name'l: "DAI stable",
  'decimals': 18
},
{
  'address': "0xcD527611AD88a9742625abE07CB8c71edD7622aF",
  'name': "TestSat",
  #'name'l: "TestSat",
  'decimals': 9
},
{
  'address': "0x2456C4e8352584C33B71B539C17d8d9bBc01e271",
  'name': "AAOR",
  #'name'l: "Abu Alumni Oriole (FXERC20)",
  'decimals': 18
},
{
  'address': "0x674f3deE1efB724890f5Ca766B73DeB049eCE5dB",
  'name': "MWY",
  #'name'l: "MealAway",
  'decimals': 18
},
{
  'address': "0xFC062e420c9979269afee7b3F5E38Cb09761CA6A",
  'name': "WOLFBIT",
  #'name'l: "wolfbit",
  'decimals': 18
},
{
  'address': "0xDaCAd987446167808b37305d3886FB37D58056Cb",
  'name': "LeafMoon",
  #'name'l: "LeafMoon",
  'decimals': 9
},
{
  'address': "0x48B0A925D219884036245bf59629F0D395983b79",
  'name': "MOMENTS",
  #'name'l: "Moments for Ever",
  'decimals': 18
},
{
  'address': "0x5aB9Fe9ED17e171020850bCBE255d612F483068b",
  'name': "SaberNooripour",
  #'name'l: "SRNR",
  'decimals': 18
},
{
  'address': "0x3bd80F62B5afd73Fd5d9a7630B2A2ADbB2504B92",
  'name': "ANTICOVID",
  #'name'l: "ANTICOVID",
  'decimals': 18
},
{
  'address': "0x364751eaf0CcDe6B2051527C4bd48d346b2E5c31",
  'name': "TestSat1",
  #'name'l: "TestSat1",
  'decimals': 9
},
{
  'address': "0x61c331D25BAD1B2eA5123C71B7Dc6B4A97346518",
  'name': "TestSat1",
  #'name'l: "TestSat1",
  'decimals': 9
},
{
  'address': "0xd6F00c26F81f7B9C79206B60767177Ff185D6e23",
  'name': "PHPX2",
  #'name'l: "Xiaz Peso Pegged",
  'decimals': 8
},
{
  'address': "0x66111bBf86cD4C0c87a1C4249bdacAECDBABe373",
  'name': "CISKEK",
  #'name'l: "Ciskek Coin",
  'decimals': 18
},
{
  'address': "0xe30A551811C5d1e038008157D2213f1d93367bea",
  'name': "AITURENG",
  #'name'l: "AITURENG",
  'decimals': 18
},
{
  'address': "0x5127F8D2Ca1f189004a01A248A6F96E76dd4aad7",
  'name': "ADC",
  #'name'l: "airdrop coin",
  'decimals': 8
},
{
  'address': "0x93F6E3d231bbEd91D7194F5180E70c9617597966",
  'name': "JBD",
  #'name'l: "JB DAO",
  'decimals': 18
},
{
  'address': "0x551F43bf9B4e80ef0704c3F014d7b2af0165Aa70",
  'name': "TFI",
  #'name'l: "TOKODEFI.COM",
  'decimals': 18
},
{
  'address': "0x10DCf1E237741eD0042EE7eC0C57053C819d6D0e",
  'name': "SAM",
  #'name'l: "Samantha",
  'decimals': 9
},
{
  'address': "0xAC63686230f64BDEAF086Fe6764085453ab3023F",
  'name': "USV",
  #'name'l: "Universal Store of Value",
  'decimals': 9
},
{
  'address': "0x63B2d6a81E74c0344d591d80bDBFB636d82e5d95",
  'name': "NEON",
  #'name'l: "NEON",
  'decimals': 18
},
{
  'address': "0x31A9A2DE2380aD19EE1D545500c8851fC14dc3C8",
  'name': "JEJ",
  #'name'l: "JEJA",
  'decimals': 18
},
{
  'address': "0xDf2f7F546136Ef47078107681eAe80d8aa9af5D5",
  'name': "FREAK",
  #'name'l: "Freak Token",
  'decimals': 18
},
{
  'address': "0x7654dc67f6558422610A54cFc2437C80Ad744d26",
  'name': "GMTT",
  #'name'l: "The Green Machine Tip Token",
  'decimals': 18
},
{
  'address': "0x010Fd3cD0c0Cb2772840F0F7b7293e14D984c598",
  'name': "FCRE",
  #'name'l: "FC Repacking Enterprise",
  'decimals': 18
},
{
  'address': "0x0bD49815EA8e2682220BCB41524c0dd10Ba71d41",
  'name': "PYM",
  #'name'l: "Playermon",
  'decimals': 18
},
{
  'address': "0xbEa1731a67a776Dff232AFE654B183D42109C46B",
  'name': "buy",
  #'name'l: "buyby",
  'decimals': 18
},
{
  'address': "0x57a514ef9E6382286d1AC8CBa43A63ECe964954c",
  'name': "alch",
  #'name'l: "alchemy",
  'decimals': 18
},
{
  'address': "0x7Acd2441E03c7f4a3B1C6639cCc2A2F9c4c3f443",
  'name': "test",
  #'name'l: "Lunea Johns",
  'decimals': 18
},
{
  'address': "0xa6e89766eed7310ec749E5C6e7CeDf3822B4e543",
  'name': "GSG",
  #'name'l: "Quin Mays",
  'decimals': 18
},
{
  'address': "0xa3B9720aaA60934F658F1627E29806B743e15f38",
  'name': "Vela",
  #'name'l: "Juliet Murray",
  'decimals': 18
},
{
  'address': "0xF5bC9BcF31D26C7A1e0671DeE4437952a7240e8b",
  'name': "NWS",
  #'name'l: "Newsroom",
  'decimals': 18
},
{
  'address': "0x4f761952c1C74d8B4183Ab905cf1fd4d7Cc49e41",
  'name': "GURU",
  #'name'l: "Nihdi",
  'decimals': 9
},
{
  'address': "0x33e94c00E11846f108C144737568cf1AFBE23B20",
  'name': "GURU",
  #'name'l: "Guru",
  'decimals': 9
},
{
  'address': "0x58c1BBb508e96CfEC1787Acf6Afe1C7008A5B064",
  'name': "HOGE",
  #'name'l: "hoge.finance",
  'decimals': 9
},
{
  'address': "0xEdf8E3Cde2411C46132b2126524EB0fE195028Dd",
  'name': "MEGAHOGE",
  #'name'l: "MegaHoge (like a whole lot of HOGE)",
  'decimals': 18
},
{
  'address': "0x1c8dD8d22c5417B3fe8033c8E73690956A2cbFE1",
  'name': "GIGAHOGE",
  #'name'l: "GigaHoge (like a lot lot of HOGE)",
  'decimals': 18
},
{
  'address': "0x71118EA77cf5d5D2B06e916C75804419574B6303",
  'name': "DUDE",
  #'name'l: "dude",
  'decimals': 18
},
{
  'address': "0xD7A298827BD8Ecb3E3ADb88aBf093AC982B7c368",
  'name': "WFC",
  #'name'l: "WO1FCOIN",
  'decimals': 18
},
{
  'address': "0x7114B8Fa679f8d2016E456e6d479a8d5380E4870",
  'name': "rrr",
  #'name'l: "rrr",
  'decimals': 18
},
{
  'address': "0x795dafBa614170E62E47d16A204616e6212aB116",
  'name': "MSC",
  #'name'l: "MUSIC",
  'decimals': 18
},
{
  'address': "0x665b386a421bc94Dbccc21923C731992B3E329Af",
  'name': "TOK",
  #'name'l: "TOKEN",
  'decimals': 18
},
{
  'address': "0x8a65151A6312E4CA8907c4510D8e90F50D51e914",
  'name': "tir",
  #'name'l: "trytry",
  'decimals': 18
},
{
  'address': "0xddEd32F03BFE6b8B0013415EB2758a64ea6c765E",
  'name': "GURU",
  #'name'l: "GURU ",
  'decimals': 8
},
{
  'address': "0x87F9F190a08fF32d86E778Cd3e1479A816072D10",
  'name': "ZHOP",
  #'name'l: "ZHOP",
  'decimals': 9
},
{
  'address': "0x5eF1292fa801a6D6f160981370d966DA9B72A8b0",
  'name': "GURU",
  #'name'l: "Guru",
  'decimals': 9
},
{
  'address': "0x057E0bd9B797f9Eeeb8307B35DbC8c12E534c41E",
  'name': "GURU",
  #'name'l: "Guru",
  'decimals': 9
},
{
  'address': "0x86139F0245d993eD3fC1f7824E261656AD231C29",
  'name': "LIQUIDGM",
  #'name'l: "liquidlockgm",
  'decimals': 18
},
{
  'address': "0xC9b23490280D38d2E0DfAd9B73e85499061c500b",
  'name': "GURU",
  #'name'l: "aGURU ",
  'decimals': 8
},
{
  'address': "0x33eBCB57ACbfe6b555332A365A810e6f512fad6F",
  'name': "OTR",
  #'name'l: "Otter",
  'decimals': 18
},
{
  'address': "0x8eC8d3e3dC0475Ce160Fe0aC9B15B0CEB96c9209",
  'name': "PLSW",
  #'name'l: "Pulse World",
  'decimals': 18
},
{
  'address': "0x7ac69FeC92c15fC27Bfe6782323A90A87c5D6cce",
  'name': "DEGEN",
  #'name'l: "Degenerate Gamblers Token",
  'decimals': 18
},
{
  'address': "0x457fB110F55c3627d1B418dCA1F56307f856de84",
  'name': "POLYWGMI",
  #'name'l: "POLYWGMI",
  'decimals': 18
},
{
  'address': "0xE06Bd4F5aAc8D0aA337D13eC88dB6defC6eAEefE",
  'name': "IXT",
  #'name'l: "PlanetIX",
  'decimals': 18
},
{
  'address': "0x70F7c1d03713bbaBe7C71DaDf721487978f550C6",
  'name': "METRO",
  #'name'l: "METRO",
  'decimals': 18
},
{
  'address': "0xAfa4EC99216fF294a99CB63dd26Aab6528D09F52",
  'name': "1ori",
  #'name'l: "Ariel Farrell",
  'decimals': 18
},
{
  'address': "0x3e66e42074DC857Cb66911B39755dA6B8b2C80e5",
  'name': "FOAM",
  #'name'l: "Foamr",
  'decimals': 18
},
{
  'address': "0xDEdCAA8FF7dCE584ED2eBBE908A7CD0c0556D8b7",
  'name': "PDC",
  #'name'l: "PandaCoin",
  'decimals': 18
},
{
  'address': "0x86ba07C251725Dad5e711659d5EFe62A6FE9d2A1",
  'name': "IPT",
  #'name'l: "Index Pool Token",
  'decimals': 18
},
{
  'address': "0xAaEaDf870Dc82430Ad65729DD98b65Cb9510CAca",
  'name': "FIR",
  #'name'l: "fire token",
  'decimals': 18
},
{
  'address': "0x74ABc691274Dff728475481d456e47ED921B2Ba8",
  'name': "PDC",
  #'name'l: "PandaCoin",
  'decimals': 18
},
{
  'address': "0x4f287583F7C0a19722256Ecd282398d224AC2D7A",
  'name': "ATS",
  #'name'l: "Ats Token Garden",
  'decimals': 18
},
{
  'address': "0x8f7c1e76599A7E5aBC10E2746E9c4FA74099d78B",
  'name': "PAPER",
  #'name'l: "PAPER V2",
  'decimals': 18
},
{
  'address': "0x09a3C431162a4Ddb791f86DE6D03e1851e4c0Eb0",
  'name': "l-2XDPI-Nov26",
  #'name'l: "Long 2XDPI Nov26",
  'decimals': 18
},
{
  'address': "0x6f370dba99E32A3cAD959b341120DB3C9E280bA6",
  'name': "wsKLIMA",
  #'name'l: "Wrapped sKLIMA",
  'decimals': 18
},
{
  'address': "0xed2f2C4811086aCC92235E5d9e77f743f50b1861",
  'name': "nff",
  #'name'l: "Hillary Trevino",
  'decimals': 18
},
{
  'address': "0x406986B465Ba454d56F76AC050732fEEe6F08998",
  'name': "qqq",
  #'name'l: "qqq",
  'decimals': 18
},
{
  'address': "0x5c9b7c81B72Ead172F18f947a616E672D73DF079",
  'name': "tttt",
  #'name'l: "ttt",
  'decimals': 18
},
{
  'address': "0xa56d5Ad7E9C11Da373b996e64E2995aDf4729656",
  'name': "iii",
  #'name'l: "ii",
  'decimals': 18
},
{
  'address': "0xae1c209A8375b02e0ae69d67999999BD0ADA169c",
  'name': "RHCP",
  #'name'l: "RHCP",
  'decimals': 8
},
{
  'address': "0x854fFf7c3a336E1194F3c6f44d7bc137aB294379",
  'name': "www",
  #'name'l: "www",
  'decimals': 18
},
{
  'address': "0x07fC484a81F3E3797FF0824aa356302E513Cb63d",
  'name': "SDN",
  #'name'l: "Shiden Network",
  'decimals': 18
},
{
  'address': "0x117F6F7E74847b1C29C272E65d1953308219abb7",
  'name': "ASTR",
  #'name'l: "Astar Network",
  'decimals': 18
},
{
  'address': "0x924c1120c53572B2eA95720cC8b5cC42614ef2eF",
  'name': "APE",
  #'name'l: "Ape Index",
  'decimals': 18
},
{
  'address': "0x57194feaca970A4E98A19C365FE144fB54F657DB",
  'name': "UFO",
  #'name'l: "THE TRUTH (PoS)",
  'decimals': 18
},
{
  'address': "0x1e1bC1EA99Fbd727914C4aE31eF091A103796BcC",
  'name': "C2",
  #'name'l: "Crypto Cigarettes ",
  'decimals': 18
},
{
  'address': "0xdFB75b53cbd28273c80e5D947f4C5Fbc9852bA2c",
  'name': "DUN",
  #'name'l: "DUNCAN",
  'decimals': 18
},
{
  'address': "0x25fd7f9434528687979275D367EcC5B3e3A8fa7A",
  'name': "TST",
  #'name'l: "My pool TOKEN",
  'decimals': 18
},
{
  'address': "0x55189C71194c75F7CD275092ed148Dc0D05Cfcca",
  'name': "NDX",
  #'name'l: "NgonDex",
  'decimals': 18
},
{
  'address': "0xb6D963F0fC41c0313F7fDcA4113fB09E9dAC27CE",
  'name': "poll",
  #'name'l: "pool token",
  'decimals': 18
},
{
  'address': "0xEFeE2de82343BE622Dcb4E545f75a3b9f50c272D",
  'name': "TRY",
  #'name'l: "TryHards",
  'decimals': 18
},
{
  'address': "0x5484886d3731eDd0058A217c8Ff06eFAE422fB36",
  'name': "FEO$",
  #'name'l: "FEOPOLY2",
  'decimals': 18
},
{
  'address': "0x0A796033990eFb0da1BE40eBD24203ae06850bCf",
  'name': "safebaby",
  #'name'l: "safebaby",
  'decimals': 18
},
{
  'address': "0xCfB8aeaDb266aAf77Da64A2FB32B520Ad142cb60",
  'name': "jeve",
  #'name'l: "juventus",
  'decimals': 18
},
{
  'address': "0xddC52a7595afC4Ad768425EC8D5077B79663AF6A",
  'name': "XANAX",
  #'name'l: "Xancoin",
  'decimals': 18
},
{
  'address': "0x5233abdD49A1d26d127aB0FaE03dFa9161F5F68B",
  'name': "PAJARITOS",
  #'name'l: "TESTBIRDS",
  'decimals': 18
},
{
  'address': "0x5e5f02A8219cd783ef6CB215cfc7992941db509D",
  'name': "PAJARONES",
  #'name'l: "TESTBIRDS2",
  'decimals': 18
},
{
  'address': "0x2E26E038B7aF7CA21f12A048cEA6cE80F33C80De",
  'name': "NROC",
  #'name'l: "MoonRoc",
  'decimals': 18
},
{
  'address': "0x452cDe08f78160145B27428CdCc4B117BD904259",
  'name': "NEKRO",
  #'name'l: "Nekrogoblikoin",
  'decimals': 18
},
{
  'address': "0xB2c0dda2063F395F04244402D6ab3d7402C2DD6f",
  'name': "ksfe",
  #'name'l: "kiss",
  'decimals': 18
},
{
  'address': "0xf28164A485B0B2C90639E47b0f377b4a438a16B1",
  'name': "dQUICK",
  #'name'l: "Dragon QUICK",
  'decimals': 18
},
{
  'address': "0x3924da4FB1070612433F89B459b60E6f49b6BEA6",
  'name': "LPD",
  #'name'l: "La Palma DAO Token",
  'decimals': 18
},
{
  'address': "0xb1Eb4BeA854a5910FE6d592bdFd65De44d2D9803",
  'name': "int",
  #'name'l: "inter",
  'decimals': 18
},
{
  'address': "0x8B4c53E751561175269289e1C722918999f10ae4",
  'name': "La2",
  #'name'l: "Azalia Espinoza",
  'decimals': 18
},
{
  'address': "0xe7a9B1Ac5AA9Ac04A361EF6B0e3D198E1Ff5EF35",
  'name': "DTOP_DEMO",
  #'name'l: "DTOP",
  'decimals': 9
},
{
  'address': "0x1294F670d5c92C24F4E0bbaF5eAB310f3B143B4C",
  'name': "ica",
  #'name'l: "stol",
  'decimals': 18
},
{
  'address': "0x43cD58207E58Fd3415179C414Efa27A80f8894a7",
  'name': "test",
  #'name'l: "test",
  'decimals': 18
},
{
  'address': "0x5B3dcB07244dCCBd22A42080AE8b35E7a7593ED3",
  'name': "$",
  #'name'l: "$",
  'decimals': 18
},
{
  'address': "0x8c6bc14C3149E99aa08d1FE2868d4025698fB519",
  'name': "ttkk",
  #'name'l: "ttokken",
  'decimals': 18
},
{
  'address': "0x918e2A9c9c3d9813890457e39A7924be6b29675e",
  'name': "$",
  #'name'l: "$",
  'decimals': 18
},
{
  'address': "0xa4eDecaBbC01A878b274e3A58d1002c6DAB04018",
  'name': "COBWEB",
  #'name'l: "COBWEB",
  'decimals': 18
},
{
  'address': "0x0542fe1e82633fEd2930542f8Dd51Ff0C598E715",
  'name': "GEN",
  #'name'l: "Genesis",
  'decimals': 18
},
{
  'address': "0xa63B340c25b58EDAe6DD1606f1B07Cb3c99847AE",
  'name': "testAMI",
  #'name'l: "test",
  'decimals': 9
},
{
  'address': "0xaaA49b31b42e210E829e985EF7e970faeC38e4B4",
  'name': "YKK",
  #'name'l: "YonkyKoin",
  'decimals': 9
},
{
  'address': "0x67161852BaDdFC1CA3B898E6156b780FcFfE758B",
  'name': "ARWNG",
  #'name'l: "Arwing",
  'decimals': 18
},
{
  'address': "0x03B82B2B7B33911CDdA0130c751f5D064354f323",
  'name': "MCN1",
  #'name'l: "MCoinFund1",
  'decimals': 18
},
{
  'address': "0x07e509E233BAFe16805aB8822093494D603720f6",
  'name': "DD",
  #'name'l: "Diamond Dollars",
  'decimals': 18
},
{
  'address': "0x71cc8410482767a4558989BCadA1A692E6F44457",
  'name': "SPD",
  #'name'l: "SPEED",
  'decimals': 18
},
{
  'address': "0xD125443F38A69d776177c2B9c041f462936F8218",
  'name': "FBX",
  #'name'l: "FireBotToken",
  'decimals': 18
},
{
  'address': "0x58aA24b719FB649C3114B8e50699ec4E40Fd82c7",
  'name': "Ver2",
  #'name'l: "Freya Bryan",
  'decimals': 18
},
{
  'address': "0x6C71aA1DB9c09D537a840f3BCD36B99E8A508C5a",
  'name': "2611",
  #'name'l: "TEST2611",
  'decimals': 18
},
{
  'address': "0x4d656759c94B5EE799B8FAe18ABA23d6739558aC",
  'name': "F26",
  #'name'l: "FINAL2611",
  'decimals': 18
},
{
  'address': "0xf01eB236bb31F21cB8505e2d546626c857F01226",
  'name': "ADD",
  #'name'l: "ASDASD",
  'decimals': 18
},
{
  'address': "0x375C22a8EF54cD743C1FB2F5F2df95BeD24b982B",
  'name': "TV5",
  #'name'l: "TESTV5",
  'decimals': 18
},
{
  'address': "0x43e7165f3466232A914eDf6C5B1654350F96F828",
  'name': "PYF",
  #'name'l: "Python Finance",
  'decimals': 8
},
{
  'address': "0x8cFbE527bCFdcE5651D9260c3421B5E3A09B2bCd",
  'name': "CRG",
  #'name'l: "CryptoGor",
  'decimals': 18
},
{
  'address': "0x2420943C8Ce4c0E16539F2ab1F663c973Bfb5640",
  'name': "STKS",
  #'name'l: "STKS",
  'decimals': 18
},
{
  'address': "0x7E88B6FC3Dd4899dBb3b418782E3719d145657d4",
  'name': "DIVO",
  #'name'l: "Divocakos",
  'decimals': 18
},
{
  'address': "0x594524c7E51292782757EBC13cbA0aB0a0d949Aa",
  'name': "CAON",
  #'name'l: "CaonCoin",
  'decimals': 18
},
{
  'address': "0x462fEBEc8323C7c4383d95Bf3576AeAf776ea5dd",
  'name': "JUMP",
  #'name'l: "Jump",
  'decimals': 9
},
{
  'address': "0xF84BD51eab957c2e7B7D646A3427C5A50848281D",
  'name': "AGAr",
  #'name'l: "AGA Rewards (PoS)",
  'decimals': 8
},
{
  'address': "0xc1c93D475dc82Fe72DBC7074d55f5a734F8cEEAE",
  'name': "PGX",
  #'name'l: "Pegaxy Stone",
  'decimals': 18
},
{
  'address': "0xCCb2568Ab18607f25c04226Aa1120F1025d69Cd1",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x2fBb70E452057ef8f87B143EBb68Aa12510612FB",
  'name': "FSR",
  #'name'l: "Tad Cunningham",
  'decimals': 18
},
{
  'address': "0xD6268B01ec22ccF339b03AA4EBBD1DaD46ec23fC",
  'name': "MAG",
  #'name'l: "Magcoin",
  'decimals': 18
},
{
  'address': "0xd058d61737E2eC840a2C4CfC2942cAEBDA1b4fD3",
  'name': "JUMP",
  #'name'l: "Jump",
  'decimals': 9
},
{
  'address': "0x9c2C5fd7b07E95EE044DDeba0E97a665F142394f",
  'name': "1INCH",
  #'name'l: "1Inch (PoS)",
  'decimals': 18
},
{
  'address': "0x6722Fc5eCf7a7d0A607790f62978622eF5D062d1",
  'name': "MARK",
  #'name'l: "Benchmark",
  'decimals': 9
},
{
  'address': "0x6968105460f67c3BF751bE7C15f92F5286Fd0CE5",
  'name': "MONA",
  #'name'l: "Monavale",
  'decimals': 18
},
{
  'address': "0xa4Dc6e03dFe83C31325D4BE56cF6B6ecbFe39823",
  'name': "MARK",
  #'name'l: "Benchmark",
  'decimals': 9
},
{
  'address': "0x831E5CE6B52Fe13655cE1D7FF3e813821200b9A7",
  'name': "CUBE",
  #'name'l: "CubeDAO",
  'decimals': 18
},
{
  'address': "0x8DF74088b3aeCfd0cB97BcFd053B173782f01e3A",
  'name': "KWIK",
  #'name'l: "Kwikswap (PoS)",
  'decimals': 18
},
{
  'address': "0xd72357dAcA2cF11A5F155b9FF7880E595A3F5792",
  'name': "STORJ",
  #'name'l: "StorjToken (PoS)",
  'decimals': 8
},
{
  'address': "0x4e9d760637DA87fe3003Adc8e1dAD2fE0aE3c671",
  'name': "EoC",
  #'name'l: "Essence of Creation",
  'decimals': 18
},
{
  'address': "0x7D5ba87BacdC5323C7349428740B2879e0330A37",
  'name': "WIT",
  #'name'l: "WIT",
  'decimals': 9
},
{
  'address': "0x8B93aB7a87d29c112cB34888b1892CBDC923f003",
  'name': "miln",
  #'name'l: "milan",
  'decimals': 18
},
{
  'address': "0x5b01F376A44653dD332942F089cA1c23f669B775",
  'name': "ttt",
  #'name'l: "lazio",
  'decimals': 18
},
{
  'address': "0x2e77F56bC9Ac39BD05D8c012075B47455777b8a0",
  'name': "MTALC",
  #'name'l: "TALESHCOIN",
  'decimals': 14
},
{
  'address': "0x6FEC029b2CB2b0E565f4840eCf41337E5705E8c4",
  'name': "QPQ",
  #'name'l: "Quid Pro Quo",
  'decimals': 18
},
{
  'address': "0xB2d957faE155B53721BbD6f091eE3E1750aCd17F",
  'name': "TTONE",
  #'name'l: "Test1",
  'decimals': 9
},
{
  'address': "0x49B1bE61A8Ca3f9A9F178d6550e41E00D9162159",
  'name': "GGTK",
  #'name'l: "GGToken (PoS)",
  'decimals': 18
},
{
  'address': "0x04568467f0AAe5fb85Bf0e031ee66FF2C200a6Fb",
  'name': "sGURU",
  #'name'l: "Staked Guru",
  'decimals': 9
},
{
  'address': "0x9fcfA0956683BED055988Ee65983756dF510D300",
  'name': "ABC",
  #'name'l: "ABCToken",
  'decimals': 18
},
{
  'address': "0x3BCdA500Eec201efC25fc1813C0D1A5f208437f3",
  'name': "jmt",
  #'name'l: "jhometic",
  'decimals': 18
},
{
  'address': "0x307c1e49B4C5ce5e08EDEE7b75853B4bc90482E3",
  'name': "BBB",
  #'name'l: "BBBoken",
  'decimals': 18
},
{
  'address': "0x27BB9487313F26b19025f8b84368051398eE1703",
  'name': "DKSH",
  #'name'l: "DakshKhyat",
  'decimals': 18
},
{
  'address': "0x3E64C23896e9f017CCCd002d5533ecC726323232",
  'name': "DLP",
  #'name'l: "DLP_3e64c238",
  'decimals': 18
},
{
  'address': "0x528d599CdcB19efc706CB79658d870553DE57F1b",
  'name': "BM",
  #'name'l: "Bridge mint ",
  'decimals': 18
},
{
  'address': "0x3062329e91DaEFd497E0b01b6180C283d51F7702",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xE7e61313adA763138159B6728Ae7c2Fc9A1cdE07",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x4fcd480262973A5a0521F1e9FeBc9DF86C04e67f",
  'name': "AT",
  #'name'l: "Armenian Token",
  'decimals': 18
},
{
  'address': "0xe1d3C6f2dC2bc587fD8934834B301093108A2C42",
  'name': "SAMI",
  #'name'l: "Safe Minu",
  'decimals': 9
},
{
  'address': "0x8d457BCa8c633AA28Baf9F3541580341A741B66f",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x3519f711619b418Dc8c99f3d10a378129E0F85c6",
  'name': "SAMI",
  #'name'l: "Safe Minu",
  'decimals': 9
},
{
  'address': "0x7737D589D7c153B71C44183E1403e597330D6BF4",
  'name': "BT",
  #'name'l: "BullishToken",
  'decimals': 18
},
{
  'address': "0x9f132C24E0981162223ee143b2169413b576B87D",
  'name': "TT",
  #'name'l: "TestToken",
  'decimals': 18
},
{
  'address': "0x7Dc47Cfb674bEb5827283F6140F635680A5cE992",
  'name': "BOLLY",
  #'name'l: "Bollycoin (PoS)",
  'decimals': 18
},
{
  'address': "0x9Bfd230a470173D301CB949d1E74F70b2C683E0F",
  'name': "CAPS",
  #'name'l: "BottleCaps",
  'decimals': 18
},
{
  'address': "0xe9248CdeE9Ec4A6f6aA0090F339313f85d131c27",
  'name': "PEPES",
  #'name'l: "Augusto",
  'decimals': 18
},
{
  'address': "0xAd1d50BDD82FfF71BAbdfa5cb170A598e142fE06",
  'name': "CTT",
  #'name'l: "Cultural Computing Token",
  'decimals': 18
},
{
  'address': "0x96ef559a89C64359B4408048c99e772793268a3d",
  'name': "BBST",
  #'name'l: "Bitcoin Hedge Token",
  'decimals': 18
},
{
  'address': "0xb1163002C7cB1892D8B188580E9B7E92dc140A49",
  'name': "PET",
  #'name'l: "PETToken",
  'decimals': 18
},
{
  'address': "0x263026E7e53DBFDce5ae55Ade22493f828922965",
  'name': "RIC",
  #'name'l: "Ricochet",
  'decimals': 18
},
{
  'address': "0xcc7E369f09b40B3cABf3e495D118F9c446821519",
  'name': "NYFD",
  #'name'l: "NYFD",
  'decimals': 18
},
{
  'address': "0xCAa7349CEA390F89641fe306D93591f87595dc1F",
  'name': "USDCx",
  #'name'l: "Super USDC (PoS)",
  'decimals': 18
},
{
  'address': "0x02677c45FA858B9fFec24fc791bF72cdf4A8A8Df",
  'name': "RicheSwap",
  #'name'l: "RicheSwap.io",
  'decimals': 18
},
{
  'address': "0x214f95e46270693590621e40d439B33a49BcDF80",
  'name': "roma",
  #'name'l: "roma",
  'decimals': 18
},
{
  'address': "0x31fCaC368Db3E972Cf93bf9523914Ae3Ea04f354",
  'name': "Corr",
  #'name'l: "Lucius Hickman",
  'decimals': 18
},
{
  'address': "0x921EA9db0A0f04115AB997Ee6B782D41Da60E278",
  'name': "csu1",
  #'name'l: "cameraSpeedUp1",
  'decimals': 18
},
{
  'address': "0x893Ec45A70AefdF12A8e1c16f448731eb52Fa279",
  'name': "wsu",
  #'name'l: "windowSpeedUp",
  'decimals': 18
},
{
  'address': "0x860bCD24cb93010473b9dd0dD39FfCB1Ce733A13",
  'name': "STONKS2",
  #'name'l: "STONKS2",
  'decimals': 18
},
{
  'address': "0x8e3A41dAEaC873A97c989c2B2DcC693FF9DE5d46",
  'name': "FNC",
  #'name'l: "FRENETIC",
  'decimals': 18
},
{
  'address': "0x46FEB5BE82aB66dB1662AAC6e58090721307895f",
  'name': "KOOKY",
  #'name'l: "KookyToken",
  'decimals': 18
},
{
  'address': "0x3f63721E521E56F2A540AFf5B0FC68895Ecfc215",
  'name': "TEST_DEMO",
  #'name'l: "TEST",
  'decimals': 9
},
{
  'address': "0xE15E0Bb3ea24B76Aa0481fB3715EB8E7C11978D6",
  'name': "SAU",
  #'name'l: "Sauron",
  'decimals': 18
},
{
  'address': "0xF671101C4187A23422B662EcD55B23BFe7dbc11C",
  'name': "MARK",
  #'name'l: "Benchmark",
  'decimals': 9
},
{
  'address': "0x838c6dA8fa8dE593aC59f2E18Dbbe3C050d833d8",
  'name': "DRLLA",
  #'name'l: "AndyLivesOn",
  'decimals': 18
},
{
  'address': "0xCF28274A6D3AaeD0aC10d5b9cEE61d2e04DeA56f",
  'name': "STONKS3",
  #'name'l: "STONKS3",
  'decimals': 18
},
{
  'address': "0xdAc90b281B099089d59960Df31108EE9604C5c36",
  'name': "STONKS20",
  #'name'l: "STONKS20",
  'decimals': 18
},
{
  'address': "0xebc5ad087804ee6386059ED103882E56ced2AeDe",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x2a19eCD88798E940f277317bb142B92D3A94CD23",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x7b3a30744C73db919a3c8089D01522a83D0559D6",
  'name': "FF",
  #'name'l: "FakeFrax",
  'decimals': 18
},
{
  'address': "0x4a9bdFdD47D8e3E17C89F6155e78e93b1B644A28",
  'name': "DAD",
  #'name'l: "Dads",
  'decimals': 18
},
{
  'address': "0xa0f891fFDc9f81F976EC169B79B5533F375FAC8B",
  'name': "TCN",
  #'name'l: "TCOIN",
  'decimals': 18
},
{
  'address': "0x0380487100985096A3DE9f338140c6CC041fF05E",
  'name': "INU",
  #'name'l: "INU",
  'decimals': 18
},
{
  'address': "0x98702fF897f51d5aA10Fb2DFC1AE44a0cC2966f3",
  'name': "QUI",
  #'name'l: "Orlando Gill",
  'decimals': 18
},
{
  'address': "0x38095b478d7f027BC90a98C9980e37ce5f3E7855",
  'name': "SIN",
  #'name'l: "Rhiannon Pope",
  'decimals': 18
},
{
  'address': "0x2324BCa641589f6bC530759415cd3b3Ed8056f1e",
  'name': "tsd",
  #'name'l: "Rashad William",
  'decimals': 18
},
{
  'address': "0x196783458Eb4142102d1F1B83D33302D42Ffb1Ca",
  'name': "sny",
  #'name'l: "sonny",
  'decimals': 18
},
{
  'address': "0xC250e9987A032ACAC293d838726C511E6E1C029d",
  'name': "CLAM2",
  #'name'l: "Otter Clam",
  'decimals': 9
},
{
  'address': "0xf7719cAA08Df8300e98627a88C19B567093d0504",
  'name': "ANT",
  #'name'l: "AnimalToken",
  'decimals': 18
},
{
  'address': "0xa9A8c2AF3290D9586759a8Db9513c4d4999451D5",
  'name': "BBR",
  #'name'l: "BountyBuilder",
  'decimals': 18
},
{
  'address': "0x84660c6F979Cd4A19B7e37954634Acfc42859912",
  'name': "MOM",
  #'name'l: "MOM",
  'decimals': 18
},
{
  'address': "0x7274Fb4e497c6C36A9a49cA24c098F07221483B3",
  'name': "HUSKY",
  #'name'l: "Husky Coin",
  'decimals': 18
},
{
  'address': "0xd8cA34fd379d9ca3C6Ee3b3905678320F5b45195",
  'name': "gOHM",
  #'name'l: "Governance OHM",
  'decimals': 18
},
{
  'address': "0x003eAB9075C6Fe49FC276B8Cca9Cfa3aE0F0593C",
  'name': "USDX2",
  #'name'l: "Xiaz Dollar Pegged",
  'decimals': 8
},
{
  'address': "0xb8ca540d92C17f79817C6Ec8794bA99bfd7e9aB1",
  'name': "LUXY",
  #'name'l: "LUXY",
  'decimals': 18
},
{
  'address': "0xD4945a3D0De9923035521687D4bf18cC9B0c7c2A",
  'name': "LUXY",
  #'name'l: "LUXY",
  'decimals': 18
},
{
  'address': "0xfEc4c82059e720E0cC614bf952cF5D91A71483c2",
  'name': "BANK",
  #'name'l: "Gringotts Bank",
  'decimals': 9
},
{
  'address': "0x98d9d01AC0e34109F26329ab999A4320089381F3",
  'name': "SHIBLONMOON",
  #'name'l: "Shiblon Moon",
  'decimals': 18
},
{
  'address': "0x091bC658C7e997C5bF1Dce7ddcC1113dA0e3C55E",
  'name': "ERTH",
  #'name'l: "Earth",
  'decimals': 18
},
{
  'address': "0x3eB177A6693eC81d1E170136f8AD02fffBE172a7",
  'name': "AUMI",
  #'name'l: "AutoMatic",
  'decimals': 18
},
{
  'address': "0xd7BD224D972c83669116c92C97eA0bE711A3A1e7",
  'name': "testGAS",
  #'name'l: "testGAS",
  'decimals': 18
},
{
  'address': "0x0Cc98f9494dc5218973aD312815e441BC92879C7",
  'name': "OITO",
  #'name'l: "Oito.work",
  'decimals': 18
},
{
  'address': "0xe26bCC38B72279c31617D3227b9dECFd9F04f40c",
  'name': "GGG",
  #'name'l: "Golden Chain",
  'decimals': 18
},
{
  'address': "0x76548CCbe16ff729d5CeE793b4fFd9773C98EF01",
  'name': "TGD",
  #'name'l: "Lacy Mckay",
  'decimals': 18
},
{
  'address': "0xD0513DB39d87e8825389fEB10BD911dC53B3a153",
  'name': "FINT",
  #'name'l: "Fintropy",
  'decimals': 18
},
{
  'address': "0x60bb86D2F66e4DB57e5f9B99D987B0A79e0787B0",
  'name': "FINT",
  #'name'l: "Fintropy",
  'decimals': 18
},
{
  'address': "0x7E53933c21B44fD59b5adaa89c98fA19Aad00455",
  'name': "RMK",
  #'name'l: "Papiermark",
  'decimals': 18
},
{
  'address': "0x3D1a00C514763f69e356D03C2a900648f97FE7E6",
  'name': "DGH",
  #'name'l: "Blake Hunt",
  'decimals': 18
},
{
  'address': "0x3Ad707dA309f3845cd602059901E39C4dcd66473",
  'name': "ETH2x-FLI-P",
  #'name'l: "ETH 2x Flexible Leverage Index",
  'decimals': 18
},
{
  'address': "0x46b67d2fA15a2b166D6d37B06a8235Fb73dd8faE",
  'name': "DOG",
  #'name'l: "Liberty Heath",
  'decimals': 18
},
{
  'address': "0x1f6D0928E6d28379345f0c7cb1aE1E60246A719D",
  'name': "TCT",
  #'name'l: "TheCoolestToken",
  'decimals': 18
},
{
  'address': "0x7d060E1F8857c5A1d0C2b460CB589a1FA05ee85e",
  'name': "HYT",
  #'name'l: "Eagan Irwin",
  'decimals': 18
},
{
  'address': "0xD4814770065F634003A8d8D70B4743E0C3f334ad",
  'name': "ONT",
  #'name'l: "Poly-Peg ONT",
  'decimals': 9
},
{
  'address': "0x348e62131fce2F4e0d5ead3Fe1719Bc039B380A9",
  'name': "PYR",
  #'name'l: "PYR Token",
  'decimals': 18
},
{
  'address': "0x3Cc1c73fB0Cf5e2cFC636Edbc128Af968A2b3d84",
  'name': "RXC",
  #'name'l: "Rexxcoin",
  'decimals': 5
},
{
  'address': "0x832E8B330D8f0bcAF184e9EEB32B445e1B5D74d2",
  'name': "QPQ",
  #'name'l: "Quid Pro Quo",
  'decimals': 18
},
{
  'address': "0xDddc0d6ce229164ec73e2075f488824B1E033EF5",
  'name': "ATL",
  #'name'l: "Falcons - Super Bowl QPQ",
  'decimals': 18
},
{
  'address': "0xA8E0004799f98555701C7b6BB2e6eec7aF4A9BE0",
  'name': "NE",
  #'name'l: "Patriots - Super Bowl QPQ",
  'decimals': 18
},
{
  'address': "0xfcf137C95d5cb2542f3af9d24Cd3aA0babf0393F",
  'name': "FCT",
  #'name'l: "Fat Cat",
  'decimals': 18
},
{
  'address': "0x0c87294df2B65Ff4Cb2E2A4045512606F1f8C1CE",
  'name': "Beat",
  #'name'l: "Beatitudes Prospers Coin",
  'decimals': 18
},
{
  'address': "0x632527567de4977A4C5bf8c20F85f9064285D700",
  'name': "MTA",
  #'name'l: "Matcha",
  'decimals': 9
},
{
  'address': "0xA3F0AB07f9198BC65a1a211433AC1395c81ba207",
  'name': "Fu",
  #'name'l: "Fu Blessing",
  'decimals': 17
},
{
  'address': "0x454F2e567aA8e42e74684995E2Bee7E355B03084",
  'name': "Jesus",
  #'name'l: "Jesus Love You",
  'decimals': 17
},
{
  'address': "0x1EB446C015885155B4c3491D9BB20868Dcbc22E5",
  'name': "SofaNauts",
  #'name'l: "StarShipSofa",
  'decimals': 9
},
{
  'address': "0x213e886C8aa8506e309507531585b72A8913f1A9",
  'name': "CHT",
  #'name'l: "CHT",
  'decimals': 18
},
{
  'address': "0x0542BFa9Eb020432F5f413fCa8A4a3B37571bFd5",
  'name': "TANFT",
  #'name'l: "Taiwan Artist NFT Token",
  'decimals': 18
},
{
  'address': "0x0D1084883FA87e884C15a29c5832a19A1e4c9765",
  'name': "COX",
  #'name'l: "Cox",
  'decimals': 18
},
{
  'address': "0x5878E998542d87CC0f668F4207b95e090D85F110",
  'name': "POK",
  #'name'l: "Idola Rush",
  'decimals': 18
},
{
  'address': "0x3eCdeB8fC5023839B92b0c293D049D61069e02b1",
  'name': "GENX",
  #'name'l: "GenX Token",
  'decimals': 18
},
{
  'address': "0x5cfDF4CCa482d419dA979C10B70039c28F2a1f08",
  'name': "JAX",
  #'name'l: "JAX Token (PoS)",
  'decimals': 18
},
{
  'address': "0x1F435c17d7Ff631218827F9BA43a696650a9D512",
  'name': "LMLT",
  #'name'l: "Limelight (PoS)",
  'decimals': 18
},
{
  'address': "0xdEC11a43d621C5259C35Ab24Fd30AfE0525cF030",
  'name': "7sp",
  #'name'l: "7coin",
  'decimals': 18
},
{
  'address': "0xf52D8Ebf5C84665c4C4d76660fe7969b7100E820",
  'name': "PCH",
  #'name'l: "Poochie",
  'decimals': 5
},
{
  'address': "0x5fBC60ACe9f8989196a0928f3f0F699aaF59099E",
  'name': "GRA",
  #'name'l: "Grant",
  'decimals': 18
},
{
  'address': "0x07c6040d6B9EC07346E1dA22DfE25B32EEC6F922",
  'name': "ETH",
  #'name'l: "Lesley Black",
  'decimals': 18
},
{
  'address': "0xD3C2e3eFc17eD355eFE05A5A9a6c94587fDba7c9",
  'name': "FUZZ",
  #'name'l: "fuzzy logic",
  'decimals': 18
},
{
  'address': "0x91ab4459A4054164148Ec9652968b6265603114B",
  'name': "JCCOIN",
  #'name'l: "JcToken",
  'decimals': 18
},
{
  'address': "0xfACf3F677B94A979C627B4556e06CD72994f5bCe",
  'name': "FLEX",
  #'name'l: "FlexToken",
  'decimals': 6
},
{
  'address': "0x788ebdadB245Ad809d38f0d4Bd3CDAc2f2703B8b",
  'name': "XIAOYUN",
  #'name'l: "Xiaoyun",
  'decimals': 18
},
{
  'address': "0x2f8c7ffe46DFF519FB6E8F61b1E0b5D07eAfe3aA",
  'name': "MARC",
  #'name'l: "Marc",
  'decimals': 18
},
{
  'address': "0x7a8EeA30E9aA9448701a780dADA19234eae6b2F5",
  'name': "LTK",
  #'name'l: "LietuvosTOKEN",
  'decimals': 18
},
{
  'address': "0x0FE2b011B80eE8Dba80B1558aa60E0730ddC08B7",
  'name': "OGC",
  #'name'l: "OGCoin",
  'decimals': 18
},
{
  'address': "0x2484BCa09F9A4F3E4b0a3C56690527CFa8c8DD63",
  'name': "TOKX",
  #'name'l: "tokenX",
  'decimals': 18
},
{
  'address': "0x2e502BF17E29fe9D59F616501A1d189e93fC676f",
  'name': "808TA",
  #'name'l: "808TA",
  'decimals': 18
},
{
  'address': "0x1A87df9F6109818BC7b62FED74b65Bd2F7e075b2",
  'name': "TEST",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0xBB7B33aAfBDF128650ccd8d46407e508BF009Ae0",
  'name': "GOMI",
  #'name'l: "GOMI",
  'decimals': 18
},
{
  'address': "0xa5b0f8A3A71C795c279a45d4703046616FEA73C4",
  'name': "GDT",
  #'name'l: "Channing Robles",
  'decimals': 18
},
{
  'address': "0x6837DD0ac03F4d62072feabE2C1B14C027C14984",
  'name': "yty",
  #'name'l: "Ferris Mueller",
  'decimals': 18
},
{
  'address': "0x461349B6f788731EBE02f039B8153b9B60CaD424",
  'name': "BDG",
  #'name'l: "Amela Odom",
  'decimals': 18
},
{
  'address': "0xe9BE0c92914a517C1f7f16ECD2de9980903cA9a3",
  'name': "LOL",
  #'name'l: "Dane Fox",
  'decimals': 18
},
{
  'address': "0x313d65FbAd15EC98a802586Bb90c0b74772B25E0",
  'name': "VDG",
  #'name'l: "Luke Martinez",
  'decimals': 18
},
{
  'address': "0x9b9fd017e08FFeEfd781cEa07440E8C1A3230199",
  'name': "MNL",
  #'name'l: "TaShya Mccarthy",
  'decimals': 18
},
{
  'address': "0x742767c19aAFacCd01A92c5503004869C94c73A7",
  'name': "GEN",
  #'name'l: "Genesis",
  'decimals': 18
},
{
  'address': "0x69628e74b1A46AB9AdE0dd85ab55Ae50568380DD",
  'name': "GEN",
  #'name'l: "Genesis",
  'decimals': 18
},
{
  'address': "0x51Fd44E6bD7B45ECdA874C568bbD67995a0a40B9",
  'name': "KDG",
  #'name'l: "Micah Clements",
  'decimals': 18
},
{
  'address': "0x85bE46e058Ee5c141368Fe4CA5490a26d3e45b7e",
  'name': "HUU",
  #'name'l: "Aimee Barber",
  'decimals': 18
},
{
  'address': "0xf9Bf364578ec37A50035A388c5e32805cc1aF6a9",
  'name': "MOP",
  #'name'l: "Salvador Leblanc",
  'decimals': 18
},
{
  'address': "0x27845cFFF80407100481d2eEF169e9887D641939",
  'name': "HILLTOP",
  #'name'l: "Hilltop",
  'decimals': 18
},
{
  'address': "0x8BFEF97813bFb1DEF7c9Ab0D3559CE042747d9E7",
  'name': "TSTLQ",
  #'name'l: "Test Liquidita",
  'decimals': 9
},
{
  'address': "0x636f87ee296E3cB8d89d28039BA97bb9Fb350093",
  'name': "SwissBot",
  #'name'l: "0xsbc",
  'decimals': 18
},
{
  'address': "0xC5B57e9a1E7914FDA753A88f24E5703e617Ee50c",
  'name': "POP",
  #'name'l: "Popcorn (PoS)",
  'decimals': 18
},
{
  'address': "0xDa3Bd278a39AE57439eE26B361118173bC70f21F",
  'name': "EGPT",
  #'name'l: "EGPTEX",
  'decimals': 18
},
{
  'address': "0x1A158f156b0b387Ce995E8009571BEb241A3d90f",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0xD02bEd96a2e46D3FdC58fD960f440206DAa8b256",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0xd4C0c5dDA03c6b3e911CD8DE1D10863E19b751C6",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0xe6c4E42B89998d21e84DBb8CB7E8BED279757AA9",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x0A7a35c8d104878C72AC76665F7849BA2715C728",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0x6a2aA07090AA69b450945d11eFc73daaad258A57",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x89a9a2d21D7Df668cd752F344964f74b4f1996c2",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0xe5C440f3d079c9F1F12865cf980Db85f063C4eF5",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0x353882967aBfC4F3d0546f5bA5191a338346D712",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xf700213700B310c5717C57074c345aeB2057F5Ee",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0xfA3C310fEC7eF958272cc64b0B3226A57ea0dC52",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0xa483E19fECD66a8687A67ebd51d76D1896902919",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0x27D3CA4607F8D9E9cfd79f7451Ac141251c4DF4b",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x903538578659265118472adA9C792bf157F1c9ea",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0xa0bd33490f21ad8148503e47DAe59207A1bA5B6c",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0xE308C321aFeCEe577301A94B2Af1E81460F69328",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0x9C62B5079e994165d8BC7A12b46Be079047dA5C7",
  'name': "PGC",
  #'name'l: "Pugcoin",
  'decimals': 18
},
{
  'address': "0x043e45A17e994B180Efe3Ba84bf866d1De35A3e8",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0x917c5e8CE2a92794D0d57C80bB4CEeA9Da5bdb8d",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0xB66a66285181FC6e927E49bB4bBcAa98B65fBd5d",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xc30BF33e262E5590Aaa616234c94abaE686e40eD",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0xCbEa2812b2d2D387fc9c871da55F70e6F470f70D",
  'name': "safe-meta",
  #'name'l: "Safe Metamask License",
  'decimals': 0
},
{
  'address': "0x491380EaA3462069948B7503739e145BB6A0a27e",
  'name': "ftt",
  #'name'l: "fttoke",
  'decimals': 18
},
{
  'address': "0xaa0fb99C05A7312Db814026e79404238B441312C",
  'name': "TKFD",
  #'name'l: "Melodie Valencia",
  'decimals': 18
},
{
  'address': "0x9DCED98e2030A1596609200952B5578Fac2aB517",
  'name': "MTKPROVA",
  #'name'l: "MyTokenProva",
  'decimals': 18
},
{
  'address': "0xfE22Ec61Cbb4059afc38124E6D5ad0eFDE019639",
  'name': "APA",
  #'name'l: "Ella Hobbs",
  'decimals': 18
},
{
  'address': "0xb393a6070e4149B80d7841a8189c71b3ddb16B11",
  'name': "BUSD",
  #'name'l: "BUSD",
  'decimals': 18
},
{
  'address': "0xbc1a6023BeE61EE80A5702cF1595D0f17B91Ca1e",
  'name': "TEST",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0xDc6da1A1251608Fc6B82fD66c89D9dfA3c3D09b5",
  'name': "EAT",
  #'name'l: "Chastity Wright",
  'decimals': 18
},
{
  'address': "0xFB05912093218a563776CF7f2C0733d16DfAa33D",
  'name': "51A",
  #'name'l: "Alien51",
  'decimals': 18
},
{
  'address': "0x09C5a4BCA808bD1ba2b8E6B3aAF7442046B4ca5B",
  'name': "VSP",
  #'name'l: "VesperToken (PoS)",
  'decimals': 18
},
{
  'address': "0x416E244f3f46A26B6a9d5b81c325cce0Ba0114Df",
  'name': "ZXVC",
  #'name'l: "ZXVC",
  'decimals': 9
},
{
  'address': "0x96528afFf7742E0542A57237EAa0092EE0e5351a",
  'name': "ETHM",
  #'name'l: "Ethereum Meta (Wormhole)",
  'decimals': 18
},
{
  'address': "0x7D3dfd002e174DC1AcE793b0ffD46F03ef24dB31",
  'name': "REVUSD",
  #'name'l: "REVUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0x259C7270305CBF2099463bE6b2F951709F5c1f53",
  'name': "REV",
  #'name'l: "REV Protocol Share",
  'decimals': 18
},
{
  'address': "0x62A3C5d6346A842d24053D871Ebe908A78cb46ab",
  'name': "EVEM",
  #'name'l: "EVER META (PoS)",
  'decimals': 18
},
{
  'address': "0x0E541510921F63C05aBFC12331ac43E58FC8b1D3",
  'name': "GGGG",
  #'name'l: "GGGG",
  'decimals': 18
},
{
  'address': "0x8177DD1F0082BD4eb1E55a2932Cc92EC90ac0D7A",
  'name': "XBNCH",
  #'name'l: "XCHAIR TOKEN",
  'decimals': 8
},
{
  'address': "0xd3d03Ca035DE4Edca6E2421aF1B31EB4f261f132",
  'name': "VDGF",
  #'name'l: "Wayne Campbell",
  'decimals': 18
},
{
  'address': "0xF30A835DbF9eC1850663085a6Bf1ec9E7aE78884",
  'name': "FDG",
  #'name'l: "Mikayla Casey",
  'decimals': 18
},
{
  'address': "0x3989E748bC196BF2ac68AfB28F23a9747154A824",
  'name': "TOKN",
  #'name'l: "the token",
  'decimals': 18
},
{
  'address': "0x539FC8fD6e07b6b27Fc3A3062d1C4DcC1984f981",
  'name': "ERT",
  #'name'l: "Fitzgerald Michael",
  'decimals': 18
},
{
  'address': "0xa75998F2DC7be70E8b10c34C2e47e7cfE076438c",
  'name': "VOL",
  #'name'l: "Isaiah Ferrell",
  'decimals': 18
},
{
  'address': "0xE3e77171b0Cccc2293EA48F0430F75F1a6103f78",
  'name': "GEN",
  #'name'l: "Genesis",
  'decimals': 18
},
{
  'address': "0x5FfB435F9Aacc005391C05Da461B75286F27C129",
  'name': "TRCH",
  #'name'l: "Trump Christmas",
  'decimals': 9
},
{
  'address': "0xFDDf8F3C7e610610E61113e5061827F3D401b84B",
  'name': "SABR",
  #'name'l: "SABRIS",
  'decimals': 18
},
{
  'address': "0x2E68a16aE558906b407Ef43fe062C4eBFAD7B753",
  'name': "TBD",
  #'name'l: "Token BD",
  'decimals': 6
},
{
  'address': "0x2F5eF983fe245e5dC827FE3F380DBE70Cdcf216B",
  'name': "WOONE",
  #'name'l: "Wrapped OnlyOne",
  'decimals': 18
},
{
  'address': "0x62B14A99b964359BF9cD3049df59a0655B99cbb7",
  'name': "COMM",
  #'name'l: "Derek Mcdaniel",
  'decimals': 18
},
{
  'address': "0x46D63bEEd70265ae3d4ECa7ECB720cF98954cc86",
  'name': "ENS",
  #'name'l: "Ethereum #'name' Service",
  'decimals': 18
},
{
  'address': "0x080aA1B0506Da10D3C8BB306aE11874899138B6A",
  'name': "REDPILL",
  #'name'l: "RED PILL TOKEN",
  'decimals': 18
},
{
  'address': "0x1E84e79526Fc0cCF35b07191E4488B90d9CAbD9f",
  'name': "VDF",
  #'name'l: "Melvin Flynn",
  'decimals': 18
},
{
  'address': "0x3E9813D86Ada4836DdFC01a26784E1Bd7C92A6a0",
  'name': "SAP",
  #'name'l: "Jorden Castaneda",
  'decimals': 18
},
{
  'address': "0x02188348dB637BD6fdAc95cc8F1EAfBfcf611945",
  'name': "tBAYC",
  #'name'l: "Tokenized BAYC",
  'decimals': 18
},
{
  'address': "0x4eeB587E9235475A256bDA69b44f2Dd59033C89d",
  'name': "yCRO",
  #'name'l: "YMicro Cap",
  'decimals': 18
},
{
  'address': "0x00A6FF3d29d72D238082173e33d7a15c72359CE3",
  'name': "GTAV",
  #'name'l: "GTA V CASH",
  'decimals': 18
},
{
  'address': "0x4c28f48448720e9000907BC2611F73022fdcE1fA",
  'name': "WETH",
  #'name'l: "Wrapped Ether",
  'decimals': 18
},
{
  'address': "0xC8e3Ebc1DBBebc7E92a507B8e888Ff1648129A72",
  'name': "GAL",
  #'name'l: "Galactic Empires",
  'decimals': 18
},
{
  'address': "0xD8379ce76b414436229045f27C54c16DbE660a51",
  'name': "DGTR",
  #'name'l: "Nelle Byers",
  'decimals': 18
},
{
  'address': "0x4d4c268264901b4F20Da9e8dD7762Fe250f7C23e",
  'name': "PROD",
  #'name'l: "Productivity",
  'decimals': 18
},
{
  'address': "0x9611452965b63cFeA2C9774e5386AB6D4F0abf16",
  'name': "IND",
  #'name'l: "Indorse Token (PoS)",
  'decimals': 18
},
{
  'address': "0x73360e88Ee1D124E7dBcA250dB529Ca6220F76D2",
  'name': "REDPILL",
  #'name'l: "RedPill",
  'decimals': 18
},
{
  'address': "0xfF2035C39c7Ed6981fB61aB75f436A098305eD43",
  'name': "SHERMAN",
  #'name'l: "MongooseCoin",
  'decimals': 18
},
{
  'address': "0x610762690b97B3634190bad96026b29C9CEF1c8C",
  'name': "LARRY",
  #'name'l: "Larrycoin",
  'decimals': 18
},
{
  'address': "0x3697C1Bdee2cE80Dc845022f5938007a101Dd7a8",
  'name': "GROW",
  #'name'l: "DEFI SEED",
  'decimals': 18
},
{
  'address': "0x05E5C2EcC4d4e95b15f9A3BC45803B7612C2E620",
  'name': "t1",
  #'name'l: "test1",
  'decimals': 9
},
{
  'address': "0xEAeCC18198a475c921B24b8A6c1C1f0f5F3F7EA0",
  'name': "SEED",
  #'name'l: "Seed (PoS)",
  'decimals': 18
},
{
  'address': "0x45B5F9F7eaf4CcFD4b8035BE84191C6E5e57dF3A",
  'name': "TMFI",
  #'name'l: "The Metaverse Futures Index",
  'decimals': 18
},
{
  'address': "0xEe9A352F6aAc4aF1A5B9f467F6a93E0ffBe9Dd35",
  'name': "MASQ",
  #'name'l: "MASQ (PoS)",
  'decimals': 18
},
{
  'address': "0x7c123a3eE274a10B85b282E9B0F026B94d50fDD7",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0x9853BebecE8cFe7063b4557B31dC4Aa7dad670c5",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0xb1C9f075f81F989402013Eb4ba06711EaB0E05fE",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0xE689f912aDF91271e2608Cffcd5342517304798a",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x2fC50b83271d5B594f547c8d75D36fB0e8079693",
  'name': "LOM",
  #'name'l: "LOMAS",
  'decimals': 18
},
{
  'address': "0x443607DdAdD1be9e94c681eab4464BD0c6eBB2dF",
  'name': "WMYT",
  #'name'l: "WMYT",
  'decimals': 3
},
{
  'address': "0xb3229469d613Cb8c2dE89c5096d1fCaaDC9Ce1e4",
  'name': "GML",
  #'name'l: "Gaming Life ",
  'decimals': 18
},
{
  'address': "0x8f40efd7cA11938310eb86E98a34b948044b705a",
  'name': "NKL",
  #'name'l: "Nikel",
  'decimals': 18
},
{
  'address': "0xdD2AF2E723547088D3846841fbDcC6A8093313d6",
  'name': "GOGO",
  #'name'l: "GOGOcoin",
  'decimals': 18
},
{
  'address': "0x12275273B54ea40A728A6BC5300b3e837e648050",
  'name': "BTOR",
  #'name'l: "BALTIMORA",
  'decimals': 18
},
{
  'address': "0xD53a22b6039667675FB597D8d3826d9A525Af6ac",
  'name': "PPRO",
  #'name'l: "PARABOLICPROFIT",
  'decimals': 8
},
{
  'address': "0xC3E35245040375c5939c0139b18C588d75CB5873",
  'name': "MONGOOSE",
  #'name'l: "Mongoose Coin",
  'decimals': 18
},
{
  'address': "0xadd053A09F95E565B25d8b9B84D0fcFaa962465E",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x31019E5Ebc6a834c9F6333B948758e6c7985Fd98",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xe6289aFE6CD1EA91c4D91f7Fb455b6d11Db84c1d",
  'name': "HXY",
  #'name'l: "HEXLY",
  'decimals': 18
},
{
  'address': "0xEFe243F48148F948212061e6C819e83ba4eF7a7d",
  'name': "PEBO",
  #'name'l: "PEBO Coin",
  'decimals': 9
},
{
  'address': "0xB73cDC71247fDF8160DA2B003e28E0a847a20cA6",
  'name': "ILM",
  #'name'l: "I Like Myself",
  'decimals': 9
},
{
  'address': "0xC0BDFCAD70e456a666A2881EF6E550b8906538b4",
  'name': "$TITS",
  #'name'l: "Test This Shit",
  'decimals': 8
},
{
  'address': "0x167F7993791406186a461EfB7059C701b0286A81",
  'name': "XME",
  #'name'l: "Meme Economy",
  'decimals': 18
},
{
  'address': "0xEeEa11157D80Ab4e469De2ea82e21f048864AeF5",
  'name': "CANDYS",
  #'name'l: "Candy Devil NFT",
  'decimals': 9
},
{
  'address': "0xc2b09f78EeE5D2c7879b6D11D9e397201C8f3970",
  'name': "SEBA",
  #'name'l: "SEBAS",
  'decimals': 18
},
{
  'address': "0x23001f892c0C82b79303EDC9B9033cD190BB21c7",
  'name': "LUSD",
  #'name'l: "LUSD Stablecoin (PoS)",
  'decimals': 18
},
{
  'address': "0xF868939Ee81F04f463010BC52EAb91c0839eF08c",
  'name': "ATK",
  #'name'l: "Attack",
  'decimals': 18
},
{
  'address': "0x04429fbb948BBD09327763214b45e505A5293346",
  'name': "ABR",
  #'name'l: "Allbridge",
  'decimals': 18
},
{
  'address': "0x4c4F242cC1F5c83Df875458Bf817FF72f0004086",
  'name': "M&C",
  #'name'l: "Mars&Cars",
  'decimals': 18
},
{
  'address': "0x4293A4BffB425d423f1C506DEBA297293d6c1Ec5",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x000D613f1051CeE1229C5144d02d40459EEB7a08",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0xB199F6529d3619674Cf9732F8a63Ca1f4a827873",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x272B72744d18A5960652b8f11430dDA090ed49d3",
  'name': "META",
  #'name'l: "metaDAO",
  'decimals': 18
},
{
  'address': "0x8d82195494F8dA6cf65D24047ABdd06d9Cf81562",
  'name': "VEL",
  #'name'l: "Mallory Coffey",
  'decimals': 18
},
{
  'address': "0xb3295D49f8737af46Fe32797229dd11a153D11f9",
  'name': "Utopia Game",
  #'name'l: "Utopia Game",
  'decimals': 8
},
{
  'address': "0x555FB66071288B01CEfb1226831957716b95f02a",
  'name': "BLAQCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x2B3b875FCb81852A13Cc1aA69B7e5A3352DB49c8",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x60Dad7F0e4cC04359140d99487eDBD968fd63b0c",
  'name': "FakeFrax",
  #'name'l: "FakeFrax",
  'decimals': 18
},
{
  'address': "0x6a0e1035049CF6b5F07172E2a6F11F9C66a786a3",
  'name': "FakeFrax",
  #'name'l: "FakeFrax",
  'decimals': 18
},
{
  'address': "0x6f008c07E43aeb5fA1afe4B0578747ea84e362a5",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x99cEd5F65518a6CcDCE65EBc8977018adc502b0b",
  'name': "BLAQCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x1f9F0a6C66e87b755691c6c8912a7746ed0edE01",
  'name': "BLAQCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x1f42Ec453E7642D55b22e7AaeFf22401856a0937",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0xaE562ee56f1Ff02dC52DfaE8364e845626C99BbC",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x9de376A7559309CA95ceB12A01ebE7F8FC035B31",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x2b8280f8D0515859084A5a58B3427d7080614f16",
  'name': "SANDM",
  #'name'l: "Sand Matic",
  'decimals': 18
},
{
  'address': "0x9Cb74C8032b007466865f060ad2c46145d45553D",
  'name': "IDEX",
  #'name'l: "IDEX Token (PoS)",
  'decimals': 18
},
{
  'address': "0xd67272b68148e0cD5944D07Cc28E5C6e3e352c04",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x73e4B7697bdBfBEA5E89a1f2a43E7cB47C52f546",
  'name': "GG",
  #'name'l: "GOODGAME",
  'decimals': 18
},
{
  'address': "0x42eA65bc60D5932b33c44985E4352F86cF9E5Aa6",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x785a0c64D6e7c533574FAf42D258C070C3D973d0",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0xc5498Bc75B8852250D895A061e00232E340f4A46",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0x1066c6753FFaf8540F691643A6D683e23599c4ab",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0x125086dbDeb0DE70fa3ab70Ec22aE3509D97467a",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0x57ccb25CCdae2700F5CE636FeC48B5B743BFA2A4",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0x815540Ba44cdA902d53F7C3f9c45BfcdFD460Ccc",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x9CFF81630c4d37CDb56d6342238A40BF7d7Bde05",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0x6d332bA62B24a14DC5117A47Ca1017C3861EBAdE",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xbcca2453Dd44A6cd7a0824C7Ae5835C5BD4247c5",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0xE18bb653FB8FfE49E811DD727CeF3EaAb6C69f95",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0xf9626089AC519a7BBFD4b1985aD96E5694D86d58",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0x91943239bD6F6A37f72F9E35Bb26795fB9ceacEC",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0xF1a0E6e694F458614FEcA96ee6829025A3D39DD2",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0x1977b1bbdcBBbf232a4A8F2b9c0490eD7a57BB3E",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xEB65BB1Cc1C956e39408f0CD93EC76378c13a825",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0x821B40ec40bDB030dB7d2c07C34eb67e5459267c",
  'name': "INC",
  #'name'l: "IBNCOIN",
  'decimals': 18
},
{
  'address': "0x76D0e957c9213ae9cb80aA1a8bff3DC2f87462a2",
  'name': "EST2",
  #'name'l: "Octavius Dillon",
  'decimals': 18
},
{
  'address': "0x11f683f09eAA2791a47283BE5246A25F2C549404",
  'name': "ETA",
  #'name'l: "Breanna Steele",
  'decimals': 18
},
{
  'address': "0x7c3F9bc020A8FdFeFE4dE72b3D140E8FCb4Dd2DE",
  'name': "DUIS",
  #'name'l: "Jorden Bridges",
  'decimals': 18
},
{
  'address': "0x335dc4875607a0684a5B3f6988BE717ED250C12C",
  'name': "SINT",
  #'name'l: "Kylee Torres",
  'decimals': 18
},
{
  'address': "0x0372273ED72270374A51C4316BCE4a13b7a887d3",
  'name': "SSS",
  #'name'l: "ssss",
  'decimals': 18
},
{
  'address': "0x63aD78D8007030130bB5b40E48B0FA2Cc700f294",
  'name': "ALTS",
  #'name'l: "ALTS Token",
  'decimals': 18
},
{
  'address': "0x400C10A734816493EF5f612947074403B723e38d",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x23416f3E95Ee746D71788D26bDD0968CfB03cFB3",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x280adbf34314c7794f67D8E05fF631B3Fbd982EF",
  'name': "t3",
  #'name'l: "test3",
  'decimals': 9
},
{
  'address': "0xb836Ef888F88895cc7852110f5A121f94DF107D2",
  'name': "t3",
  #'name'l: "test3",
  'decimals': 9
},
{
  'address': "0x8f956E187bdc8d3c4bad99DCf22e65D183572858",
  'name': "KTN",
  #'name'l: "KlausToken",
  'decimals': 18
},
{
  'address': "0x3a68028Ebd27DD4fd8889d90b825aC8Ea06BEf8f",
  'name': "PLASMA",
  #'name'l: "Plasma",
  'decimals': 0
},
{
  'address': "0xeE1a4A2784DE6f25C42848f7c82fb2D314d1d80D",
  'name': "UNI-V2",
  #'name'l: "Uniswap V2",
  'decimals': 18
},
{
  'address': "0x1948Ab93A74c768E641E974015278F447712c0F1",
  'name': "SGP",
  #'name'l: "ShomonGreenPolymer",
  'decimals': 18
},
{
  'address': "0xf504B682Bd08b65cFf95f82255687DC0CE2fb5C3",
  'name': "TREX",
  #'name'l: "TREX",
  'decimals': 18
},
{
  'address': "0x613D5D57Ce31A8EB3d9AB9750F79dF3b57cC9F56",
  'name': "LONG",
  #'name'l: "LongTerm Token",
  'decimals': 18
},
{
  'address': "0xd0258a3fD00f38aa8090dfee343f10A9D4d30D3F",
  'name': "VOXEL",
  #'name'l: "VOXEL Token",
  'decimals': 18
},
{
  'address': "0xdAfa3DF0D20A38e921B75BD8350F08d7A423DC9D",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x835BA011Ec70e695879185dF3d46939DBfBeF7E5",
  'name': "aABI",
  #'name'l: "Alpha Abachi",
  'decimals': 9
},
{
  'address': "0x245b25F3677d0b6C3AC69fBB0f75d4cb782ebe4E",
  'name': "SANTY",
  #'name'l: "Santa Inu",
  'decimals': 18
},
{
  'address': "0x293b3B56cCf37FCE9bd4d8A3E276ff6c24Bc72B4",
  'name': "BDG",
  #'name'l: "BitDegree Token (PoS)",
  'decimals': 18
},
{
  'address': "0x3EE3F36A01aa5D12CdFD89BA5Cfcf127D588e14b",
  'name': "NT1",
  #'name'l: "NerveTest",
  'decimals': 18
},
{
  'address': "0x87371034216e6f8a7e122F227dBbdd54c0868F55",
  'name': "CANE",
  #'name'l: "CaneCoin",
  'decimals': 18
},
{
  'address': "0xe848C81F2f834aA665Ff05B8439354fD5da4D055",
  'name': "WOONE",
  #'name'l: "Wrapped OnlyOne",
  'decimals': 18
},
{
  'address': "0xC4a25b0113FfB29f706f75A188DC6D9a41f10849",
  'name': "mRATIOMOON",
  #'name'l: "ETHBTC 2x Long",
  'decimals': 18
},
{
  'address': "0x94fDFcbD7b864479036a2A36ccEf832DB49b027B",
  'name': "NT2",
  #'name'l: "NerveTest",
  'decimals': 18
},
{
  'address': "0x2a5ac3938FC4267F4D785285D1598EAe237bf0dd",
  'name': "BMC",
  #'name'l: "Blue Monster Coin",
  'decimals': 18
},
{
  'address': "0xD1F456486bfd2645E0f455C158Df649006881D90",
  'name': "B3VR",
  #'name'l: "B34V3R",
  'decimals': 18
},
{
  'address': "0xBFd52A73378591B45221B953bEE3db2cfE2529C4",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xdbe6FB5C686409d5A949123E1F010E98Fe9377d5",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0xF840BC3182A432699B647a8e22aEB7cAe9300E57",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0x5bD9c2EB03a2A96796D03a98AA65fB470D64FC8F",
  'name': "PTT",
  #'name'l: "Persian Tiger Token",
  'decimals': 18
},
{
  'address': "0x2aE6b676C04F3f8Eb72B485778B298A7c875c8CF",
  'name': "EWMATIC",
  #'name'l: "ERCWMATIC",
  'decimals': 18
},
{
  'address': "0x8B54356f3A1306f49C6de879277De8F6739e09Fb",
  'name': "MINO",
  #'name'l: "MINO",
  'decimals': 9
},
{
  'address': "0x8c9F46C8e44C2B2aDB9580818110E78852A7b12A",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xA649325Aa7C5093d12D6F98EB4378deAe68CE23F",
  'name': "BNB",
  #'name'l: "Binance",
  'decimals': 18
},
{
  'address': "0x60AE376adD09cAFD393577173F643F6aDb00c898",
  'name': "Kool",
  #'name'l: "Kool",
  'decimals': 18
},
{
  'address': "0x5C173A51468694C0114aad0c14cbEA350f40C33e",
  'name': "LORB",
  #'name'l: "Leviathan Lobster Token",
  'decimals': 18
},
{
  'address': "0x5290Ad3d83476CA6A2b178Cd9727eE1EF72432af",
  'name': "imUSD",
  #'name'l: "Interest bearing mStable USD (Polygon PoS)",
  'decimals': 18
},
{
  'address': "0xb679456F4fb4F8b89EeAa03f59BC3836bf4FE4d2",
  'name': "XAI",
  #'name'l: "AstroFi Token",
  'decimals': 18
},
{
  'address': "0x6C865c287B235124DABC75bAD20190Aa15FA131e",
  'name': "CHAN",
  #'name'l: "Loligon",
  'decimals': 18
},
{
  'address': "0x9120599e41a6ceEc2EDBED4b412eE0a2274c38bD",
  'name': "v1-PRE-SPORE",
  #'name'l: "Spore Token Pre Production v1",
  'decimals': 18
},
{
  'address': "0x400f72D6f8bCbff97e19a97De9b902C4B47a8458",
  'name': "BRUT",
  #'name'l: "Brutus Inu Token",
  'decimals': 8
},
{
  'address': "0x1e9889611da17293daf7A317d65e42353B2f0a04",
  'name': "v2-PRE-SPORE",
  #'name'l: "Spore Token Pre Production v2",
  'decimals': 18
},
{
  'address': "0xB140665ddE25c644c6B418e417C930dE8A8a6Ac9",
  'name': "ATRI",
  #'name'l: "Atari (PoS)",
  'decimals': 0
},
{
  'address': "0x927B74A3b73eAB4AF71B475eC3FE84793F74F299",
  'name': "Eur",
  #'name'l: "Euro",
  'decimals': 18
},
{
  'address': "0xB763b8bBF3074078120fb56e5bE5c4EECc63FE6D",
  'name': "Euro",
  #'name'l: "Euro",
  'decimals': 18
},
{
  'address': "0x25aCE4409d2ff52CA4789d706F699A5084273Af5",
  'name': "SPACOIN",
  #'name'l: "SpaCoin",
  'decimals': 9
},
{
  'address': "0xd0Ffe4033B9407408c49f3F93CAf803ff8b27631",
  'name': "BZC",
  #'name'l: "BZC DAO",
  'decimals': 7
},
{
  'address': "0xeb45921FEDaDF41dF0BfCF5c33453aCedDA32441",
  'name': "pZUG",
  #'name'l: "pZUG",
  'decimals': 18
},
{
  'address': "0x36763d262243Ca67186487ADD95256F5892a6Fd0",
  'name': "NFTMG",
  #'name'l: "NFT Music Group",
  'decimals': 18
},
{
  'address': "0xCD2aB1B5C7c1800cf54c0D4b1757ff7b6f654b20",
  'name': "9",
  #'name'l: "WA9LNY",
  'decimals': 18
},
{
  'address': "0xD770b4f7Cc4FD9395bb62762CFBbbc008E37a415",
  'name': "WAGWAM",
  #'name'l: "WeAreGonnaWorkAtMcDonalds",
  'decimals': 18
},
{
  'address': "0xc30F68091FB72469b0e0481E2551Aa5E759D6271",
  'name': "EVG",
  #'name'l: "Evkagame",
  'decimals': 18
},
{
  'address': "0x0d654C6Ae5F99DdddEDF8Ac8e139EF5230c3c661",
  'name': "TGL",
  #'name'l: "The Gaming Life ",
  'decimals': 18
},
{
  'address': "0xf8101bEFDC322Be3A79f930DEAf6B4CF2f65e521",
  'name': "GMA",
  #'name'l: "Goldma",
  'decimals': 9
},
{
  'address': "0xdc13598ee040f6a6D2fa979c795d863C75B9ea84",
  'name': "CON",
  #'name'l: "Charissa Shaw",
  'decimals': 18
},
{
  'address': "0x37Af67AA51f6c89CBF116C2a726Ac37B7Fff0445",
  'name': "PERF",
  #'name'l: "MacKenzie Dickerson",
  'decimals': 18
},
{
  'address': "0x34667ED7C36cBBbF2d5d5c5c8d6Eb76a094EDb9F",
  'name': "GENE",
  #'name'l: "GenomesDAO (PoS)",
  'decimals': 18
},
{
  'address': "0x6E8a8726639d12935b3219892155520bdC57366B",
  'name': "GNOME",
  #'name'l: "GenomesDAO Governance (PoS)",
  'decimals': 18
},
{
  'address': "0xcb016D39cd7608c37f1D8f4192Ec103242Bc456d",
  'name': "TCDAI",
  #'name'l: "Test Curve DAI",
  'decimals': 18
},
{
  'address': "0xCfb499eE80aE56e83354D4ebC79710a2926aA1f8",
  'name': "TMSU",
  #'name'l: "Test Curve MSU",
  'decimals': 18
},
{
  'address': "0xa0cB0Ce7C6d93A7EBD72952Feb4407Dddee8a194",
  'name': "SHIBAKEN",
  #'name'l: "ShibaKen.Finance",
  'decimals': 0
},
{
  'address': "0xe8377A076adAbb3F9838afB77Bee96Eac101ffB1",
  'name': "MSU",
  #'name'l: "MetaSoccer Universe",
  'decimals': 18
},
{
  'address': "0x04b33078Ea1aEf29bf3fB29c6aB7B200C58ea126",
  'name': "SAFLE",
  #'name'l: "Safle",
  'decimals': 18
},
{
  'address': "0x6706Ed5878732cb878eC2F701eFE18f5037c183D",
  'name': "DTV",
  #'name'l: "DetectivCoin",
  'decimals': 18
},
{
  'address': "0x7d795bcb8Bf5c339b5383023D11F59c13070c311",
  'name': "v5-PRE-SPORE",
  #'name'l: "Spore Token Pre Production v5",
  'decimals': 18
},
{
  'address': "0x49413090e04cE1ecCC7F38a9660FF58b84E58e86",
  'name': "REV",
  #'name'l: "REV Protocol Share",
  'decimals': 18
},
{
  'address': "0xb2b1B72acCBc25DD8F69d99C0D1365aDb1A6c716",
  'name': "REVUSD",
  #'name'l: "REVUSD Stablecoin",
  'decimals': 18
},
{
  'address': "0x64B2A38bb7e935DA3D4529b0Bb4Df5b13B77316b",
  'name': "BLOG",
  #'name'l: "Blog Token",
  'decimals': 18
},
{
  'address': "0xAf1dCBEEB176d4A07C5601b7df12ce89341FC802",
  'name': "v10-PRE-SPORE",
  #'name'l: "Spore Token Pre Production v10",
  'decimals': 18
},
{
  'address': "0xd6007220Be73CDbCA36e5fD7fbB0e80241dBea2E",
  'name': "v10-PRE-SPORE",
  #'name'l: "Spore Token Pre Production v10",
  'decimals': 18
},
{
  'address': "0xa8aE212eD56248D69bDC87f3733f437E9Cf1403D",
  'name': "SCY",
  #'name'l: "SCAMMY",
  'decimals': 8
},
{
  'address': "0xAab4da35245BEd1F1a653122e03FA5C9Af020dD7",
  'name': "v20-preSPORE",
  #'name'l: "Spore Token Pre Prod v20",
  'decimals': 18
},
{
  'address': "0xA5f235cC3248Fb34eE23075B359701DCc5D6F4f4",
  'name': "v21-pSPORE",
  #'name'l: "Spore Token Pre Prod v21",
  'decimals': 18
},
{
  'address': "0xc41320FA8AfC2f7C318bd6EA611C7A9060f7Cd67",
  'name': "v27-pSPORE",
  #'name'l: "Spore Token Pre Prod v27",
  'decimals': 18
},
{
  'address': "0x3cABD2d298b9172533aD47D3F692e8FE13673160",
  'name': "SCRED",
  #'name'l: "Street Credit",
  'decimals': 18
},
{
  'address': "0xFded7D3278D71b61b3840Aa85D660E83d9F62D32",
  'name': "v55-pSPORE",
  #'name'l: "Spore Token Pre Prod v55",
  'decimals': 18
},
{
  'address': "0x797F615E3C5D8DDaFA754Da725d3F13d4F096E4e",
  'name': "v58-pSPORE",
  #'name'l: "Spore Token Pre Prod v58",
  'decimals': 18
},
{
  'address': "0x875663D5021D83C381e2738EEF83AfE3adC389C9",
  'name': "v60-pSPORE",
  #'name'l: "Spore Token Pre Prod v60",
  'decimals': 18
},
{
  'address': "0x43310f33Cb4e77d8f0A709Cb6F0be32D22c6Dbcd",
  'name': "SPORE-II",
  #'name'l: "Spore Token II",
  'decimals': 18
},
{
  'address': "0xFcC101eA0CFa67B9490cf72e3020b7A927Daa12E",
  'name': "SPORE-II",
  #'name'l: "Spore Token II",
  'decimals': 18
},
{
  'address': "0x83000597e8420aD7e9EDD410b2883Df1b83823cF",
  'name': "P125",
  #'name'l: "P125 Token (PoS)",
  'decimals': 18
},
{
  'address': "0xdB545b324BD881B29D72C393546010C400af4dC5",
  'name': "GODMO",
  #'name'l: "x10 Token Set",
  'decimals': 18
},
{
  'address': "0x4b1427A3C4564A7d009CcFCf12a2Ce3998FD05f8",
  'name': "BGD",
  #'name'l: "ngd token",
  'decimals': 18
},
{
  'address': "0x1050B6DA18f674d15A36E5E906f1C636C9D6600E",
  'name': "t4",
  #'name'l: "test4",
  'decimals': 9
},
{
  'address': "0xF67E6cA3028a6C4d723f0434bC018a7bC953E5D1",
  'name': "CUMCOIN",
  #'name'l: "fake#'name'",
  'decimals': 18
},
{
  'address': "0x655b3CA7F5956FCaa7137477d86b1042C257941d",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x07c9e51dc3D7b649862C7F43d9C8BD54584a588d",
  'name': "GMG",
  #'name'l: "Gaminger",
  'decimals': 9
},
{
  'address': "0x171e7C3Aa467CBE972A1596e14124BeC5Df0AB7A",
  'name': "NUBI",
  #'name'l: "NUBICoin",
  'decimals': 18
},
{
  'address': "0x4AAdd8D5B53B665F07aF7dbAD56A7A6779B63E68",
  'name': "DSHIT",
  #'name'l: "Degen Shit",
  'decimals': 18
},
{
  'address': "0x1ea936097A79AE4F520c3B4ae8eC057675aEe801",
  'name': "OAG",
  #'name'l: "OperalAG",
  'decimals': 0
},
{
  'address': "0x66520438bD8212BB274F7C83AEc6d727FfBd691d",
  'name': "DFG",
  #'name'l: "Jolene Weiss",
  'decimals': 18
},
{
  'address': "0x4a48Af25893d919CE24442933ad5b1053506DBE8",
  'name': "BTC",
  #'name'l: "Bitcoin",
  'decimals': 18
},
{
  'address': "0xE1E78A5DB703fc6e450fa91230e2eBaF1c7b4846",
  'name': "MATIC",
  #'name'l: "Matic Token",
  'decimals': 18
},
{
  'address': "0x37Bfdbe2B08Cd8dE08862CC7975115c2189183e4",
  'name': "ETH",
  #'name'l: "Ethereum",
  'decimals': 18
},
{
  'address': "0xdcE1F3b11299084062f5D2933F6ea8559bC985A2",
  'name': "CATDOG",
  #'name'l: "Cat Dog Inu",
  'decimals': 18
},
{
  'address': "0x9E2d266D6c90F6C0D80a88159b15958f7135B8Af",
  'name': "SSX",
  #'name'l: "StakeShare",
  'decimals': 18
},
{
  'address': "0x1E67124681b402064CD0ABE8ed1B5c79D2e02f64",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x2cf644bF98ceE0a7C9C7DF312Ca3d0d9C01c17f3",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x9e5cc3aF2c87527Fdb48eb783E84E0fD9a59918a",
  'name': "MBT",
  #'name'l: "Magic Ball Token",
  'decimals': 18
},
{
  'address': "0xd6fA50b52aEa311a28EfBA64C36D81b3CDC3EeE5",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xa27c6bcdE368b47b1Cb145527F71e5d4720FE3Eb",
  'name': "FARZA",
  #'name'l: "Farza Coin",
  'decimals': 18
},
{
  'address': "0x69557011D08173A2F56a4d16fC8A68c4119FE429",
  'name': "SHATDOGE",
  #'name'l: "Elon's Diarrhea Disaster",
  'decimals': 9
},
{
  'address': "0x60FE7AC540Db0De06076c95b890a8f0318BAE3B2",
  'name': "32MBSDCARD",
  #'name'l: "Mocha Frappe",
  'decimals': 9
},
{
  'address': "0x7B7531709De25B0d00c0577916973e01043285dC",
  'name': "CUTE",
  #'name'l: "cute",
  'decimals': 18
},
{
  'address': "0xF723A8a4D4dddFA4AC41F6Ad124BA5496B6003EE",
  'name': "JIMMY",
  #'name'l: "Jimmycoin",
  'decimals': 18
},
{
  'address': "0xf9f7dE2c971c881409F20d4582C9Fe6a06A67945",
  'name': "VJT",
  #'name'l: "VJTBTC",
  'decimals': 18
},
{
  'address': "0x5c39fF172D54Efd81f81a6169554BE18d7E71e9B",
  'name': "SCASH",
  #'name'l: "SHOMONcash",
  'decimals': 18
},
{
  'address': "0x6F5907a1c2b7ce8C61682147DEb091483A564892",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xf315E8885Fd50793dE0D32DA806Fc6EFd7000915",
  'name': "MATIC",
  #'name'l: "Matic Token",
  'decimals': 18
},
{
  'address': "0xBB2Ea6F3a9d169301B4f98726EdC4077aFFF83c5",
  'name': "BPT",
  #'name'l: "Boomcoin",
  'decimals': 8
},
{
  'address': "0xCc7E52F043E1a8D81B613E9d81Ca9C0d3110b44e",
  'name': "TGA",
  #'name'l: "The Golden Army Token",
  'decimals': 18
},
{
  'address': "0x5431390F6a98ae2Baa92c3da0690272E1554a50e",
  'name': "ACTN",
  #'name'l: "Action Coin on Polygon",
  'decimals': 18
},
{
  'address': "0x8C72f5dF6f4C2568DbaB0fc3Db64c388D542c770",
  'name': "uniinu",
  #'name'l: "day2datas totally awesome liquid doggie memecoin",
  'decimals': 18
},
{
  'address': "0xAE36Fe31369c76bbE5CfCa133c9c23CD6254b0f7",
  'name': "VFR",
  #'name'l: "Gil Greene",
  'decimals': 18
},
{
  'address': "0x4f2c24a5701340B7951945083264Cf0ea2860AfE",
  'name': "UTS",
  #'name'l: "Anthony Acevedo",
  'decimals': 18
},
{
  'address': "0xe2Acf21ff697853453548DB0EFC524E116335acf",
  'name': "III",
  #'name'l: "The Index Index Index",
  'decimals': 18
},
{
  'address': "0xae20563403DDd9107eC5C7f2AbBc9864E2039Dc8",
  'name': "XMIPA6",
  #'name'l: "XMIPA6",
  'decimals': 18
},
{
  'address': "0x94C18174840F80D49d59DC3a1742aF0B884A8184",
  'name': "SWAM",
  #'name'l: "SwapMatic Token (PoS)",
  'decimals': 18
},
{
  'address': "0xDF44cb429a57e51152AA4EF99B0119756C721FBF",
  'name': "IMTU",
  #'name'l: "Imperfectu Token",
  'decimals': 2
},
{
  'address': "0xB8060D8fc453561Cfb1d30A6cA36FD3c7669472D",
  'name': "CA",
  #'name'l: "CoinAltar",
  'decimals': 18
},
{
  'address': "0xBf0eA60F6dbB35f9BfE9EA5b532B7795772Af541",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xa9C1740fA56e4c0f6Ce5a792fd27095C8b6CCd87",
  'name': "KINE",
  #'name'l: "Kine Governance Token",
  'decimals': 18
},
{
  'address': "0x2db0Db271a10661e7090b6758350E18F6798a49D",
  'name': "MOT",
  #'name'l: "Mobius Token",
  'decimals': 18
},
{
  'address': "0x9fFFb2F49adFC231B44dDCFf3FfCF0E81b06430A",
  'name': "moUSD",
  #'name'l: "moUSD",
  'decimals': 18
},
{
  'address': "0xcE62fE753e7D6b7480956a282E6854403e9D1A66",
  'name': "ZERG",
  #'name'l: "Zergling",
  'decimals': 18
},
{
  'address': "0xcc90c29600DD5E885fa88ad8685927F5D8d5AAd0",
  'name': "LOK 1M",
  #'name'l: "LOK 1M",
  'decimals': 18
},
{
  'address': "0x17664F5B46038D945F3f0d81b406aED6aee03C26",
  'name': "LOK 1M",
  #'name'l: "LOK 1M",
  'decimals': 18
},
{
  'address': "0xb5084E416E1Cab01a00a8a023Ca3CE3B15b53DA5",
  'name': "UT2",
  #'name'l: "Yuri Mack",
  'decimals': 18
},
{
  'address': "0x5BCda6E59262A96a599Ea938c9B679714c105Bba",
  'name': "wBKC",
  #'name'l: "Wrapped BKC",
  'decimals': 18
},
{
  'address': "0x7feE95a4EAA73D1c0b1f9B20fA0B2b5A9C2cba0a",
  'name': "Rave",
  #'name'l: "Rave Sausages",
  'decimals': 2
},
{
  'address': "0x03F24774dBe81a4b59F3DCE128250749F69407B2",
  'name': "FTT",
  #'name'l: "Field Trip Token",
  'decimals': 18
},
{
  'address': "0xab3D689C22a2Bb821f50A4Ff0F21A7980dCB8591",
  'name': "PRXY",
  #'name'l: "Proxy",
  'decimals': 18
},
{
  'address': "0xd51ff4085C8045eE9Be38FBe6757Ef359b441046",
  'name': "ABO",
  #'name'l: "ABOANAN",
  'decimals': 18
},
{
  'address': "0x34504Fe9DF477B2768Ef0be497C80e578D695525",
  'name': "BBB",
  #'name'l: "Golden Chain",
  'decimals': 18
},
{
  'address': "0xF21D8682C7dC54a342D9E2420832fd58DcBFE40d",
  'name': "AAA",
  #'name'l: "Golden Chain",
  'decimals': 18
},
{
  'address': "0xF21917bC081aFEa1eC687508C374264D9F721477",
  'name': "RETH",
  #'name'l: "Realms of Ethernity",
  'decimals': 18
},
{
  'address': "0x6F620EC89B8479e97A6985792d0c64F237566746",
  'name': "WPC",
  #'name'l: "WePiggy Coin",
  'decimals': 18
},
{
  'address': "0xa9b57fD025901faaC10d5d5AE658a9779892684a",
  'name': "UFGJ",
  #'name'l: "Indigo Hines",
  'decimals': 18
},
{
  'address': "0x8f0a75b9C53137517Ed1953e04C868584895fE5c",
  'name': "SFEW",
  #'name'l: "sfew",
  'decimals': 18
},
{
  'address': "0x53676eC2c90f261EBDafDFe6e87870158c845560",
  'name': "WET",
  #'name'l: "Vladimir Rutledge",
  'decimals': 18
},
{
  'address': "0x7CC43c32A9CcfB0d3eD29030fdF86fC028977099",
  'name': "SING",
  #'name'l: "GOGOSING",
  'decimals': 8
},
{
  'address': "0x1cb3D1aB5FDD40b51ec04c6e956634c685c7E7B8",
  'name': "POLYMOON",
  #'name'l: "PolyMoon",
  'decimals': 9
},
{
  'address': "0x149749B691993B218904cC8C15684bBEb9568B3a",
  'name': "BMP",
  #'name'l: "BuyMePlease",
  'decimals': 0
},
{
  'address': "0xb7d4fD5d5d2f92f12841CB6a7FA5daa201d5F67f",
  'name': "SLR",
  #'name'l: "Solar parker",
  'decimals': 18
},
{
  'address': "0xcF9a0988f9ae24a0248C862A2d31418D9256be0f",
  'name': "TTG",
  #'name'l: "the_tokengames",
  'decimals': 18
},
{
  'address': "0xA3be492848D6cc4992346E786fbB25F4E3c71b4D",
  'name': "CATs",
  #'name'l: "CATCOINsc",
  'decimals': 18
},
{
  'address': "0x607f73DC55276c358977BD7aE069039841115e63",
  'name': "PATIC",
  #'name'l: "Patic",
  'decimals': 18
},
{
  'address': "0x84342e932797FC62814189f01F0Fb05F52519708",
  'name': "NHT",
  #'name'l: "Neighbourhoods Token",
  'decimals': 18
},
{
  'address': "0xA07e9Df78648E5704275263403A3dC11f159b655",
  'name': "BOOBA",
  #'name'l: "BennySplitty",
  'decimals': 9
},
{
  'address': "0xE9afCd8601e765835998E70684B5c99a44bf6787",
  'name': "YLLWFRMLA",
  #'name'l: "Yellow Formula",
  'decimals': 9
},
{
  'address': "0xE411D55Fb9D8d9d2A0b4161F08AdF768b23A584B",
  'name': "PYLNT",
  #'name'l: "PYLNT (PoS)",
  'decimals': 18
},
{
  'address': "0x88C949b4eB85a90071f2C0beF861BDDEe1a7479D",
  'name': "mSHEESHA",
  #'name'l: "SHEESHA POLYGON",
  'decimals': 18
},
{
  'address': "0xB355f4F4CC84a9429a59d5c2B98d77016f7EC482",
  'name': "BTCBR",
  #'name'l: "BitcoinBR",
  'decimals': 18
},
{
  'address': "0x95Ab7Fa3Ea50f153170Ef355e8Aa5725154aEdBc",
  'name': "DUNE",
  #'name'l: "Dune",
  'decimals': 18
},
{
  'address': "0xB4b880ECA618AFDf72B0F6f62526917637C159D9",
  'name': "SGZ",
  #'name'l: "Sergiuz",
  'decimals': 18
},
{
  'address': "0x42d61D766B85431666B39B89C43011f24451bFf6",
  'name': "PSP",
  #'name'l: "ParaSwap (PoS)",
  'decimals': 18
},
{
  'address': "0x85411293b434E5C9b5E35C7248Dc6711c7BA1Ddd",
  'name': "TG",
  #'name'l: "Trilly Gang",
  'decimals': 18
},
{
  'address': "0x89a09BD708AcDdD5452Bc83dF69D5BD98341fbc2",
  'name': "REDH",
  #'name'l: "REDH",
  'decimals': 18
},
{
  'address': "0xD573A1529f67eEE93934Aa76E50A024F44E3701A",
  'name': "QZYBE",
  #'name'l: "HerosymaNagasakee",
  'decimals': 18
},
{
  'address': "0xE83c63642A52E42D2EF5eCfc3BC9D264a1cb4E5E",
  'name': "NIHHA",
  #'name'l: "lmaocantbreathe",
  'decimals': 18
},
{
  'address': "0xc93B81a6DEfBaA95Cb73ab80Ef4256Be54BB7407",
  'name': "FIVEF",
  #'name'l: "5-5000",
  'decimals': 18
},
{
  'address': "0xe368e830bC7F4767d98cb8B492cA220AE09e2283",
  'name': "TAMBZ",
  #'name'l: "rgfjfghjfdfbhgdfe",
  'decimals': 18
},
{
  'address': "0xF4129A4D9f722bfE815175FB03295b34741Fd757",
  'name': "ASJDHB",
  #'name'l: "asxasxasas",
  'decimals': 18
},
{
  'address': "0x15aa48F4b962E4C49452Cfd48956C86027ecC6e5",
  'name': "WFDWJL",
  #'name'l: "sdfcsdvsdvds",
  'decimals': 18
},
{
  'address': "0x45582Df42C4F44E7d81F666d0abb3fEd77b796b9",
  'name': "ASDSAS",
  #'name'l: "xasdasd",
  'decimals': 18
},
{
  'address': "0xc93B81a6DEfBaA95Cb73ab80Ef4256Be54BB7407",
  'name': "FIVEF",
  #'name'l: "5-5000",
  'decimals': 18
},
{
  'address': "0xe368e830bC7F4767d98cb8B492cA220AE09e2283",
  'name': "TAMBZ",
  #'name'l: "rgfjfghjfdfbhgdfe",
  'decimals': 18
},
{
  'address': "0x4381C9Fba18f6e7Ddb46Fbd4aFDcD04d9ce4Ae89",
  'name': "BUL",
  #'name'l: "bul",
  'decimals': 18
},
{
  'address': "0xF4129A4D9f722bfE815175FB03295b34741Fd757",
  'name': "ASJDHB",
  #'name'l: "asxasxasas",
  'decimals': 18
},
{
  'address': "0x684ac59b7C5Ab16b91fD33Ba446889c357f98C5c",
  'name': "QZYBE",
  #'name'l: "fasdasdw",
  'decimals': 18
},
{
  'address': "0xE5c30310b2CDb9d2698Ce27fd17c384544656C00",
  'name': "BMUSK",
  #'name'l: "Baby Musk",
  'decimals': 18
},
{
  'address': "0x7c17B42a10C5EFc54107A10F6914AC0027c6917A",
  'name': "SACASC",
  #'name'l: "saxcas",
  'decimals': 18
},
{
  'address': "0x6749441Fdc8650b5b5a854ed255C82EF361f1596",
  'name': "LUCHA",
  #'name'l: "Luchadores.io LUCHA Token",
  'decimals': 18
},
{
  'address': "0x72548521eDDb0bbdCC3C55AB63Ca08c541d8171D",
  'name': "GPT2",
  #'name'l: "GrumpyPolyTest2",
  'decimals': 9
},
{
  'address': "0xc4652cf9CffCd93B3E5b237CbF683515c2d92b92",
  'name': "GPT3",
  #'name'l: "GrumpyPolyTest3",
  'decimals': 9
},
{
  'address': "0x5F050C14af95395fbb9785dbcd678AB7076a0537",
  'name': "GPT4",
  #'name'l: "GrumpyPolyTest4",
  'decimals': 9
},
{
  'address': "0x46123245B82dA0806F66A2cB68Fc10bFA3A0ca6f",
  'name': "FHTAGN",
  #'name'l: "Cthulhu",
  'decimals': 18
},
{
  'address': "0xA551EFe6aA2f608AA85c4FB20C5720A2fF05f5d1",
  'name': "GOR",
  #'name'l: "Gorilla",
  'decimals': 9
},
{
  'address': "0x476fF0d0529Acd9Ac90728dF0c2fFd08E5089fc8",
  'name': "POLYMOON",
  #'name'l: "PolyMoon",
  'decimals': 9
},
{
  'address': "0x1596e6e3C9fbf74dD2367077c1296a87164956E8",
  'name': "POLYMOON",
  #'name'l: "PolyMoon",
  'decimals': 9
},
{
  'address': "0xaa404804Ba583c025Fa64c9a276A6127CEB355c6",
  'name': "CPR",
  #'name'l: "CIPHER",
  'decimals': 2
},
{
  'address': "0x4a9C6068f84ACcF4F9115D11c54a74ec8DE1652E",
  'name': "cerUSD",
  #'name'l: "cerUSD",
  'decimals': 18
},
{
  'address': "0x72820c24FD36d6EE82F72211ae7173a17Fb20b7B",
  'name': "CERBY",
  #'name'l: "CERBY",
  'decimals': 18
},
{
  'address': "0xC64bb184602B32841EBCbc432141045F80e497b7",
  'name': "USDC",
  #'name'l: "USDC",
  'decimals': 18
},
{
  'address': "0xdef1fac7Bf08f173D286BbBDcBeeADe695129840",
  'name': "CERBY",
  #'name'l: "Cerby Token",
  'decimals': 18
},
{
  'address': "0x6d7A6A35Dc0Be6397D885C84bed8e677370fBD93",
  'name': "RICH",
  #'name'l: "Rich Coin",
  'decimals': 18
},
{
  'address': "0x608FC8841cC21c2573b50f10E33CA3128B5D721B",
  'name': "BOOBIES",
  #'name'l: "Boobies",
  'decimals': 15
},
{
  'address': "0x064424bE39D59EfBE2601027a6338D03DDE3d476",
  'name': "polyTCG2",
  #'name'l: "TCG 2.0 Polygon",
  'decimals': 9
},
{
  'address': "0xa75f9fffe9B3B86ACbC12afd14ae6c992136C9c7",
  'name': "PVS",
  #'name'l: "Polyverse",
  'decimals': 9
},
{
  'address': "0x24eF3595f46ca564594D5eb21BD1FC22C1c94934",
  'name': "SNAX",
  #'name'l: "Scooby Doo Inu",
  'decimals': 18
},
{
  'address': "0xdf8c63B426515D9318256b54a72B388950f2A5dE",
  'name': "NUDES",
  #'name'l: "Nudes",
  'decimals': 9
},
{
  'address': "0xF9509b07cF67D1539B3d21e654Cb36F9D4F28E19",
  'name': "CSDCSC",
  #'name'l: "c vxvxc",
  'decimals': 18
},
{
  'address': "0xBa40aDdF4D1cA069890F393Cc832Be25e075D9aF",
  'name': "SDFSDFS",
  #'name'l: "sedfsdf",
  'decimals': 18
},
{
  'address': "0x656CC078fe81BB4D0012b2D2e6Cb0c0ed305eA69",
  'name': "CVXCVX",
  #'name'l: "xcvxcvx",
  'decimals': 18
},
{
  'address': "0xF82a129328313D003ADAd40bccd9E72B3d4a402b",
  'name': "SFM",
  #'name'l: "safeelon mars",
  'decimals': 18
},
{
  'address': "0x8965C088868b932Ff89bB0d4354Ab725bd5dAB38",
  'name': "QXC",
  #'name'l: "QXCHANGE",
  'decimals': 18
},
{
  'address': "0xCd150B1F528F326f5194c012f32Eb30135C7C2c9",
  'name': "OOKI",
  #'name'l: "Ooki Token (PoS)",
  'decimals': 18
},
{
  'address': "0x5d146d8B1dACb1EBBA5cb005ae1059DA8a1FbF57",
  'name': "CADC",
  #'name'l: "CAD Coin (PoS)",
  'decimals': 18
},
{
  'address': "0x28B29AdD8cF65F03149e39BFB8d499da987cD488",
  'name': "SMT",
  #'name'l: "Social Media Token",
  'decimals': 8
},
{
  'address': "0x960800237344ad3eA4b5C1F8C6F5FC196C947d80",
  'name': "ESF",
  #'name'l: "Elonsaidfloki",
  'decimals': 18
},
{
  'address': "0xDe86d653EbED7073564903f1dB642d70936C366c",
  'name': "FS",
  #'name'l: "Floki Santa",
  'decimals': 9
},
{
  'address': "0x3311Ea247878D0Fb980c8910eA811Daa1e9dA1D8",
  'name': "PCHI",
  #'name'l: "Peach Coin",
  'decimals': 18
},
{
  'address': "0xE69da3B9030Cb0bB2e8ade9864BE75b9A8900eC2",
  'name': "D",
  #'name'l: "Disqus",
  'decimals': 9
},
{
  'address': "0x89dFE2f59F344897bA6923475626caF18bf9028a",
  'name': "hlc",
  #'name'l: "health",
  'decimals': 12
},
{
  'address': "0x2EA3E8f750cbc55C293E6008E8B5a654eBBd0600",
  'name': "TNO",
  #'name'l: "TNodeOrange (PoS)",
  'decimals': 8
},
{
  'address': "0x1829Be13b7dD7F07312D7D27318d0913EaAf83Bf",
  'name': "DTI",
  #'name'l: "Dantez Token Invest",
  'decimals': 8
},
{
  'address': "0x4e1581f01046eFDd7a1a2CDB0F82cdd7F71F2E59",
  'name': "ICE",
  #'name'l: "IceToken",
  'decimals': 18
},
{
  'address': "0xa5B6C1C2c7E5Eebaded001d2ccAcEdBBa4543afe",
  'name': "STONE ",
  #'name'l: "Stone finance ",
  'decimals': 18
},
{
  'address': "0x9F43e49626650a230Fe50d38875ee12AdB64F23E",
  'name': "GO",
  #'name'l: "Go Finance ",
  'decimals': 18
},
{
  'address': "0xe642F437B2e6D9D69d95a69e9e47CBF76A38E854",
  'name': "DARO",
  #'name'l: "MohenjoDaro",
  'decimals': 18
},
{
  'address': "0x9396D4AD4Cb39749A27cfFa7181Cb29d8bb8FB40",
  'name': " C",
  #'name'l: "C",
  'decimals': 18
},
{
  'address': "0x02C7fD8909858FB5734fd305610B30AaF3E10355",
  'name': "B",
  #'name'l: "B",
  'decimals': 18
},
{
  'address': "0x000EcC4AE4406e74234fAdBC92970886B1E81A29",
  'name': "A",
  #'name'l: "A",
  'decimals': 18
},
{
  'address': "0x167855fC9B315Ab7bd0069456ee698E124EAc429",
  'name': "ROCK",
  #'name'l: "Rock",
  'decimals': 18
},
{
  'address': "0x9b77dA280471eD14122cc4Ac7B9b01EB54D7dDFB",
  'name': "SUS ",
  #'name'l: "Sus finance ",
  'decimals': 18
},
{
  'address': "0x4883e17EF26441259379EdC74Bb3e87eaA4EFee7",
  'name': "COOFFEE",
  #'name'l: "coffee",
  'decimals': 18
},
{
  'address': "0xE14d1d0fEAED80Ac5ECE73fb7947F6057bb83b4e",
  'name': "ABBA ",
  #'name'l: "ABBA defi ",
  'decimals': 18
},
{
  'address': "0x3385a664c1A24181d89A8498806f7a374073632E",
  'name': "WHALE ",
  #'name'l: "Whale ",
  'decimals': 18
},
{
  'address': "0xa608686B8e06B04C2FddF3314349a101CA3441B3",
  'name': "WEED",
  #'name'l: "Weed",
  'decimals': 18
},
{
  'address': "0xA99C98cA72D844CA4b3E08e33A15c0b72bB58cFF",
  'name': "LILY",
  #'name'l: "Lily",
  'decimals': 18
},
{
  'address': "0x174AB4a517F123E2A250515ddcfE73cC5807F6A0",
  'name': "X",
  #'name'l: "X",
  'decimals': 18
},
{
  'address': "0xbb91EDDCb769A3dc12F997A1423A811314395671",
  'name': "SQD ",
  #'name'l: "Squidcoin",
  'decimals': 18
},
{
  'address': "0x3b8411975240bF032d2ae1399f110091692e35E6",
  'name': "WOOF",
  #'name'l: "Woof",
  'decimals': 18
},
{
  'address': "0x6f90242Cd70663555Ba061b913E63564810112E5",
  'name': "FEET",
  #'name'l: "Feet",
  'decimals': 18
},
{
  'address': "0xcD86152047e800d67BDf00A4c635A8B6C0e5C4c2",
  'name': "NACHO",
  #'name'l: "NACHO",
  'decimals': 18
},
{
  'address': "0x8e684871c5997ed63bf84DC0DFaB1aa031Ec7493",
  'name': "PMT",
  #'name'l: "polyMETA",
  'decimals': 18
},
{
  'address': "0x9f8d1C9C9bD9Dc1DBB6A8D863211f001F03Ea4ba",
  'name': "P2",
  #'name'l: "P2 Coin",
  'decimals': 18
},
{
  'address': "0xeEef481b50787A99f9cf4ba5cE0b82fa25e8b2c4",
  'name': "P1",
  #'name'l: "P1 Coin",
  'decimals': 18
},
{
  'address': "0x2cf7e671A80841c496d3007803389753F76Dd702",
  'name': "Corbo",
  #'name'l: "Corbin",
  'decimals': 18
},
{
  'address': "0x02e5d6c2702729c551d23D794ba477F80c1aE608",
  'name': "ABC",
  #'name'l: "ABC finance",
  'decimals': 18
},
{
  'address': "0x010066F2F96543F54981A422F8Ac3604F95d9AD2",
  'name': "MOO",
  #'name'l: "Moo",
  'decimals': 18
},
{
  'address': "0x98De701d3302d5C1C44e80f388DdfCd8c139Fb94",
  'name': "HYYPER",
  #'name'l: "hyyperform",
  'decimals': 9
},
{
  'address': "0xd06A626F413a8eAcC2BaE0B176a51BFeC02436f5",
  'name': "MAX",
  #'name'l: "Max defi",
  'decimals': 18
},
{
  'address': "0xE48edBA14D5789d2C6A40b3993e9Ae34c54bAcf7",
  'name': "ETOWN",
  #'name'l: "ETown",
  'decimals': 18
},
{
  'address': "0x0a7F27e370168B1E1BE2eF77a8Ba28D66983c515",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x926343fDfB1e4ea14dB6087889480F4ffD6Ae240",
  'name': "VTID",
  #'name'l: "Vermont Interent Design",
  'decimals': 9
},
{
  'address': "0xbCCA7B6CCFfC62Bf538EC4c6e8bF211E39e3EA92",
  'name': "Tanner",
  #'name'l: "Tanner Token",
  'decimals': 18
},
{
  'address': "0x3E3a5500C936E907ebCCFA34bF884A6E4a7CE24d",
  'name': "CRYSTL",
  #'name'l: "Crystal",
  'decimals': 18
},
{
  'address': "0xc54a5024b6c5e565772729b783021f60a8f9139c",
  'name': "SMOKE",
  #'name'l: "Smoke (PoS)",
  'decimals': 18
},
{
  'address': "0x027FCBA0Bf12853269C625C762dba8D59e52cd9c",
  'name': "BOOBA",
  #'name'l: "BennySplitty",
  'decimals': 9
},
{
  'address': "0xEf023867C1002D6AC7F3e63d84896230a3BB830D",
  'name': "AEG",
  #'name'l: "Aegis",
  'decimals': 18
},
{
  'address': "0x5a2981343027fD9c79804f8F12BF7030dd2e2bF8",
  'name': "GULI",
  #'name'l: "GULITOGALA",
  'decimals': 18
},
{
  'address': "0x32Cd639639eF8e885b456A88f9763F02DbA7eE14",
  'name': "E-PAY",
  #'name'l: "EPAY",
  'decimals': 9
},
{
  'address': "0xbcf131997de512BCDfe468843b0fc19221847b9b",
  'name': "CIMA.AI",
  #'name'l: "CIMA.AI",
  'decimals': 18
},
{
  'address': "0x5de4005155933c0e1612Ce808f12B4cd8DAabc82",
  'name': "ARMOR",
  #'name'l: "Armor (PoS)",
  'decimals': 18
},
{
  'address': "0x7C36208173fa65d2FFfD609B54910F5cB2487a97",
  'name': "COA",
  #'name'l: "COA Capital Index",
  'decimals': 18
},
{
  'address': "0x33693d872e9c9aaaf339351DA75d44D3104aC7f4",
  'name': "SENZUBEAN",
  #'name'l: "Senzu Beans",
  'decimals': 8
},
{
  'address': "0xABF65CbA6819BDA6268A056458bDEb85fc7Dfb7d",
  'name': "RobE",
  #'name'l: "RobE.Protocol",
  'decimals': 18
},
{
  'address': "0x96492C30724a07cEe73e46e8421A8C296FD00f40",
  'name': "Jawani",
  #'name'l: "Jawani Token",
  'decimals': 18
},
{
  'address': "0xB691c77730fDFA52d6BA4f15d8F404A7d2f67393",
  'name': "ONIX",
  #'name'l: "Onix",
  'decimals': 18
},
{
  'address': "0x76B7f60963f116A1F70B9C5e0f035bB129ac627B",
  'name': "POLYCUB-TEST",
  #'name'l: "PolyCub-TEST",
  'decimals': 18
},
{
  'address': "0x58576F8f500AFeF7a7C42cdF074B74B9256638Ed",
  'name': "CRYT",
  #'name'l: "CRY Test",
  'decimals': 9
},
{
  'address': "0xA2623C3938CF45c76aaA9678bFdeAC0991cA778B",
  'name': "ETH2AI",
  #'name'l: "Ether2AI",
  'decimals': 18
},
{
  'address': "0xbc9EB2482B08b3d9ae64841d69076574b843F8C9",
  'name': "Mr1ch4l",
  #'name'l: "Mr1ch4l",
  'decimals': 0
},
{
  'address': "0xa42fc534e7bc353Cd230EE399BC4c7141837FEEC",
  'name': "RobE",
  #'name'l: "RobE.Protocol",
  'decimals': 18
},
{
  'address': "0xc919e6f6353B988Dc1d0fDeBA94BE72625B462a0",
  'name': "GCH",
  #'name'l: "Golden Chain",
  'decimals': 18
},
{
  'address': "0x3850c968c96a7e092F8CC06628640488Cd7D2CE1",
  'name': "BADPRICE",
  #'name'l: "Can_devs_do_something",
  'decimals': 18
},
{
  'address': "0x1B8EEAE11AE6d378558f45638B4395b7c5bc3549",
  'name': "HFV",
  #'name'l: "HFV",
  'decimals': 18
},
{
  'address': "0x23f07a1C03e7C6D0C88e0E05E79B6E3511073fD5",
  'name': "CDS",
  #'name'l: "Crypto Development Services",
  'decimals': 8
},
{
  'address': "0x19793B454D3AfC7b454F206Ffe95aDE26cA6912c",
  'name': "am3CRV-gauge",
  #'name'l: "Curve.fi am3CRV RewardGauge Deposit",
  'decimals': 18
},
{
  'address': "0x8CFD9992d1183d561678AE5c870dE40F3731c41F",
  'name': "LAMBOINU",
  #'name'l: "Lambo Inu",
  'decimals': 18
},
{
  'address': "0x70D8F92Abf2A47432224836D69a500aA3De0f007",
  'name': "REL",
  #'name'l: "Relix Finance",
  'decimals': 18
},
{
  'address': "0xCD6EaF64087a1F3AE6ae5Ab4cdf83568a4152F9e",
  'name': "ROBe2",
  #'name'l: "ROBe2.Protocol",
  'decimals': 18
},
{
  'address': "0x4610A09231e175D67e7202Bc927d4B6cb8801C9C",
  'name': "CASTIRON",
  #'name'l: "CASTIRON",
  'decimals': 18
},
{
  'address': "0x8A2505E1c5ccE5584b9C9950537d729A6AE841E7",
  'name': "LUCID",
  #'name'l: "STABILITY",
  'decimals': 18
},
{
  'address': "0x69CDBE609e492718ECa28f948C6e016A6f4E2e24",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x93d2575994ed83Ccc1BceE858912BD0D6c13CA32",
  'name': "FORGE",
  #'name'l: "LittleHeroes",
  'decimals': 18
},
{
  'address': "0x35C2b0C00A14bb2de4561C4014A10C67dc41a0b2",
  'name': "Beli",
  #'name'l: "Beli",
  'decimals': 18
},
{
  'address': "0x95f45Ede7b1cF2F944879988f47bC67F51558651",
  'name': "BRCC",
  #'name'l: "Broccoli Coin",
  'decimals': 18
},
{
  'address': "0x1b12bDef2d562E19dd3B8cB66F61f1e1b714d491",
  'name': "XA9",
  #'name'l: "XANTA9 (Wormhole)",
  'decimals': 18
},
{
  'address': "0xE9E2A1273b416eC6e2bc595320D5b0E2B19eB882",
  'name': "BIZLAL",
  #'name'l: "bizlal",
  'decimals': 18
},
{
  'address': "0x84072C5D4150B9D2EEA0e3345d343d5333673125",
  'name': "PP",
  #'name'l: "Panda Panda",
  'decimals': 18
},
{
  'address': "0x29F1e986FCa02B7E54138c04C4F503DdDD250558",
  'name': "VSQ",
  #'name'l: "VSQ",
  'decimals': 9
},
{
  'address': "0x7bDa64742bacbfd6D9312921F6b072ED08Fcb7c0",
  'name': "ABC",
  #'name'l: "Alpha Beta Coin",
  'decimals': 18
},
{
  'address': "0x5c045E634CaCB348357E03259bc033D0f3A3724f",
  'name': "RKT",
  #'name'l: "Rocket",
  'decimals': 18
},
{
  'address': "0x1e7C54F618a6260Fb2eB9Cf4BE995B062A87e2B4",
  'name': "str",
  #'name'l: "start",
  'decimals': 18
},
{
  'address': "0xE8cA065853526316Ca386fd5AC849012940eA32e",
  'name': "ZJEB",
  #'name'l: "LewusCoin",
  'decimals': 18
},
{
  'address': "0x4F4aE19018DCFacac87A79E2291b03bD08824B91",
  'name': "FROST",
  #'name'l: "Frost",
  'decimals': 18
},
{
  'address': "0x40a79C66306C4D5C06B24c3AEb7EBC59af1fFAC6",
  'name': "DIG",
  #'name'l: "DIGITS",
  'decimals': 18
},
{
  'address': "0x787f5740f23415e4c3e96D1E55E97B033F8A70b5",
  'name': "LVC",
  #'name'l: "Levcoin",
  'decimals': 18
},
{
  'address': "0x44083699F5fcC4ef06c150BE5dD026F51Fa5fD30",
  'name': "NOKIA",
  #'name'l: "Flip Phone",
  'decimals': 9
},
{
  'address': "0x820F598f5203e2CDd2990cD9a21fE36247A404D7",
  'name': "T4",
  #'name'l: "test4",
  'decimals': 18
},
{
  'address': "0x6710ae7Bd52e09847a151Ebf2912D3e4DAf56467",
  'name': "IMAD",
  #'name'l: "IMAD Token",
  'decimals': 18
},
{
  'address': "0x707a07c5f35a2098D84559Bba646A5dA1daB1F85",
  'name': "BOPO",
  #'name'l: "BoomerPoints",
  'decimals': 18
},
{
  'address': "0x993791E8aB6d21d10be16A97661BDE0F88c0F579",
  'name': "UIN",
  #'name'l: "UINANCE",
  'decimals': 18
},
{
  'address': "0xCEfd1c15e6Ef84c95d2bbF930C7c9Ddf743146cF",
  'name': "Nka",
  #'name'l: "Nokia",
  'decimals': 18
},
{
  'address': "0x9373A141F7e510E92279D8E1619F9f57a8B88AFD",
  'name': "T5",
  #'name'l: "test5",
  'decimals': 18
},
{
  'address': "0x502B8CadC8e52d3c6334CC46524ccfC5625De212",
  'name': "CANNA",
  #'name'l: "Cannabis",
  'decimals': 18
},
{
  'address': "0x9429e42fE5725590dd4957bECa8991853bC97EEb",
  'name': "t5",
  #'name'l: "test5",
  'decimals': 9
},
{
  'address': "0x009E61595C40DB5901Aa7CE67819DD0020938A1f",
  'name': "T6",
  #'name'l: "test6",
  'decimals': 18
},
{
  'address': "0xCcAE06Ec0787c07D7dF5a60856C73A113Fc7CF9A",
  'name': "IDA",
  #'name'l: "IdaMurni",
  'decimals': 18
},
{
  'address': "0xb424650c45da1fF9C5C81b5c9f42D50F92a795B9",
  'name': "RETH",
  #'name'l: "Realms of Ethernity",
  'decimals': 18
},
{
  'address': "0x6DF922BCbEA7a7B8e22518DD8317139DEeeE73BF",
  'name': "TGC",
  #'name'l: "The Great Coins",
  'decimals': 18
},
{
  'address': "0x6EEb61Fed9E1654d9065184E77c187aDC1d9222c",
  'name': "GGT",
  #'name'l: "Global Gift Token",
  'decimals': 8
},
{
  'address': "0x61f4077DB6Ced7F155fa3b548c2800d388d05D3f",
  'name': "DDAO",
  #'name'l: "Doggy Dao",
  'decimals': 18
},
{
  'address': "0x47a35180688654ace98717a33dbCC8Ca9b736eDa",
  'name': "WZO",
  #'name'l: "WinZOCoin",
  'decimals': 18
},
{
  'address': "0x4a4a0871ba5F2560707d298d47fFa6956b0EFcF4",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xE5417Af564e4bFDA1c483642db72007871397896",
  'name': "GNS",
  #'name'l: "Gains Network",
  'decimals': 18
},
{
  'address': "0x607445Ffd2416F95A46D68480aa2c0F1A3ffE4bf",
  'name': "JGA",
  #'name'l: "JAYGOLDINGART",
  'decimals': 18
},
{
  'address': "0xdf9B4b57865B403e08c85568442f95c26b7896b0",
  'name': "SFF",
  #'name'l: "Sunflower Farm",
  'decimals': 18
},
{
  'address': "0xBE32B7ACD03bcc62F25EBaBD169a35e69ef17601",
  'name': "DNC",
  #'name'l: "DNice",
  'decimals': 18
},
{
  'address': "0xE4DB97A2AAFbfef40D1a4AE8B709f61d6756F8e1",
  'name': "mooSushiUSDC-ETH",
  #'name'l: "Moo Sushi USDC-ETH",
  'decimals': 18
},
{
  'address': "0x62Add2b8Ff6E7a35720A001B40C22588D584FD13",
  'name': "pBONESHARDS",
  #'name'l: "pBoneShards",
  'decimals': 18
},
{
  'address': "0x8E3daC652540A8E5128AFd2DDF2D0c2099E4d4ab",
  'name': "DFX-TVL-KPI",
  #'name'l: "DFX TVL KPI Option",
  'decimals': 18
},
{
  'address': "0xd269af9008C674B3814b4830771453D6a30616eb",
  'name': "VIBES",
  #'name'l: "VIBES",
  'decimals': 18
},
{
  'address': "0xe9EB211208b52434bcFf5E830D5BD4EcfFC0B73F",
  'name': "ZPN",
  #'name'l: "Zippin",
  'decimals': 8
},
{
  'address': "0x4731479cd56E3A55f8207Db9734e3FDB5e136D43",
  'name': "usd",
  #'name'l: "u suck d",
  'decimals': 18
},
{
  'address': "0xE7095C7e56b02a52FA0729A4260490b7a594b77E",
  'name': "CHG",
  #'name'l: "Charg Coin",
  'decimals': 18
},
{
  'address': "0xE597A380d0F8C3dA6f8Ddb16D190bE6f89Cf3bEb",
  'name': "MONEY",
  #'name'l: "GIVE ME YOUR MONEY",
  'decimals': 18
},
{
  'address': "0xb96A8456cAE2e2B5eEb464f398264CdBC5487677",
  'name': "Quickv2",
  #'name'l: "Quickv2",
  'decimals': 9
},
{
  'address': "0x8311881F9e30603273f80D8A7992B250E7dd38Ae",
  'name': "CR8",
  #'name'l: "Create",
  'decimals': 18
},
{
  'address': "0x0C9C3B35b3cBde5459a777b8a1150F27B17CA77C",
  'name': "YNT",
  #'name'l: "YaaNat",
  'decimals': 18
},
{
  'address': "0x524D42592B2235f30c4CbE70e273912d616a1356",
  'name': "EQUA",
  #'name'l: "EQUA Cash",
  'decimals': 18
},
{
  'address': "0x4bA3F40530b008129da2F9C02f8bF4b19eDC0b36",
  'name': "CREW",
  #'name'l: "CREW",
  'decimals': 18
},
{
  'address': "0xD6c06EDF02fBFF31a5d906F07ab4076623e2A6f6",
  'name': "HIR",
  #'name'l: "HigherPolygonCoin",
  'decimals': 18
},
{
  'address': "0xC895E0587CfcFB6d97Eac26F58c14e396945Aeda",
  'name': "ssa",
  #'name'l: "Slim Suli Art",
  'decimals': 18
},
{
  'address': "0x182dB1252C39073eeC9d743F13b5eeb80FDE314e",
  'name': "KITTY",
  #'name'l: "KITTY",
  'decimals': 18
},
{
  'address': "0xB932D203f83B8417Be0F61D9dAFad09cc24a4715",
  'name': "CAT",
  #'name'l: "CAT",
  'decimals': 18
},
{
  'address': "0x20F4F80d2CB021C59ae3EF42F6Da176e1b8e801C",
  'name': "AGZ22",
  #'name'l: "Argz Coin 2022",
  'decimals': 16
},
{
  'address': "0x837A67B2A3AE2D543F2cF8E2fC27Ec6E4D9AA7D2",
  'name': "ABI",
  #'name'l: "Abachi",
  'decimals': 9
},
{
  'address': "0xE3aeA3dF5d1219dF88Ea455a3C550Eb7056d3fE9",
  'name': "MUSTACHE",
  #'name'l: "Mustache Tokens",
  'decimals': 18
},
{
  'address': "0x87D988bbEBDc7B6593122CfEe3d31ed823A28aC3",
  'name': "LOL",
  #'name'l: "LOL",
  'decimals': 9
},
{
  'address': "0x5D41F6587b744a79fC6370966Dfe9BBaBA002022",
  'name': "LOL",
  #'name'l: "LOL",
  'decimals': 9
},
{
  'address': "0x06D3C3b4E609F3535347BD8a7f33ea9E54ceaC00",
  'name': "LOL",
  #'name'l: "LOL",
  'decimals': 9
},
{
  'address': "0x12225cc311e74E774C8E7980af5D6D9d95f6aa7B",
  'name': "LOL",
  #'name'l: "LOL",
  'decimals': 9
},
{
  'address': "0x6d5f5317308C6fE7D6CE16930353a8Dfd92Ba4D7",
  'name': "ABI",
  #'name'l: "Abachi",
  'decimals': 9
},
{
  'address': "0xE6469Ba6D2fD6130788E0eA9C0a0515900563b59",
  'name': "UST",
  #'name'l: "UST (Wormhole)",
  'decimals': 6
},
{
  'address': "0xC4C341148CF121F1fa962Fca211B0057E0eB7D41",
  'name': "APLX",
  #'name'l: "APPLE100X",
  'decimals': 8
},
{
  'address': "0x06F34105B7DfedC95125348A8349BdA209928730",
  'name': "GRIMWEED",
  #'name'l: "Grimweed",
  'decimals': 0
},
{
  'address': "0xAbC454b770cdd7f21F16815D62e2DDaCBbf3cbe2",
  'name': "RZIG",
  #'name'l: "Roubzigon",
  'decimals': 18
},
{
  'address': "0x6Be1dEBa9b5CCC38EA43ad36d6d4AF2392402533",
  'name': "cwe",
  #'name'l: "Chow Wallet",
  'decimals': 9
},
{
  'address': "0x00aAC621B719FfC3480059dbB6a1ce0F3dFE5514",
  'name': "chow",
  #'name'l: "Chow.financial",
  'decimals': 9
},
{
  'address': "0x9CC8179BF19CbdD847F0e1F23399467e0De29807",
  'name': "SCKO",
  #'name'l: "Sicko (Wormhole)",
  'decimals': 18
},
{
  'address': "0x122A972Ee66D139c5074e0c410dEFe2C05F300DA",
  'name': "EAUSD",
  #'name'l: "Elves Attack Stable USD",
  'decimals': 6
},
{
  'address': "0xb4EeF1853F04AEef75F5C476dD27170AF2f8C124",
  'name': "RAD",
  #'name'l: "Radiant",
  'decimals': 18
},
{
  'address': "0x466D5cd361C37e713cc42f70e544b34b85Df3134",
  'name': "CHAINPAL",
  #'name'l: "CHAINPAL TOKEN",
  'decimals': 18
},
{
  'address': "0xE3f415E7d9ae12A691d02D0C21ef5c56592CEaD7",
  'name': "KTA",
  #'name'l: "KTA",
  'decimals': 18
},
{
  'address': "0x20828B944A9B3c19916DeC685Da8489DE6db28D5",
  'name': "KTE",
  #'name'l: "KTE",
  'decimals': 18
},
{
  'address': "0x5187eE21C6cC348d83E64A3CA7F9EDA850ca1bf3",
  'name': "ED",
  #'name'l: "EtherscanDAO",
  'decimals': 18
},
{
  'address': "0x235737dBb56e8517391473f7c964DB31fA6ef280",
  'name': "KASTA",
  #'name'l: "KastaToken",
  'decimals': 18
},
{
  'address': "0xcF0AA6361145f41099a5A9790220944BBcC5E770",
  'name': "KRT",
  #'name'l: "Kretek",
  'decimals': 9
},
{
  'address': "0xc4E77f589Bccc0c9ee0D81CB08110f4c5ED25073",
  'name': "ARCHIS",
  #'name'l: "Archis",
  'decimals': 18
},
{
  'address': "0xB13238Bde6be750799CeC4c5bfdA61A7B38310dC",
  'name': "QuickV3",
  #'name'l: "QuickV3",
  'decimals': 18
},
{
  'address': "0xAEc815Ae1E9AB58f49692aeC2840FfC82C56F7E5",
  'name': "IDOL",
  #'name'l: "IDOL",
  'decimals': 18
},
{
  'address': "0xc85140d1CDBd8639308AEdacE04cEb0D996A61c3",
  'name': "cmon",
  #'name'l: "letsgo",
  'decimals': 9
},
{
  'address': "0x26c7679cE7519e41386A31BAA94695BC97877Dc1",
  'name': "cmon2",
  #'name'l: "letsgo2",
  'decimals': 9
},
{
  'address': "0x2856180C1f2933Ba9b434d311564288F62Bb58cb",
  'name': "'name'",
  #'name'l: "lets3",
  'decimals': 9
},
{
  'address': "0x1d9D7C3eeeF5a5Db990c2870752eE73Ec0939359",
  'name': "KRP",
  #'name'l: "Kreepy (Wormhole)",
  'decimals': 18
},
{
  'address': "0x0650c6e62E6003dC5D271F275d4BfD7c9fD8Df0E",
  'name': "LLFUND",
  #'name'l: "LandLord Fund coin",
  'decimals': 18
},
{
  'address': "0xe1f48d9c0217200425355ca8F9Db38AcB25bFfc5",
  'name': "8_1857",
  #'name'l: "8_1857",
  'decimals': 2
},
{
  'address': "0x3acDd41dc953fcdF41AA10862B8019a76bA34166",
  'name': "MUSD",
  #'name'l: "MUSD",
  'decimals': 5
},
{
  'address': "0x73Dd9Dfe73aB3f0F36BbBA02e589627Ab79e5eDC",
  'name': "BRDM",
  #'name'l: "BRDMpad Token",
  'decimals': 18
},
{
  'address': "0xe4DB44baE1391F0AE45cFA35Abef62941B343e77",
  'name': "MYTE",
  #'name'l: "MYTE",
  'decimals': 18
},
{
  'address': "0xaa5204B434b4D18800960b6B504425e1Ce4822DD",
  'name': "9_2214",
  #'name'l: "9_2214",
  'decimals': 2
},
{
  'address': "0x94A6421bA5a8D055Da67751aFDb9AaC9591BB826",
  'name': "9_2255",
  #'name'l: "9_2255",
  'decimals': 2
},
{
  'address': "0xAAF165e75B4C9370d22b971AF08c630e76Bfa70c",
  'name': "wOMI",
  #'name'l: "Wrapped OMI Token (PoS)",
  'decimals': 18
},
{
  'address': "0xB52CFBca305e13c4C6774846F8d42BB1F0eC51d0",
  'name': "wOMI",
  #'name'l: "Wrapped OMI Token (Wormhole)",
  'decimals': 18
},
{
  'address': "0x896Bc51151B3Bf94b1Cdfb8a2536a54B87e172d6",
  'name': "COCA",
  #'name'l: "COCA",
  'decimals': 18
},
{
  'address': "0x6804b07d883D0169C05233332CcF17aA956424c5",
  'name': "FLEATO",
  #'name'l: "Fleato (PoS)",
  'decimals': 18
},
{
  'address': "0x31272a759bb0DA3ab75544Ba892Fe1C335740Be1",
  'name': "Libra",
  #'name'l: "Libra Meta ",
  'decimals': 9
},
{
  'address': "0x9B6Da34b4013F8558CeD14ee8ae620B5174882FC",
  'name': "GRINGO",
  #'name'l: "GRINGO",
  'decimals': 18
},
{
  'address': "0x331f778017402Be6c1FE014Ad825267cf97C5cD5",
  'name': "LIR",
  #'name'l: "Lirium",
  'decimals': 18
},
{
  'address': "0xBAA2Ae99dD40E29a6541AD28548b1ffE9390482C",
  'name': "BOOGIE",
  #'name'l: "Booger Token",
  'decimals': 18
},
{
  'address': "0xE516be297c846a4a4bF9ec163D6864BB552825Ef",
  'name': "NKE",
  #'name'l: "Nike",
  'decimals': 18
},
{
  'address': "0xdD638b2159A8F374f7ADA9dEE59371e86Ec164E9",
  'name': "DRKH",
  #'name'l: "Dark Horse Coin",
  'decimals': 16
},
{
  'address': "0x9bc1E0aC94Ef09E1B6EEd26CB1BBE8de32AA55B1",
  'name': "WINT",
  #'name'l: "Winter",
  'decimals': 18
},
{
  'address': "0xAad3D1d4cd0EA3a99341Bd8D24575c7fadAf3a37",
  'name': "",
  #'name'l: "AI",
  'decimals': 18
},
{
  'address': "0xc965B8fF279DFe65F83f3Cb641861566ABF3543d",
  'name': "FOLLY",
  #'name'l: "Folly",
  'decimals': 18
},
{
  'address': "0x42F6bdCfd82547e89F1069Bf375aa60e6c6c063d",
  'name': "CIV",
  #'name'l: "Civilization (PoS)",
  'decimals': 18
},
{
  'address': "0xD66eCC2b4AfE01Aa7F70f3615b99FBBf6eF9A494",
  'name': "TRG",
  #'name'l: "Trg Coin",
  'decimals': 18
},
{
  'address': "0x3f91BC18d0F40C8411Ba6d485D4Fd7063A3D0cDB",
  'name': "EVM_BRIDGE",
  #'name'l: "EVM_BRIDGE",
  'decimals': 18
},
{
  'address': "0x44d09156c7b4ACf0C64459Fbcced7613F5519918",
  'name': "$KMC",
  #'name'l: "$KMC",
  'decimals': 18
},
{
  'address': "0x9c2c5daE9e07B020A4Bb45f693a725aed14A0669",
  'name': "GNT",
  #'name'l: "Goddess Nature Token",
  'decimals': 18
},
{
  'address': "0x3ACD12456144fE234E5Aa8F753E424FC49921FC7",
  'name': "chk1",
  #'name'l: "test_a",
  'decimals': 2
},
{
  'address': "0x1fb89Ded7b9E6d6215C70a7F7C8644158f5fc1D6",
  'name': "OTST",
  #'name'l: "opentest",
  'decimals': 18
},
{
  'address': "0x85dE135fF062Df790A5f20B79120f17D3da63b2d",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x9ceE70895726B0ea14E6019C961dAf32222a7C2f",
  'name': "PAGE",
  #'name'l: "Page (PoS)",
  'decimals': 8
},
{
  'address': "0x181277916197ba92e845e70c0f37cbF98C768689",
  'name': "NFTHunter",
  #'name'l: "NFT Hunter",
  'decimals': 18
},
{
  'address': "0x969b2013F1db0F719Ba89b42A93f3a2acf3D0815",
  'name': "MINT",
  #'name'l: "MintCoffinNails",
  'decimals': 18
},
{
  'address': "0x69178A5b15a3A075B660E671B44bB385758251c4",
  'name': "BELI",
  #'name'l: "Beli Token",
  'decimals': 18
},
{
  'address': "0x5FFD62D3C3eE2E81C00A7b9079FB248e7dF024A8",
  'name': "GNO",
  #'name'l: "Gnosis Token (PoS)",
  'decimals': 18
},
{
  'address': "0x0C51f415cF478f8D08c246a6C6Ee180C5dC3A012",
  'name': "HOT",
  #'name'l: "HOLO (PoS)",
  'decimals': 18
},
{
  'address': "0x568044eEf27FC03482B51C34C939481bEBc0875B",
  'name': "APR",
  #'name'l: "APR",
  'decimals': 18
},
{
  'address': "0x9C31536c150A81885eCc69D53a53aef371D30bc8",
  'name': "PEP",
  #'name'l: "PEPPONE",
  'decimals': 18
},
{
  'address': "0x0749902ae8eD9c6A508271BAd18F185dBA7185d4",
  'name': "WETH",
  #'name'l: "Wrapped Ether",
  'decimals': 18
},
{
  'address': "0xc11db8E2231b292634C0a2130cDED0653784E1Ee",
  'name': "ILI",
  #'name'l: "ILI",
  'decimals': 18
},
{
  'address': "0x88dBAee5Af2f1434e82bb600C9119Cd82c69bBFE",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x9cd6746665D9557e1B9a775819625711d0693439",
  'name': "LUNA",
  #'name'l: "LUNA (Wormhole)",
  'decimals': 6
},
{
  'address': "0xbA0147786D3986854aaC5C412F54736ED1cB483F",
  'name': "GOATX",
  #'name'l: "GOATX",
  'decimals': 18
},
{
  'address': "0xaF88cDd91861600c5AD14399e9d32C05C12a1539",
  'name': "zMATIC",
  #'name'l: "Zero Matic",
  'decimals': 18
},
{
  'address': "0x61299774020dA444Af134c82fa83E3810b309991",
  'name': "RNDR",
  #'name'l: "Render Token",
  'decimals': 18
},
{
  'address': "0x1631244689EC1fEcbDD22fb5916E920dFC9b8D30",
  'name': "OVR",
  #'name'l: "OVR (PoS)",
  'decimals': 18
},
{
  'address': "0xc26D47d5c33aC71AC5CF9F776D63Ba292a4F7842",
  'name': "BNT",
  #'name'l: "Bancor Network Token (PoS)",
  'decimals': 18
},
{
  'address': "0x080063b28E79C7D130E9bB55F5f93134354c4d62",
  'name': "testAMGC",
  #'name'l: "testAMGC",
  'decimals': 18
},
{
  'address': "0x67Aa0E7f68E359D34E2C0d2B162B72d1b66fCA7c",
  'name': "tnat",
  #'name'l: "tnat",
  'decimals': 18
},
{
  'address': "0xd1d4480D4181340f98A086C410A6226fB672F044",
  'name': "tnat",
  #'name'l: "tnat",
  'decimals': 18
},
{
  'address': "0x05C8d88CE808B9843B680A847fE2A0B41E235252",
  'name': "ELIRA",
  #'name'l: "eLira",
  'decimals': 18
},
{
  'address': "0x3629dAfE1dD50166F5552bEEa63158b3406Fe8bd",
  'name': "ACNE",
  #'name'l: "Acne (Wormhole)",
  'decimals': 18
},
{
  'address': "0x381d168DE3991c7413d46e3459b48A5221E3dfE4",
  'name': "CUBO",
  #'name'l: "CUBO token",
  'decimals': 18
},
{
  'address': "0xac51C4c48Dc3116487eD4BC16542e27B5694Da1b",
  'name': "ATOM",
  #'name'l: "Cosmos (PoS)",
  'decimals': 6
},
{
  'address': "0x77CBe0689908c544a6856f344352e8B976Cd184a",
  'name': "SPARTAN",
  #'name'l: "SPARTANCOIN",
  'decimals': 18
},
{
  'address': "0x5423063af146F5abF88Eb490486E6B53FA135eC9",
  'name': "CNDL",
  #'name'l: "Candle (PoS)",
  'decimals': 18
},
{
  'address': "0xB7bDEB0Fa068328897e2ad171C9D668530200dFE",
  'name': "GIF",
  #'name'l: "Global Index Fund",
  'decimals': 18
},
{
  'address': "0x1b53eDdC80d307345bD1D89e6A0350ac3777f7f3",
  'name': "IND",
  #'name'l: "ind",
  'decimals': 18
},
{
  'address': "0x606461304c2Be6A34Ab960BceEf2126f488c7036",
  'name': "QUI2",
  #'name'l: "Lilah Washington",
  'decimals': 18
},
{
  'address': "0x16fCA7ed10EBC378Ead7A02d3B3e968271a3dd55",
  'name': "INDIE",
  #'name'l: "Indiverse",
  'decimals': 18
},
{
  'address': "0x5E0294Af1732498C77F8dB015a2d52a76298542B",
  'name': "ORION",
  #'name'l: "Orion Money Token (Wormhole)",
  'decimals': 18
},
{
  'address': "0x8c638C60428b98b71232531f173E7A43B973f79b",
  'name': "verse",
  #'name'l: "verse",
  'decimals': 18
},
{
  'address': "0xaeE24d5296444c007a532696aaDa9dE5cE6caFD0",
  'name': "SWD",
  #'name'l: "SW DAO [via ChainPort.io]",
  'decimals': 18
},
{
  'address': "0x041dEE4Be8Dd8A5C2927444A533e30320ffF50D3",
  'name': "NWO22",
  #'name'l: "NewWorldOrder",
  'decimals': 18
},
{
  'address': "0x5E19Cbe29D7B67CE45FDB0935169c1e1dF8Cf458",
  'name': "BD",
  #'name'l: "BitDollars",
  'decimals': 18
},
{
  'address': "0x9A555fc38c23d64567EC199f7CAc6Df2768179B2",
  'name': "GEMZ",
  #'name'l: "GEMS ZIRION",
  'decimals': 18
},
{
  'address': "0x66e16D50c07A01BB473eC794349d45aa1a0E5Dc2",
  'name': "FOAM",
  #'name'l: "FOAM Token (PoS)",
  'decimals': 18
},
{
  'address': "0x79948EEaDe7A2BFBeCC49A6084D65229a8Cf8Fe8",
  'name': "TGCH",
  #'name'l: "Golden Chain",
  'decimals': 18
},
{
  'address': "0x9f5DEF8B58F2d574aF3562b8038Cd66746C9fC40",
  'name': "DOGE",
  #'name'l: "(PoS) Dogecoin",
  'decimals': 18
},
{
  'address': "0xA247B0476C11DAb0be132e91fe63b2b7085d7C0E",
  'name': "BERYL",
  #'name'l: "Beryl",
  'decimals': 18
},
{
  'address': "0xAE99915429188F006736d9Bd065616877373c086",
  'name': "ENLT",
  #'name'l: "Enlightenment",
  'decimals': 18
},
{
  'address': "0xae8Dc2A69e1029d68B2C663cd21B94fbB2F79d24",
  'name': "LMLT",
  #'name'l: "Limelight",
  'decimals': 9
},
{
  'address': "0x478CA805BF2A08F8377988371b0EEd6d3423429B",
  'name': "KPOL",
  #'name'l: "KapolToken",
  'decimals': 18
},
{
  'address': "0x68d77Ad30dEfAD49f9FdADd20dD6f6D29547126d",
  'name': "BFT",
  #'name'l: "Bifrost",
  'decimals': 18
},
{
  'address': "0x687565af1d121193377f9e90d29B4304A0ccDdcD",
  'name': "WOSP",
  #'name'l: "WOSP",
  'decimals': 18
},
{
  'address': "0x82Cc4F8a33Fb5898662Fa22A3F5bbCdd89750D3C",
  'name': "UZ",
  #'name'l: "UZOO",
  'decimals': 18
},
{
  'address': "0x2356D0B581eAafD83694b7c636Ce2Ef942613dEf",
  'name': "CAPZ",
  #'name'l: "BottleCapz",
  'decimals': 18
},
{
  'address': "0x33284C0B3aDF5586CBadc6707670F1b3F8B5CBaC",
  'name': "UNI-V2",
  #'name'l: "Uniswap V2",
  'decimals': 18
},
{
  'address': "0x7573c3372D4a329dfD1860316Fc36C7BCEecF022",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0x22AADbdB89534C3C455E59066AfE0ce9FEC0436A",
  'name': "ViCiVest",
  #'name'l: "ViCiVest",
  'decimals': 18
},
{
  'address': "0x5536a8E754A445a85129510eE69cB932177635fF",
  'name': "VFO",
  #'name'l: "ViCiFloki",
  'decimals': 18
},
{
  'address': "0x90F3edc7D5298918F7BB51694134b07356F7d0C7",
  'name': "DDAO",
  #'name'l: "DEFI HUNTERS DAO Token",
  'decimals': 18
},
{
  'address': "0x5dd5d28d0205bE20F4B4E144c368b64ef63a1F81",
  'name': "PENT",
  #'name'l: "PENT",
  'decimals': 18
},
{
  'address': "0xA7dC6e8e775EF111D57e1a42BD5CF73883323d36",
  'name': "PENT",
  #'name'l: "PENT",
  'decimals': 18
},
{
  'address': "0xC6c1f684151eb235472139477F869b2e8385C416",
  'name': "PENT",
  #'name'l: "PENT",
  'decimals': 18
},
{
  'address': "0x8940145a2c0722C0142065A233116f6Db3AEAAA8",
  'name': "PENT",
  #'name'l: "PENT",
  'decimals': 18
},
{
  'address': "0xc2755915a85C6f6c1C0F3a86ac8C058F11Caa9C9",
  'name': "SLP",
  #'name'l: "SushiSwap LP Token",
  'decimals': 18
},
{
  'address': "0xAa7DbD1598251f856C12f63557A4C4397c253Cea",
  'name': "MCO2",
  #'name'l: "Moss Carbon Credit (PoS)",
  'decimals': 18
},
{
  'address': "0x9C88fffF3644f8A2146aea2EFD6fB209960D5ecD",
  'name': "Light",
  #'name'l: "GuidingLightStudio",
  'decimals': 10
},
{
  'address': "0xB6768Dd6167433822A54663BE92697eEE05a1C20",
  'name': "LMLT",
  #'name'l: "Limelight",
  'decimals': 9
},
{
  'address': "0xb2292580Da060611621EaE62D4d43d56b67adc2a",
  'name': "ZxUSD",
  #'name'l: "ZxUSD",
  'decimals': 2
},
{
  'address': "0xbAC4fBd731bBEaef5e2131a6009D06c064Ff5f89",
  'name': "MONOCL",
  #'name'l: "Monoclonal Antibodies",
  'decimals': 8
},
{
  'address': "0x07d5bf841beb877c9bE550B79cb0d49e4e091Dec",
  'name': "IAN",
  #'name'l: "ian",
  'decimals': 18
},
{
  'address': "0x071AC29d569a47EbfFB9e57517F855Cb577DCc4C",
  'name': "GFC",
  #'name'l: "GCOIN",
  'decimals': 18
},
{
  'address': "0x6c1C9f90F59E97B0551C71605B98e51Eb71f4000",
  'name': "JEX",
  #'name'l: "JEX",
  'decimals': 18
},
{
  'address': "0x6ef9dA0D18f7eAeE738C5f4ac727C3f4999581a6",
  'name': "SAMPO",
  #'name'l: "Sampo Token",
  'decimals': 18
},
{
  'address': "0x5d0915f929FC090fd9c843a53e7e30335dD199bc",
  'name': "pTREAT",
  #'name'l: "pTREAT",
  'decimals': 18
},
{
  'address': "0xE1e549Ef22139f3f739Cd2c2b1edb83f37C39502",
  'name': "SMGT",
  #'name'l: "SAMARAG",
  'decimals': 18
},
{
  'address': "0x03478d9735e07E9ed9ee6e2B0F363b6C07621A45",
  'name': "ZSDAO",
  #'name'l: "ZeusDAO",
  'decimals': 18
},
{
  'address': "0x1346FdB62241e238Be9F84A2FC364c0657757015",
  'name': "NEWT",
  #'name'l: "Eye of Newt",
  'decimals': 0
},
{
  'address': "0x9d781d8dB06111E3B05c8290A087cCd5f3b9EcD2",
  'name': "HELH",
  #'name'l: "Helheim Finance",
  'decimals': 18
},
{
  'address': "0x6765d98C2C39743AcF6DbD258eFAf3b23c6afea2",
  'name': "mFOOD",
  #'name'l: "Mithraeum Food",
  'decimals': 18
},
{
  'address': "0x8bC8b0b98DA854E3864b663368d9b25A7be337b2",
  'name': "mWOOD",
  #'name'l: "Mithraeum Wood",
  'decimals': 18
},
{
  'address': "0x9ab9151c4e5Dd43216FC517e92B2af6bBBE52329",
  'name': "EAR2",
  #'name'l: "Sophia Ellison",
  'decimals': 18
},
{
  'address': "0x84ACaAD50edeb33D50D2dbbc5f0db24170944720",
  'name': "OFF",
  #'name'l: "Gregory Snow",
  'decimals': 18
},
{
  'address': "0x428aC1de3FC08c0F3A47745C964f7d677716981F",
  'name': "IBZ",
  #'name'l: "IBIZA Token (PoS)",
  'decimals': 18
},
{
  'address': "0xcF51ab7398315DbA6588Aa7fb3Df7c99D3D1F4dD",
  'name': "hNOBT",
  #'name'l: "Hope Nobt",
  'decimals': 18
},
{
  'address': "0xdE61923B4C94C55E90085F3FEEe4651Af1Db893c",
  'name': "BETTY",
  #'name'l: "BettyWhiteCoin",
  'decimals': 18
},
{
  'address': "0xa0c56f2259cA43a6F2933987E22d5e640b48a34f",
  'name': "Light (S)",
  #'name'l: "Guiding Light Stable",
  'decimals': 2
},
{
  'address': "0xCC55C3EA6412A5e94f994D8A93901adcDe283349",
  'name': "Light",
  #'name'l: "Guiding Light Studio",
  'decimals': 2
},
{
  'address': "0xCe34140F45B2eea8d34e8259e6ba74fc05Ac6c0a",
  'name': "SHIBAV",
  #'name'l: "Shiba Volcano",
  'decimals': 18
},
{
  'address': "0x5c4b7CCBF908E64F32e12c6650ec0C96d717f03F",
  'name': "BNB",
  #'name'l: "Binance Token",
  'decimals': 18
},
{
  'address': "0x87C3896ef2D51b151E3A70290e306F9F0c0630B6",
  'name': "NO21",
  #'name'l: "no21",
  'decimals': 18
},
{
  'address': "0x672255E73E9FcB8d8971b6e2622057bAa84B5Afe",
  'name': "PLAY",
  #'name'l: "Herocoin (PoS)",
  'decimals': 18
},
{
  'address': "0xb44d5e8055499d71BABEC798f89E8cFb9F2A9774",
  'name': "TYT",
  #'name'l: "TraeYoungToken",
  'decimals': 18
},
{
  'address': "0xDE0E1F6Fd2B00E690A656817C2384ED171588F48",
  'name': "ELP",
  #'name'l: "Esowood Lich Phylactery ",
  'decimals': 18
},
{
  'address': "0x7D645CBbCAdE2A130bF1bf0528b8541d32D3f8Cf",
  'name': "ALRTO",
  #'name'l: "Alerto",
  'decimals': 18
},
{
  'address': "0xb8a9c3CBc8AEbBc0130f1b38A694d8D73b50185a",
  'name': "MST",
  #'name'l: "Matic Space Token",
  'decimals': 18
},
{
  'address': "0x94b45F046aa7A45815bDFdFe9ae50D782819ade0",
  'name': "INR",
  #'name'l: "INR",
  'decimals': 18
},
{
  'address': "0x0EC3854a9bAe95E4C5ccce224A1257E1fEB5372b",
  'name': "TAXI",
  #'name'l: "Taxi",
  'decimals': 18
},
{
  'address': "0x34F9d1D6f765a638B2c1264090327ee4E8cb181A",
  'name': "NUGZ",
  #'name'l: "Sativa Farms Token",
  'decimals': 18
},
{
  'address': "0x6db7f16d8Dd1E120acF2965B8c86d8BDEc8c4aDd",
  'name': "WABEWT",
  #'name'l: "Wrapped AllianceBridge Energy Web Token",
  'decimals': 18
},
{
  'address': "0x2Af9cADA7d35E80D69fBA3c81B8319E0361d9631",
  'name': "W? EWD ?",
  #'name'l: "Wrapped EnergyWeb DOGE",
  'decimals': 18
},
{
  'address': "0x829ae5c38B28f852B823228829681E910010aDc3",
  'name': "ando",
  #'name'l: "ando",
  'decimals': 18
},
{
  'address': "0xa967625EB982573D1ee72E5CE47B017520E16291",
  'name': "SGO",
  #'name'l: "StadiumGO",
  'decimals': 18
},
{
  'address': "0x5273b6D3BAc507f6B13B79F7fD6dc422E4f50f39",
  'name': "TST",
  #'name'l: "Test",
  'decimals': 18
},
{
  'address': "0x53CF566cf80e1a26Bfc16D055C866A72fdcBaEe7",
  'name': "BTST",
  #'name'l: "Bitcoin Stable (PoS)",
  'decimals': 18
},
{
  'address': "0xCD2bA3d8161eBcB3FdBeFC3E6a65b1906Bbc42c0",
  'name': "ILW",
  #'name'l: "illiWo",
  'decimals': 18
},
{
  'address': "0x2d9BB362cBF5f84B3d321B34d1e0dB5f23c60754",
  'name': "VHIN2",
  #'name'l: "VHI2",
  'decimals': 9
},
{
  'address': "0x74f2FdE099061460ead6C04a6b374Cb739d2141e",
  'name': "t7",
  #'name'l: "test7",
  'decimals': 9
},
{
  'address': "0xb884d159241677F4624856dc650204ee9f592Ef0",
  'name': "GAIAC",
  #'name'l: "Gaia Coin",
  'decimals': 9
},
{
  'address': "0xaF408531CeEb192088dFE34e788Ba4bd60968519",
  'name': "WARP",
  #'name'l: "Warp Bond",
  'decimals': 18
},
{
  'address': "0x1f6402120b048D60f2aB0221224b4c2BA5Bdb335",
  'name': "SST",
  #'name'l: "SmatStake",
  'decimals': 18
},
{
  'address': "0x73daFf403D63BB89d2dE71995Cb19E26cddEa5C6",
  'name': "REAPER",
  #'name'l: "Reaper Protocol",
  'decimals': 9
},
{
  'address': "0xa1d92186D3619eC2cE7C91467Fa2FDd0dE992714",
  'name': "NCOINP",
  #'name'l: "NCoin",
  'decimals': 5
},
{
  'address': "0x8b6311DB02D6d1754Dee951F7F9Ff2f207A57eED",
  'name': "DPD",
  #'name'l: "DPD Token",
  'decimals': 12
},
{
  'address': "0xAB88342a5F54C14493C33F9172e6854627008d29",
  'name': "DIM",
  #'name'l: "DIMITRI TOKEN",
  'decimals': 18
},
{
  'address': "0x4CDde30DABe200F1BB4e7593a44A0eA044FCb07e",
  'name': "FIX",
  #'name'l: "Fixed",
  'decimals': 18
},
{
  'address': "0x9A58fA00C394b2A4C818679Ab4430209CEFAB1b3",
  'name': "TORA",
  #'name'l: "TORA Coin",
  'decimals': 18
},
{
  'address': "0xA960a83F05D8F1B02A437328f1b13F82dBD179b7",
  'name': "SOL",
  #'name'l: "Solidity",
  'decimals': 18
},
{
  'address': "0xE04d7765aDE546C411D4B9020Fe134E7E0c90927",
  'name': "GMA",
  #'name'l: "GoldmaToken$",
  'decimals': 9
},
{
  'address': "0xBFe0eA5a9306201d70164bb6735240E5651969b2",
  'name': "GMA",
  #'name'l: "GoldmaToken$",
  'decimals': 9
},
{
  'address': "0x46B35c64804ae4722041DC3d36619c3E2d9eBB0d",
  'name': "GMA",
  #'name'l: "GoldmaToken$",
  'decimals': 9
},
{
  'address': "0x00cB8f9Ff8e1034047D33dD33F0535DBa2513e66",
  'name': "GMA",
  #'name'l: "GoldmaToken$",
  'decimals': 9
},
{
  'address': "0x9A1A1cf27D4800a0D70a3aA9F5ef1b7bD72A9541",
  'name': "BFT",
  #'name'l: "Bifrost",
  'decimals': 18
},
{
  'address': "0x533C5a09E586D25245f33D2A4000E25C5e86D6AA",
  'name': "REAPER",
  #'name'l: "Reaper Protocol",
  'decimals': 9
},
{
  'address': "0xC6a6c7269eD3c875303cD339B040d61355d1084f",
  'name': "BFT",
  #'name'l: "Bifrost",
  'decimals': 18
},
{
  'address': "0xA82E240eA4717a367D5c368B7D5E4c41f77855c0",
  'name': "POLYGUN",
  #'name'l: "PolyGun",
  'decimals': 18
},
{
  'address': "0x8A311C8CD682e42755f46aB37bF807966D0C3007",
  'name': "MEC",
  #'name'l: "Memecoin",
  'decimals': 18
},
{
  'address': "0xc3cFFDAf8F3fdF07da6D5e3A89B8723D5E385ff8",
  'name': "RBC",
  #'name'l: "Rubic (PoS)",
  'decimals': 18
},
{
  'address': "0x870aeCb477387f55d79cA572Fb3Caec59F189821",
  'name': "AIA",
  #'name'l: "AIA w-eth MATIC",
  'decimals': 18
},
{
  'address': "0x9c4d6D35f1A1C465e5298aacC053C1279dC7630F",
  'name': "CYPUNK",
  #'name'l: "Cyberpunk",
  'decimals': 8
},
{
  'address': "0x04977E869e56f75b7816eFd41C75CC4f7D4325Af",
  'name': "USDB",
  #'name'l: "Bancor USD Token (Wormhole)",
  'decimals': 18
},
{
  'address': "0x45d9dFd954afED83c5bad2E2239E1602dc9B2053",
  'name': "EAR",
  #'name'l: "EAR",
  'decimals': 6
},
{
  'address': "0xabCCA87e198638bA642Af7c32148f4Ef7CD2897d",
  'name': "TGCH",
  #'name'l: "Golden Chain",
  'decimals': 18
},
{
  'address': "0x0A81bfCc9809034B08740F9F3e95d048bc74Ed92",
  'name': "",
  #'name'l: "VLR Token",
  'decimals': 8
},
{
  'address': "0x077c2AaD56C44A3d678895249B6A438F7bD972d7",
  'name': "VALERI",
  #'name'l: "VALERI Token",
  'decimals': 8
},
{
  'address': "0x7c7DAAF2dB46fEFd067f002a69FD0BE14AeB159f",
  'name': "renLUNA",
  #'name'l: "renLUNA",
  'decimals': 6
},
{
  'address': "0x7e94De269df2eb9F4D0443d46500191F19C9A8dA",
  'name': "UNITY",
  #'name'l: "Unity",
  'decimals': 18
},
{
  'address': "0x887650A6236A8e4dfE7Cd3f61d00343a90679401",
  'name': "GRIM",
  #'name'l: "Grimace Coin",
  'decimals': 18
},
{
  'address': "0x3F46a70adB395cddb81FF9bFE3B62aDae1B44816",
  'name': "WARP",
  #'name'l: "Warp Token",
  'decimals': 9
},
{
  'address': "0x63CD45309FED12af86B41c91b942f9749404af19",
  'name': "muchroom",
  #'name'l: "muchroom Token",
  'decimals': 9
},
{
  'address': "0x49a0400587A7F65072c87c4910449fDcC5c47242",
  'name': "MIM",
  #'name'l: "Magic Internet Money",
  'decimals': 18
},
{
  'address': "0x3CE442bd5190516665436587b9E613655C0C78AD",
  'name': "ZNG",
  #'name'l: "ZENICHANGE",
  'decimals': 9
},
{
  'address': "0x356b241E5211dD131934BE4877334E08dC107984",
  'name': "IVS",
  #'name'l: "Stalin",
  'decimals': 8
},
{
  'address': "0x228b5C21ac00155cf62c57bcc704c0dA8187950b",
  'name': "NXD",
  #'name'l: "Nexus Dubai",
  'decimals': 18
},
{
  'address': "0x458375f621d93f90Ec5ae0b674471e9f2F21645e",
  'name': "ASL",
  #'name'l: "Meta analysis protocol",
  'decimals': 6
},
{
  'address': "0xa77944a08f2e127aC8392eC19C094DfEDDdC604C",
  'name': "MUSH",
  #'name'l: "Mush",
  'decimals': 18
},
{
  'address': "0x71A77015f0F6061Cb89aF0B0477734c8D47b1ffB",
  'name': "SHDY",
  #'name'l: "ShibDogeYe",
  'decimals': 18
},
{
  'address': "0xcb88e394f32cbeE4E5339913Cc09121208C7DD0B",
  'name': "muchroom",
  #'name'l: "muchroom Token",
  'decimals': 9
},
{
  'address': "0x7F242faa8AD603dB3C18c30bd1C88130abCd8088",
  'name': "TTTT",
  #'name'l: "Test1",
  'decimals': 18
},
{
  'address': "0x4c2A13D5E2D7A903911367512Ef9E4778Ef9083F",
  'name': "NFTa",
  #'name'l: "JR Collection Token",
  'decimals': 18
},
{
  'address': "0x42b088B89692D8AC99490454c440BbC507Eb0Ff3",
  'name': "WOW",
  #'name'l: "WOW",
  'decimals': 18
},
{
  'address': "0x7385034B28dbA5a3aCc916Aab15a0B2a665A6067",
  'name': "AFRO",
  #'name'l: "AfroAmericanCoin",
  'decimals': 18
},
{
  'address': "0x3E3779675ed89a42db9faf3524B7E8A8b51281d0",
  'name': "VEEX",
  #'name'l: "Vayner Token",
  'decimals': 18
},
{
  'address': "0x0123dd44eAaB58Eb368A2a6183D1623d29204a93",
  'name': "NUGZ",
  #'name'l: "Sativa Farms NUGZ",
  'decimals': 18
},
{
  'address': "0x6AcdA5E7EB1117733DC7Cb6158fc67f226b32022",
  'name': "ZRO",
  #'name'l: "ZROToken",
  'decimals': 18
},
{
  'address': "0x5D195d77Aa87f304cdf39bd3CE14B7BE27b6609D",
  'name': "JEM",
  #'name'l: "jem.aplesyrup.com",
  'decimals': 18
},
{
  'address': "0x6bfB6244a018a926C1d96a4e65A687Ba01afA4a6",
  'name': "uwu",
  #'name'l: "otaku",
  'decimals': 18
},
{
  'address': "0x63F02B3FB3DB44576D1D8bF6665C27da548b5261",
  'name': "AEG",
  #'name'l: "Aegis",
  'decimals': 18
},
{
  'address': "0x6b0284AfEba980c0818Ec5D28384c4FeE3b03973",
  'name': "BLS",
  #'name'l: "BullToken",
  'decimals': 2
},
{
  'address': "0x122903661d4930d436d300fD2Fe6F808e3085217",
  'name': "POL",
  #'name'l: "Polycoin",
  'decimals': 18
},
{
  'address': "0x58FfF03a723e21880534C347e5F849fA2C61bEc3",
  'name': "LOKO",
  #'name'l: "Cafe Crypto Token",
  'decimals': 18
},
{
  'address': "0x40523D49107d49582695053Fd9433d73ff6d75C2",
  'name': "CBC",
  #'name'l: "CUBIC",
  'decimals': 18
},
{
  'address': "0x9ec9551d4A1a1593b0ee8124D98590CC71b3B09D",
  'name': "hUSDC",
  #'name'l: "USD Coin Hop Token",
  'decimals': 6
},
{
  'address': "0x0B300c129EE1Ff3268154Cfc95165Ed9140F036e",
  'name': "testLMLT",
  #'name'l: "LmltTest",
  'decimals': 9
},
{
  'address': "0x41b3966B4FF7b427969ddf5da3627d6AEAE9a48E",
  'name': "NEXO",
  #'name'l: "Nexo (PoS)",
  'decimals': 18
},
{
  'address': "0x8051568bC88D01160d4Bb367a2C8eA0138D0c2d9",
  'name': "MSDAO",
  #'name'l: "Movie Studio DAO Token",
  'decimals': 18
},
{
  'address': "0x2aF1D53393a17B548a07d8ff4CfA873044399fCA",
  'name': "TEAR",
  #'name'l: "Teardrop coin",
  'decimals': 18
},
{
  'address': "0x64060aB139Feaae7f06Ca4E63189D86aDEb51691",
  'name': "UNIM",
  #'name'l: "Unicorn Milk",
  'decimals': 18
},
{
  'address': "0xB79a6C0571e72daA9D8383200CF2330d42AEadBe",
  'name': "GRINGO",
  #'name'l: "GRINGO",
  'decimals': 18
},
{
  'address': "0xbd59Bda91372cDc07643F76cacC20D3d880050d3",
  'name': "PICK",
  #'name'l: "PickUp Token",
  'decimals': 18
},
{
  'address': "0x1e06408DaE0638B4B4564F65dA4319f382e9469D",
  'name': "VHIN2",
  #'name'l: "VHI2",
  'decimals': 9
},
{
  'address': "0x543bbE485270d9E75f21ea99718da702b339379a",
  'name': "VHIN3",
  #'name'l: "VHI3",
  'decimals': 9
},
{
  'address': "0x374aF2dB27A0c655BEBA4323b4C4273DC30Eba73",
  'name': "NXTT",
  #'name'l: "NextEarthToken",
  'decimals': 18
},
{
  'address': "0x30E37610aD2fa5A587B7790A30938183434142f3",
  'name': "CR7",
  #'name'l: "Cristiano Ronaldo",
  'decimals': 18
},
{
  'address': "0xB4456f338A921E243E1374D65136b6c36d1a40e7",
  'name': "ALIGHT",
  #'name'l: "Aural Light DAO",
  'decimals': 18
},
{
  'address': "0x91716DA21bd370F0beAa0eBf2e58BBAa4E614507",
  'name': "NIG",
  #'name'l: "Pepe",
  'decimals': 18
},
{
  'address': "0x06176Ae811D20c404B729dCD48E839b70ba3acFA",
  'name': "GFNC",
  #'name'l: "GrafenoCoin",
  'decimals': 8
},
{
  'address': "0x262BeE6504cc30DB0A19f6Bea177EAD8C0d139a4",
  'name': "LLAMA",
  #'name'l: "Llama Token",
  'decimals': 18
},
{
  'address': "0x10A8529AfF17B87066cc668bb77Adc92d2435938",
  'name': "6IX",
  #'name'l: "6ix",
  'decimals': 8
},
{
  'address': "0x80AB6dc6e6Ca99f2319213cd97fa02c14E4bd434",
  'name': "FSI",
  #'name'l: "Focused Sharpe Index ",
  'decimals': 18
},
{
  'address': "0x165997aaFa86aD7FAa9906B6c8ED15d536E65Bf6",
  'name': "BLBG",
  #'name'l: "www.BloombergToken.com",
  'decimals': 18
},
{
  'address': "0x115D8bFeDbE07703991527Db711f715A39bd8f9f",
  'name': "OVRT",
  #'name'l: "Overture Song Management",
  'decimals': 18
},
{
  'address': "0x5a0625604dd302c40D9023060e929822578D1aFF",
  'name': "fBTC",
  #'name'l: "fakeBTC",
  'decimals': 18
},
{
  'address': "0x7b6211A54D97B6d98DED9DE41daa722a505E9E53",
  'name': "fUSDT",
  #'name'l: "fakeUSDT",
  'decimals': 18
},
{
  'address': "0x7EA5E774D2Db3b17da5218D8e66e95e11c37806c",
  'name': "VHIN2",
  #'name'l: "VHI2",
  'decimals': 9
},
{
  'address': "0x736009da4438a009523E49C98e332F7086E8f887",
  'name': "SOGGA",
  #'name'l: "SoggaToken",
  'decimals': 18
},
{
  'address': "0xaE14b0AFBa354050c58aea291615a6d85bbc5fa3",
  'name': "SoHe",
  #'name'l: "SocialHeirs",
  'decimals': 18
},
{
  'address': "0x3b64d9c811d0AcB97Ac2E610B31E0cBbca7cC51A",
  'name': "BADX",
  #'name'l: "BadXGirls",
  'decimals': 18
},
{
  'address': "0xd52D9bA6FCBadB1FE1E3aca52CbB72c4D9bbb4eC",
  'name': "GFI",
  #'name'l: "GtpsFinance",
  'decimals': 18
},
{
  'address': "0x00fF0a20a6C7208847F9C62F2c1C308D8F0709Fe",
  'name': "UCREDIT",
  #'name'l: "Undisclosed Credits",
  'decimals': 18
},
{
  'address': "0x3a2F651bBbEABEF36412be01659B93D0c6F2bF1f",
  'name': "CODE",
  #'name'l: "BitCode",
  'decimals': 9
},
{
  'address': "0x039795Cc4221d5d7F3D15a1f9F8e696916E9fF10",
  'name': "CT",
  #'name'l: "Credit Token",
  'decimals': 18
},
{
  'address': "0x3da78d5C0EA557C28B4dC92A6629ABb03dC6dC7D",
  'name': "AlertoCrv33CRV-f",
  #'name'l: "Curve.fi Factory USD Metapool: AlertoCrv3",
  'decimals': 18
},
{
  'address': "0x10e93B7bFA1b32673EFd07A91439851FaA5E7Cf4",
  'name': "META POINT",
  #'name'l: "Meta Point",
  'decimals': 9
},
{
  'address': "0x8914B29F7Bea602A183E89D6843EcB251D56D07e",
  'name': "CRVALRTO-f",
  #'name'l: "Curve.fi Factory Plain Pool: CRV/ALRTO",
  'decimals': 18
},
{
  'address': "0xb0F9Cb6Fe9ce344525F557D112fd82dc6CdE6f55",
  'name': "MJT",
  #'name'l: "MJT Lottery",
  'decimals': 18
},
{
  'address': "0x63fB1c30c547ec273d258E195b8877CC2A94a184",
  'name': "$USD",
  #'name'l: "Dollar Sign USD",
  'decimals': 0
},
{
  'address': "0x1f1dF13C89feb23f8076A80C7767169697614D2E",
  'name': "ARA",
  #'name'l: "Nuchain ARA Token",
  'decimals': 18
},
{
  'address': "0x1044669Ed21Cd9F75527DF4babC4a35A0b7685D5",
  'name': "VMT",
  #'name'l: "Vinhos Minho ",
  'decimals': 18
},
{
  'address': "0x7168C51e6E37AacED3AA7A15a03F77eBC90197c0",
  'name': "IDEXUSDT3CRV-f",
  #'name'l: "Curve.fi Factory USD Metapool: IDEX/USDT",
  'decimals': 18
},
{
  'address': "0xD34656c3F6C48987300faC434Fd1B80AED8F8642",
  'name': "TEST",
  #'name'l: "My Test Set",
  'decimals': 18
},
{
  'address': "0x919B22450c38108bB624c4c72B085Cd7C0442b80",
  'name': "MHP",
  #'name'l: "Minor Health Potion",
  'decimals': 0
},
{
  'address': "0x1D0f246ABE4454678EeB1D2e4E763471940b73e3",
  'name': "?",
  #'name'l: "Penguin Party Pebble",
  'decimals': 18
},
{
  'address': "0x7A53ebC249383F22010189CE9a1415db7e53Bb2d",
  'name': "BFI",
  #'name'l: "BFI v0 Token",
  'decimals': 9
},
{
  'address': "0xcECf60B95109Cb4C897b22877612228f0C76E52c",
  'name': "Lithereum3CRV-f",
  #'name'l: "Curve.fi Factory USD Metapool: Lithereum",
  'decimals': 18
},
{
  'address': "0x622703d6517BdeDF1FA5d076D30dcbB00ee18d5C",
  'name': "Lithereum-f",
  #'name'l: "Curve.fi Factory Plain Pool: SOL+LUNA+AAVE+maUSD",
  'decimals': 18
},
{
  'address': "0x1cfe63B04892735bcD2325a5806CB33B2c0C8A32",
  'name': "XBBX",
  #'name'l: "BitblocksDAO",
  'decimals': 18
},
{
  'address': "0x71880e3bE349dBcA28F4D485B66eD47fc6aF6eb6",
  'name': "GLYCINE",
  #'name'l: "Glycine",
  'decimals': 9
},
{
  'address': "0x3bfE9F4e25ed2793610BD78aFe766871F62AA11c",
  'name': "Dream",
  #'name'l: "Dreamcome",
  'decimals': 18
},
{
  'address': "0xb5B15b41D1a8bDd5a8f481bb398036C3b8605f50",
  'name': "Norus",
  #'name'l: "StopRussia",
  'decimals': 7
},
{
  'address': "0xae357fF86777Bb3b45ffCe43241c8390df6b06ca",
  'name': "HYPE",
  #'name'l: "Hyper",
  'decimals': 18
},
{
  'address': "0xC5fff43Dca9D2d2719F268bC5f0106A733121626",
  'name': "VHIN3",
  #'name'l: "VHI3",
  'decimals': 9
},
{
  'address': "0x282d8efCe846A88B159800bd4130ad77443Fa1A1",
  'name': "mOCEAN",
  #'name'l: "Ocean Token (PoS)",
  'decimals': 18
},
{
  'address': "0x412D331961Ee8E90F17d48dA673277C9657667F1",
  'name': "HARA",
  #'name'l: "Harambe",
  'decimals': 18
},
{
  'address': "0x7F376373FAC6347f6392d672BFb6D3959477929B",
  'name': "VHIN2",
  #'name'l: "VHI2",
  'decimals': 9
},
{
  'address': "0x60B22830f12475fA4ac10d6e8ca8c769C8088F1A",
  'name': "VHIN4",
  #'name'l: "VHI4",
  'decimals': 9
},
{
  'address': "0xd3688D6926Aa00668579455966DAE7433eEe82Db",
  'name': "CBT",
  #'name'l: "can burn token",
  'decimals': 18
},
{
  'address': "0x8b94710759F744607FAA8B84433680777f0256F0",
  'name': "VHIN",
  #'name'l: "Vallhund Inu",
  'decimals': 9
},
{
  'address': "0x9fe19698aE613Ae626CC3670A92A105e1089D68E",
  'name': "HOM",
  #'name'l: "HOMToken",
  'decimals': 9
},
{
  'address': "0xB6448b01A2FBfCa59211B5B34A3FFB71FA80A728",
  'name': "TML",
  #'name'l: "TOMORROWLAND",
  'decimals': 18
},
{
  'address': "0xd1c8B718dB806C93edDbAc650AE978112410915f",
  'name': "NOODLE",
  #'name'l: "Noodle token",
  'decimals': 18
},
{
  'address': "0x4C756637eEA32056EDE331e00039fe6dae734093",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0xb3c9dc133Bb8c22ba1771A15cAE244185587e31f",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x65900e92670F4FDb8f44d12237686Cd4900b6A25",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0xD644c7f90A9d1fb7353515646B2Ca029FdE6FE65",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0xbFb4D9459EC704A3919a29954244ad753e7Bcb89",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x0c63E4c1a13A92d46Ce0797bD5BbA57B67fb177B",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x1eB645Bffce30BFFDDCfeE2C1557681a87dc00BE",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x748490F8D30975F4B06e239293f312315Afc917F",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0xb21361CfA7Ac7419Ce6F745a0519618343521165",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x02a2cB09d1CcE19B870Ea44dFa9774Aaf757a9d8",
  'name': "TTK",
  #'name'l: "Test Token",
  'decimals': 18
},
{
  'address': "0x31172dD9a7ce3e6B470126EdBFbe318ec0003743",
  'name': "LNW",
  #'name'l: "Linaw Collective ",
  'decimals': 18
},
{
  'address': "0x723a42dff0bdCE09B7DCf86F4D47D8Be491E6345",
  'name': "MUG",
  #'name'l: "MultiGuild",
  'decimals': 9
},
{
  'address': "0xc084E5FEA082FB7105939b3A8b18BF7D8203cA45",
  'name': "TOKI",
  #'name'l: "tokk",
  'decimals': 18
},
{
  'address': "0x5d54B7F5C54538aE6E2e4064E068539ec05955C2",
  'name': "AMVT",
  #'name'l: "Alien Metaverse Token",
  'decimals': 18
},
{
  'address': "0x228bEEE59786722FF3921d7A9622959805f19B9c",
  'name': "AMT",
  #'name'l: "Alien Meta Token",
  'decimals': 18
},
{
  'address': "0x6Cd667f14d379Dee05De329a6eb1280ff02ECc08",
  'name': "AMMT",
  #'name'l: "Alien MAXI Meta Token",
  'decimals': 18
},
{
  'address': "0x5b746af50a36Fb048Cc7F94c47399bEbDf1fa585",
  'name': "PABT",
  #'name'l: "Porn And Base Token",
  'decimals': 18
},
{
  'address': "0x5434Fbcb072b6FD514d6B2Dd50224E9cE38E5738",
  'name': "GAIAC",
  #'name'l: "Gaia Coin",
  'decimals': 18
},
{
  'address': "0x267Ab21F7F61B13cAB73C3b70cD8D5307a046334",
  'name': "UKR",
  #'name'l: "UA COIN",
  'decimals': 6
},
{
  'address': "0x49f55b53CeE43241B4D4765443a9a19F62c296a3",
  'name': "APER",
  #'name'l: "Jocelyn Underwood",
  'decimals': 18
},
{
  'address': "0x3a7E6F651C8b20Bf487172BCb3746a2dd56aA1D9",
  'name': "LENS",
  #'name'l: "Lens (PoS)",
  'decimals': 18
},
{
  'address': "0x846e21D68d4f504c811d1015f16Dd9bB0F02B6aE",
  'name': "METAMUSK",
  #'name'l: "MetaMusk",
  'decimals': 9
},
{
  'address': "0xBB25487C0f4ed9e670fF0B6fFb3Fbdc4142B44B3",
  'name': "QSHEK",
  #'name'l: "Quantum Shekel",
  'decimals': 18
},
{
  'address': "0x3bc13AEF8CF1445b251effde8375Be91ec7f4369",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x1F9921203BE371a1c8FEa9d2BF3a1f86dB4179Fc",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x24eb627569DE2a543bd2e87539314abaE694ED9d",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x5BD44CaD516A52da97430643F0f555Ba07A0B3c3",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xd60d2B5Bd2Afb1A25D7e3901189a5C00fC305602",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xAc988Dd7178218ef4433E76B859D4d990Ed2A309",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x6E6DEf15645029519157Ab0eb8C46DBd7aa0c775",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x88c936a3FcFF48C7c432537261CfeA9dA534d04b",
  'name': "HAI",
  #'name'l: "SafeHai",
  'decimals': 18
},
{
  'address': "0x7A11052F1FB8a021F6c7e4A80B923b778B20c440",
  'name': "Apple",
  #'name'l: "Apple ABC",
  'decimals': 18
},
{
  'address': "0x4f70C70469FA714CA230fc4a89a285787135023a",
  'name': "TES",
  #'name'l: "TSTER pLACE",
  'decimals': 18
},
{
  'address': "0x78C320F94993a66aa30d14d19046D005cD199962",
  'name': "PPDEX",
  #'name'l: "Pepedex v2",
  'decimals': 18
},
{
  'address': "0x97a8F0112aE7773A1be686DC21e9493F8C2E05D1",
  'name': "MOON",
  #'name'l: "MoonCoin",
  'decimals': 9
},
{
  'address': "0x969ceE3AF01ab58620DaBA25fd93Fc08AB285a46",
  'name': "MDCKING",
  #'name'l: "MDcKING",
  'decimals': 9
},
{
  'address': "0xc3764139E5b8eB34F9Bf29cBE95096e296530ACd",
  'name': "syg",
  #'name'l: "syngen",
  'decimals': 18
},
{
  'address': "0x0b6fe691A690ed464921582791A398C31A337476",
  'name': "GALER",
  #'name'l: "GALER",
  'decimals': 16
},
{
  'address': "0x8A1d1585A119569deFc6f1FD641E09CB6Bc2971b",
  'name': "3553",
  #'name'l: "BgdJbt III",
  'decimals': 18
},
{
  'address': "0x5af5B59579fdF2caf63682Ca54f4670a94829767",
  'name': "DEGEN",
  #'name'l: "DEGEN INU",
  'decimals': 9
},
{
  'address': "0xA798bA9A2188ad61Be6b930C5B6a69a3C7d4aed3",
  'name': "MCDEGEN",
  #'name'l: "MCDEGEN INU",
  'decimals': 9
},
{
  'address': "0x390D087575EAEbBcb8d4Baad3bc69BCE94Ee6F37",
  'name': "Otong123",
  #'name'l: "WAGMI INU",
  'decimals': 9
},
{
  'address': "0x1F0c81faccDD0aeE8b30dAd98d30D64Ca780b06D",
  'name': "HDOGE",
  #'name'l: "Hyper Doge",
  'decimals': 9
},
{
  'address': "0xC35De09873D366EEe607a975903b49AB8dE7B90C",
  'name': "ZPAE",
  #'name'l: "ZelaaPayAE",
  'decimals': 9
},
{
  'address': "0xa574Dc46710194E11e542364AF23E658304cA26B",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0xD2e6b39b18A5b497cAc29573Cb37A66D25C7464A",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x441d1F894E555d7edc128F6D62e9797423a9f1f1",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0xD4aEda62dF792c6C8B0eB8c12dE89197EC3CE8bD",
  'name': "DAI",
  #'name'l: "Dai Stablecoin",
  'decimals': 18
},
{
  'address': "0x26eAA81CcDd6c678Cc383d6C600b7a21a02a0360",
  'name': "DAI",
  #'name'l: "Dai Stablecoin",
  'decimals': 18
},
{
  'address': "0xA0F0d42641a0719D153f1581479F333146F18066",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x12ec6e41e35773f8D41CC90C5Dc8D791666f5944",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0xcF98103A2aaA4f830ab9ef8A9294D852Db5b147f",
  'name': "DAI",
  #'name'l: "Dai Stablecoin",
  'decimals': 18
},
{
  'address': "0x5fcC2517D337b29ed5d8F85CD3e47D41b3862757",
  'name': "STST",
  #'name'l: "SushiTest",
  'decimals': 18
},
{
  'address': "0xCAbA280C96ca6F3c64c620C304E77c48Ce473Fda",
  'name': "CLOUT",
  #'name'l: "Clout Token",
  'decimals': 9
},
{
  'address': "0x22e3f02f86Bc8eA0D73718A2AE8851854e62adc5",
  'name': "FLAME",
  #'name'l: "FireStarter",
  'decimals': 18
},
{
  'address': "0xc6C855AD634dCDAd23e64DA71Ba85b8C51E5aD7c",
  'name': "ICE",
  #'name'l: "Decentral Games ICE",
  'decimals': 18
},
{
  'address': "0xcC1B9517460D8aE86fe576f614d091fCa65a28Fc",
  'name': "VIS",
  #'name'l: "Vigorus",
  'decimals': 18
},
{
  'address': "0x0102bbfDdFFBd8d28d3a1b9C47017F62F42768f2",
  'name': "50C",
  #'name'l: "50 Cent",
  'decimals': 18
},
{
  'address': "0x4d8e671cC4BE52e08Ab256eD72EB2C5c974c9d56",
  'name': "TNH",
  #'name'l: "TNHToken",
  'decimals': 18
},
{
  'address': "0xCfEC09616c44CbafF3B0D60414e041aa7aaBBF15",
  'name': "YTYY",
  #'name'l: "4360",
  'decimals': 18
},
{
  'address': "0x4c1741a5f742951de4dDadD2b4ca25D8D5594a9A",
  'name': "MINU",
  #'name'l: "Xander Guy",
  'decimals': 18
},
{
  'address': "0xC3fF9FE268b613c426Fb3d64c95E4e9E9E89B0B6",
  'name': "2448",
  #'name'l: "Pool Token3387",
  'decimals': 18
},
{
  'address': "0x3393354d03e1913adB98A77bFaF4A2596728Af65",
  'name': "HVE-T",
  #'name'l: "Honey Test",
  'decimals': 18
},
{
  'address': "0x4741f6f0f41299C1Cd3Fe11e7e87CE180332c1B4",
  'name': "6585",
  #'name'l: "Pool Token1013",
  'decimals': 18
},
{
  'address': "0x17b5fA55299C23E50c6Dce718c68b1b80BF96172",
  'name': "1502",
  #'name'l: "Pool Token9567",
  'decimals': 18
},
{
  'address': "0x3Ba0B99b3D10519858f1D73262C3164DB6b91c7b",
  'name': "7608",
  #'name'l: "Pool Token5491",
  'decimals': 18
},
{
  'address': "0x1B91dAE2386d61Ff623bdffABf8B5B9c4C98f9BE",
  'name': "642",
  #'name'l: "Pool Token4351",
  'decimals': 18
},
{
  'address': "0x65345F98E53E805b931AA4Faa2102e2E0D2CDA9A",
  'name': "3943",
  #'name'l: "Pool Token  2915",
  'decimals': 18
},
{
  'address': "0x2C82Dac9e6AAda92b24c1F5478000c8C4e31C591",
  'name': "3823",
  #'name'l: "Pool Token  9143",
  'decimals': 18
},
{
  'address': "0x167574dB299CDF213a80a301fb5aE383A8A9f2E8",
  'name': "6579",
  #'name'l: "Pool Token  4791",
  'decimals': 18
},
{
  'address': "0xbd9bCa8Ad9902e90800eA48202F1E7Ebb60D636C",
  'name': "VHIN",
  #'name'l: "Vallhund Inu",
  'decimals': 9
},
{
  'address': "0x53c86399Ed6deDDcDa58c184c0Db61FDfF7784b2",
  'name': "BTC",
  #'name'l: "BITCOIN",
  'decimals': 18
},
{
  'address': "0x275F6bCd5bE1020aBf0a36AE3568c854d30D0F2d",
  'name': "2165",
  #'name'l: "Pool Token  4618",
  'decimals': 18
},
{
  'address': "0x269A400019C9C08F165Bb8Ef2C3481ab6642Cdfd",
  'name': "BEAT",
  #'name'l: "Jaden Holt",
  'decimals': 18
},
{
  'address': "0xa33B2D26903D70dfb6f4a141BE450bf0349e1D69",
  'name': "AKX",
  #'name'l: "AkinuX",
  'decimals': 18
},
{
  'address': "0x6e233F43DDA432F7A525272edC9fb83Dd36aa91B",
  'name': "TWS",
  #'name'l: "Tweest",
  'decimals': 18
},
{
  'address': "0x436E29d38F81AfafA08903c5dC268B6be5722e1b",
  'name': "FIB",
  #'name'l: "Fibonacci",
  'decimals': 18
},
{
  'address': "0xC16b4045562547109cd421653EDA3D8E63e9bC41",
  'name': "TCSR",
  #'name'l: "TEST CRYPTO SPACE RACE",
  'decimals': 18
},
{
  'address': "0x763c716736b27A02B7e55e36a8609a116210412e",
  'name': "STUD",
  #'name'l: "STUDS",
  'decimals': 18
},
{
  'address': "0x0d37fA622516CFa95C9f1Fe327925837AA69187C",
  'name': "PBTC",
  #'name'l: "Polygon BITCOIN",
  'decimals': 8
},
{
  'address': "0x30E123B0BE157792fAdD478107beBd66985BD172",
  'name': "ShitDoge",
  #'name'l: " ✒️ ShitDoge",
  'decimals': 8
},
{
  'address': "0x2f519393adF8Af5201Ac24e393F66e9B9217A5d1",
  'name': "UrMum",
  #'name'l: " ✒️ UrMum",
  'decimals': 8
},
{
  'address': "0xa0D64C22629d6E02AB25FA0C3e7bbC4d5711C4eE",
  'name': "COPS",
  #'name'l: "COPS",
  'decimals': 18
},
{
  'address': "0x5430a0B6C11f870571ffA891d59dec8C4608Ea9A",
  'name': "tPOKT",
  #'name'l: "ThunderPOKT",
  'decimals': 6
},
{
  'address': "0x995F5d7a4729C1Fce1AbaE40862BC73AC8a6CFf3",
  'name': "BDD",
  #'name'l: "Bing Dwen Dwen",
  'decimals': 9
},
{
  'address': "0x8eDE0EfCD28d33A529AD4B9a5b0193bF9105D956",
  'name': "WPAB42",
  #'name'l: "Wrapped Porn and Bas 42",
  'decimals': 18
},
{
  'address': "0x21aE6609fb168Cc0371DC8292943658E0fC967E5",
  'name': "COD",
  #'name'l: "CallOfDuty",
  'decimals': 18
},
{
  'address': "0x8774fA8aAd6e217460026210C90E2Ef8AD11ca94",
  'name': "PUSH",
  #'name'l: "Push Notification Token",
  'decimals': 0
},
{
  'address': "0x82355AED16D297e8B672d50182A7F0446EDf6a13",
  'name': "MEME2",
  #'name'l: "MEME2",
  'decimals': 18
},
{
  'address': "0xcC9f1FcaB316c73Ad3c35C02d5220a4338be69Bf",
  'name': "DefiBalls",
  #'name'l: "DefiBalls",
  'decimals': 18
},
{
  'address': "0x9B6C7CFE1A1890B8Ab5bA207112C504ccC3989fE",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xc59DE17B50993ddf854B51Ac4532E26994f8655a",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xa91EcCd8215fd11BB9ff71765E503355ec86A121",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xACb145abFEE17398AC2336be9CFD92a8dab79188",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x18f2D044a16e84076A6aC66dF354B23cE2D3Ed67",
  'name': "BLOP",
  #'name'l: "BLOPToken",
  'decimals': 18
},
{
  'address': "0x9F93ACA246F457916E49Ec923B8ed099e313f763",
  'name': "hUSDT",
  #'name'l: "Tether USD Hop Token",
  'decimals': 6
},
{
  'address': "0x0011734931a9b801cE57277D5148069EF0b4A900",
  'name': "MBB",
  #'name'l: "BARNBUCKS",
  'decimals': 9
},
{
  'address': "0x669902e2e3cfDD251d8F1D42df1418E3F9f888d1",
  'name': "LENS",
  #'name'l: "Lens",
  'decimals': 18
},
{
  'address': "0x6DEa2667D300DEbAd02914ec4cf48d65182F029F",
  'name': "CK1",
  #'name'l: "Carbon Killer One",
  'decimals': 18
},
{
  'address': "0x2fb36d7dD2B8EfbaeB434C18437EE5232A1c57a8",
  'name': "xc",
  #'name'l: "xerecard",
  'decimals': 18
},
{
  'address': "0x5827901B63168C92c3047B166eCc35adacB28594",
  'name': "NICOTINE",
  #'name'l: "Nicotine Free",
  'decimals': 9
},
{
  'address': "0xa2AB6A08519BaFDEDC07494284A65Cec0fDC6288",
  'name': "DIAT",
  #'name'l: "Diantom Dao",
  'decimals': 9
},
{
  'address': "0x1465E68a7c74Be59C79E6788cc9b4Da9959C3b92",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x30E10b73D4A213518903aE97Bc14742410352118",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xA11490fE148C43dCd059F1704c77159a05Fa089c",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xC85Ad80c4aC9D8Deb50b04Ad309d261332Bd1472",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x8dC61e3F1A61749Ffc1381D020120Ad6f84D7c45",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x7FE4c93F1A5Ee99AFfB9979dC9e9bE5dD6cEe8D1",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x8fC95a1FC1ec27f6C0EBfD383121c3dab6bCabbD",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x332Dfc091a0e4369c65f490D0454237BD5be8a73",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x87C9c1aB096A5fbBfEe242826Fcad35731fB1D09",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x987752f852e37B24EF5E06f044bA904Ab65C8117",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xbDA9fd788D1078549b92AE4BdE7164BD632CA1Ad",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0xbabc4E9aC611Ae48D3c5c0928c298ad009D7a3f3",
  'name': "FIREFLY",
  #'name'l: "Firefly Token",
  'decimals': 18
},
{
  'address': "0x1fb5635cAbF218D44989BADCb51804C8b46A2297",
  'name': "TST",
  #'name'l: "Test",
  'decimals': 18
},
{
  'address': "0x0260b99FFD553ed023DB9658f5B9bc246cF1bea5",
  'name': "TST",
  #'name'l: "Test",
  'decimals': 18
},
{
  'address': "0x65F25E531f5A7F61DA356b9b3209e581F88c345E",
  'name': "EST",
  #'name'l: "Curran Stanley",
  'decimals': 18
},
{
  'address': "0x0136FB493A977a6c2441A20e4E5Eb3B7bb062612",
  'name': "Wxxxx",
  #'name'l: "Wkxxx",
  'decimals': 9
},
{
  'address': "0x02649C1Ff4296038De4b9bA8F491b42b940A8252",
  'name': "XGEM",
  #'name'l: "Exchange Genesis Ethlas Medium",
  'decimals': 18
},
{
  'address': "0x0359eC1828bf80D2BC99E71D62108c25e3419Ed2",
  'name': "ONEverse",
  #'name'l: "ONEverse",
  'decimals': 9
},
{
  'address': "0x07c334458f98426eFc7fBA1F15d7156A0ec0a637",
  'name': "NOST",
  #'name'l: "Quinn Lewis",
  'decimals': 18
},
{
  'address': "0x0A02D33031917d836Bd7Af02F9f7F6c74d67805F",
  'name': "PKLAY",
  #'name'l: "Orbit Bridge Polygon Klay",
  'decimals': 18
},
{
  'address': "0x0bbc50F35c2519A8A59A9553A2D1D5b8679Ac9CD",
  'name': "GOLD",
  #'name'l: "$GOLD",
  'decimals': 18
},
{
  'address': "0x0d0B8488222F7f83B23E365320a4021b12eAD608",
  'name': "NXTT",
  #'name'l: "NextEarthToken",
  'decimals': 18
},
{
  'address': "0x0DcBfa223d69edadB70c90F12B014fcFF8D281b2",
  'name': "AJC",
  #'name'l: "AJ Coin",
  'decimals': 18
},
{
  'address': "0x16385c846eE5DFaeF09AE406B4fC15D01aecEDe4",
  'name': "CSE",
  #'name'l: "Cause",
  'decimals': 18
},
{
  'address': "0x18a8565367A9c5eE633070184a4E2737b08aCDfe",
  'name': "KFC",
  #'name'l: "Peron Token",
  'decimals': 18
},
{
  'address': "0x18c5Ed3c231d54BFC1F7bA178379d2DE41f4D945",
  'name': "ETTv0",
  #'name'l: "Etest Finance",
  'decimals': 18
},
{
  'address': "0x193498E20002577C28A42A8A839BdA7C78283533",
  'name': "EIUS",
  #'name'l: "Brody Hill",
  'decimals': 18
},
{
  'address': "0x1E2671fA6B4aE5B61226B7391fa87CBB55CF3Cf5",
  'name': "Apple",
  #'name'l: "Apple ABC",
  'decimals': 18
},
{
  'address': "0x259ba1bC783dA697F20fB25793BCc46cc39e5e30",
  'name': "BITDAO",
  #'name'l: "bitcodeDAO",
  'decimals': 18
},
{
  'address': "0x2aaE7C64C201d0cFcf7e2aDDDEfdF2688f60AfDE",
  'name': "Litas",
  #'name'l: "Lithuanian Crypto Litas",
  'decimals': 18
},
{
  'address': "0x2bC07124D8dAc638E290f401046Ad584546BC47b",
  'name': "TOWER",
  #'name'l: "TOWER",
  'decimals': 18
},
{
  'address': "0x2Bde1792707d4b0e85b4C6dAdD403EB8eD579c7A",
  'name': "DOGE KING",
  #'name'l: "DOGE KING",
  'decimals': 9
},
{
  'address': "0x2d21AC15216f1e8C8B5d3D3e06Cb6cbFf528b550",
  'name': "BONE",
  #'name'l: "Beta One",
  'decimals': 18
},
{
  'address': "0x2d4678E71590c56Eb37869832a3642c405e1C252",
  'name': "SAITAMA",
  #'name'l: "Saitama Inu (PoS) ",
  'decimals': 9
},
{
  'address': "0x2E698E867880DfC2B3c918053D385aF9dA2fE866",
  'name': "gDIAT",
  #'name'l: "Governance DIAT",
  'decimals': 18
},
{
  'address': "0x33369949eb0DDb21a5D4F83f18e813604157fB76",
  'name': "DIAT",
  #'name'l: "Diatom DAO",
  'decimals': 9
},
{
  'address': "0x340CC8F092E508895A825356abA1e74F3a8347DF",
  'name': "FNT",
  #'name'l: "Fortnite Token",
  'decimals': 18
},
{
  'address': "0x3440916Ef90b3aE444a6e0b7EADA23f641965e43",
  'name': "DOGG",
  #'name'l: "Dogg Token",
  'decimals': 18
},
{
  'address': "0x3Eb7e868b1F34FF4c4F8dd68BdfB4C8A5D01602A",
  'name': "SEC",
  #'name'l: "SECOND",
  'decimals': 18
},
{
  'address': "0x40Fb0BF25b52f183482E8Fba7D2341688EeFc613",
  'name': "ABT",
  #'name'l: "Agricultura Biológica",
  'decimals': 18
},
{
  'address': "0x490941AfA7Fbd995aa99221FAF6994aBBb626Ebd",
  'name': "sDIAT",
  #'name'l: "Staked DIAT",
  'decimals': 9
},
{
  'address': "0x496E02917bBAbA1a5C2122cD4D2D91A111a4505a",
  'name': "FLD",
  #'name'l: "Fluid finance",
  'decimals': 18
},
{
  'address': "0x49b3C84410ec4c76984a291Bfb02e185bFC30D41",
  'name': "PYWH",
  #'name'l: "Polywealth",
  'decimals': 18
},
{
  'address': "0x50950C7C2Df8EB88F567519a428a13E175bE7274",
  'name': "SLM",
  #'name'l: "Salum",
  'decimals': 8
},
{
  'address': "0x55975321D9d22587d1742DC68B35481C8DBB0Db8",
  'name': "FF",
  #'name'l: "FemtoFarthing",
  'decimals': 18
},
{
  'address': "0x59C86611e9ef2F453dFDD45EA23de62103bfD7D4",
  'name': "uchiha",
  #'name'l: "uchiha",
  'decimals': 18
},
{
  'address': "0x5d34C8954b91514486C31fBa9Da3F11f0f0dA597",
  'name': "AIMT2",
  #'name'l: "AimedgeTest2",
  'decimals': 18
},
{
  'address': "0x5FF1CD7C9766BEce41fA571D2Ca35f5B01314163",
  'name': "MEGADOUCHEINU",
  #'name'l: "MegaDouche Inu",
  'decimals': 9
},
{
  'address': "0x642Eb6CcE398B977284375e6C3eF1A54BA57D28E",
  'name': "aLMLT",
  #'name'l: "AlphaLimelight",
  'decimals': 18
},
{
  'address': "0x6691D7202f0B6e89073297b5a849482Cdad1824b",
  'name': "DOGGY",
  #'name'l: "DOGGY CUTIE Coin",
  'decimals': 2
},
{
  'address': "0x699Eb6C52be6efDf8206176B6E3c243c88a59874",
  'name': "BTC",
  #'name'l: "Bitcoin",
  'decimals': 18
},
{
  'address': "0x6D0bA101447c92dF17d511a94fA8D8d8951b3843",
  'name': "YOGA",
  #'name'l: "Yoga Coin",
  'decimals': 18
},
{
  'address': "0x6Fdba1A4f28D7077Cfd3080f70C13020BC5B5865",
  'name': "FLIP",
  #'name'l: "Polyflip",
  'decimals': 18
},
{
  'address': "0x720614D0e2506362089cd3e59581a1f314F4c1C7",
  'name': "PL1",
  #'name'l: "POOLONE",
  'decimals': 18
},
{
  'address': "0x775DF1194E6E50D6A0e0197B555e643BC5410252",
  'name': "DIAT",
  #'name'l: "Diatom DAO",
  'decimals': 9
},
{
  'address': "0x78C442a21cB2D06AC49b9B7A87649FDD4A035648",
  'name': "NDM",
  #'name'l: "Endium",
  'decimals': 18
},
{
  'address': "0x7A9568aE827CD28Bf8365fD51BAA2dbcd7D3F465",
  'name': "GAS",
  #'name'l: "Gas DAO (PoS)",
  'decimals': 18
},
{
  'address': "0x7c99441B64E6cF448872fbE7a37Fa0A963cB40B5",
  'name': "FUCKBALLS",
  #'name'l: "FUCKBALLS",
  'decimals': 9
},
{
  'address': "0x7F0c2Bcd40b7Dc98ac2ba75c25c98DF56b56a016",
  'name': "t8",
  #'name'l: "test8",
  'decimals': 9
},
{
  'address': "0x86de9493fdf751Fb210796B6c3c414b41C8659D1",
  'name': "BANSOS",
  #'name'l: "BANSOS",
  'decimals': 18
},
{
  'address': "0x8aC0C43717484A958A8fF48E7D7137Db1f43bC73",
  'name': "RND",
  #'name'l: "RandomCoin",
  'decimals': 18
},
{
  'address': "0x8c6589310C086546E52b49a064D369Af3eac37Cb",
  'name': "FUSDT",
  #'name'l: "FUSDT",
  'decimals': 18
},
{
  'address': "0x9fDC23fe295104Ac55fef09363c56451D0E37CFA",
  'name': "rkl",
  #'name'l: "Rickle (PoS)",
  'decimals': 18
},
{
  'address': "0xa4248cB19567330320aEeD7fEa4ceCa3531843Ec",
  'name': "ETTv1",
  #'name'l: "Etest Finance",
  'decimals': 18
},
{
  'address': "0xA77A35331E6FC34a7a2fE0176B258BC772A135a2",
  'name': "$POOP",
  #'name'l: "POOP Token",
  'decimals': 18
},
{
  'address': "0xA8603c31D7D2c29A339D3Ae46413c18FE4A96f81",
  'name': "TAG",
  #'name'l: "Synctag",
  'decimals': 8
},
{
  'address': "0xA9C9f90509F9070D210573Cd4c63DF0C1C50BC05",
  'name': "ERT",
  #'name'l: "Eternal Racer Terminal",
  'decimals': 18
},
{
  'address': "0xab3a9eA136dbBFBC1911fe73DdaC4dA7425a9c9f",
  'name': "GODZ",
  #'name'l: "god zilla",
  'decimals': 9
},
{
  'address': "0xb0779866dB56dEb3fc31cC3d5c80EcF21b5E9Ec0",
  'name': "JTKTEST",
  #'name'l: "JhonTokenTEST",
  'decimals': 18
},
{
  'address': "0xBA2Ad4342EaEbA15328d1Ab5Aa51EFa12097ce14",
  'name': "REDDOT",
  #'name'l: "REDDOT Token",
  'decimals': 18
},
{
  'address': "0xBd108681Bd793C691B30c2981FFD5AFDB309eb28",
  'name': "CONS",
  #'name'l: "Imani Gomez",
  'decimals': 18
},
{
  'address': "0xbEc1Cd771be627f4BC30C25b31670746f999dFe9",
  'name': "GTM",
  #'name'l: "GOLD TIGER MUSIC TOKEN",
  'decimals': 18
},
{
  'address': "0xbf8454D580c3f3A104F2495E2a6bB5CCE5935013",
  'name': "LABO",
  #'name'l: "Rama Morton",
  'decimals': 18
},
{
  'address': "0xC31803905B693489D7eb05e5660D3F7d1CBaD040",
  'name': "PRC",
  #'name'l: "PrinceCoin",
  'decimals': 18
},
{
  'address': "0xC3fd62d85aad6Dbe56c02Ea448135c5e5c6C8cf0",
  'name': "WGS",
  #'name'l: "WksGames",
  'decimals': 9
},
{
  'address': "0xC8f44553770CDc491f10C0b47F0172bfB4175ee5",
  'name': "$POOP",
  #'name'l: "POOP Token",
  'decimals': 18
},
{
  'address': "0xcB6F356Fb0B7bb57daa6aC96B40C667455Bf35A2",
  'name': "SRERC20",
  #'name'l: "SimpleERC20",
  'decimals': 12
},
{
  'address': "0xcbcF80C70F86dB75a02DAf0f88467f8c378E7D79",
  'name': "APEX",
  #'name'l: "APEDEX",
  'decimals': 18
},
{
  'address': "0x6Fdba1A4f28D7077Cfd3080f70C13020BC5B5865",
  'name': "FLIP",
  #'name'l: "Polyflip",
  'decimals': 18
},
{
  'address': "0x720614D0e2506362089cd3e59581a1f314F4c1C7",
  'name': "PL1",
  #'name'l: "POOLONE",
  'decimals': 18
},
{
  'address': "0x775DF1194E6E50D6A0e0197B555e643BC5410252",
  'name': "DIAT",
  #'name'l: "Diatom DAO",
  'decimals': 9
},
{
  'address': "0x78C442a21cB2D06AC49b9B7A87649FDD4A035648",
  'name': "NDM",
  #'name'l: "Endium",
  'decimals': 18
},
{
  'address': "0x7A9568aE827CD28Bf8365fD51BAA2dbcd7D3F465",
  'name': "GAS",
  #'name'l: "Gas DAO (PoS)",
  'decimals': 18
},
{
  'address': "0x7c99441B64E6cF448872fbE7a37Fa0A963cB40B5",
  'name': "FUCKBALLS",
  #'name'l: "FUCKBALLS",
  'decimals': 9
},
{
  'address': "0x7F0c2Bcd40b7Dc98ac2ba75c25c98DF56b56a016",
  'name': "t8",
  #'name'l: "test8",
  'decimals': 9
},
{
  'address': "0x86de9493fdf751Fb210796B6c3c414b41C8659D1",
  'name': "BANSOS",
  #'name'l: "BANSOS",
  'decimals': 18
},
{
  'address': "0x8aC0C43717484A958A8fF48E7D7137Db1f43bC73",
  'name': "RND",
  #'name'l: "RandomCoin",
  'decimals': 18
},
{
  'address': "0x8c6589310C086546E52b49a064D369Af3eac37Cb",
  'name': "FUSDT",
  #'name'l: "FUSDT",
  'decimals': 18
},
{
  'address': "0x9fDC23fe295104Ac55fef09363c56451D0E37CFA",
  'name': "rkl",
  #'name'l: "Rickle (PoS)",
  'decimals': 18
},
{
  'address': "0xa4248cB19567330320aEeD7fEa4ceCa3531843Ec",
  'name': "ETTv1",
  #'name'l: "Etest Finance",
  'decimals': 18
},
{
  'address': "0xA77A35331E6FC34a7a2fE0176B258BC772A135a2",
  'name': "$POOP",
  #'name'l: "POOP Token",
  'decimals': 18
},
{
  'address': "0xA8603c31D7D2c29A339D3Ae46413c18FE4A96f81",
  'name': "TAG",
  #'name'l: "Synctag",
  'decimals': 8
},
{
  'address': "0xA9C9f90509F9070D210573Cd4c63DF0C1C50BC05",
  'name': "ERT",
  #'name'l: "Eternal Racer Terminal",
  'decimals': 18
},
{
  'address': "0xab3a9eA136dbBFBC1911fe73DdaC4dA7425a9c9f",
  'name': "GODZ",
  #'name'l: "god zilla",
  'decimals': 9
},
{
  'address': "0xb0779866dB56dEb3fc31cC3d5c80EcF21b5E9Ec0",
  'name': "JTKTEST",
  #'name'l: "JhonTokenTEST",
  'decimals': 18
},
{
  'address': "0xBA2Ad4342EaEbA15328d1Ab5Aa51EFa12097ce14",
  'name': "REDDOT",
  #'name'l: "REDDOT Token",
  'decimals': 18
},
{
  'address': "0xBd108681Bd793C691B30c2981FFD5AFDB309eb28",
  'name': "CONS",
  #'name'l: "Imani Gomez",
  'decimals': 18
},
{
  'address': "0xbEc1Cd771be627f4BC30C25b31670746f999dFe9",
  'name': "GTM",
  #'name'l: "GOLD TIGER MUSIC TOKEN",
  'decimals': 18
},
{
  'address': "0xbf8454D580c3f3A104F2495E2a6bB5CCE5935013",
  'name': "LABO",
  #'name'l: "Rama Morton",
  'decimals': 18
},
{
  'address': "0xC31803905B693489D7eb05e5660D3F7d1CBaD040",
  'name': "PRC",
  #'name'l: "PrinceCoin",
  'decimals': 18
},
{
  'address': "0xC3fd62d85aad6Dbe56c02Ea448135c5e5c6C8cf0",
  'name': "WGS",
  #'name'l: "WksGames",
  'decimals': 9
},
{
  'address': "0xC8f44553770CDc491f10C0b47F0172bfB4175ee5",
  'name': "$POOP",
  #'name'l: "POOP Token",
  'decimals': 18
},
{
  'address': "0xcB6F356Fb0B7bb57daa6aC96B40C667455Bf35A2",
  'name': "SRERC20",
  #'name'l: "SimpleERC20",
  'decimals': 12
},
{
  'address': "0xcbcF80C70F86dB75a02DAf0f88467f8c378E7D79",
  'name': "APEX",
  #'name'l: "APEDEX",
  'decimals': 18
},
{
  'address': "0x787DCDDFEeFF157653fa43C733990Bf9440f1cf0",
  'name': "NECE",
  #'name'l: "Kirk Roy",
  'decimals': 18
},
{
  'address': "0x4369bAD2aBb80a234f38757A4b3406cA8818c3b4",
  'name': "WYOYO",
  #'name'l: "Wrapped Yoyo",
  'decimals': 18
},
{
  'address': "0x85fe1e5108367AFCeFe8eFa3f017f80D6A414afa",
  'name': "NAD",
  #'name'l: "New Age Digital",
  'decimals': 18
},
{
  'address': "0x144E9C2ED7860a76154C034e50689Ce48e75fA9a",
  'name': "SINT",
  #'name'l: "Ginger Golden",
  'decimals': 18
},
{
  'address': "0x8c0Ec810e02a76b89721C127E0D5062830C6b488",
  'name': "QUO",
  #'name'l: "Kiona Perry",
  'decimals': 18
},
{
  'address': "0x1197Ae7F43695Be80127365b494E8BF850f4752A",
  'name': "pBOT-f",
  #'name'l: "Curve.fi Factory Plain Pool: Polygon Arbitrage Bot",
  'decimals': 18
},
{
  'address': "0x64FFf0e27c223097c824f9d9278eFD5B55c3430e",
  'name': "MATIC/ALRT-f",
  #'name'l: "Curve.fi Factory Plain Pool: WMATIC/ALERTO",
  'decimals': 18
},
{
  'address': "0x82c93dFF887Eb9d57fbd55D837db2a74422b9482",
  'name': "iPURP",
  #'name'l: "ironPURPLE",
  'decimals': 18
},
{
  'address': "0x43a97177B639AF19Efabfee6E9DF1f5Da3cFaAf1",
  'name': "RNVI",
  #'name'l: "Renovi",
  'decimals': 18
},
{
  'address': "0xa75D50BE7462Ce4FE473bb218D051Ba9bFC15F0c",
  'name': "SKRLA",
  #'name'l: "Grilla Skrilla",
  'decimals': 18
},
{
  'address': "0x9c07621FaE6228ee45b42C93a562c76C005f48a3",
  'name': "SOR",
  #'name'l: "SunOfRekt",
  'decimals': 18
},
{
  'address': "0x6603C91E795E4d73d34345e4893b85048dFf832c",
  'name': "",
  #'name'l: "Nuclear bomb",
  'decimals': 18
},
{
  'address': "0xA7925127BAa2A98D84c5Ff65d6D30A20D026AE86",
  'name': "MD",
  #'name'l: "Money Dollar",
  'decimals': 18
},
{
  'address': "0x5a1de22F25aD8a178EA22969AEd436f6A31Be766",
  'name': "Jesus Saves",
  #'name'l: "Jesus Saves",
  'decimals': 18
},
{
  'address': "0x5755Fd34E5b6D60E535278136c37A9c067051AA7",
  'name': "Babyjesus",
  #'name'l: "Baby Jesus",
  'decimals': 18
},
{
  'address': "0x04D93418F78b43bE30B78139fb8C876db30EA07d",
  'name': "DAI",
  #'name'l: "Dai Stablecoin",
  'decimals': 18
},
{
  'address': "0x885dA5626b565b9c11Df39631196f669A90F1859",
  'name': "BLKD",
  #'name'l: "BlackDAO",
  'decimals': 9
},
{
  'address': "0x78E328a6Ad1F1D394B576d2c55d4AA5be26E0C12",
  'name': "FRAX",
  #'name'l: "FRAX TOKEN",
  'decimals': 18
},
{
  'address': "0x19360b76c07e821eB8a7Fc5E38AF38C6c12cD0E3",
  'name': "TST",
  #'name'l: "Test",
  'decimals': 18
},
{
  'address': "0x91B7B4e9CA2754bffd684C3aF2407c781C9067d0",
  'name': "MF",
  #'name'l: "MetaFighter",
  'decimals': 18
},
{
  'address': "0x9468ddD60F850c3BCF55EDD2A108E700836c8633",
  'name': "BATT",
  #'name'l: "BatToken",
  'decimals': 9
},
{
  'address': "0x4Cc525b0Ca1a76A78aD37A13BF2EC181A95Cb039",
  'name': "BMH",
  #'name'l: "Baby Matic Holder",
  'decimals': 10
},
{
  'address': "0x924cEE5DE02EC896075648955163FE7dF07d4C24",
  'name': "011",
  #'name'l: "Bgd_Jbt",
  'decimals': 18
},
{
  'address': "0x7B6Ddddc65201Cb731035D135F8b88aB3c8C358e",
  'name': "CHEEMS",
  #'name'l: "CHEEMS INU",
  'decimals': 18
},
{
  'address': "0x95e28342130d41040d4e90A2b2ac417107047D10",
  'name': "CONS",
  #'name'l: "Cheryl Barnes",
  'decimals': 18
},
{
  'address': "0xA0B82C8294E6cb5Ec01D0A4217Aa1FBE922d6886",
  'name': "QWWE",
  #'name'l: "Walter",
  'decimals': 18
},
{
  'address': "0x441b7Be893864AE46984159EA73693EAC65A2586",
  'name': "CAM",
  #'name'l: "CAM",
  'decimals': 18
},
{
  'address': "0xB22ecDFe16BeF29cE48A63cDE0aDd3E8b536d122",
  'name': "THUG",
  #'name'l: "THUG",
  'decimals': 18
},
{
  'address': "0xC125D5429a1e1fc1946f40fEFfcA1c7859bF1d80",
  'name': "OMI",
  #'name'l: "OMI Token (Wormhole)",
  'decimals': 18
},
{
  'address': "0x9CD42aed7d44EE801C827A8E5DCF41DF534E9e82",
  'name': "OMI",
  #'name'l: "OMI Token (PoS)",
  'decimals': 18
},
{
  'address': "0xA90754c37403903641a009EE1a6dC146BAc91D93",
  'name': "LOL",
  #'name'l: "CC",
  'decimals': 18
},
{
  'address': "0x81f0986D8Fc0858c31F97441677B8e2d7C2fD535",
  'name': "CRS",
  #'name'l: "croeseid",
  'decimals': 18
},
{
  'address': "0x7cC15fEf543f205Bf21018F038F591C6BaDa941c",
  'name': "POLYCUB",
  #'name'l: "PolyCub",
  'decimals': 18
},
{
  'address': "0x207333606C71824927d58aFD5981eEB39547A92A",
  'name': "DII",
  #'name'l: "Daichi",
  'decimals': 6
},
{
  'address': "0x67B78D31A40dACC5aCf7648C2Ad88bDBF6EeEc1C",
  'name': "B-52",
  #'name'l: "B-52",
  'decimals': 18
},
{
  'address': "0xCa2a18877D6B715d0E53A69845Ec25237a0315F5",
  'name': "Bull",
  #'name'l: "BullCoin",
  'decimals': 2
},
{
  'address': "0x90B9597bBFDcbc86253d27d6B9a13079c5155f9f",
  'name': "ECX",
  #'name'l: "ECX Token (PoS)",
  'decimals': 18
},
{
  'address': "0xA936e1f747d14fC30d08272D065c8aeF4ab7f810",
  'name': "WLD",
  #'name'l: "wLitiDAO",
  'decimals': 18
},
{
  'address': "0x70a20d48C5Ca3794dc96Af740825117c422C5798",
  'name': "TANK",
  #'name'l: "TANK",
  'decimals': 18
},
{
  'address': "0x3c108F33FF5443ADc7dFE8a1b43829d27cCFE183",
  'name': "STC",
  #'name'l: "Sustainable",
  'decimals': 9
},
{
  'address': "0x3a879931d80d6B1221F5f1887BAC929dA2c699F2",
  'name': "333",
  #'name'l: "333",
  'decimals': 18
},
{
  'address': "0x613a489785C95afEB3b404CC41565cCff107B6E0",
  'name': "RADIO",
  #'name'l: "RadioShack Token",
  'decimals': 18
},
{
  'address': "0x43E335c151699307eaa28AC7c1387f76Fe0c1445",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x84DAcA37777534630b61740DCb699413Da41dD75",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x89d05A3307a122687D3f8D497729782408493453",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0xa9B7F1f421294e8Aae4f0fE237af84dF0a747185",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x30f836841049AC0bAC5Ae8aA0229a7B1C0c00fF0",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x814D2FC14B56167aA03052e66eF72DaAa13443d8",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x73D349e9b9e39424a0eBF781878449bd57B946c0",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x1A0bd176691DfcA94988e0aD69C0099D007e2C2b",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x5Af71a7e73658E6e2dF125B3fbA1ce4E2bf70EF0",
  'name': "REGGAE",
  #'name'l: "Reggae Hill",
  'decimals': 18
},
{
  'address': "0x61b3D3B564299602B5126db4E630875dE3B36113",
  'name': "HOBO",
  #'name'l: "HOBO",
  'decimals': 9
},
{
  'address': "0x6E48B656c2ee92E724B161A69ca206Dd113FA7fe",
  'name': "WATERSL",
  #'name'l: "Water to Save Lives",
  'decimals': 18
},
{
  'address': "0x3aAd782d27F801bD3BF8583d6F7bc1842d2d3fa5",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x3e1fd14f1FFC34806D65803d9ECCD38523dB71b7",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x50878a6aA5cb1478637e50E3a9A38913051ce345",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0xA29083e5E96a592b70E61baeCa7ca92895e848de",
  'name': "Rock",
  #'name'l: "RockBuddy",
  'decimals': 18
},
{
  'address': "0x8712e1dB58eF14f5Ec630342395ec42758187907",
  'name': "SPD",
  #'name'l: "Speed Matic",
  'decimals': 18
},
{
  'address': "0x9026510676dEF354B0Ea9D98e089ad166FbB224B",
  'name': "NZNFT",
  #'name'l: "NeonzNFT",
  'decimals': 18
},
{
  'address': "0x0e3059081f7e3Bb03D0A377949E6D91483f3E4AA",
  'name': "$ESI",
  #'name'l: "Empyrean Source",
  'decimals': 18
},
{
  'address': "0x9aCb7988A3409ad1B5430972c9c5077A3c76A26E",
  'name': "TOKER",
  #'name'l: "The Toker Token",
  'decimals': 18
},
{
  'address': "0x7Ecb5699D8E0a6572E549Dc86dDe5A785B8c29BC",
  'name': "MORI",
  #'name'l: "Shomori",
  'decimals': 18
},
{
  'address': "0x255C4779Ff47Fa3bF607fc1CB9A8fA4340bB6a7C",
  'name': "TST",
  #'name'l: "TEST",
  'decimals': 18
},
{
  'address': "0xad01DFfe604CDc172D8237566eE3a3ab6524d4C6",
  'name': "C3",
  #'name'l: "C3 Token",
  'decimals': 18
},
{
  'address': "0xC3C7d422809852031b44ab29EEC9F1EfF2A58756",
  'name': "LDO",
  #'name'l: "Lido DAO Token (PoS)",
  'decimals': 18
},
{
  'address': "0xb5c2792Ee47dA90cf39ef034a3b3D3dcD884AE15",
  'name': "NYLCN",
  #'name'l: "NylonCoin",
  'decimals': 10
},
{
  'address': "0x8c059898ca6274750b6bF1cf38F2848347C490cc",
  'name': "SOS",
  #'name'l: "SOS (PoS)",
  'decimals': 18
},
{
  'address': "0x27e0627272BfEB993A4013f90F52d357fCC75Fcd",
  'name': "LUCADA",
  #'name'l: "LuckyADA",
  'decimals': 18
},
{
  'address': "0xA1388e73c51B37383B1Ab9dCe8317eF5A0349CC5",
  'name': "VERSE",
  #'name'l: "Shibaverse",
  'decimals': 18
},
{
  'address': "0x5d2375C6af4b7dE4e395ADa20aab937895B4fa70",
  'name': "MSC",
  #'name'l: "MetaSoccer Cash",
  'decimals': 18
},
{
  'address': "0x3B9b24991fC6F3CBe518843cBcd43fB937A65FB8",
  'name': "SCAT",
  #'name'l: "SnowCat",
  'decimals': 9
},
{
  'address': "0x76873Fce79B74e00E20597179f633DA169b8fa64",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xb12bA956F474BD8dDcb843f3067822418785764A",
  'name': "SCAT",
  #'name'l: "SnowCat",
  'decimals': 9
},
{
  'address': "0x4FAfad147c8Cd0e52f83830484d164e960BdC6C3",
  'name': "QWLA",
  #'name'l: "Qawalla Token (PoS)",
  'decimals': 18
},
{
  'address': "0x5daAe277c141384F2D2c3DD0f9dB62797E723760",
  'name': "REZ",
  #'name'l: "Rez",
  'decimals': 18
},
{
  'address': "0xC0Fd9DfeE340Cd13a27ce370a02661d0FE11CeBD",
  'name': "TRUTH",
  #'name'l: "TruthLink",
  'decimals': 18
},
{
  'address': "0x010935e2Fc4cb587c52a07FE623Fc0Be160D4a2e",
  'name': "CLOUT",
  #'name'l: "Clout",
  'decimals': 9
},
{
  'address': "0x1EE8821Ea2ACE20517ee666c5216f9B849FF37b1",
  'name': "SCAT",
  #'name'l: "SnowCat",
  'decimals': 9
},
{
  'address': "0x4924974805580D891557b1E25be9cAc4B88f8c5a",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0xc0e50b303BBCcEF55d44A8F64839749fDAF97301",
  'name': "wxSCAT",
  #'name'l: "Wrapped xSCAT",
  'decimals': 18
},
{
  'address': "0x4eAe087558ee5A72215b80d22e9b5fA3914B0350",
  'name': "PUNK",
  #'name'l: "Punks",
  'decimals': 18
},
{
  'address': "0x50454511E14bdC6359a4C0C380E5027324c7452A",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x6EE15D61a3A03193c5a452f0D2AF4b9784116616",
  'name': "SCAT",
  #'name'l: "SnowCat",
  'decimals': 9
},
{
  'address': "0x3Fcc0C5d2d25a6aB24C4df7a2D36bb60E865a7ad",
  'name': "SCAT",
  #'name'l: "SnowCat",
  'decimals': 9
},
{
  'address': "0x8EaDc96BD1679BD64dBb1bF62Fb68e3D64A5850c",
  'name': "EDAI",
  #'name'l: "ERCDAI",
  'decimals': 18
},
{
  'address': "0x59d348B888793e213803c8B95AA60d8A18A18481",
  'name': "EWBTC",
  #'name'l: "ERCWBTC",
  'decimals': 8
},
{
  'address': "0x49394AfF1A64fD7d4697D2E251cAAeDAFc6ACEcc",
  'name': "FTM",
  #'name'l: "Fantom",
  'decimals': 18
},
{
  'address': "0x2C82964534a25DFc86a2018C1c61F39359972098",
  'name': "FSR",
  #'name'l: "FakeShare",
  'decimals': 18
},
{
  'address': "0x26c98eF58120F0985B4275A0466D36F845C45dA7",
  'name': "FDL",
  #'name'l: "FakeDollar",
  'decimals': 18
},
{
  'address': "0x2c17a079E65732159C207cD11f037fA5fd0C0587",
  'name': "SnapShiba",
  #'name'l: "Shiba Snap",
  'decimals': 3
},
{
  'address': "0xaA8f08F251180B8de72bbcE4b00B0f68A36b62C0",
  'name': "CLOUT",
  #'name'l: "Clout",
  'decimals': 9
},
{
  'address': "0x7313D0D52789Dc233f6C984a257ad649c442105b",
  'name': "CLOUT",
  #'name'l: "Clout",
  'decimals': 9
},
{
  'address': "0x464BD809db5E5ce9f1B9693631157E3a524cB457",
  'name': "QUAS",
  #'name'l: "Barron token",
  'decimals': 18
},
{
  'address': "0xbF75b3FB52EBb467201FCE4CA67CCf94dee2eC92",
  'name': "COSMIX",
  #'name'l: "Cosmix Token",
  'decimals': 18
},
{
  'address': "0xC61BabE7e8d66f160F7e2882E59C0FF58157F68e",
  'name': "WWWW",
  #'name'l: "CC",
  'decimals': 18
},
{
  'address': "0x3f1A749ef99f91978e897AF6256910213D593bfD",
  'name': "XXXXXX",
  #'name'l: "XXXXX",
  'decimals': 18
},
{
  'address': "0x849E3ff78E5b48eb2Ad875565536390FfF16A667",
  'name': "XXXXXX",
  #'name'l: "XXXXX",
  'decimals': 18
},
{
  'address': "0x1C931836980b38E28D50E4027F6880B30CC71861",
  'name': "tst1",
  #'name'l: "test 1",
  'decimals': 18
},
{
  'address': "0xac823e5D5BDe11E9c3429fea35144F05be604846",
  'name': "tst2",
  #'name'l: "test 2",
  'decimals': 18
},
{
  'address': "0xa95cDA81dd94D4f9221524663ecc7ceBc7a23853",
  'name': "DETH",
  #'name'l: "dETH",
  'decimals': 18
},
{
  'address': "0x632fbF85F77978437073a8CE5CEEC29e3209514c",
  'name': "vUNIT",
  #'name'l: "Virtual Unit",
  'decimals': 18
},
{
  'address': "0x3f9599b86Cfd9FCc08c52bdD563275e8148296C0",
  'name': "MIR",
  #'name'l: "MIRACLE",
  'decimals': 18
},
{
  'address': "0x0A1Dcc07160935F78B0849e6Af83eB9c98FA2e37",
  'name': "BET",
  #'name'l: "Sherbet",
  'decimals': 18
},
{
  'address': "0xAdA58DF0F643D959C2A47c9D4d4c1a4deFe3F11C",
  'name': "CRO",
  #'name'l: "CRO (PoS)",
  'decimals': 8
},
{
  'address': "0x3E22A53D331550271065eB0b251b1F765b14166B",
  'name': "NFT$",
  #'name'l: "NFT Artist’s Token",
  'decimals': 18
},
{
  'address': "0x033f42316E23E16e445f1D37294A4dD857D694FA",
  'name': "H2O",
  #'name'l: "M.M.",
  'decimals': 18
},
{
  'address': "0x0700A83446EFe9c0b23b046e87C10089657a00C3",
  'name': "dWETH",
  #'name'l: "debug Wrapped ETH",
  'decimals': 18
},
{
  'address': "0x871DDE7d54b0E1614488700dA78bE98184cCec04",
  'name': "dWBTC",
  #'name'l: "debug Wrapped BTC",
  'decimals': 8
},
{
  'address': "0x8F7b9E4d11C542737DdD07ff1FBBa2663Ffa5e33",
  'name': "dUSDC",
  #'name'l: "debug USD Coin",
  'decimals': 6
},
            {
                'name': 'QUICK',
                'address': '0x831753DD7087CaC61aB5644b308642cc1c33Dc13',
                'decimals': 18,
            },
            {
                'name': 'AAVE',
                'address': '0xD6DF932A45C0f255f85145f286eA0b292B21C90B',
                'decimals': 18,
            },
            {
                'name': 'SUSHI',
                'address': '0x0b3F868E0BE5597D5DB7fEB59E1CADBb0fdDa50a',
                'decimals': 18,
            },
            {
                'name': 'DFYN',
                'address': '0xC168E40227E4ebD8C1caE80F7a55a4F0e6D66C97',
                'decimals': 18,
            },
            {
                'name': 'BIFI',
                'address': '0xFbdd194376de19a88118e84E279b977f165d01b8',
                'decimals': 18,
            },
            {
                'name': 'AVAX',
                'address': '0x2C89bbc92BD86F8075d1DEcc58C7F4E0107f286b',
                'decimals': 18,
            },
            {
                'name': 'ADDY',
                'address': '0xc3FdbadC7c795EF1D6Ba111e06fF8F16A20Ea539',
                'decimals': 18,
            },
            {
                'name': 'BAL',
                'address': '0x9a71012B13CA4d3D0Cdc72A177DF3ef03b0E76A3',
                'decimals': 18,
            },
            {
                'name': 'LINK',
                'address': '0x53E0bca35eC356BD5ddDFebbD1Fc0fD03FaBad39',
                'decimals': 18,
            },
            {
                'name': 'UNI',
                'address': '0xb33EaAd8d922B1083446DC23f610c2567fB5180f',
                'decimals': 18,
            },
            {
                'name': 'MANA',
                'address': '0xA1c57f48F0Deb89f569dFbE6E2B7f46D33606fD4',
                'decimals': 18,
            },
            {
                'name': 'UST',
                'address': '0x692597b009d13C4049a947CAB2239b7d6517875F',
                'decimals': 18,
            },
            {
                'name': 'CRV',
                'address': '0x172370d5Cd63279eFa6d502DAB29171933a610AF',
                'decimals': 18,
            },
            {
                'name': 'SAND',
                'address': '0xBbba073C31bF03b8ACf7c28EF0738DeCF3695683',
                'decimals': 18,
            },
            {
                'name': 'COMP',
                'address': '0x8505b9d2254A7Ae468c0E9dd10Ccea3A837aef5c',
                'decimals': 18,
            },
            {
                'name': 'SNX',
                'address': '0x50B728D8D964fd00C2d0AAD81718b71311feF68a',
                'decimals': 18,
            },
            {
                'name': '1INCH',
                'address': '0x9c2C5fd7b07E95EE044DDeba0E97a665F142394f',
                'decimals': 18,
            },
            {
                'name': 'YFI',
                'address': '0xDA537104D6A5edd53c6fBba9A898708E465260b6',
                'decimals': 18,
            },
        ],
        'sides' : [
            {
                'name': 'WMATIC',
                'address': '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270',
                'decimals': 18,
                'minAmount': 1,
            },
            {
                'name': 'WETH',
                'address': '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619',
                'decimals': 18,
                'minAmount': 0.001,
            },
            {
                'name': 'USDC',
                'address': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
                'decimals': 6,
                'minAmount': 1,
            },
        ],
    },
}

import json
def readJson(filename: str) -> dict:
    f = open(filename, 'r')
    parsedJson = json.load(f)
    f.close()
    return parsedJson

abi = {
    'IUniswapRouter': readJson('abi/IUniswapRouter.json'),
    'IUniswapFactory': readJson('abi/IUniswapFactory.json'),
    'IUniswapPair': readJson('abi/IUniswapPair.json'),
    'IExchangeOracle': readJson('abi/IExchangeOracle.json'),
    'IArbitrageExecutor': readJson('abi/IArbitrageExecutor.json'),
    'IERC20': readJson('abi/IERC20.json'),
}
