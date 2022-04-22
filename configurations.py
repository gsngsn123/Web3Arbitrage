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
        "gasPrice": 70,        
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
  'address': '0x97c23237E71492b6d2327804e2a73e1Ae6B95553',
  'name': 'CAT',
  #Name: 'Catcoin',
  'decimals': 18
},
{
  'address': '0x983C059D1be984F8f06C2559351C5ab1CB1dcDb7',
  'name': 'TITAN',
  #Name: 'Titan Token',
  'decimals': 18
},
{
  'address': '0x983F6d60db79ea8cA4eB9968C6aFf8cfA04B3c63',
  'name': 'SNM',
  #Name: 'SONM Token',
  'decimals': 18
},
{
  'address': '0x984C134A8809571993Fd1573fB99F06Dc61E216f',
  'name': 'ACG',
  #Name: 'Artchain Global Token',
  'decimals': 8
},
{
  'address': '0x988DaDD0B82fA7d94d9e6f084A08755bFD4da860',
  'name': 'WSCOIN',
  #Name: 'WSCOIN',
  'decimals': 18
},
{
  'address': '0x98968f0747E0A261532cAcC0BE296375F5c08398',
  'name': 'MOONCAT',
  #Name: 'MoonCats',
  'decimals': 18
},
{
  'address': '0x98ad9B32dD10f8D8486927D846D4Df8BAf39Abe2',
  'name': 'VLO',
  #Name: 'VELO Token',
  'decimals': 18
},
{
  'address': '0x99295f1141d58A99e939F7bE6BBe734916a875B8',
  'name': 'LPL',
  #Name: 'LinkPool',
  'decimals': 18
},
{
  'address': '0x992D6ef73506a28d084dD092722f686Fb5570E38',
  'name': 'TNO',
  #Name: 'TNodeOrange',
  'decimals': 8
},
{
  'address': '0x998FFE1E43fAcffb941dc337dD0468d52bA5b48A',
  'name': 'IDRT',
  #Name: 'Rupiah Token',
  'decimals': 2
},
{
  'address': '0x9992eC3cF6A55b00978cdDF2b27BC6882d88D1eC',
  'name': 'POLY',
  #Name: 'Polymath',
  'decimals': 18
},
{
  'address': '0x99A412f6f704436bD3e131502Be53d2506Aa1f47',
  'name': 'MINU',
  #Name: 'Moon Inu',
  'decimals': 9
},
{
  'address': '0x99D8a9C45b2ecA8864373A26D1459e3Dff1e17F3',
  'name': 'MIM',
  #Name: 'Magic Internet Money',
  'decimals': 18
},
{
  'address': '0x99ea4dB9EE77ACD40B119BD1dC4E33e1C070b80d',
  'name': 'QSP',
  #Name: 'Quantstamp Token',
  'decimals': 18
},
{
  'address': '0x99fE3B1391503A1bC1788051347A1324bff41452',
  'name': 'SX',
  #Name: 'SportX',
  'decimals': 18
},
{
  'address': '0x9AD5D6C438267BdADA28d37e3793954A804Cdf78',
  'name': 'POW',
  #Name: 'POWNFT',
  'decimals': 18
},
{
  'address': '0x9AF4f26941677C706cfEcf6D3379FF01bB85D5Ab',
  'name': 'DRT',
  #Name: 'DomRaiderToken',
  'decimals': 8
},
{
  'address': '0x9b00e6E8D787b13756eb919786c9745054DB64f9',
  'name': 'wSIENNA',
  #Name: 'Sienna (ERC20)',
  'decimals': 18
},
{
  'address': '0x9B02dD390a603Add5c07f9fd9175b7DABE8D63B7',
  'name': 'SPI',
  #Name: 'Shopping.io',
  'decimals': 18
},
{
  'address': '0x9B52cc7d6b8668179E2BB8de4903c1C8739091CD',
  'name': 'HAPPY',
  #Name: 'TheHappyCoin.co Token',
  'decimals': 18
},
{
  'address': '0x9B9f0DAd27516C237c6Ea3024d4CDAea0C6B2ce9',
  'name': 'EROC',
  #Name: 'EmeraldRockets',
  'decimals': 10
},
{
  'address': '0x9b9fB226E98C4e90DB2830C9aefa9cfcBE3b000a',
  'name': 'KITTY',
  #Name: 'CryptoKitties [Gen 0]',
  'decimals': 18
},
{
  'address': '0x9ba60bA98413A60dB4C651D4afE5C937bbD8044B',
  'name': 'YLA',
  #Name: 'Yearn Lazy Ape Index',
  'decimals': 18
},
{
  'address': '0x9BdE098Be22658d057C3F1F185e3Fd4653E2fbD1',
  'name': 'KP2R',
  #Name: 'KP2R.Network',
  'decimals': 18
},
{
  'address': '0x9C061DF134d11412151E9c200ce3F9f6F295094a',
  'name': 'SEC',
  #Name: 'Suck Elons Cock',
  'decimals': 9
},
{
  'address': '0x9C2dc0c3CC2BADdE84B0025Cf4df1c5aF288D835',
  'name': 'COR',
  #Name: 'COR Token',
  'decimals': 18
},
{
  'address': '0x9c405acf8688AfB61B3197421cDeeC1A266c6839',
  'name': 'DOGY',
  #Name: 'DogeYield',
  'decimals': 18
},
{
  'address': '0x9C78EE466D6Cb57A4d01Fd887D2b5dFb2D46288f',
  'name': 'MUST',
  #Name: 'Must',
  'decimals': 18
},
{
  'address': '0x9C790A79916296CBA9D7e602933df09E0C4D6a29',
  'name': 'YGEM',
  #Name: 'generation.finance',
  'decimals': 18
},
{
  'address': '0x9cA85572E6A3EbF24dEDd195623F188735A5179f',
  'name': 'y3Crv',
  #Name: 'yearn Curve.fi DAI/USDC/USDT',
  'decimals': 18
},
{
  'address': '0x9cea2eD9e47059260C97d697f82b8A14EfA61EA5',
  'name': 'PUNK',
  #Name: 'Punk',
  'decimals': 18
},
{
  'address': '0x9cEB84f92A0561fa3Cc4132aB9c0b76A59787544',
  'name': 'DOKI',
  #Name: 'DokiDokiFinance',
  'decimals': 18
},
{
  'address': '0x9CF4679c67BEE8dA2D6F58c64592fFf6beE79330',
  'name': 'Yfic',
  #Name: 'YearnCash',
  'decimals': 18
},
{
  'address': '0x9d409a0A012CFbA9B15F6D4B36Ac57A46966Ab9a',
  'name': 'yvBOOST',
  #Name: 'Yearn Compounding veCRV yVault',
  'decimals': 18
},
{
  'address': '0x9D47894f8BECB68B9cF3428d256311Affe8B068B',
  'name': '$ROPE',
  #Name: '$ROPE',
  'decimals': 18
},
{
  'address': '0x9D4Aa5600e0C8c2085Bb82D946Ca6642742a8250',
  'name': 'HOPE',
  #Name: 'HOPE',
  'decimals': 18
},
{
  'address': '0x9D79d5B61De59D882ce90125b18F74af650acB93',
  'name': 'NSBT',
  #Name: 'Neutrino System Base Token',
  'decimals': 6
},
{
  'address': '0x9E5405a11E42e7d48fbF4F2E979695641c15189b',
  'name': 'RDM',
  #Name: 'Primitive V1 Redeem',
  'decimals': 18
},
{
  'address': '0x9E78b8274e1D6a76a0dBbf90418894DF27cBCEb5',
  'name': 'UniFi',
  #Name: 'UniFi',
  'decimals': 18
},
{
  'address': '0x9EA3b5b4EC044b70375236A281986106457b20EF',
  'name': 'DELTA',
  #Name: 'DELTA.financial - deep DeFi derivatives',
  'decimals': 18
},
{
  'address': '0x9F678E91219b89066a709aA6fB10631F2F5Bf2F7',
  'name': 'FUKYU',
  #Name: 'Fukyu',
  'decimals': 18
},
{
  'address': '0x9f7229aF0c4b9740e207Ea283b9094983f78ba04',
  'name': 'TAD',
  #Name: 'Tadpole',
  'decimals': 18
},
{
  'address': '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2',
  'name': 'MKR',
  #Name: 'Maker',
  'decimals': 18
},
{
  'address': '0xA00F236BA4bDFA84cAA1a7F8734CCb6B160be2EE',
  'name': 'ABU84',
  #Name: '1984 St Marys Class',
  'decimals': 18
},
{
  'address': '0xa0246c9032bC3A600820415aE600c6388619A14D',
  'name': 'FARM',
  #Name: 'FARM Reward Token',
  'decimals': 18
},
{
  'address': '0xA0b73E1Ff0B80914AB6fe0444E65848C4C34450b',
  'name': 'CRO',
  #Name: 'CRO',
  'decimals': 8
},
{
  'address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
  'name': 'USDC',
  #Name: 'USD Coin',
  'decimals': 6
},
{
  'address': '0xa0E2A28FD7B1E4e7e5CceD5C5bB00f7d24A5C282',
  'name': 'TNG',
  #Name: 'TNodeGreen',
  'decimals': 8
},
{
  'address': '0xa117000000f279D81A1D3cc75430fAA017FA5A2e',
  'name': 'ANT',
  #Name: 'Aragon Network Token',
  'decimals': 18
},
{
  'address': '0xa1454f9c704AF96636F3A7532b9a04c411f85680',
  'name': 'BSP',
  #Name: 'BallSwap',
  'decimals': 18
},
{
  'address': '0xa150Db9b1Fa65b44799d4dD949D922c0a33Ee606',
  'name': 'DRC',
  #Name: 'Digital Reserve Currency',
  'decimals': 0
},
{
  'address': '0xA15C7Ebe1f07CaF6bFF097D8a589fb8AC49Ae5B3',
  'name': 'NPXS',
  #Name: 'Pundi X Token',
  'decimals': 18
},
{
  'address': '0xA1AFFfE3F4D611d252010E3EAf6f4D77088b0cd7',
  'name': 'RFI',
  #Name: 'reflect.finance',
  'decimals': 9
},
{
  'address': '0xa1d0E215a23d7030842FC67cE582a6aFa3CCaB83',
  'name': 'YFII',
  #Name: 'YFII.finance',
  'decimals': 18
},
{
  'address': '0xa1d6Df714F91DeBF4e0802A542E13067f31b8262',
  'name': 'RFOX',
  #Name: 'RFOX',
  'decimals': 18
},
{
  'address': '0xA1d7b2d891e3A1f9ef4bBC5be20630C2FEB1c470',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xa1e72267084192Db7387c8CC1328fadE470e4149',
  'name': 'tfTUSD',
  #Name: 'TrueFi TrueUSD',
  'decimals': 18
},
{
  'address': '0xA1f82E14bc09A1b42710dF1A8a999B62f294e592',
  'name': 'eCFX',
  #Name: 'ethereum Conflux',
  'decimals': 18
},
{
  'address': '0xa1faa113cbE53436Df28FF0aEe54275c13B40975',
  'name': 'ALPHA',
  #Name: 'AlphaToken',
  'decimals': 18
},
{
  'address': '0xA23D33D5e0a61bA81919bfD727c671bB03ab0feA',
  'name': 'IQ',
  #Name: 'pTokens IQ',
  'decimals': 18
},
{
  'address': '0xa283aA7CfBB27EF0cfBcb2493dD9F4330E0fd304',
  'name': 'MM',
  #Name: 'MMToken',
  'decimals': 18
},
{
  'address': '0xA2b4C0Af19cC16a6CfAcCe81F192B024d625817D',
  'name': 'KISHU',
  #Name: 'Kishu Inu',
  'decimals': 9
},
{
  'address': '0xA2cb4950e1F07F2b889BE1e489A6E60df545a840',
  'name': 'ABC',
  #Name: 'ABC',
  'decimals': 18
},
{
  'address': '0xA31B1767e09f842ECFd4bc471Fe44F830E3891AA',
  'name': 'ROOBEE',
  #Name: 'ROOBEE',
  'decimals': 18
},
{
  'address': '0xA389d50A9D8163cbFa4145FD41f8865715A64929',
  'name': 'DOGEREUM',
  #Name: 'Dogereum',
  'decimals': 18
},
{
  'address': '0xa3BeD4E1c75D00fa6f4E5E6922DB7261B5E9AcD2',
  'name': 'MTA',
  #Name: 'Meta',
  'decimals': 18
},
{
  'address': '0xA3E059c0b01F07F211c85bF7b4f1d907AfB011df',
  'name': 'eMax',
  #Name: 'EthereumMax',
  'decimals': 18
},
{
  'address': '0xA41D6262cf6EA867DFFa8Ab4a45A0925E94defE0',
  'name': 'VISION',
  #Name: 'Work Hard Vision',
  'decimals': 18
},
{
  'address': '0xa4202F65C2E2CBB1973CeC7336557e24bc1b063F',
  'name': 'BAYC',
  #Name: 'Bored Ape Yacht Club NFTX',
  'decimals': 18
},
{
  'address': '0xa44E5137293E855B1b7bC7E2C6f8cD796fFCB037',
  'name': 'SENT',
  #Name: 'SENTinel',
  'decimals': 8
},
{
  'address': '0xa47c8bf37f92aBed4A126BDA807A7b7498661acD',
  'name': 'UST',
  #Name: 'Wrapped UST Token',
  'decimals': 18
},
{
  'address': '0xA487bF43cF3b10dffc97A9A744cbB7036965d3b9',
  'name': 'DERI',
  #Name: 'Deri',
  'decimals': 18
},
{
  'address': '0xA4CCC61b79a21692d78DA43fc25d3Afa6855fae5',
  'name': 'NWT',
  #Name: 'Newton',
  'decimals': 18
},
{
  'address': '0xA4EED63db85311E22dF4473f87CcfC3DaDCFA3E3',
  'name': 'RBC',
  #Name: 'Rubic',
  'decimals': 18
},
{
  'address': '0xA60bF48f8de6470B9C9D3e1AB78088cE3d89FaeF',
  'name': 'BLOB',
  #Name: 'Blobfish Token',
  'decimals': 0
},
{
  'address': '0xA64BD6C70Cb9051F6A9ba1F163Fdc07E0DfB5F84',
  'name': 'aLINK',
  #Name: 'Aave Interest bearing LINK',
  'decimals': 18
},
{
  'address': '0xa6610Ed604047e7B76C1DA288172D15BcdA57596',
  'name': 'SACKS',
  #Name: 'SACKS',
  'decimals': 18
},
{
  'address': '0xA6621965508BF4f41927c63793B493Fa12cBae6d',
  'name': 'MOONCAT',
  #Name: 'MoonCats Rescue',
  'decimals': 18
},
{
  'address': '0xa67E83917b438E11A58f119A2Bd9cC5dAaB86041',
  'name': 'ECAM',
  #Name: 'ECAM',
  'decimals': 18
},
{
  'address': '0xa6e2f89B03d1B7a2D8fA7F28B971bf2A7bE0F91B',
  'name': 'HOTDOGE',
  #Name: 'HotDoge Token',
  'decimals': 18
},
{
  'address': '0xa735954B9037eA07607323411f3DBD5441B09E8F',
  'name': 'DOGSP',
  #Name: 'DogeSpace',
  'decimals': 18
},
{
  'address': '0xa7DE087329BFcda5639247F96140f9DAbe3DeED1',
  'name': 'STA',
  #Name: 'Statera',
  'decimals': 18
},
{
  'address': '0xA866F0198208Eb07c83081d5136BE7f775c2399e',
  'name': 'KORE',
  #Name: 'Kore',
  'decimals': 18
},
{
  'address': '0xa8707C3051d5730130DA60db969cBD7C1343b5F2',
  'name': 'MPT11',
  #Name: 'My Pocket Token 11',
  'decimals': 18
},
{
  'address': '0xA8B3b1392b17F64d5a50B4B4Bd3800324d07800b',
  'name': 'SVC001',
  #Name: 'Stacker.vc VCFund1 Token',
  'decimals': 8
},
{
  'address': '0xA8bD98f383A567DBc82dBcAF5FE899fe0668d67b',
  'name': 'LOVE',
  #Name: 'Love',
  'decimals': 18
},
{
  'address': '0xA8e7AD77C60eE6f30BaC54E2E7c0617Bd7B5A03E',
  'name': 'zLOT',
  #Name: 'zLOT',
  'decimals': 18
},
{
  'address': '0xA91ac63D040dEB1b7A5E4d4134aD23eb0ba07e14',
  'name': 'BEL',
  #Name: 'Bella',
  'decimals': 18
},
{
  'address': '0xA9215acA9821C6C2d6801aE6ed63CD7817Ca4FaF',
  'name': 'AIA',
  #Name: 'AIA Token',
  'decimals': 3
},
{
  'address': '0xa9261e47033Ae52b5cA6AdC3844cdd5f3b2Bc375',
  'name': 'XTREM',
  #Name: 'Xtremtoken',
  'decimals': 0
},
{
  'address': '0xa92E7c82B11d10716aB534051B271D2f6aEf7Df5',
  'name': 'ARA',
  #Name: 'Ara Token',
  'decimals': 18
},
{
  'address': '0xA9B1Eb5908CfC3cdf91F9B8B3a74108598009096',
  'name': 'Auction',
  #Name: 'Bounce Token',
  'decimals': 18
},
{
  'address': '0xa9fE4601811213c340e850ea305481afF02f5b28',
  'name': 'yvWETH',
  #Name: 'WETH yVault',
  'decimals': 18
},
{
  'address': '0xAa6E8127831c9DE45ae56bB1b0d4D4Da6e5665BD',
  'name': 'ETH2x-FLI',
  #Name: 'ETH 2x Flexible Leverage Index',
  'decimals': 18
},
{
  'address': '0xaA7a9CA87d3694B5755f213B5D04094b8d0F0A6F',
  'name': 'TRAC',
  #Name: 'Trace Token',
  'decimals': 18
},
{
  'address': '0xaa9Ad45c1D3c5380D5d1CEE324023b461FC72F89',
  'name': 'SUPERMARIO',
  #Name: 'Super Mario',
  'decimals': 18
},
{
  'address': '0xAACa86B876ca011844b5798ECA7a67591A9743C8',
  'name': 'BIOS',
  #Name: 'BIOS',
  'decimals': 18
},
{
  'address': '0xAB1C02c7d5EbfddBb8824CCd193E7df59b34A841',
  'name': 'BMB',
  #Name: 'Bombic Finance',
  'decimals': 18
},
{
  'address': '0xab63f1857eaD863D7D70B4eba999662f64E4d66a',
  'name': 'USDR',
  #Name: 'USD Robinhood',
  'decimals': 6
},
{
  'address': '0xAB9c92A9337A1494C6D545E48187Fa37144403c8',
  'name': 'PUNK-ATTR-5',
  #Name: 'Punk-Attr-5',
  'decimals': 18
},
{
  'address': '0xabA49Db7E374cc6954401DC0A886E0B02670536e',
  'name': 'AVASTR-RANK-60',
  #Name: 'Avastar-Rank-60',
  'decimals': 18
},
{
  'address': '0xAba8cAc6866B83Ae4eec97DD07ED254282f6aD8A',
  'name': 'YAMv2',
  #Name: 'YAMv2',
  'decimals': 24
},
{
  'address': '0xABe580E7ee158dA464b51ee1a83Ac0289622e6be',
  'name': 'XFT',
  #Name: 'Offshift',
  'decimals': 18
},
{
  'address': '0xaC0104Cca91D167873B8601d2e71EB3D4D8c33e0',
  'name': 'CWS',
  #Name: 'Crowns',
  'decimals': 18
},
{
  'address': '0xaCae4330035c19D798cdF49b984106603a266D0c',
  'name': 'TYR',
  #Name: 'Tyrannos',
  'decimals': 8
},
{
  'address': '0xad0887734461aF8C6033068bDE4047Dbe84074cc',
  'name': 'aswap',
  #Name: 'arbiswap',
  'decimals': 8
},
{
  'address': '0xaD2aa3C57570AD9811bA8Ee90316f9C73F78035A',
  'name': 'CLN',
  #Name: 'Casino Land Network',
  'decimals': 6
},
{
  'address': '0xad32A8e6220741182940c5aBF610bDE99E737b2D',
  'name': 'DOUGH',
  #Name: 'PieDAO DOUGH v2',
  'decimals': 18
},
{
  'address': '0xad4353347f05438Ace12aef7AceF6CB2b4186C00',
  'name': 'uSTONKS_0921',
  #Name: 'uSTONKS Index Token September 2021',
  'decimals': 6
},
{
  'address': '0xAd4f86a25bbc20FfB751f2FAC312A0B4d8F88c64',
  'name': 'ROOM',
  #Name: 'OptionRoom Token',
  'decimals': 18
},
{
  'address': '0xaD5e8B98B28FF14469644c86D4047fE00BD8cB30',
  'name': 'MGAx',
  #Name: 'MGA Stablecoin',
  'decimals': 18
},
{
  'address': '0xaD5Fe5B0B8eC8fF4565204990E4405B2Da117d8e',
  'name': 'TRXC',
  #Name: 'TRONCLASSIC',
  'decimals': 0
},
{
  'address': '0xAD6683b7f3618c44F5CA6040902812Dd890DdE4d',
  'name': 'TNO',
  #Name: 'TNOS COIN',
  'decimals': 18
},
{
  'address': '0xad7BFDCe99D4D8eb77C77e50a5aA4E6e526FD8f6',
  'name': 'ARCHETYPE',
  #Name: 'Archetype',
  'decimals': 18
},
{
  'address': '0xada279f9301C01A4eF914127a6C2a493Ad733924',
  'name': 'XSUc25-0531',
  #Name: 'XSUSHI 25 Call [31 May 2021]',
  'decimals': 18
},
{
  'address': '0xADE00C28244d5CE17D72E40330B1c318cD12B7c3',
  'name': 'ADX',
  #Name: 'AdEx Network',
  'decimals': 18
},
{
  'address': '0xAE1eaAE3F627AAca434127644371b67B18444051',
  'name': 'YOP',
  #Name: 'YOP',
  'decimals': 8
},
{
  'address': '0xae4fADE35556B0910d7D5fc42762dd29472A8f40',
  'name': 'FEM',
  #Name: 'FEM',
  'decimals': 18
},
{
  'address': '0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84',
  'name': 'stETH',
  #Name: 'Liquid staked Ether 2.0',
  'decimals': 18
},
{
  'address': '0xaea46A60368A7bD060eec7DF8CBa43b7EF41Ad85',
  'name': 'FET',
  #Name: 'Fetch',
  'decimals': 18
},
{
  'address': '0xaF90579D216816f27E3DCC601a0d10613A874fA8',
  'name': 'UCHI',
  #Name: 'UCHI',
  'decimals': 18
},
{
  'address': '0xaf988afF99d3d0cb870812C325C588D8D8CB7De8',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xafcE9B78D409bF74980CACF610AFB851BF02F257',
  'name': 'LFBTC',
  #Name: 'Lift.Kitchen BTC',
  'decimals': 18
},
{
  'address': '0xAFF40Fc748Bb27CeFfEd88C0e9fD39027fF1a736',
  'name': 'VSPT',
  #Name: 'VesperTestToken',
  'decimals': 18
},
{
  'address': '0xB040041FDD14164A566f94f7789fc2e6b5Bf9c58',
  'name': 'RC_DAI_0.25_TRIBE_2021_4_30',
  #Name: 'Ruler Protocol rToken',
  'decimals': 18
},
{
  'address': '0xb05097849BCA421A3f51B249BA6CCa4aF4b97cb9',
  'name': 'FLOAT',
  #Name: 'Float Protocol: FLOAT',
  'decimals': 18
},
{
  'address': '0xb0D634b9c006FFA1e36FEC5E8Af2133b21Df4934',
  'name': 'dUSD',
  #Name: 'dUSD',
  'decimals': 18
},
{
  'address': '0xB1191F691A355b43542Bea9B8847bc73e7Abb137',
  'name': 'KIRO',
  #Name: 'Kirobo',
  'decimals': 18
},
{
  'address': '0xB1bF54d4BeEB77E5b99Fd2CA7811191D80D79f88',
  'name': 'CSATM',
  #Name: 'CryptoSmart ATM',
  'decimals': 2
},
{
  'address': '0xb1dC9124c395c1e97773ab855d66E879f053A289',
  'name': 'YAX',
  #Name: 'yAxis',
  'decimals': 18
},
{
  'address': '0xb1F4b66104353eC63D8d59D3da42C0b4Fb06E7f3',
  'name': 'FLOKI',
  #Name: 'Floki Inu',
  'decimals': 9
},
{
  'address': '0xb1f871Ae9462F1b2C6826E88A7827e76f86751d4',
  'name': 'GNYerc20',
  #Name: 'GNYerc20',
  'decimals': 18
},
{
  'address': '0xb220D53F7D0f52897Bcf25E47c4c3DC0bac344F8',
  'name': 'EUSD',
  #Name: 'EUSD',
  'decimals': 18
},
{
  'address': '0xb29663Aa4E2e81e425294193616c1B102B70a158',
  'name': 'LDN',
  #Name: 'Ludena Protocol',
  'decimals': 18
},
{
  'address': '0xb3829e5755fAfB97396109768895B1026ACC003F',
  'name': 'BC',
  #Name: 'Bcoin',
  'decimals': 18
},
{
  'address': '0xb3B4431F812A74BdfC148d6bDdfAdEcdC63FC083',
  'name': 'COLLECTIVE',
  #Name: 'collective',
  'decimals': 18
},
{
  'address': '0xB3Fa04A6FE3df11147Dd12909D4D4ce0EaCE915a',
  'name': '28T',
  #Name: 'Super28coin',
  'decimals': 8
},
{
  'address': '0xB423c1fb5414f0711c71181995FF59FfA6D31146',
  'name': 'TUNA',
  #Name: 'TunaSwap',
  'decimals': 18
},
{
  'address': '0xB4371dA53140417CBb3362055374B10D97e420bB',
  'name': 'SWTH',
  #Name: 'Switcheo Token',
  'decimals': 8
},
{
  'address': '0xb4bebD34f6DaaFd808f73De0d10235a92Fbb6c3D',
  'name': 'YETI',
  #Name: 'Yearn Ecosystem Token Index',
  'decimals': 18
},
{
  'address': '0xb4FBed161bEbcb37afB1Cb4a6F7cA18b977cCB25',
  'name': 'DOGES',
  #Name: 'DOGEswap',
  'decimals': 18
},
{
  'address': '0xb525Ecee288B99216CD481C56b6EFbdbE9bF90b5',
  'name': 'KUMA',
  #Name: 'Kuma Inu',
  'decimals': 18
},
{
  'address': '0xb5317944aC530A8fA9D31CbFb01fa5154F874CfA',
  'name': 'RINGER',
  #Name: 'Ringer',
  'decimals': 18
},
{
  'address': '0xb58DFBB72e648a0b035B8C85B3628123CC9bb881',
  'name': 'MIS2',
  #Name: 'MIS2',
  'decimals': 18
},
{
  'address': '0xb5A0931b1B7F21C2F557fd4FDdCcb504e71AE32D',
  'name': 'AVASTR-BASIC',
  #Name: 'Avastar-Basic',
  'decimals': 18
},
{
  'address': '0xb5b8F5616Fe42d5ceCA3e87F3FddbDd8F496d760',
  'name': 'ZPR',
  #Name: 'ZperToken',
  'decimals': 18
},
{
  'address': '0xb628Bc994e39CE264ECa6f6EE1620909816A9F12',
  'name': 'PRPS',
  #Name: 'Purpose',
  'decimals': 18
},
{
  'address': '0xB6A53b84e5744bBd5858a8653C0967c924A67827',
  'name': 'NMBL',
  #Name: 'Nimble',
  'decimals': 7
},
{
  'address': '0xB6eD7644C69416d67B522e20bC294A9a9B405B31',
  'name': '0xBTC',
  #Name: '0xBitcoin Token',
  'decimals': 8
},
{
  'address': '0xB6ff96B8A8d214544Ca0dBc9B33f7AD6503eFD32',
  'name': 'SYNC',
  #Name: 'SYNC',
  'decimals': 18
},
{
  'address': '0xB72B31907C1C95F3650b64b2469e08EdACeE5e8F',
  'name': 'vBZRX',
  #Name: 'bZx Vesting Token',
  'decimals': 18
},
{
  'address': '0xb72c84a9084b21b3Fd10Ca41661fb7538cEA7b56',
  'name': 'MIC',
  #Name: 'MIC',
  'decimals': 18
},
{
  'address': '0xb73F00feEAFc232C247516AA180261fEc0E909fc',
  'name': 'MITTN',
  #Name: 'Mr Mittenz',
  'decimals': 18
},
{
  'address': '0xb753428af26E81097e7fD17f40c88aaA3E04902c',
  'name': 'SFI',
  #Name: 'Spice',
  'decimals': 18
},
{
  'address': '0xb7602F7dc4d0A7074604f7f374600c5c67AA4Bf7',
  'name': 'CDF',
  #Name: 'Common',
  'decimals': 2
},
{
  'address': '0xb772481226124cAeD78C7B4654424020b06118Ed',
  'name': 'DEAFBEEF',
  #Name: 'DEAFBEEF Synth Poems',
  'decimals': 18
},
{
  'address': '0xb78B3320493a4EFaa1028130C5Ba26f0B6085Ef8',
  'name': 'DRC',
  #Name: 'Dracula Token',
  'decimals': 18
},
{
  'address': '0xB7acb10b6e1d15d2e5760a9fb328E10008dfCC3C',
  'name': '0XMON',
  #Name: '0xmons',
  'decimals': 18
},
{
  'address': '0xb825FF3Ca3454C133a9747Fb15a0EE1f51309D0A',
  'name': 'SINGULARITY',
  #Name: 'Singularity',
  'decimals': 18
},
{
  'address': '0xb8A58E3FD883b0230F4B47C4319e68CB7bB22339',
  'name': 'FHCT',
  #Name: 'Futurehead Coin Trust',
  'decimals': 9
},
{
  'address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52',
  'name': 'BNB',
  #Name: 'BNB',
  'decimals': 18
},
{
  'address': '0xb9892F9A892f3e251fc58B9076c56aDD528eb8A6',
  'name': 'MYM',
  #Name: 'Moyom',
  'decimals': 18
},
{
  'address': '0xb9d4b4d710E47E6782f3FFD6740dfa65FD637C08',
  'name': 'Morf',
  #Name: 'Morph',
  'decimals': 18
},
{
  'address': '0xb9EF770B6A5e12E45983C5D80545258aA38F3B78',
  'name': 'ZCN',
  #Name: '0chain',
  'decimals': 10
},
{
  'address': '0xba100000625a3754423978a60c9317c58a424e3D',
  'name': 'BAL',
  #Name: 'Balancer',
  'decimals': 18
},
{
  'address': '0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55',
  'name': 'BAND',
  #Name: 'BandToken',
  'decimals': 18
},
{
  'address': '0xBa13afEcda9beB75De5c56BbAF696b880a5A50dD',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xba4418f862A8d37c67991d658a3C5C09bD8C7366',
  'name': 'CROWN',
  #Name: 'Kassia Kommercial Crown',
  'decimals': 18
},
{
  'address': '0xBA50933C268F567BDC86E1aC131BE072C6B0b71a',
  'name': 'ARPA',
  #Name: 'ARPA Token',
  'decimals': 18
},
{
  'address': '0xBae5F2D8a1299E5c4963eaff3312399253f27Ccb',
  'name': 'SOAR',
  #Name: 'SOAR.FI',
  'decimals': 9
},
{
  'address': '0xBB0E17EF65F82Ab018d8EDd776e8DD940327B28b',
  'name': 'AXS',
  #Name: 'Axie Infinity Shard',
  'decimals': 18
},
{
  'address': '0xBB14B9B385ca3bd3668BbA114b555B3a3e1fA705',
  'name': 'NYAN',
  #Name: 'NyanCatToken',
  'decimals': 18
},
{
  'address': '0xbbBBBBB5AA847A2003fbC6b5C16DF0Bd1E725f61',
  'name': 'BPRO',
  #Name: 'B.Protocol',
  'decimals': 18
},
{
  'address': '0xBBbbCA6A901c926F240b89EacB641d8Aec7AEafD',
  'name': 'LRC',
  #Name: 'LoopringCoin V2',
  'decimals': 18
},
{
  'address': '0xBbff34E47E559ef680067a6B1c980639EEb64D24',
  'name': 'L2',
  #Name: 'Leverj Gluon',
  'decimals': 18
},
{
  'address': '0xbC192Ada0CE9D181C453a09209c5EA2838e105cA',
  'name': 'SHIBASWAP',
  #Name: 'SHIBASWAP',
  'decimals': 18
},
{
  'address': '0xbc194e6f748a222754C3E8b9946922c09E7d4e91',
  'name': 'LEV',
  #Name: 'Lever Token',
  'decimals': 18
},
{
  'address': '0xbC396689893D065F41bc2C6EcbeE5e0085233447',
  'name': 'PERP',
  #Name: 'Perpetual',
  'decimals': 18
},
{
  'address': '0xBC4B615C6C1bD10bc4E93A55EeE7688A7C42e5CB',
  'name': '4YE5',
  #Name: 'Fourier5',
  'decimals': 18
},
{
  'address': '0xBC5CeF436eADAcadfa8daFb63088F09F21dEa7E9',
  'name': 'GWEI',
  #Name: 'Gwei Token (Forked from WETH10)',
  'decimals': 9
},
{
  'address': '0xBC6DA0FE9aD5f3b0d58160288917AA56653660E9',
  'name': 'alUSD',
  #Name: 'Alchemix USD',
  'decimals': 18
},
{
  'address': '0xbc766B23F820BE4315F8CA8e527Dd3b4B1B13233',
  'name': 'DFc',
  #Name: 'Deflation function',
  'decimals': 18
},
{
  'address': '0xbC81BF5B3173BCCDBE62dba5f5b695522aD63559',
  'name': 'XPb',
  #Name: 'Lead Token',
  'decimals': 18
},
{
  'address': '0xBCd6a2DdAfbaa7f424698ed69E717C0c0F1e99BF',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xbCDa9E0658f4eECF56A0bd099e6DBc0C91f6A8c2',
  'name': 'sil',
  #Name: 'SushiswapV2 IL Protection',
  'decimals': 8
},
{
  'address': '0xBCfb0617ca95aF460E4051166b3Ab2AD99687dc4',
  'name': 'VGX',
  #Name: 'VGX',
  'decimals': 18
},
{
  'address': '0xBD0001Bb1a7EBDc64899161b48C60bcbef62004E',
  'name': 'YFFU2',
  #Name: 'YFFU.Finance 2.0',
  'decimals': 18
},
{
  'address': '0xBD2F0Cd039E0BFcf88901C98c0bFAc5ab27566e3',
  'name': 'DSD',
  #Name: 'Dynamic Set Dollar',
  'decimals': 18
},
{
  'address': '0xbD62253c8033F3907C0800780662EaB7378a4B96',
  'name': 'USDG',
  #Name: 'United States dollar of Galaxy',
  'decimals': 9
},
{
  'address': '0xbDbf245c690d54b67C6e610A28486A2C6dE08bE6',
  'name': 'Sunder',
  #Name: 'Sunder Goverance Token',
  'decimals': 18
},
{
  'address': '0xBdC087d1237CbFbba2C792eBcfA149c8b7978aCd',
  'name': 'W0ND3R',
  #Name: 'Defi Wonderland',
  'decimals': 18
},
{
  'address': '0xbDd4f273C2b0f0B84a51BD733AAc617D91159376',
  'name': 'BALT',
  #Name: 'BMoreToken',
  'decimals': 8
},
{
  'address': '0xbDEC45952B5E234EdDC2981B43eeD360826D5087',
  'name': 'MOGX',
  #Name: 'Mogu Token',
  'decimals': 18
},
{
  'address': '0xBe80cEED72E1798c631fcd92F611367aBD7F836F',
  'name': 'INS',
  #Name: 'Coin98 Insights',
  'decimals': 18
},
{
  'address': '0xBEc6Cf25aFB79b975E57b93f3216e468F8FED910',
  'name': 'IMTY',
  #Name: 'ImmunityToken',
  'decimals': 18
},
{
  'address': '0xbeCd3F2A2280314a553267650e20b719abEdCb04',
  'name': 'LAMBO',
  #Name: 'LamboCoin',
  'decimals': 18
},
{
  'address': '0xbf1F9A14F3ba62370215eA0f476a99eD17225b74',
  'name': 'PATHFINDER',
  #Name: 'Pathfinder',
  'decimals': 18
},
{
  'address': '0xbf2179859fc6D5BEE9Bf9158632Dc51678a4100e',
  'name': 'ELF',
  #Name: 'ELF Token',
  'decimals': 18
},
{
  'address': '0xbF4a2DdaA16148a9D0fA2093FfAC450ADb7cd4aa',
  'name': 'ETHMNY',
  #Name: 'Ethereum Money',
  'decimals': 2
},
{
  'address': '0xbF66E58702e87271c0c5260F5f7Da2f8283Bff37',
  'name': 'USDD',
  #Name: 'USDD',
  'decimals': 18
},
{
  'address': '0xc00e94Cb662C3520282E6f5717214004A7f26888',
  'name': 'COMP',
  #Name: 'Compound',
  'decimals': 18
},
{
  'address': '0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F',
  'name': 'SNX',
  #Name: 'Synthetix Network Token',
  'decimals': 18
},
{
  'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
  'name': 'WETH',
  #Name: 'Wrapped Ether',
  'decimals': 18
},
{
  'address': '0xC051A79D62E7592b42fFd5884aE0d90Ed8eE0085',
  'name': 'SPWN',
  #Name: 'SPAWN',
  'decimals': 8
},
{
  'address': '0xC06AC15756043f9AB9dd18657697E054B9e51E8B',
  'name': 'CRIB',
  #Name: 'Cribini',
  'decimals': 18
},
{
  'address': '0xc0Ba6EEe30932C18E6Cd19F433Fe84186500148A',
  'name': 'GCAC',
  #Name: 'Global Cannabis Applications Corp',
  'decimals': 18
},
{
  'address': '0xC0Eb85285d83217CD7c891702bcbC0FC401E2D9D',
  'name': 'HVN',
  #Name: 'Hive Project Token',
  'decimals': 8
},
{
  'address': '0xc1091350291e228518beaE7B775D05c353789C9E',
  'name': 'WUSD',
  #Name: 'Wrapped USD',
  'decimals': 18
},
{
  'address': '0xc12d099be31567add4e4e4d0D45691C3F58f5663',
  'name': 'AUC',
  #Name: 'Auctus Token',
  'decimals': 18
},
{
  'address': '0xC12D1c73eE7DC3615BA4e37E4ABFdbDDFA38907E',
  'name': 'KICK',
  #Name: 'KickToken',
  'decimals': 8
},
{
  'address': '0xc15A251158A3A98F868425fB2B2ee198De4759B5',
  'name': 'xAAPL',
  #Name: 'Apple Inc',
  'decimals': 6
},
{
  'address': '0xc163EaDe1a642D8ccEf1046bAE2569A00cB647Ed',
  'name': 'UVU',
  #Name: 'Comunion UVU Token',
  'decimals': 8
},
{
  'address': '0xc22B30E4cce6b78aaaADae91E44E73593929a3e9',
  'name': 'RAC',
  #Name: 'RAC',
  'decimals': 18
},
{
  'address': '0xc22c6C6e1c78d1996B81782eBE750d96721ba4EC',
  'name': 'POB',
  #Name: 'Proof of Beauty',
  'decimals': 18
},
{
  'address': '0xC28E27870558cF22ADD83540d2126da2e4b464c2',
  'name': 'SASHIMI',
  #Name: 'SashimiToken',
  'decimals': 18
},
{
  'address': '0xc3589F56B6869824804A5EA29F2c9886Af1B0FcE',
  'name': 'HNY',
  #Name: 'Honey',
  'decimals': 18
},
{
  'address': '0xC36824905dfF2eAAEE7EcC09fCC63abc0af5Abc5',
  'name': 'BAB',
  #Name: 'BAB',
  'decimals': 18
},
{
  'address': '0xc3B5284B2c0cfa1871a6ac63B6d6ee43c08BDC79',
  'name': 'BGAN',
  #Name: 'BASTARD GAN PUNKS V2',
  'decimals': 18
},
{
  'address': '0xC3D03e4F041Fd4cD388c549Ee2A29a9E5075882f',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xC40D16476380e4037e6b1A2594cAF6a6cc8Da967',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xC4376cFdaB7302c47155b8D40c0E1941aE662526',
  'name': 'LAGER',
  #Name: 'Lager Finance',
  'decimals': 18
},
{
  'address': '0xc460aE61f7fD34ACA255F9114Cd496F50B2CFE1b',
  'name': 'MON',
  #Name: 'MonaCoin',
  'decimals': 18
},
{
  'address': '0xc4bf60B93ac60dB9A45AD232368d50de0A354849',
  'name': 'KITTY-GEN-0-F',
  #Name: 'Kitty-Gen-0-Fast',
  'decimals': 18
},
{
  'address': '0xC4d20bd7d1AEB427a0573ee0F259dB25329333cF',
  'name': 'ySUSHI 21',
  #Name: 'Yield Dollar Sushi 21',
  'decimals': 18
},
{
  'address': '0xc4De189Abf94c57f396bD4c52ab13b954FebEfD8',
  'name': 'B20',
  #Name: 'B.20',
  'decimals': 18
},
{
  'address': '0xc4E15973E6fF2A35cC804c2CF9D2a1b817a8b40F',
  'name': 'ibBTC',
  #Name: 'Interest-Bearing BTC',
  'decimals': 18
},
{
  'address': '0xC51a271900D6E7Fa0E11E2F4b59F066D40969fe9',
  'name': 'ERO',
  #Name: 'Erotore',
  'decimals': 3
},
{
  'address': '0xC567bca531992352166252ea5121e535432E81eD',
  'name': 'TAR',
  #Name: 'Tartarus',
  'decimals': 8
},
{
  'address': '0xC57d533c50bC22247d49a368880fb49a1caA39F7',
  'name': 'PTF',
  #Name: 'PowerTrade Fuel Token',
  'decimals': 18
},
{
  'address': '0xC58596D7C48bcFf23541A31251f09802BA597657',
  'name': 'oneWING',
  #Name: 'oneWING',
  'decimals': 9
},
{
  'address': '0xc5bDdf9843308380375a611c18B50Fb9341f502A',
  'name': 'yveCRV-DAO',
  #Name: 'veCRV-DAO yVault',
  'decimals': 18
},
{
  'address': '0xC5Fa164247d2F8D68804139457146eFBde8370F6',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xc666081073E8DfF8D3d1c2292A29aE1A2153eC09',
  'name': 'DGTX',
  #Name: 'DigitexFutures',
  'decimals': 18
},
{
  'address': '0xc6e2da4A9dBe3DFe5A0836B182e0a762A0F8ebd9',
  'name': 'FCKS',
  #Name: 'FucKoin',
  'decimals': 18
},
{
  'address': '0xc6E6660Fd4895786C10A259577367dfF3d152FD8',
  'name': 'DULY',
  #Name: 'DULY',
  'decimals': 18
},
{
  'address': '0xc7283b66Eb1EB5FB86327f08e1B5816b0720212B',
  'name': 'TRIBE',
  #Name: 'Tribe',
  'decimals': 18
},
{
  'address': '0xc76160CE8E26E0Cf61A78a5a749478D22d91461d',
  'name': 'R2R',
  #Name: 'R2R coin',
  'decimals': 18
},
{
  'address': '0xC76FB75950536d98FA62ea968E1D6B45ffea2A55',
  'name': 'COL',
  #Name: 'COL',
  'decimals': 18
},
{
  'address': '0xC77A91BEF771a0b62A81ef776BC5071713025dDe',
  'name': 'POPCOIN',
  #Name: 'PopCoin',
  'decimals': 18
},
{
  'address': '0xC8120381FFaAE4c79dd51f71affdc9F88420B505',
  'name': 'BABES-BASIC',
  #Name: 'Babes-Basic',
  'decimals': 18
},
{
  'address': '0xC837305EcDcB66FD8014a7e58985D72908bbfDF0',
  'name': 'FMT',
  #Name: 'Fudmart Token',
  'decimals': 18
},
{
  'address': '0xC88F47067dB2E25851317A2FDaE73a22c0777c37',
  'name': 'oneBTC',
  #Name: 'oneBTC',
  'decimals': 9
},
{
  'address': '0xc8AA432112814B9CAB53811D4340Ed45482CB2b5',
  'name': 'GLYPH',
  #Name: 'Glyph',
  'decimals': 18
},
{
  'address': '0xc926990039045611eb1DE520C1E249Fd0d20a8eA',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xc944E90C64B2c07662A292be6244BDf05Cda44a7',
  'name': 'GRT',
  #Name: 'Graph Token',
  'decimals': 18
},
{
  'address': '0xC94B0F0205AA1948341F06F899E662D80074d338',
  'name': 'unknown',
  #Name: 'unknown',
  'decimals': 0
},
{
  'address': '0xC96c1609A1a45CcC667B2b7FA6508e29617f7b69',
  'name': '2GT',
  #Name: '2GT_token',
  'decimals': 18
},
{
  'address': '0xC9cB53B48A2f3A9e75982685644c1870F1405CCb',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xCa3FE04C7Ee111F0bbb02C328c699226aCf9Fd33',
  'name': 'SEEN',
  #Name: 'seen.haus',
  'decimals': 18
},
{
  'address': '0xCa5d29B3e74D59EBcDF09111495d86F319886A40',
  'name': 'WHEY',
  #Name: 'WheyToken',
  'decimals': 18
},
{
  'address': '0xcA6693abA63C3AB0803E14ef7d32Dd37D1F55bEc',
  'name': 'BACON',
  #Name: 'BACON Network',
  'decimals': 18
},
{
  'address': '0xCa7e925bA8938A1b587172658b6C24054329aeF8',
  'name': 'bulldoge',
  #Name: 'bulldoge',
  'decimals': 18
},
{
  'address': '0xcAaa93712BDAc37f736C323C93D4D5fDEFCc31CC',
  'name': 'CRD',
  #Name: 'CryptalDash',
  'decimals': 18
},
{
  'address': '0xcae516AA57D04EBf9b92813050282333F7587d2F',
  'name': 'UNI',
  #Name: 'Uniswap V3',
  'decimals': 18
},
{
  'address': '0xCb2286d9471cc185281c4f763d34A962ED212962',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xcb46C550539ac3DB72dc7aF7c89B11c306C727c2',
  'name': 'pONT',
  #Name: 'Poly Ontology Token',
  'decimals': 9
},
{
  'address': '0xCb5f72d37685C3D5aD0bB5F982443BC8FcdF570E',
  'name': 'ROOT',
  #Name: 'RootKit',
  'decimals': 18
},
{
  'address': '0xcBc1065255cBc3aB41a6868c22d1f1C573AB89fd',
  'name': 'CRETH2',
  #Name: 'Cream ETH 2',
  'decimals': 18
},
{
  'address': '0xcbd55D4fFc43467142761A764763652b48b969ff',
  'name': 'ASTRO',
  #Name: 'AstroTools.io',
  'decimals': 18
},
{
  'address': '0xCc3F1441e84f124A65Bc9798A69A5C4cEbC20dFF',
  'name': 'MORPH',
  #Name: 'Polymorphs',
  'decimals': 18
},
{
  'address': '0xcc5CB920D39d4d43E68d373a4889Bb6d88ED2497',
  'name': 'POOLZ',
  #Name: 'Poolz',
  'decimals': 18
},
{
  'address': '0xcc7ab8d78dBA187dC95bF3bB86e65E0C26d0041f',
  'name': 'SPACE',
  #Name: 'Spacelens',
  'decimals': 18
},
{
  'address': '0xccA213BA15832862c61d096c75bdf0FC90e0F62F',
  'name': 'STADX',
  #Name: 'Stadia',
  'decimals': 18
},
{
  'address': '0xCccB6460bC41A6Db9C830b8318F3557bAff0Dfd1',
  'name': 'DOPL.',
  #Name: 'Doppler',
  'decimals': 18
},
{
  'address': '0xCD1cb16a67937ff8Af5D726e2681010cE1E9891a',
  'name': 'MIS',
  #Name: 'ThemisToken',
  'decimals': 8
},
{
  'address': '0xcD91538B91B4ba7797D39a2f66E63810b50A33d0',
  'name': 'STABLEx',
  #Name: 'ARC STABLEx',
  'decimals': 18
},
{
  'address': '0xCe78AB22CD0331a52Af7Bb4b622edFa792819D47',
  'name': 'RUDA',
  #Name: 'RUDAWORLD',
  'decimals': 18
},
{
  'address': '0xce9aFAF5b0dA6cE0366aB40435A48ccff65d2ED7',
  'name': 'BOBA',
  #Name: 'BobaToken',
  'decimals': 18
},
{
  'address': '0xCEfF51756c56CeFFCA006cD410B03FFC46dd3a58',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xCF2b421011ffF1200bD8bf5B9Cdc7EA179F445ff',
  'name': 'unknown',
  #Name: 'unknown',
  'decimals': 0
},
{
  'address': '0xcfc013B416bE0Bd4b3bEdE35659423B796f8Dcf0',
  'name': 'MBTC',
  #Name: 'Matrix BTC Token',
  'decimals': 8
},
{
  'address': '0xCFc9A86fCcF24eF495194540e1a3d3D523893355',
  'name': 'RDM',
  #Name: 'Primitive V1 Redeem',
  'decimals': 18
},
{
  'address': '0xCFD111c4c0DaEAE6351bcdC80a993e78923845AB',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xd010874156506FF12ddd1F2cf380cEb7676FB95d',
  'name': 'KAD',
  #Name: 'KAIDO',
  'decimals': 6
},
{
  'address': '0xD01ef7C0A5d8c432fc2d1a85c66cF2327362E5C6',
  'name': 'fETH',
  #Name: 'Ankr Eth2 Futures',
  'decimals': 18
},
{
  'address': '0xD0660cD418a64a1d44E9214ad8e459324D8157f1',
  'name': 'WOOFY',
  #Name: 'Woofy',
  'decimals': 12
},
{
  'address': '0xd084944d3c05CD115C09d072B9F44bA3E0E45921',
  'name': 'FOLD',
  #Name: 'Manifold Finance',
  'decimals': 18
},
{
  'address': '0xd0d7A9f2021958e51d60D6966b7BbeD9D1CB22B5',
  'name': 'ENX',
  #Name: 'ENEX.SPACE',
  'decimals': 10
},
{
  'address': '0xD1Ff31E3D8B78F06AEa4EAbB534bf5Aa23278341',
  'name': 'ILVA',
  #Name: 'ILVA',
  'decimals': 16
},
{
  'address': '0xd234BF2410a0009dF9c3C63b610c09738f18ccD7',
  'name': 'DTR',
  #Name: 'Dynamic Trading Rights',
  'decimals': 8
},
{
  'address': '0xD23Ac27148aF6A2f339BD82D0e3CFF380b5093de',
  'name': 'SI',
  #Name: 'SIREN',
  'decimals': 18
},
{
  'address': '0xd26114cd6EE289AccF82350c8d8487fedB8A0C07',
  'name': 'OMG',
  #Name: 'OMGToken',
  'decimals': 18
},
{
  'address': '0xD26c338fBf7E02dd8711424567B2BABA3d5DCE3A',
  'name': 'WAFL',
  #Name: 'Waffle',
  'decimals': 2
},
{
  'address': '0xd2877702675e6cEb975b4A1dFf9fb7BAF4C91ea9',
  'name': 'LUNA',
  #Name: 'Wrapped LUNA Token',
  'decimals': 18
},
{
  'address': '0xD291E7a03283640FDc51b121aC401383A46cC623',
  'name': 'RGT',
  #Name: 'Rari Governance Token',
  'decimals': 18
},
{
  'address': '0xd303Cf6FDc49689Cf42DdB44824d446664b76E95',
  'name': 'TIDE',
  #Name: 'Tide',
  'decimals': 18
},
{
  'address': '0xD3360862277BA00BAC19192240046F086629A6cD',
  'name': 'OWP',
  #Name: 'OneWorldPlan',
  'decimals': 6
},
{
  'address': '0xd3dd721B74d72F29677a94C4B318f16A7F7426bC',
  'name': 'DCS',
  #Name: 'DCS',
  'decimals': 18
},
{
  'address': '0xD3f85d18206829f917929BbBF738C1e0CE9AF7fC',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xD417144312DbF50465b1C641d016962017Ef6240',
  'name': 'CQT',
  #Name: 'Covalent Query Token',
  'decimals': 18
},
{
  'address': '0xD46bA6D942050d489DBd938a2C909A5d5039A161',
  'name': 'AMPL',
  #Name: 'Ampleforth',
  'decimals': 9
},
{
  'address': '0xD478161C952357F05f0292B56012Cd8457F1cfbF',
  'name': 'POLK',
  #Name: 'Polkamarkets',
  'decimals': 18
},
{
  'address': '0xd4e52512B756F5dD4C98F3472C24e88061Ee711B',
  'name': 'LASER',
  #Name: 'LASER COIN',
  'decimals': 18
},
{
  'address': '0xD533a949740bb3306d119CC777fa900bA034cd52',
  'name': 'CRV',
  #Name: 'Curve DAO Token',
  'decimals': 18
},
{
  'address': '0xD5525D397898e5502075Ea5E830d8914f6F0affe',
  'name': 'MEME',
  #Name: 'MEME',
  'decimals': 8
},
{
  'address': '0xd5c52B857339815b36318e05120EA4C496230127',
  'name': 'SOLVAULT',
  #Name: 'SOLVAULT FINANCE GOVERNANCE',
  'decimals': 18
},
{
  'address': '0xD5cd84D6f044AbE314Ee7E414d37cae8773ef9D3',
  'name': '1ONE',
  #Name: 'Harmony ONE',
  'decimals': 18
},
{
  'address': '0xd5Db36E4Dd196BE70dbE5DFB4A912b0046FD245d',
  'name': 'DHT',
  #Name: 'Dolphin Token',
  'decimals': 9
},
{
  'address': '0xD70240Dd62F4ea9a6A2416e0073D72139489d2AA',
  'name': 'GLYPH',
  #Name: 'Autoglyphs',
  'decimals': 18
},
{
  'address': '0xD75EA151a61d06868E31F8988D28DFE5E9df57B4',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xd785f5525C645B8D3c98DFce381d0a38DE5de02C',
  'name': 'BLME',
  #Name: 'BeeLeaf Me',
  'decimals': 18
},
{
  'address': '0xD7B7d3C0bdA57723Fb54ab95Fd8F9EA033AF37f2',
  'name': 'PYLON',
  #Name: 'PYLON',
  'decimals': 18
},
{
  'address': '0xD7F8032777C50aFD2e7AFa41912a4d8038127271',
  'name': 'MUA',
  #Name: 'MUAN',
  'decimals': 18
},
{
  'address': '0xd835Ca52892135fD89Afe6FE2e1391B1cFE2c838',
  'name': 'DM',
  #Name: 'Deutsche Mark',
  'decimals': 18
},
{
  'address': '0xD9Cb47e5A7D8243756133FCEc6E9Bdc40896CCEF',
  'name': 'MIS',
  #Name: 'MIS',
  'decimals': 18
},
{
  'address': '0xda4C5AEA122260e70616E979592735F12FE20499',
  'name': 'AXN',
  #Name: 'AXION',
  'decimals': 18
},
{
  'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
  'name': 'USDT',
  #Name: 'Tether USD',
  'decimals': 6
},
{
  'address': '0xDADA00A9C23390112D08a1377cc59f7d03D9df55',
  'name': 'DUNG',
  #Name: 'Degen$ Farm Dung',
  'decimals': 18
},
{
  'address': '0xDafd66636E2561b0284EDdE37e42d192F2844D40',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xDb0f18081b505A7DE20B18ac41856BCB4Ba86A1a',
  'name': 'pWING',
  #Name: 'Poly Ontology Wing Token',
  'decimals': 9
},
{
  'address': '0xdB25f211AB05b1c97D595516F45794528a807ad8',
  'name': 'EURS',
  #Name: 'STASIS EURS Token',
  'decimals': 2
},
{
  'address': '0xdBbd999efa8dE5038234c7C9518435e98283d8ff',
  'name': 'DHINU',
  #Name: 'DIAMONDHANDSINU',
  'decimals': 18
},
{
  'address': '0xdBdb4d16EdA451D0503b854CF79D55697F90c8DF',
  'name': 'ALCX',
  #Name: 'Alchemix',
  'decimals': 18
},
{
  'address': '0xdbDD6F355A37b94e6C7D32fef548e98A280B8Df5',
  'name': 'UWL',
  #Name: 'UniWhales.io',
  'decimals': 18
},
{
  'address': '0xdC57e9B624b931aa8202F3A8d54F09fa8ce7981F',
  'name': 'OSST',
  #Name: 'Open Sesame Token',
  'decimals': 18
},
{
  'address': '0xDc5864eDe28BD4405aa04d93E05A0531797D9D59',
  'name': 'FNT',
  #Name: 'Falcon',
  'decimals': 6
},
{
  'address': '0xdC76450Fd7E6352733fe8550efABfF750B2De0e3',
  'name': 'DYNA',
  #Name: 'BerezkaDynamic',
  'decimals': 18
},
{
  'address': '0xDc7eE965B4F62C1Ed2A2da72B20a143Bfe31fD32',
  'name': 'TWERKY',
  #Name: 'Twerky Pepe',
  'decimals': 18
},
{
  'address': '0xDcB01cc464238396E213a6fDd933E36796eAfF9f',
  'name': 'YLD',
  #Name: 'Yield',
  'decimals': 18
},
{
  'address': '0xdCB5D9060f7A5a43b26328982EB71d7E449545FE',
  'name': 'SPCE',
  #Name: 'Space Force',
  'decimals': 18
},
{
  'address': '0xdcD6456Aba437cD7a038B5b2Ec767C0eEC834d67',
  'name': 'Φ$',
  #Name: 'PHICASH',
  'decimals': 18
},
{
  'address': '0xdcDc1c1cC33AA817CbDBe8F5E2390BF7cc43dc4B',
  'name': 'AVASTR',
  #Name: 'Avastars',
  'decimals': 18
},
{
  'address': '0xDDB3422497E61e13543BeA06989C0789117555c5',
  'name': 'COTI',
  #Name: 'COTI Token',
  'decimals': 18
},
{
  'address': '0xDDC912F739CDf59f21Edd62A36EE83e2C1D6aB33',
  'name': 'KSD',
  #Name: 'KIMSUNDAL',
  'decimals': 2
},
{
  'address': '0xDDE73732248f4d11A918eAE83cEBB034cC69875e',
  'name': 'VMSC',
  #Name: 'VMS chain',
  'decimals': 8
},
{
  'address': '0xDe25486CCb4588Ce5D9fB188fb6Af72E768a466a',
  'name': 'CDSD',
  #Name: 'address ion Dynamic Set Dollar',
  'decimals': 18
},
{
  'address': '0xDe79d36aB6D2489dd36729A657a25f299Cb2Fbca',
  'name': 'CurveBTC+',
  #Name: 'Curve BTC Plus',
  'decimals': 18
},
{
  'address': '0xdECE0F6864c1511369ae2c30B90Db9f5fe92832c',
  'name': 'DSCPL',
  #Name: 'DISCIPLINA',
  'decimals': 18
},
{
  'address': '0xDEE0FeF656D1b84Cf0967274eFE75C7A36BaD813',
  'name': 'LCS',
  #Name: 'Liberty Cash Plus',
  'decimals': 18
},
{
  'address': '0xdeFCb64c13442D40db6e45CF7fE1E064e5E360C9',
  'name': 'NYAN',
  #Name: 'NyanCatToken',
  'decimals': 18
},
{
  'address': '0xdf48cd3b64766957B230314Ee93bFbeF9582cDeb',
  'name': 'SQUIGGLE',
  #Name: 'Chromie Squiggle',
  'decimals': 18
},
{
  'address': '0xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8',
  'name': 'yDAI+yUSDC+yUSDT+yTUSD',
  #Name: 'Curve.fi yDAI/yUSDC/yUSDT/yTUSD',
  'decimals': 18
},
{
  'address': '0xdFC3829b127761a3218bFceE7fc92e1232c9D116',
  'name': 'WPRCY',
  #Name: 'Wrapped PRCY',
  'decimals': 8
},
{
  'address': '0xDFe66B14D37C77F4E9b180cEb433d1b164f0281D',
  'name': 'stETH',
  #Name: 'stakedETH',
  'decimals': 18
},
{
  'address': '0xe04Ed6D0dCe0E6b11a8971f2595f5C2939Ccc27F',
  'name': 'WSBT',
  #Name: 'WallStreetBetsToken',
  'decimals': 0
},
{
  'address': '0xe067B137881A65689773F2cC3C199B21b258303d',
  'name': 'USxD',
  #Name: 'United Stock exchange Dollars',
  'decimals': 18
},
{
  'address': '0xE0839f9b9688a77924208aD509e29952dc660261',
  'name': 'yCREDIT',
  #Name: 'Stable Yield Credit',
  'decimals': 8
},
{
  'address': '0xE094b1653a3427E6A61c41281640f1aDA9bFf079',
  'name': 'RecovEarth',
  #Name: 'Earth Recapture Preserve',
  'decimals': 18
},
{
  'address': '0xE09B10EFA59F6E17052E9A2D947bAd6214E7CC90',
  'name': 'LFETH',
  #Name: 'Lift.Kitchen ETH',
  'decimals': 18
},
{
  'address': '0xE0aD1806Fd3E7edF6FF52Fdb822432e847411033',
  'name': 'ONX',
  #Name: 'OnX.finance',
  'decimals': 18
},
{
  'address': '0xE0C33EBEEdDDb898b2b7e44d6c0B56860b298075',
  'name': 'BMTN',
  #Name: 'BMToken',
  'decimals': 18
},
{
  'address': '0xe1406825186D63980fd6e2eC61888f7B91C4bAe4',
  'name': 'VBTC',
  #Name: 'Strudel BTC',
  'decimals': 18
},
{
  'address': '0xE1Ab817B1edA1B05785B731060658885c91acd89',
  'name': 'METAL',
  #Name: 'METAL',
  'decimals': 18
},
{
  'address': '0xe1f238374943bB9A2d254dfB713B3B2fF8efdb87',
  'name': 'ETRD',
  #Name: 'ETradingStakeToken',
  'decimals': 18
},
{
  'address': '0xE1F83480F5937364bDa3410f034C42BDdeA6Ec85',
  'name': 'INTR',
  #Name: 'Intro',
  'decimals': 18
},
{
  'address': '0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30',
  'name': 'INJ',
  #Name: 'Injective Token',
  'decimals': 18
},
{
  'address': '0xe379a60A8FC7C9DD161887fFADF3054790576c8D',
  'name': 'XSUc25-0621',
  #Name: 'XSUSHI 25 Call [30 June 2021]',
  'decimals': 18
},
{
  'address': '0xe3818504c1B32bF1557b16C238B2E01Fd3149C17',
  'name': 'PLR',
  #Name: 'PILLAR',
  'decimals': 18
},
{
  'address': '0xE3B59AcD6c24331b3bBEdbaacBd34871f486815c',
  'name': 'SLT',
  #Name: 'SushiswapV2 ILTest',
  'decimals': 8
},
{
  'address': '0xE3dA4e02BDFfb004C463dABB846d77d4e0d34163',
  'name': 'wndrLP',
  #Name: 'Wonderland wndrLP',
  'decimals': 18
},
{
  'address': '0xE41d2489571d322189246DaFA5ebDe1F4699F498',
  'name': 'ZRX',
  #Name: '0x Protocol Token',
  'decimals': 18
},
{
  'address': '0xe4455FdEc181561e9Ffe909Dde46AAEaeDC55283',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xe4589f7785cA9c5001bdB29a96f948773cDF95CC',
  'name': 'SUSHIDOGE',
  #Name: 'SushiDoge',
  'decimals': 18
},
{
  'address': '0xe4815AE53B124e7263F08dcDBBB757d41Ed658c6',
  'name': 'ZKS',
  #Name: 'Zks',
  'decimals': 18
},
{
  'address': '0xE48972fCd82a274411c01834e2f031D4377Fa2c0',
  'name': '2KEY',
  #Name: 'TwoKeyEconomy',
  'decimals': 18
},
{
  'address': '0xE4AE84448DB5CFE1DaF1e6fb172b469c161CB85F',
  'name': 'UOP',
  #Name: 'Utopia Open Platform',
  'decimals': 18
},
{
  'address': '0xE4E55bE3A8D9DB6C8f33f5834Eca7c446A494116',
  'name': 'ULC',
  #Name: 'Ultimatalioniscoin',
  'decimals': 18
},
{
  'address': '0xE4f726Adc8e89C6a6017F01eadA77865dB22dA14',
  'name': 'BCP',
  #Name: 'PieDAO Balanced Crypto Pie',
  'decimals': 18
},
{
  'address': '0xe53EC727dbDEB9E2d5456c3be40cFF031AB40A55',
  'name': 'SUPER',
  #Name: 'SuperFarm',
  'decimals': 18
},
{
  'address': '0xE5B826Ca2Ca02F09c1725e9bd98d9a8874C30532',
  'name': 'ZEON',
  #Name: 'ZEON',
  'decimals': 18
},
{
  'address': '0xe5feeaC09D36B18b3FA757E5Cf3F8dA6B8e27F4C',
  'name': 'NFTI',
  #Name: 'NFT INDEX',
  'decimals': 18
},
{
  'address': '0xE60017a033229af351827f0C8FF0D5a2E256B9Ef',
  'name': 'BTA',
  #Name: 'Bitcoinasset',
  'decimals': 18
},
{
  'address': '0xE6279E1c65DD41b30bA3760DCaC3CD8bbb4420D6',
  'name': 'REB',
  #Name: 'Rebased',
  'decimals': 9
},
{
  'address': '0xe632e1EA781df32c60AB11052958744CBfBc439A',
  'name': 'BAKC',
  #Name: 'Bored Ape Kennel Club',
  'decimals': 18
},
{
  'address': '0xe6710e0CdA178f3D921f456902707B0d4C4A332B',
  'name': 'JULIEN',
  #Name: 'Julien',
  'decimals': 4
},
{
  'address': '0xE692c8D72bd4aC7764090d54842a305546dd1dE5',
  'name': 'aBLOCK',
  #Name: 'ANY Blocknet',
  'decimals': 8
},
{
  'address': '0xE7069E147CD7085abb493f7990c684029DEaDCdD',
  'name': 'JRE',
  #Name: 'JuraToken',
  'decimals': 18
},
{
  'address': '0xe7689B2C21242e07870AAA0ffee1eC11833d5E24',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xE7eE0b13928aFEE21a634deBBe59693b13658420',
  'name': 'RC_COVER_250_DAI_2021_3_31',
  #Name: 'Ruler Protocol rToken',
  'decimals': 18
},
{
  'address': '0xE7F4c89032A2488D327323548AB0459676269331',
  'name': 'WAIFU',
  #Name: 'Waifusion',
  'decimals': 18
},
{
  'address': '0xe8679fe133f38f19e1cFFEBA98a4BAA5c897Ce51',
  'name': 'BTY',
  #Name: 'BitcoYield',
  'decimals': 18
},
{
  'address': '0xE94B97b6b43639E238c851A7e693F50033EfD75C',
  'name': 'RNBW',
  #Name: 'Rainbow Token',
  'decimals': 18
},
{
  'address': '0xE95A203B1a91a908F9B9CE46459d101078c2c3cb',
  'name': 'aETHB',
  #Name: 'Ankr Eth2 Reward Bearing Bond',
  'decimals': 18
},
{
  'address': '0xe9F84dE264E91529aF07Fa2C746e934397810334',
  'name': 'SAK3',
  #Name: 'Sake',
  'decimals': 18
},
{
  'address': '0xEa319e87Cf06203DAe107Dd8E5672175e3Ee976c',
  'name': 'SURF',
  #Name: 'SURF.Finance',
  'decimals': 18
},
{
  'address': '0xea5f88E54d982Cbb0c441cde4E79bC305e5b43Bc',
  'name': 'PARETO',
  #Name: 'Pareto Network Token',
  'decimals': 18
},
{
  'address': '0xea6412Fb370e8d1605E6aEeAA21aD07C3C7e9F24',
  'name': 'MUSH',
  #Name: 'MUSH',
  'decimals': 18
},
{
  'address': '0xEABB8996eA1662cAd2f7fB715127852cd3262Ae9',
  'name': 'CNFI',
  #Name: 'Connect Financial',
  'decimals': 18
},
{
  'address': '0xeAD35F584B21FE77bd7673921e909032101DbdE5',
  'name': 'CARD',
  #Name: 'Ether Cards',
  'decimals': 18
},
{
  'address': '0xeB10a2423810fAeF05e99333e501b7Eb1AC8CaFa',
  'name': 'SNL',
  #Name: 'SaturdayNightDoge',
  'decimals': 18
},
{
  'address': '0xEB4C2781e4ebA804CE9a9803C67d0893436bB27D',
  'name': 'renBTC',
  #Name: 'renBTC',
  'decimals': 8
},
{
  'address': '0xEB9951021698B42e4399f9cBb6267Aa35F82D59D',
  'name': 'unknown',
  #Name: 'unknown',
  'decimals': 0
},
{
  'address': '0xEBd9D99A3982d547C5Bb4DB7E3b1F9F14b67Eb83',
  'name': 'ID',
  #Name: 'Everest ID',
  'decimals': 18
},
{
  'address': '0xEBE4a49dF7885d015329c919bF43e6460a858F1e',
  'name': 'SHK',
  #Name: 'SHOOK',
  'decimals': 18
},
{
  'address': '0xEc0d77a58528a218cBf41Fa6E1585c8D7A085868',
  'name': 'oneETH',
  #Name: 'oneETH',
  'decimals': 9
},
{
  'address': '0xeC34EF72683b5f35727670977c9D484B9f488401',
  'name': 'VOLCANO?',
  #Name: 'VOLCANO BTC',
  'decimals': 18
},
{
  'address': '0xec67005c4E498Ec7f55E092bd1d35cbC47C91892',
  'name': 'MLN',
  #Name: 'Melon Token',
  'decimals': 18
},
{
  'address': '0xEd0439EACf4c4965AE4613D77a5C2Efe10e5f183',
  'name': 'SHROOM',
  #Name: 'shroom.finance',
  'decimals': 18
},
{
  'address': '0xEd31fdA280153d4A38294582AEA3a1A27901aCA3',
  'name': 'Alpaca',
  #Name: 'Alpaca City',
  'decimals': 18
},
{
  'address': '0xEDc83120Ddd7F27C54A01Ff8B29b21c153eB9e52',
  'name': 'CANNA',
  #Name: 'canna',
  'decimals': 18
},
{
  'address': '0xeDEec5691f23E4914cF0183A4196bBEb30d027a0',
  'name': 'WSTA',
  #Name: 'Wrapped STA',
  'decimals': 18
},
{
  'address': '0xeDF6568618A00C6F0908Bf7758A16F76B6E04aF9',
  'name': 'ARIA20',
  #Name: 'ARIANEE',
  'decimals': 18
},
{
  'address': '0xEE06A81a695750E71a662B51066F2c74CF4478a0',
  'name': '$DG',
  #Name: 'decentral.games',
  'decimals': 18
},
{
  'address': '0xEE1482a2C48F0012862e45a992666096Fc767B78',
  'name': 'RDM',
  #Name: 'Primitive V1 Redeem',
  'decimals': 18
},
{
  'address': '0xEe8A808C478d14aec57f874351177d80D02ce454',
  'name': 'UMBR',
  #Name: 'UmbriaToken',
  'decimals': 18
},
{
  'address': '0xeEa3311250FE4c3268F8E684f7C87A82fF183Ec1',
  'name': 'ibETHv2',
  #Name: 'Interest Bearing Ether v2',
  'decimals': 8
},
{
  'address': '0xeea6D30798300F4E1d8cd819c8db3B4E6d1e29f6',
  'name': 'URANIUM',
  #Name: 'U',
  'decimals': 18
},
{
  'address': '0xeEAA40B28A2d1b0B08f6f97bB1DD4B75316c6107',
  'name': 'GOVI',
  #Name: 'GOVI',
  'decimals': 18
},
{
  'address': '0xeEE2B2a93Fd890e6373b8758E48Cc523d24Fd337',
  'name': 'GOLD',
  #Name: 'Gold',
  'decimals': 9
},
{
  'address': '0xEeEeeeeEe2aF8D0e1940679860398308e0eF24d6',
  'name': 'ETHV',
  #Name: 'Ethverse Token',
  'decimals': 18
},
{
  'address': '0xEEF9f339514298C6A857EfCfC1A762aF84438dEE',
  'name': 'HEZ',
  #Name: 'Hermez Network Token',
  'decimals': 18
},
{
  'address': '0xEF19F4E48830093Ce5bC8b3Ff7f903A0AE3E9Fa1',
  'name': 'BOTX',
  #Name: 'botXcoin',
  'decimals': 18
},
{
  'address': '0xEF5C6A88710a3C857105058F947D249bc490909D',
  'name': 'wanWASP',
  #Name: 'wanWASP@ethereum',
  'decimals': 18
},
{
  'address': '0xef6344de1fcfC5F48c30234C16c1389e8CdC572C',
  'name': 'DNA',
  #Name: 'DNA',
  'decimals': 18
},
{
  'address': '0xEF69B5697f2Fb0345cC680210fD39b593a2f9684',
  'name': 'MOUTAI',
  #Name: 'MOUTAI',
  'decimals': 18
},
{
  'address': '0xeF9Cd7882c067686691B6fF49e650b43AFBBCC6B',
  'name': 'FNX',
  #Name: 'FinNexus',
  'decimals': 18
},
{
  'address': '0xEfaB7248D36585e2340E5d25F8a8D243E6e3193F',
  'name': 'DACXI',
  #Name: 'DACXI',
  'decimals': 18
},
{
  'address': '0xf057D77Ba8ca6DC51427C1Dfd66dDba0664feD54',
  'name': 'VEGETA',
  #Name: 'VEGETA',
  'decimals': 18
},
{
  'address': '0xF0939011a9bb95c3B791f0cb546377Ed2693a574',
  'name': 'ZERO',
  #Name: 'Zero.Exchange Token',
  'decimals': 18
},
{
  'address': '0xf09A190203D7CAd3Cdb43Ee281e29B947Cb1C16f',
  'name': 'TIDE',
  #Name: 'Tide',
  'decimals': 18
},
{
  'address': '0xf0fE1A87aBf12099b77352BdCc10F5A87067b290',
  'name': 'BONSAI',
  #Name: 'Zenft Garden Society',
  'decimals': 18
},
{
  'address': '0xf121848269B49B97B1EAbcFeceAdC5f701d20e80',
  'name': 'LTE2',
  #Name: 'LEMAONTEA2',
  'decimals': 18
},
{
  'address': '0xf16e81dce15B08F326220742020379B855B87DF9',
  'name': 'ICE',
  #Name: 'IceToken',
  'decimals': 18
},
{
  'address': '0xf188370a51E0713457c8B72C114bC522be348682',
  'name': 'xINCHb',
  #Name: 'xINCH',
  'decimals': 18
},
{
  'address': '0xF18ade29a225fAa555e475eE01F9Eb66eb4a3a74',
  'name': 'PUNK-ZOMBIE',
  #Name: 'Punk-Zombie',
  'decimals': 18
},
{
  'address': '0xF1A9e30FcF023145939D9C56e5c79440c99707b3',
  'name': 'PIC',
  #Name: 'Pichi Coin',
  'decimals': 18
},
{
  'address': '0xF1cA9cb74685755965c7458528A36934Df52A3EF',
  'name': 'AVINOC',
  #Name: 'AVINOC Token',
  'decimals': 18
},
{
  'address': '0xF1d32952E2fbB1a91e620b0FD7fBC8a8879A47f3',
  'name': 'DOGEBEAR',
  #Name: '3X Short Dogecoin Token',
  'decimals': 18
},
{
  'address': '0xF1F85b2C54a2bD284B1cf4141D64fD171Bd85539',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xf21661D0D1d76d3ECb8e1B9F1c923DBfffAe4097',
  'name': 'RIO',
  #Name: 'Realio Network',
  'decimals': 18
},
{
  'address': '0xf29e46887FFAE92f1ff87DfE39713875Da541373',
  'name': 'UNC',
  #Name: 'UniCrypt',
  'decimals': 18
},
{
  'address': '0xf330D59F6755BD3088a6513fcDf2a4B97F802856',
  'name': 'FUNE',
  #Name: 'Future Network',
  'decimals': 18
},
{
  'address': '0xf3504E1ac58E333f013f1595c435C9EbEFd47eDE',
  'name': 'Xii',
  #Name: 'Stable Yield Credit',
  'decimals': 8
},
{
  'address': '0xF3c369c0d3e4E6e784d7881b3b1411F5E7e7d945',
  'name': 'NRC',
  #Name: 'NRC',
  'decimals': 18
},
{
  'address': '0xF3eb8B90C763b8B2B53E7819ac27eca8f94C8Ec2',
  'name': 'ETM',
  #Name: 'ethersmart',
  'decimals': 18
},
{
  'address': '0xF40D9507a7d4850c52a45698c9410e2c345F7A94',
  'name': 'FIDA',
  #Name: 'Bonfida Token',
  'decimals': 6
},
{
  'address': '0xf4fE56FC650d427BeC40225d68B30F4241663039',
  'name': 'IWT',
  #Name: 'Iwan Token',
  'decimals': 18
},
{
  'address': '0xF55a93b613D172b86c2Ba3981a849DaE2aeCDE2f',
  'name': 'YFX',
  #Name: 'YFX',
  'decimals': 18
},
{
  'address': '0xF5D669627376EBd411E34b98F19C868c8ABA5ADA',
  'name': 'AXS',
  #Name: 'Axie Infinity Shard',
  'decimals': 18
},
{
  'address': '0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c',
  'name': 'ENJ',
  #Name: 'Enjin Coin',
  'decimals': 18
},
{
  'address': '0xf65B5C5104c4faFD4b709d9D60a185eAE063276c',
  'name': 'TRU',
  #Name: 'Truebit',
  'decimals': 18
},
{
  'address': '0xf67041758D3B6e56D6fDafA5B32038302C3634DA',
  'name': 'TST',
  #Name: 'TBC Shopping Token',
  'decimals': 18
},
{
  'address': '0xF6b309Cc8b20F4F2693Af31BDd89A3490eBC4b0A',
  'name': 'AKELON',
  #Name: 'Akita Elonita',
  'decimals': 18
},
{
  'address': '0xf6ec87DFE1Ed3a7256Cc0c38e3c8139103e9aF3b',
  'name': 'GENE',
  #Name: 'GeneToken',
  'decimals': 18
},
{
  'address': '0xF71e21475F6Edb497C11125DC0D379291B61540d',
  'name': 'TOPO',
  #Name: 'TopoToken',
  'decimals': 7
},
{
  'address': '0xf7B098298f7C69Fc14610bf71d5e02c60792894C',
  'name': 'GUP',
  #Name: 'Guppy',
  'decimals': 3
},
{
  'address': '0xf7cE65f4dA782f0B601054D2A77F084eEbC37BB7',
  'name': 'MANUP',
  #Name: 'MEN AGAINST NONSENSE DickCrane.Com',
  'decimals': 18
},
{
  'address': '0xF7fae160c6AADb5Df7330E38d96462F60bc24EA9',
  'name': 'KTSCH',
  #Name: 'Kitschy Coin',
  'decimals': 18
},
{
  'address': '0xF88b137cfa667065955ABD17525e89EDCF4D6426',
  'name': '$ITG',
  #Name: 'iTrust Governance Token',
  'decimals': 18
},
{
  'address': '0xf8C3527CC04340b208C854E985240c02F7B7793f',
  'name': 'FRONT',
  #Name: 'Frontier Token',
  'decimals': 18
},
{
  'address': '0xf9209d900f7ad1DC45376a2caA61c78f6dEA53B6',
  'name': 'LIFT',
  #Name: 'LIFT.Kitchen',
  'decimals': 18
},
{
  'address': '0xF94b5C5651c888d928439aB6514B93944eEE6F48',
  'name': 'YLD',
  #Name: 'Yield',
  'decimals': 18
},
{
  'address': '0xF970b8E36e23F7fC3FD752EeA86f8Be8D83375A6',
  'name': 'RCN',
  #Name: 'Ripio Credit Network Token',
  'decimals': 18
},
{
  'address': '0xf99d58e463A2E07e5692127302C20A191861b4D6',
  'name': 'ANY',
  #Name: 'Anyswap',
  'decimals': 18
},
{
  'address': '0xf9C0F6B2b29fC20858935375299aEd1dDE26E50d',
  'name': 'VNYL',
  #Name: 'Vinyl Records',
  'decimals': 18
},
{
  'address': '0xF9F3AEc20B51c04625748007Bb244191ce18b44c',
  'name': 'BGANPUNK',
  #Name: 'BGANPUNK',
  'decimals': 18
},
{
  'address': '0xFA2562da1Bba7B954f26C74725dF51fb62646313',
  'name': 'ASSY',
  #Name: 'ASSY Index',
  'decimals': 18
},
{
  'address': '0xfA5047c9c78B8877af97BDcb85Db743fD7313d4a',
  'name': 'ROOK',
  #Name: 'ROOK',
  'decimals': 18
},
{
  'address': '0xFa898efdB91E35BD311c45b9B955F742b6719aa2',
  'name': 'APED',
  #Name: 'Baddest Alpha Ape Bundle ',
  'decimals': 18
},
{
  'address': '0xfAd45E47083e4607302aa43c65fB3106F1cd7607',
  'name': 'HOGE',
  #Name: 'hoge.finance',
  'decimals': 9
},
{
  'address': '0xfb130d93E49DcA13264344966A611dc79a456Bc5',
  'name': 'DOGEGF',
  #Name: 'DogeGF',
  'decimals': 18
},
{
  'address': '0xFb3cD0B8A5371fe93ef92E3988D30Df7931E2820',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xFbdd194376de19a88118e84E279b977f165d01b8',
  'name': 'BTD',
  #Name: 'Bat True Dollar',
  'decimals': 18
},
{
  'address': '0xfC1E690f61EFd961294b3e1Ce3313fBD8aa4f85d',
  'name': 'aDAI',
  #Name: 'Aave Interest bearing DAI',
  'decimals': 18
},
{
  'address': '0xFca59Cd816aB1eaD66534D82bc21E7515cE441CF',
  'name': 'RARI',
  #Name: 'Rarible',
  'decimals': 18
},
{
  'address': '0xfcfC434ee5BfF924222e084a8876Eee74Ea7cfbA',
  'name': 'DELTA rLP',
  #Name: 'Rebasing Liquidity Token - DELTA.financial',
  'decimals': 18
},
{
  'address': '0xFdb1f2C7a2888BbDCC95845C19b3Dfa4cD3cc6Fd',
  'name': 'PLEB',
  #Name: 'PLEBCOIN',
  'decimals': 18
},
{
  'address': '0xfDcdfA378818AC358739621ddFa8582E6ac1aDcB',
  'name': 'CSC',
  #Name: 'Curio Stable Coin',
  'decimals': 18
},
{
  'address': '0xfE4455fd433Ed3CA025ec7c43cb8686eD89826CD',
  'name': 'MZG',
  #Name: 'MZI GOLD',
  'decimals': 18
},
{
  'address': '0xfe5F141Bf94fE84bC28deD0AB966c16B17490657',
  'name': 'LBA',
  #Name: 'LibraToken',
  'decimals': 18
},
{
  'address': '0xfec0cF7fE078a500abf15F1284958F22049c2C7e',
  'name': 'ART',
  #Name: 'Maecenas ART Token',
  'decimals': 18
},
{
  'address': '0xfF20817765cB7f73d4bde2e66e067E58D11095C2',
  'name': 'AMP',
  #Name: 'Amp',
  'decimals': 18
},
{
  'address': '0xff56Cc6b1E6dEd347aA0B7676C85AB0B3D08B0FA',
  'name': 'ORBS',
  #Name: 'Orbs',
  'decimals': 18
},
{
  'address': '0xFf729170f0C793cc1a28Ea3c30d88c219743D0a6',
  'name': 'ZEUZ',
  #Name: 'ZEUZ',
  'decimals': 18
},
{
  'address': '0xfFffFffF2ba8F66D4e51811C5190992176930278',
  'name': 'COMBO',
  #Name: 'Furucombo',
  'decimals': 18
},
{
  'address': '0x69fa0feE221AD11012BAb0FdB45d444D3D2Ce71c',
  'name': 'XRUNE',
  #Name: 'XRUNE Token',
  'decimals': 18
},
{
  'address': '0x114f1388fAB456c4bA31B1850b244Eedcd024136',
  'name': 'COOL',
  #Name: 'Cool Cats',
  'decimals': 18
},
{
  'address': '0x54cc8F6F1540714788C6ec3593597EbD4Dd9FfF2',
  'name': 'GRAIL',
  #Name: 'GRAIL Governance Token',
  'decimals': 18
},
{
  'address': '0x94d916873B22C9C1b53695f1c002F78537B9b3b2',
  'name': 'AVS',
  #Name: 'AlgoVest',
  'decimals': 18
},
{
  'address': '0xC12C8E8187F86498EF4eD5aE60d56c9E93be3d50',
  'name': 'BABYETH',
  #Name: 'Baby Ethereum',
  'decimals': 18
},
{
  'address': '0xe804964c296E9FB666fBE67767838c1FF9Ab3209',
  'name': 'REETH',
  #Name: 'Reeth Token',
  'decimals': 18
},
{
  'address': '0xe76C6c83af64e4C60245D8C7dE953DF673a7A33D',
  'name': 'RAIL',
  #Name: 'Rail',
  'decimals': 18
},
{
  'address': '0xB018E86097D5663af3510460Aa1a53F2c893A30C',
  'name': 'SCARCE',
  #Name: 'ScarceCoin',
  'decimals': 18
},
{
  'address': '0x1aD40D30BECCBF9A8D28720AD283C1FAEA89bCf3',
  'name': 'PBAGS',
  #Name: 'Monopoly',
  'decimals': 8
},
{
  'address': '0x0521609970A38DcC9D64862037a9B35698b87389',
  'name': 'PUP',
  #Name: 'Pixel Pup',
  'decimals': 18
},
{
  'address': '0x373acdA15Ce392362e4b46ED97a7feEcD7EF9EB8',
  'name': 'SQUIG',
  #Name: 'Squiggle DAO Token',
  'decimals': 4
},
{
  'address': '0xB249C041f24eF035B9DC87C1D87088bcFcC96C8D',
  'name': 'FREED',
  #Name: 'Freedom Token',
  'decimals': 18
},
{
  'address': '0xcabb170c0fABaF1CBC373F00777e46C27BA6a774',
  'name': 'ETH2.0',
  #Name: 'ETHEREUM2.0',
  'decimals': 9
},
{
  'address': '0x496266ff0876262b0177Cef026A117AbC24B2532',
  'name': 'XDL',
  #Name: 'Parity Blockchain Dollar',
  'decimals': 4
},
{
  'address': '0x6B4c7A5e3f0B99FCD83e9c089BDDD6c7FCe5c611',
  'name': 'MM',
  #Name: 'Million',
  'decimals': 18
},
{
  'address': '0xD9F05f145CbcDB68A84E1f90506352337614866d',
  'name': 'DULY',
  #Name: 'Duly',
  'decimals': 18
},
{
  'address': '0x8B3192f5eEBD8579568A2Ed41E6FEB402f93f73F',
  'name': 'SAITAMA',
  #Name: 'Saitama Inu',
  'decimals': 9
},
{
  'address': '0x1F735f84b07cc20E9aC471C291a87b5A2428d518',
  'name': 'DBC',
  #Name: 'Deepbrainchain Token',
  'decimals': 15
},
{
  'address': '0x83B04AF7a77C727273B7a582D6Fda65472FCB3f2',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0x4a220E6096B25EADb88358cb44068A3248254675',
  'name': 'QNT',
  #Name: 'Quant',
  'decimals': 18
},
{
  'address': '0x0cB8D0B37C7487b11d57F1f33dEfA2B1d3cFccfE',
  'name': 'DANK',
  #Name: 'Dank Token',
  'decimals': 18
},
{
  'address': '0xEA47B64e1BFCCb773A0420247C0aa0a3C1D2E5C5',
  'name': 'BAYC',
  #Name: 'Bored Ape Yacht Club',
  'decimals': 18
},
{
  'address': '0xc4d586ef7Be9EBe80bD5eE4FBd228fe2Db5F2C4e',
  'name': 'PHIBA',
  #Name: 'Papa Shiba',
  'decimals': 9
},
{
  'address': '0xB39185e33E8c28e0BB3DbBCe24DA5dEA6379Ae91',
  'name': 'PHUNK',
  #Name: 'CryptoPhunks',
  'decimals': 18
},
{
  'address': '0x010a0288aF52ED61e32674D82bBc7dDBFA9a1324',
  'name': 'OT-aUSDC-30DEC2021',
  #Name: 'OT Aave interest bearing USDC 30DEC2021',
  'decimals': 6
},
{
  'address': '0xE55e3B62005a2035D48aC0C41A5A9c799F04892C',
  'name': 'OT-cDAI-30DEC2021',
  #Name: 'OT Compound Dai 30DEC2021',
  'decimals': 8
},
{
  'address': '0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2',
  'name': 'WTON',
  #Name: 'Wrapped TON',
  'decimals': 27
},
{
  'address': '0xbB4E410D9E30d5a78167798A571606f832bd4024',
  'name': 'ROOx',
  #Name: 'Kangaroo Coin',
  'decimals': 8
},
{
  'address': '0xcd46d92C46be1DbbD5CcC497e95611ABE9D507Bc',
  'name': 'FACE',
  #Name: 'ChainFaces',
  'decimals': 18
},
{
  'address': '0xfe14C65630F6F104BC8043F528dFaCe7C165e8e1',
  'name': 'FAV',
  #Name: 'FAVOR',
  'decimals': 18
},
{
  'address': '0xd23e42A5E8Fe2bD7C0557486Ac1ab57200fFC41F',
  'name': 'ELKA',
  #Name: 'ELKA',
  'decimals': 0
},
{
  'address': '0x3e52A381E08A2410fAa594Af39288C60aD9051c0',
  'name': 'CCV1',
  #Name: 'commoncore-V1',
  'decimals': 18
},
{
  'address': '0x97Aa8e14db0bc073cC7e2d42AC715427717d6042',
  'name': 'SPUNK',
  #Name: 'SPUNKS',
  'decimals': 18
},
{
  'address': '0xc716cf01532999E5dF45E1BD09743128c5932821',
  'name': 'MANEKI',
  #Name: 'Lucky Maneki',
  'decimals': 18
},
{
  'address': '0x4917A9A03bDF9BE520e0b342DA8C3c8787237302',
  'name': 'wanXRP',
  #Name: 'wanXRP@ethereum',
  'decimals': 6
},
{
  'address': '0xcDa16f62A8d3127EA0aebfacB221C1CC41b8e488',
  'name': 'MINUTE',
  #Name: '720 Minutes',
  'decimals': 18
},
{
  'address': '0xcD9b72f6E971026ea8609D2918C7BD02e1653945',
  'name': 'BEAM',
  #Name: 'Light Beams',
  'decimals': 18
},
{
  'address': '0x478e677C0bD24c848bD591Cc5273383DD5F30e4a',
  'name': 'PATH',
  #Name: 'Pathfinders',
  'decimals': 18
},
{
  'address': '0xeb5a8eEFDAE23a815072BF28de8114a825C27876',
  'name': 'HYPER',
  #Name: 'HyperHash',
  'decimals': 18
},
{
  'address': '0xFDE98A3Bf5C7F6336aE4ce1b43148aEab7b7c89A',
  'name': 'ENERGY',
  #Name: 'EnergySculpture',
  'decimals': 18
},
{
  'address': '0x2370f9d504c7a6E775bf6E14B3F12846b594cD53',
  'name': 'JPYC',
  #Name: 'JPY Coin',
  'decimals': 18
},
{
  'address': '0x2F5C3dD519E8a502c48c9FC104Eee64fDFF05F03',
  'name': 'META',
  #Name: 'Meta Bots',
  'decimals': 18
},
{
  'address': '0x16631e53C20Fd2670027C6D53EfE2642929b285C',
  'name': 'pSAFEMOON',
  #Name: 'pTokens SAFEMOON',
  'decimals': 18
},
{
  'address': '0xe944f2B46FCfc9D0E887bBeaad95268D9416d0fD',
  'name': 'BERRY',
  #Name: 'Strawberry.WTF',
  'decimals': 18
},
{
  'address': '0x9813037ee2218799597d83D4a5B6F3b6778218d9',
  'name': 'BONE',
  #Name: 'BONE SHIBASWAP',
  'decimals': 18
},
{
  'address': '0x878CF148ccBb50426043a9AFFe54Ba408221C7fA',
  'name': 'KOMBAT',
  #Name: 'Crypto Kombat Token',
  'decimals': 8
},
{
  'address': '0x45804880De22913dAFE09f4980848ECE6EcbAf78',
  'name': 'PAXG',
  #Name: 'Paxos Gold',
  'decimals': 18
},
{
  'address': '0xDDdddd4301A082e62E84e43F474f044423921918',
  'name': 'DVF',
  #Name: 'DeversiFi Token',
  'decimals': 18
},
{
  'address': '0x4c6e796Bbfe5EB37F9E3E0f66C009C8Bf2A5f428',
  'name': 'FCBTC',
  #Name: 'FC Bitcoin',
  'decimals': 8
},
{
  'address': '0x1Ee01654665303A5Dd2744e30b576941880e3A73',
  'name': 'DFNORM',
  #Name: "Degen'$ Farm Normies",
  'decimals': 18
},
{
  'address': '0xEA6C27d11cCB9306154F87d47dc1405c37242081',
  'name': 'PASTA',
  #Name: 'Spaghettification',
  'decimals': 18
},
{
  'address': '0x3aaDA3e213aBf8529606924d8D1c55CbDc70Bf74',
  'name': 'XMON',
  #Name: 'XMON',
  'decimals': 18
},
{
  'address': '0x1C1C14A6B5074905Ce5d367B0A7E098b58EbFD47',
  'name': 'FEX',
  #Name: 'FidexToken',
  'decimals': 8
},
{
  'address': '0x42259818b665075FBC91D43219bD202666b9e351',
  'name': 'ABRH',
  #Name: 'DRABRHtoken',
  'decimals': 18
},
{
  'address': '0x6443E507F53b526042d0054867A60a4C0409Cb4B',
  'name': 'CNHPD',
  #Name: 'Chainlink NFT Hub Paradise Dimension',
  'decimals': 18
},
{
  'address': '0xDA2C8cF8De7B12A223Dc38a4a125af398F04Ef5f',
  'name': 'eLife',
  #Name: 'eLife',
  'decimals': 9
},
{
  'address': '0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd',
  'name': 'GUSD',
  #Name: 'Gemini dollar',
  'decimals': 2
},
{
  'address': '0x79ebf91e22ee6064a94D10489Dd39Ed0A638FcD7',
  'name': 'CHEESE',
  #Name: 'CheeseFry',
  'decimals': 18
},
{
  'address': '0x2cc71c048A804Da930e28E93F3211dC03c702995',
  'name': 'LPK',
  #Name: 'Kripton',
  'decimals': 8
},
{
  'address': '0xC4A86561cb0b7EA1214904f26E6D50FD357C7986',
  'name': 'CHG',
  #Name: 'Charg Coin',
  'decimals': 18
},
{
  'address': '0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C',
  'name': 'BNT',
  #Name: 'Bancor Network Token',
  'decimals': 18
},
{
  'address': '0x48Fb253446873234F2fEBbF9BdeAA72d9d387f94',
  'name': 'vBNT',
  #Name: 'Bancor Governance Token',
  'decimals': 18
},
{
  'address': '0xd53998C536fc8B59b38aa0b49DBd8170d5Ebf4c2',
  'name': 'PUPS',
  #Name: 'Cryptopups',
  'decimals': 18
},
{
  'address': '0xD4f2249dd6c26446F1413f6d97F14fcaa7792545',
  'name': 'uGMC',
  #Name: 'Genesis MoonCats',
  'decimals': 18
},
{
  'address': '0xCC8Fa225D80b9c7D42F96e9570156c65D6cAAa25',
  'name': 'SLP',
  #Name: 'Smooth Love Potion',
  'decimals': 0
},
{
  'address': '0x3845badAde8e6dFF049820680d1F14bD3903a5d0',
  'name': 'SAND',
  #Name: 'SAND',
  'decimals': 18
},
{
  'address': '0xD1B859c0Dffe24C3cd5502b0F3C6fCf066da1d9a',
  'name': 'LADY',
  #Name: 'Fame Lady Squad',
  'decimals': 18
},
{
  'address': '0xB4EFd85c19999D84251304bDA99E90B92300Bd93',
  'name': 'RPL',
  #Name: 'Rocket Pool',
  'decimals': 18
},
{
  'address': '0x80C62FE4487E1351b47Ba49809EBD60ED085bf52',
  'name': 'CLV',
  #Name: 'Clover',
  'decimals': 18
},
{
  'address': '0x7500b968d6606Ae1437c5f099dCd6367E4A45211',
  'name': 'KIRA',
  #Name: 'KIRA CAVA INU',
  'decimals': 18
},
{
  'address': '0xaA67f24FEA81593d411E1B1f04F6511C8AB73ed3',
  'name': 'HAO',
  #Name: 'Hao',
  'decimals': 18
},
{
  'address': '0xdadA02029134F73aF874640eF351A8Cf85DdADA0',
  'name': 'NODE',
  #Name: 'DAppNode DAO Token',
  'decimals': 18
},
{
  'address': '0x065cC8636A00C007276ED9CB874CD59b89e6609b',
  'name': 'BLL',
  #Name: 'Billion',
  'decimals': 18
},
{
  'address': '0x36b679bd64Ed73DBfd88909cDCB892cB66Bd4CBb',
  'name': 'xMARK',
  #Name: 'Standard',
  'decimals': 9
},
{
  'address': '0xDa007777D86AC6d989cC9f79A73261b3fC5e0DA0',
  'name': 'NODE',
  #Name: 'DAppNode DAO Token',
  'decimals': 18
},
{
  'address': '0xA4e4fF5A3AeA352378a3bFefEf13765130909376',
  'name': 'CLOCK',
  #Name: 'Alien Clock',
  'decimals': 18
},
{
  'address': '0xFFE136de12a2cd95f64ceF9F36414c93e9003959',
  'name': 'DUCK',
  #Name: 'SupDucks',
  'decimals': 18
},
{
  'address': '0x2928A3922C1Ba54c6d23f3430AA5fF04bA8Eb759',
  'name': 'GOON',
  #Name: 'Goblin Goons',
  'decimals': 18
},
{
  'address': '0xc443930Ecd59e55e42Efe976B8a4bA0658f5c50a',
  'name': 'SODIUM',
  #Name: 'My Fucking Pickles',
  'decimals': 18
},
{
  'address': '0x00a9af804dc0b9658c3191cEca4D613EAe9ce5E6',
  'name': 'STX',
  #Name: 'STIX',
  'decimals': 18
},
{
  'address': '0x3A7EdeB1d059c25861bA571a7419f40a83364a86',
  'name': 'PRT',
  #Name: 'Prinster Finance',
  'decimals': 18
},
{
  'address': '0xcFA93536DF928d97036b7fed10776A1382199F4D',
  'name': 'VT',
  #Name: 'VegionToken',
  'decimals': 8
},
{
  'address': '0xdb726152680eCe3c9291f1016f1d36f3995f6941',
  'name': 'MEDIA',
  #Name: 'Media Network Token',
  'decimals': 6
},
{
  'address': '0x78e09c5ec42d505742A52FD10078a57Ea186002a',
  'name': 'TWERKY',
  #Name: 'Twerky Club',
  'decimals': 18
},
{
  'address': '0x5cD56bf2CD394ab185Ba4976FcCB68aE28930252',
  'name': 'ZODIAC',
  #Name: 'Divine Order of the Zodiac',
  'decimals': 18
},
{
  'address': '0x8B7C94bC9ec137D67fbddb203B2814F0F1F9b377',
  'name': 'WHALE',
  #Name: 'Weird Whales',
  'decimals': 18
},
{
  'address': '0x8Dca21C5C8165886Ea1fa800ff9321eC74fDE2c0',
  'name': 'SWC',
  #Name: 'SW Capital',
  'decimals': 18
},
{
  'address': '0xaaAEBE6Fe48E54f431b0C390CfaF0b017d09D42d',
  'name': 'CEL',
  #Name: 'Celsius',
  'decimals': 4
},
{
  'address': '0x515d7E9D75E2b76DB60F8a051Cd890eBa23286Bc',
  'name': 'GDAO',
  #Name: 'Governor',
  'decimals': 18
},
{
  'address': '0x7D74c70120cb34DD1cC0B1fB72493B5Ce4903072',
  'name': 'PXG',
  #Name: 'Pixelglyphs',
  'decimals': 18
},
{
  'address': '0xd2C562cd6CDae7CD97FB51474B15DbCa7886b935',
  'name': 'ROCKS',
  #Name: 'DigiRocks',
  'decimals': 18
},
{
  'address': '0x8808f054454a28c451Db3dE68672B0a964AbD0a9',
  'name': 'PCH',
  #Name: 'PlugCoinCash',
  'decimals': 18
},
{
  'address': '0xD9016A907Dc0ECfA3ca425ab20B6b785B42F2373',
  'name': 'GMEE',
  #Name: 'GAMEE',
  'decimals': 18
},
{
  'address': '0x1C9922314ED1415c95b9FD453c3818fd41867d0B',
  'name': 'TOWER',
  #Name: 'TOWER',
  'decimals': 18
},
{
  'address': '0xc690F7C7FcfFA6a82b79faB7508c466FEfdfc8c5',
  'name': 'LYM',
  #Name: 'Lympo tokens',
  'decimals': 18
},
{
  'address': '0x96E61422b6A9bA0e068B6c5ADd4fFaBC6a4aae27',
  'name': 'ibEUR',
  #Name: 'Iron Bank EUR',
  'decimals': 18
},
{
  'address': '0x163C747DBACBeC87DbBA7C7a8C83DBa50d3ef011',
  'name': 'IDH',
  #Name: 'IDHUS',
  'decimals': 18
},
{
  'address': '0xdffbF528718dA939D9646D3DF23697866209C265',
  'name': 'IAPE',
  #Name: 'InvertedApeClub',
  'decimals': 18
},
{
  'address': '0xf49cc1421FC5fCDb77089A9D7409916eFa100109',
  'name': 'JAEG1',
  #Name: 'Jaeger Set 1 ',
  'decimals': 18
},
{
  'address': '0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf',
  'name': 'PMGT',
  #Name: 'Perth Mint Gold Token',
  'decimals': 5
},
{
  'address': '0xeFe2EadF814179D93651E07607D661D2953cd55f',
  'name': 'GSA',
  #Name: 'Galactic Secret Agency',
  'decimals': 18
},
{
  'address': '0xD91E9a0fEf7C0fa4EBdAF4d0aCF55888949A2a9b',
  'name': 'MCN',
  #Name: 'MCN.VENTURES',
  'decimals': 18
},
{
  'address': '0xD6F7dB7dB116170ecb1c3b35F12c1E693bA70586',
  'name': 'CARD',
  #Name: 'Ether Cards',
  'decimals': 18
},
{
  'address': '0xC7a8B45E184138114E6085C82936A8Db93DD156a',
  'name': 'MASK',
  #Name: 'Hashmasks',
  'decimals': 18
},
{
  'address': '0x15e2c631D1A065De54bEa4C9eaf39E3E3506d969',
  'name': 'CNHSH',
  #Name: 'Chainlink NFT Hub Safe Haven',
  'decimals': 18
},
{
  'address': '0x63Aa9d05C025279F8E963ba784f1254814c1e12b',
  'name': 'SBLAND',
  #Name: 'Sandbox Land Standard',
  'decimals': 18
},
{
  'address': '0x69784fb3c658b3D5426dF28aD1A4b993FCc53747',
  'name': 'CNHHH',
  #Name: 'Chainlink NFT Hub Heavenly Hexagon',
  'decimals': 18
},
{
  'address': '0x96936443150b54cd88C865cD92dfB156881268c7',
  'name': 'ZTest',
  #Name: 'ZTest',
  'decimals': 18
},
{
  'address': '0x69428BB4272e3181dE9E3caB461e19b0131855c8',
  'name': 'SYBC',
  #Name: 'SYBC COIN',
  'decimals': 8
},
{
  'address': '0x7d7470Bc321A60cb11c7989356ad66a161C56628',
  'name': 'ZAP',
  #Name: 'ZAP',
  'decimals': 18
},
{
  'address': '0x749b964F3dd571b177fc6E415A07F62b05047dA4',
  'name': 'LSD',
  #Name: 'Bad Trip',
  'decimals': 18
},
{
  'address': '0x8Fddbcdcab0335034A4Bf4F5A19BaC1832474dba',
  'name': 'AMETHYST',
  #Name: 'Amethyst Dao',
  'decimals': 18
},
{
  'address': '0x36dCffe069a3F2878Fab2A46D81e83D462d0cBF7',
  'name': 'TCFX',
  #Name: 'Tcbcoin',
  'decimals': 18
},
{
  'address': '0xdeFA4e8a7bcBA345F687a2f1456F5Edd9CE97202',
  'name': 'KNC',
  #Name: 'Kyber Network Crystal v2',
  'decimals': 18
},
{
  'address': '0x53e305c27444232eBF6712eE361c4906C5e8058A',
  'name': 'RABBIT',
  #Name: 'Rabbit College Club',
  'decimals': 18
},
{
  'address': '0x9695e0114e12C0d3A3636fAb5A18e6b737529023',
  'name': 'DFYN',
  #Name: 'DFYN Token',
  'decimals': 18
},
{
  'address': '0xF8EB56C7e4e3c885c905A19583bF41644d35AA0a',
  'name': 'PIXLS',
  #Name: 'Pixls',
  'decimals': 18
},
{
  'address': '0xb46C73dc30eC8AB74341CfA822cAC1507B5A3b03',
  'name': 'BNANA',
  #Name: 'BoredBananas',
  'decimals': 18
},
{
  'address': '0xb347132eFf18a3f63426f4988ef626d2CbE274F5',
  'name': 'ibff',
  #Name: 'Iron Bank Fixed Forex',
  'decimals': 18
},
{
  'address': '0xEADA947790CA6bFbEa720b452d8Acad15AbEeA08',
  'name': 'MEGADUNG',
  #Name: 'Degen$ Farm Giga Mega Dung',
  'decimals': 18
},
{
  'address': '0x065C89936546b8b8371401e501C128CC510C0BfC',
  'name': 'AVASPC',
  #Name: 'AVA SPACE SRL',
  'decimals': 18
},
{
  'address': '0xc380bA4F132976D4f21381Cd6EbEFb1Fe4Cacf31',
  'name': 'SBUX',
  #Name: 'Starbuck',
  'decimals': 18
},
{
  'address': '0x07E156DA9F07CB59E220456a362c44c198B9E0fa',
  'name': 'WTF',
  #Name: 'WTF',
  'decimals': 18
},
{
  'address': '0x5c761c1a21637362374204000e383204d347064C',
  'name': 'CHIZ',
  #Name: 'SRSC Chiz Token',
  'decimals': 18
},
{
  'address': '0xb2C62E0A1F5837356e399359eCc34fcC49A02093',
  'name': 'KAMAX',
  #Name: 'KamaGang',
  'decimals': 18
},
{
  'address': '0x62C30556FDE78b3423075758Dc3fb74E2EccBfE4',
  'name': 'CYPHER',
  #Name: 'Cypher City',
  'decimals': 18
},
{
  'address': '0xF887f2aF215F985AE74b80b8FB29e3ed5a238407',
  'name': 'DBS',
  #Name: 'DEEBIES',
  'decimals': 18
},
{
  'address': '0x6Ce848f188dc4feEd490F221e7332FeB7aF00993',
  'name': 'RAT',
  #Name: 'Sewer Rat Social Club',
  'decimals': 18
},
{
  'address': '0x2539c842a35C0b0b70c7b2dC518C5289Fc2228b6',
  'name': 'JOY',
  #Name: 'The Sea of JOY',
  'decimals': 18
},
{
  'address': '0x96fF8715B2f8C769C93244C07b0EdE45bCc54F7B',
  'name': 'AVSTR',
  #Name: 'Avastar Founder #43',
  'decimals': 18
},
{
  'address': '0x08A75dbC7167714CeaC1a8e43a8d643A4EDd625a',
  'name': 'WILD',
  #Name: 'Wild Credit',
  'decimals': 18
},
{
  'address': '0x9Ff4f50efD40C915f7d1476Bf36aCB8908e0C56D',
  'name': 'ABC123',
  #Name: 'Art Blocks Curated Full Set',
  'decimals': 18
},
{
  'address': '0xaf9f549774ecEDbD0966C52f250aCc548D3F36E5',
  'name': 'RFuel',
  #Name: 'Rio Fuel Token',
  'decimals': 18
},
{
  'address': '0x33e70C9EFABDf151f5c674A4ADDC104874980c3f',
  'name': 'BUNNY',
  #Name: 'Genbit Bunnies',
  'decimals': 18
},
{
  'address': '0xf3aa39cC51E145aE992C8340FA22fCFd2d5998F3',
  'name': 'ZOM',
  #Name: 'Zombie',
  'decimals': 18
},
{
  'address': '0x711C16E6BddFF27922B148684122F805f74f4221',
  'name': 'EIP1559',
  #Name: 'Serial #1559 EIP1559 Supporter',
  'decimals': 18
},
{
  'address': '0xF1a7B8384BD785dAA5d3e08840198120848eb5C9',
  'name': 'HDZOM',
  #Name: 'HD Punks flagship Zombie',
  'decimals': 18
},
{
  'address': '0x89A64014d429509CfFdA1AEBc7eB36B9435794BD',
  'name': 'LULZ',
  #Name: 'LULZ',
  'decimals': 18
},
{
  'address': '0xb915f83F5744c3317ADd69f8b2653dd35c25cD26',
  'name': 'MARS',
  #Name: 'Mars Genesis',
  'decimals': 18
},
{
  'address': '0x5E8a5f4B2a24e1Ef33cCd98ef0e4E65624c3AE70',
  'name': 'ADBCA',
  #Name: 'Ask Doctor Bitcoin Cover Art',
  'decimals': 18
},
{
  'address': '0x6d9f52b53cCB1B7B62d4Fb1c0dd3155a4F445B75',
  'name': 'SLHERO',
  #Name: 'TheSingularityHeroes',
  'decimals': 18
},
{
  'address': '0x85F373eF7D3D4c2675e6215242670987e35886e2',
  'name': 'DINO',
  #Name: 'Long Neckie Lady',
  'decimals': 18
},
{
  'address': '0x1aceb72687B62d7FC8589e56A7Db055119d2Ae6c',
  'name': 'CHUM',
  #Name: 'Chum',
  'decimals': 18
},
{
  'address': '0x25f8087EAD173b73D6e8B84329989A8eEA16CF73',
  'name': 'YGG',
  #Name: 'Yield Guild Games Token',
  'decimals': 18
},
{
  'address': '0x72377f31e30a405282b522d588AEbbea202b4f23',
  'name': 'VRN',
  #Name: 'Varen',
  'decimals': 18
},
{
  'address': '0x07bfC92BCc5F2eDCA636a8a5b12D69b60F59795d',
  'name': 'RACE',
  #Name: 'RaceDAO',
  'decimals': 18
},
{
  'address': '0x650F44eD6F1FE0E1417cb4b3115d52494B4D9b6D',
  'name': 'MEOW',
  #Name: 'Meowshi',
  'decimals': 18
},
{
  'address': '0xab58bc75a3A4d2E24d8F67fc618bC18F19840Be4',
  'name': 'RCG',
  #Name: 'RCOIN GLOBAL',
  'decimals': 18
},
{
  'address': '0x2123fC8D0D36fbB1Bd75B30417689d157fe06017',
  'name': 'CHUM',
  #Name: 'Chum',
  'decimals': 18
},
{
  'address': '0x327673aE6B33Bd3d90f0096870059994f30Dc8AF',
  'name': 'LMT',
  #Name: 'Lympo Market Token',
  'decimals': 18
},
{
  'address': '0x00A55375002f3cDa400383F479e7Cd57Bad029A9',
  'name': 'CNJ',
  #Name: 'Conjure',
  'decimals': 18
},
{
  'address': '0x2aF72850c504dDD3c1876C66a914cAee7Ff8a46A',
  'name': 'WHL',
  #Name: 'WhaleRoom',
  'decimals': 18
},
{
  'address': '0x53eE4A83F3576e951e3A21c4ED260073C0A838fB',
  'name': 'BFI',
  #Name: 'New AGA Project Mainnet Prototype',
  'decimals': 9
},
{
  'address': '0x1559FA1b8F28238FD5D76D9f434ad86FD20D1559',
  'name': 'EDEN',
  #Name: 'Eden',
  'decimals': 18
},
{
  'address': '0x6fB3e0A217407EFFf7Ca062D46c26E5d60a14d69',
  'name': 'IOTX',
  #Name: 'IoTeX Network',
  'decimals': 18
},
{
  'address': '0xb29E76BFdf20DFC9721B426Ac91F752A493aB99f',
  'name': '$MAID',
  #Name: 'MaidCoin',
  'decimals': 18
},
{
  'address': '0x5218E472cFCFE0b64A064F055B43b4cdC9EfD3A6',
  'name': 'eRSDL',
  #Name: 'UnFederalReserveToken',
  'decimals': 18
},
{
  'address': '0xaEbfAa45F98b655f85FDd6Df3DC8E9c073a59779',
  'name': 'DUDE',
  #Name: 'thedudes',
  'decimals': 18
},
{
  'address': '0x728eb1D6858910F9eF729586248707A610680019',
  'name': 'JIRO',
  #Name: 'Jiro Inu',
  'decimals': 9
},
{
  'address': '0xed6f3Bc8E502f0ba527dd5303D79F16B3070CBBE',
  'name': 'MECHA',
  #Name: 'Mechazilla',
  'decimals': 18
},
{
  'address': '0xD72B0208101d36deaCa0fEED4f0787BF0ba4C5E6',
  'name': 'USDT',
  #Name: 'Tether USD',
  'decimals': 6
},
{
  'address': '0xa80f2C8f61c56546001f5FC2eb8D6E4e72c45d4C',
  'name': 'UNQT',
  #Name: 'Unique Utility Token',
  'decimals': 18
},
{
  'address': '0x62cF65A6c6A4568820489fACaf659Ba6b878D902',
  'name': 'CHUM',
  #Name: 'Chum',
  'decimals': 18
},
{
  'address': '0x9040e237C3bF18347bb00957Dc22167D0f2b999d',
  'name': 'STND',
  #Name: 'Standard',
  'decimals': 18
},
{
  'address': '0x0AdAD2AF911b156554BcEDB7a9eBA3C6aE951daa',
  'name': 'SNFUB',
  #Name: 'SnelfuBlue',
  'decimals': 6
},
{
  'address': '0xC70E4A4EC2eDb1c12965F3251E51DFC76E749a6c',
  'name': 'IOHK',
  #Name: 'Shirtless Charles',
  'decimals': 18
},
{
  'address': '0x956F47F50A910163D8BF957Cf5846D573E7f87CA',
  'name': 'FEI',
  #Name: 'Fei USD',
  'decimals': 18
},
{
  'address': '0xC7924bF912EBc9B92E3627aed01F816629c7e400',
  'name': 'QAZ',
  #Name: 'QAZ',
  'decimals': 18
},
{
  'address': '0xF8F237D074F637D777bcD2A4712bde793f94272B',
  'name': 'ERC223',
  #Name: 'ERC223',
  'decimals': 10
},
{
  'address': '0xE1Fc4455f62a6E89476f1072530C20CF1A0622dA',
  'name': 'PHTR',
  #Name: 'Phuture',
  'decimals': 18
},
{
  'address': '0x536fC756e3447694bc22c6cC42474641EDeece75',
  'name': 'API4',
  #Name: 'API4',
  'decimals': 18
},
{
  'address': '0x8e2B4badaC15a4ec8c56020f4Ce60faa7558c052',
  'name': 'CNFT',
  #Name: 'Communifty',
  'decimals': 18
},
{
  'address': '0x6B9dd2a8f872Ab0759d9E5208c4d80FD65503864',
  'name': 'API5',
  #Name: 'API5',
  'decimals': 18
},
{
  'address': '0x4304940f12f9740fFCE4124D0e2ec1340cc6F349',
  'name': 'PARALLEL',
  #Name: 'Parallel Alpha',
  'decimals': 18
},
{
  'address': '0xAbeA7663c472648d674bd3403D94C858dFeEF728',
  'name': 'PUDGY',
  #Name: 'Pudgy Penguins',
  'decimals': 18
},
{
  'address': '0x814f583C1978367bFf85285bC5fB668F3d4F0b03',
  'name': 'API5',
  #Name: 'API5',
  'decimals': 18
},
{
  'address': '0xaEdCe4e89671829046e668cbE849C949DF222cf9',
  'name': 'SIS',
  #Name: 'ShibaInuSpace',
  'decimals': 18
},
{
  'address': '0xAE12C5930881c53715B369ceC7606B70d8EB229f',
  'name': 'C98',
  #Name: 'Coin98',
  'decimals': 18
},
{
  'address': '0x656C00e1BcD96f256F224AD9112FF426Ef053733',
  'name': 'EFI',
  #Name: 'Efinity Token',
  'decimals': 18
},
{
  'address': '0x6F585f03F7d2a5a0d00E3d6b873F4b6CcA49F6e2',
  'name': 'KUNGFU',
  #Name: 'KungFu Hero',
  'decimals': 18
},
{
  'address': '0x970A0B8028f6ff85392824f20136DC9Fc56d7488',
  'name': 'ROBOTO',
  #Name: 'Robotos',
  'decimals': 18
},
{
  'address': '0x89020f0D5C5AF4f3407Eb5Fe185416c457B0e93e',
  'name': 'EDN',
  #Name: 'Eden Coin',
  'decimals': 18
},
{
  'address': '0x83D7D7315B918bc002376F73fCD07Ea0708E44eF',
  'name': 'SWEE',
  #Name: 'Swee Token',
  'decimals': 18
},
{
  'address': '0xB431f21561BC6785c579fA1a760087d884854fF4',
  'name': 'HEROES',
  #Name: 'Ethermore',
  'decimals': 18
},
{
  'address': '0x53F10aC913ad108b8DFbEE907A710F92f9b576dd',
  'name': 'DYSTO',
  #Name: 'DystoPunks V2',
  'decimals': 18
},
{
  'address': '0x295FC05d34Fa93E92370C7706043e0705fc6AcaA',
  'name': 'LONDON',
  #Name: "PROOF OF BEAUTY'S $LONDON GIFT",
  'decimals': 18
},
{
  'address': '0xea1F08C0deBD728753b7196d689d065D1B5d5585',
  'name': 'LONDON',
  #Name: "Proof of Beauty's $LONDON Gift",
  'decimals': 18
},
{
  'address': '0x83e031005eCb771B7ff900B3c7B0bDDE7F521c08',
  'name': 'PAINT',
  #Name: 'PaintToken',
  'decimals': 18
},
{
  'address': '0x4Af698B479D0098229DC715655c667Ceb6cd8433',
  'name': '$MAID',
  #Name: 'MaidCoin',
  'decimals': 18
},
{
  'address': '0x2e9d63788249371f1DFC918a52f8d799F4a38C94',
  'name': 'TOKE',
  #Name: 'Tokemak',
  'decimals': 18
},
{
  'address': '0x68CD750E0617Da0777f34a3c5E848a2471460E73',
  'name': 'MEOW',
  #Name: 'CryptoCat',
  'decimals': 18
},
{
  'address': '0x4AA7386Ceb1d61F2665F4AE65af0eFbC1A099A11',
  'name': 'HEA',
  #Name: 'Highest Effort Apes',
  'decimals': 18
},
{
  'address': '0x051218DE982D91C3aF03187Ed3d8A0ddE8231333',
  'name': 'DRIP',
  #Name: 'Nice Drips',
  'decimals': 18
},
{
  'address': '0xEd04915c23f00A313a544955524EB7DBD823143d',
  'name': 'ACH',
  #Name: 'Alchemy',
  'decimals': 8
},
{
  'address': '0x9D7A071E9b919079ba0D5b7381833a54f59fb4b8',
  'name': 'SUZHU',
  #Name: 'Three Arrows Cap ETH Domain',
  'decimals': 18
},
{
  'address': '0x3d3738C698E868A239Fde7EE21e37834c7a1708C',
  'name': 'ZUNK',
  #Name: 'Zunks',
  'decimals': 18
},
{
  'address': '0x01B0B287F784CCd19Cf0A7C11127a70963FD9d30',
  'name': 'PPENG',
  #Name: 'Party Penguins',
  'decimals': 18
},
{
  'address': '0x59c69D3C8786156901a81C708669C1c558832234',
  'name': '$TIARA',
  #Name: 'HOUSE OF TIARA',
  'decimals': 18
},
{
  'address': '0xE105768b1D0144478Aa946f2aB8d5a440055c2E9',
  'name': '$HALLE',
  #Name: 'HOUSE OF HALLE',
  'decimals': 18
},
{
  'address': '0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0',
  'name': 'wstETH',
  #Name: 'Wrapped liquid staked Ether 2.0',
  'decimals': 18
},
{
  'address': '0xD85301D4aB345B901A0Ef369f69f7E6fF06B97A3',
  'name': 'DCMC',
  #Name: 'DCMC',
  'decimals': 12
},
{
  'address': '0x757BC268bd50DA88b2d0cf1966652B18e56CA803',
  'name': 'YAPE',
  #Name: 'Yapeswap DAO Vision Token',
  'decimals': 18
},
{
  'address': '0xc8b76186a4BE8D399C06D9391DA531577f810dc8',
  'name': 'SHIBE',
  #Name: 'Space Shibes Doggy Daycare',
  'decimals': 18
},
{
  'address': '0x3616FD03F11E22942e4Fc01CDd0f1Ca7Cc7BB93d',
  'name': 'BCLS',
  #Name: 'Block Chain Little Sister',
  'decimals': 18
},
{
  'address': '0x0f1181779c22a1670837486e1056112fC776C6F5',
  'name': 'LUCHA',
  #Name: 'Lucha Libre Knockout',
  'decimals': 18
},
{
  'address': '0x32Fb2A84aF5515f77515806EA5aDdB54c923237d',
  'name': 'SOLO',
  #Name: 'SOLOS',
  'decimals': 18
},
{
  'address': '0x3108C33b6Fb38EFEDAeFd8b5f7ca01D5F5c7372d',
  'name': 'yUMA21',
  #Name: 'Yield Dollar UMA 21',
  'decimals': 18
},
{
  'address': '0x0F8Cd97268a49421929E7f1A0eEfbe74Ad8B60dA',
  'name': 'HDPNKR',
  #Name: 'HDPunk ? Roulette ?',
  'decimals': 18
},
{
  'address': '0x5FC28c2FA0BeE55e9837ab8f2257180F0C095C36',
  'name': 'PLANET',
  #Name: 'Procedural Space',
  'decimals': 18
},
{
  'address': '0xA3D970ABC5d4E20a7FC08fe1f18AF41058314a11',
  'name': 'WIENER',
  #Name: 'MOONDOGS ODYSSEY',
  'decimals': 18
},
{
  'address': '0x0DC5189Ec8CDe5732a01F0F592e927B304370551',
  'name': 'ASG',
  #Name: 'Asgard',
  'decimals': 9
},
{
  'address': '0x3a63cCE6952985F58bbd10c4791B6FF1ba93FfFc',
  'name': 'ANIME',
  #Name: 'Animetas',
  'decimals': 18
},
{
  'address': '0xA48D2070472aD4d872d2F5D5893488c763424e09',
  'name': 'HADES',
  #Name: 'Hades',
  'decimals': 9
},
{
  'address': '0x4Fb3CAe84a1264b8BB1911e8915F56660eC8178E',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0x1590ABe3612Be1CB3ab5B0f28874D521576e97Dc',
  'name': 'PIXEL',
  #Name: 'Pixel',
  'decimals': 18
},
{
  'address': '0xc0Dcece6D9A79607a854d42e5bB50A307c060457',
  'name': 'COBI',
  #Name: 'Citizens of Bulliever Island',
  'decimals': 18
},
{
  'address': '0x155ff1A85F440EE0A382eA949f24CE4E0b751c65',
  'name': 'EYE',
  #Name: 'Behodler.io',
  'decimals': 18
},
{
  'address': '0xE581F272706581F9Dcc362dF3C7934E99192c492',
  'name': 'PURR',
  #Name: 'Purrnelopes Country Club',
  'decimals': 18
},
{
  'address': '0x1640BD2898Eee4C36F369836a067deA8725ac0Cc',
  'name': 'DFO',
  #Name: 'DeFiato',
  'decimals': 8
},
{
  'address': '0xead894aAa04B23BC39a3005b79DB86c182a1741B',
  'name': 'BMWU',
  #Name: 'Bored Mummy Waking Up (BMWU)',
  'decimals': 18
},
{
  'address': '0x8bbf1DcCBEdD5c70d8E793d432fB56b848DD1698',
  'name': 'APEIN',
  #Name: 'Ape In',
  'decimals': 18
},
{
  'address': '0x50DE6856358Cc35f3A9a57eAAA34BD4cB707d2cd',
  'name': 'RAZOR',
  #Name: 'RAZOR',
  'decimals': 18
},
{
  'address': '0xdc8C99D7cFb6346b847bFEa9bF5F35bdCd65EcF6',
  'name': 'TRI',
  #Name: 'Triforce',
  'decimals': 18
},
{
  'address': '0x04C5D215401411C4F28e167b3e9E3290d1178CD8',
  'name': 'JYD',
  #Name: 'JunkYard Dogs',
  'decimals': 18
},
{
  'address': '0x1A4b46696b2bB4794Eb3D4c26f1c55F9170fa4C5',
  'name': 'BIT',
  #Name: 'BitDAO',
  'decimals': 18
},
{
  'address': '0xf203Ca1769ca8e9e8FE1DA9D147DB68B6c919817',
  'name': 'WNCG',
  #Name: 'Wrapped NCG',
  'decimals': 18
},
{
  'address': '0x102651c357fC873C236e05177472E77401A783B6',
  'name': 'SIMBA',
  #Name: 'Simba Coin',
  'decimals': 18
},
{
  'address': '0x4dfCa7eB71d9edbE5714652cC7Bd81003Bd2e059',
  'name': 'FROG',
  #Name: 'Sad Frogs District',
  'decimals': 18
},
{
  'address': '0x213d003eCc4750C220795f31DbcEA1fb3BFF67D1',
  'name': 'TROLL',
  #Name: "The Fuckin' Trolls v4",
  'decimals': 18
},
{
  'address': '0xB98217F7F050aad1696467A1559e726381879F33',
  'name': 'WOW',
  #Name: 'World of Women',
  'decimals': 18
},
{
  'address': '0x0aFEE744B6d9fF2B78f76Fe10b3E0199C413Fd34',
  'name': 'SOV',
  #Name: 'Store-Of-Value Token',
  'decimals': 18
},
{
  'address': '0xF34c55B03e4BD6C541786743E9C67ef1abd9EC67',
  'name': 'REIGN',
  #Name: 'Sovreign Governance Token',
  'decimals': 18
},
{
  'address': '0xbF682bd31a615123D28d611b38b0aE3d2b675C2C',
  'name': 'OT-SLP-29DEC2022',
  #Name: 'OT SushiSwap LP Token 29DEC2022',
  'decimals': 18
},
{
  'address': '0x322D6c69048330247165231EB7848A5C80a48878',
  'name': 'OT-SLP-29DEC2022',
  #Name: 'OT SushiSwap LP Token 29DEC2022',
  'decimals': 18
},
{
  'address': '0x398AeA1c9ceb7dE800284bb399A15e0Efe5A9EC2',
  'name': 'sILV',
  #Name: 'Escrowed Illuvium',
  'decimals': 18
},
{
  'address': '0x3f01FA3EBAF10b496630808D4Fa87f82bA40b926',
  'name': 'WAGMI',
  #Name: "We're All Gonna Make It",
  'decimals': 18
},
{
  'address': '0x62786Eeacc9246b4018e0146cb7a3efeACD9459D',
  'name': 'LESS',
  #Name: 'LessToken',
  'decimals': 18
},
{
  'address': '0x8185Bc4757572Da2a610f887561c32298f1A5748',
  'name': 'ALN',
  #Name: 'Aluna',
  'decimals': 18
},
{
  'address': '0xDCaACa96ed63F15E11723da0ACf8639af71C70cE',
  'name': 'WANDER',
  #Name: 'The Wanderers',
  'decimals': 18
},
{
  'address': '0x29DDF2c4F1E80DC9E95CC57a9cA03a28E4aB6D6c',
  'name': 'waLINK',
  #Name: 'Wasabi LINK',
  'decimals': 18
},
{
  'address': '0x17F59DD7fEfC2F276509EeD2Ad6B65271458177E',
  'name': 'REIGN',
  #Name: 'Sovreign Governance Token',
  'decimals': 18
},
{
  'address': '0xba5BDe662c17e2aDFF1075610382B9B691296350',
  'name': 'RARE',
  #Name: 'SuperRare',
  'decimals': 18
},
{
  'address': '0x457B1687a54CEc1ef374A0a13f10b4b4d3A5066b',
  'name': 'HDPNKH',
  #Name: 'HDPunk ?‍? Hoodies ?‍?',
  'decimals': 18
},
{
  'address': '0x622236BB180256B6Ae1a935DaE08dC0356141632',
  'name': 'WRITE',
  #Name: 'Mirror Write Token',
  'decimals': 18
},
{
  'address': '0x064E587292EC7228664F01c218fB7c28a98b2aaf',
  'name': 'NFD',
  #Name: 'NFT Doge',
  'decimals': 6
},
{
  'address': '0x6d3C6f97Ab682914369841295aaCa6178AD7b9Be',
  'name': 'GAINZ',
  #Name: "you wouldn't get it-Ratwell/Gainzy",
  'decimals': 18
},
{
  'address': '0x3A49360098cF9061630211874398EC75704C0595',
  'name': 'SUEX',
  #Name: 'SuniExchange',
  'decimals': 18
},
{
  'address': '0xDFDb7f72c1F195C5951a234e8DB9806EB0635346',
  'name': 'NFD',
  #Name: 'Feisty Doge NFT',
  'decimals': 18
},
{
  'address': '0x9A4F1FB9f4ecaB0d343658c6F1487e65C1Af2EE8',
  'name': 'YGGC',
  #Name: 'Yellow Glasses Guy',
  'decimals': 18
},
{
  'address': '0xCB5ef4bEC8bc378E3763E22e028CCB4b67BB23b8',
  'name': 'DYNO',
  #Name: 'Dyno Friends',
  'decimals': 18
},
{
  'address': '0x64b830a2fcCf31C1dcbbBE119fa15BE4b90288C1',
  'name': 'GENMASK',
  #Name: 'Generative Masks',
  'decimals': 18
},
{
  'address': '0xd98F75b1A3261dab9eEd4956c93F33749027a964',
  'name': 'SHR',
  #Name: 'ShareToken',
  'decimals': 2
},
{
  'address': '0x0c7D5ae016f806603CB1782bEa29AC69471CAb9c',
  'name': 'BFC',
  #Name: 'Bifrost',
  'decimals': 18
},
{
  'address': '0x2791BfD60D232150Bff86b39B7146c0eaAA2BA81',
  'name': 'BiFi',
  #Name: 'BiFi',
  'decimals': 18
},
{
  'address': '0x03ab458634910AaD20eF5f1C8ee96F1D6ac54919',
  'name': 'RAI',
  #Name: 'Rai Reflex Index',
  'decimals': 18
},
{
  'address': '0x33a308f15B87BB2057f1Efb199fD5C70D9eEEb18',
  'name': 'PACE',
  #Name: 'Playing Arts Crypto Edition',
  'decimals': 18
},
{
  'address': '0x72e364F2ABdC788b7E918bc238B21f109Cd634D7',
  'name': 'MVI',
  #Name: 'Metaverse Index',
  'decimals': 18
},
{
  'address': '0xBb59cf6813A56eF9b02EB830F32FA25fb3E3412F',
  'name': 'FREN',
  #Name: 'Non Fungible Frens',
  'decimals': 18
},
{
  'address': '0x30a017C4fce713CEe705270bfbB2CeC2275EB9dF',
  'name': 'HEDZ',
  #Name: 'Astrohedz',
  'decimals': 18
},
{
  'address': '0x2bB2820371ef895444e58F285FAd89B3a86fBf6d',
  'name': 'CPC',
  #Name: 'Cute Pig Club',
  'decimals': 18
},
{
  'address': '0xDF63184545A4168B8f8f307bf9dD615f61b012fa',
  'name': 'CATCTI',
  #Name: 'Catctus',
  'decimals': 18
},
{
  'address': '0x494e5434e6872C83685CE223875b8D489e1779Ff',
  'name': 'SCAT',
  #Name: 'Stray Cats',
  'decimals': 18
},
{
  'address': '0xdac9F64295eB76928e4563d0688bE9048373f13E',
  'name': 'ONI',
  #Name: '0N1 Force',
  'decimals': 18
},
{
  'address': '0x817E2aBbf377261bB3d923A8782693835430bd6d',
  'name': 'EIP',
  #Name: '1559 Supporter',
  'decimals': 18
},
{
  'address': '0xE9744AE7C29c27c4EaF0dBC11e419e28b8A87027',
  'name': 'LAMB',
  #Name: 'Lamb Duhs',
  'decimals': 18
},
{
  'address': '0xEEB588A5C9a630C3028a22e86a28Fec0771Ac113',
  'name': 'FLUF',
  #Name: 'FLUF World ',
  'decimals': 18
},
{
  'address': '0x7752758dAEF71D2e2B75D3B5287bA24296cA41a8',
  'name': 'PEN',
  #Name: 'SELL ME THIS PEN',
  'decimals': 18
},
{
  'address': '0x5637E3cDb52C3FEcD1064027AD10eba06Fa705e5',
  'name': 'SATS',
  #Name: 'Satoshibles',
  'decimals': 18
},
{
  'address': '0xCF7ADa43Dc673c4a2AC66d8122AE25755c089b6A',
  'name': 'USD0x COMP',
  #Name: 'USD0x COMPOUND',
  'decimals': 18
},
{
  'address': '0xBE22eC66710CAa72aB690BF816F8BCe785fbBac2',
  'name': 'AANT',
  #Name: 'Add A New Token',
  'decimals': 8
},
{
  'address': '0xE22c4E46C6f54e72315CA6eDA934e7b766b0173D',
  'name': 'BEXT',
  #Name: 'BYTEDEX',
  'decimals': 18
},
{
  'address': '0x28440E006Cf85A7159e7e97A0A03385C75c47623',
  'name': 'NFS',
  #Name: 'Shiba Inu NFT',
  'decimals': 18
},
{
  'address': '0xce98bc63fD11525b515C597648000d3A1FE06091',
  'name': 'ETHi',
  #Name: 'Ethereum-i',
  'decimals': 9
},
{
  'address': '0x17163D305866c7E02004235ECb3921fd5B5e5d84',
  'name': 'SOUL',
  #Name: 'Lost Souls Sanctuary',
  'decimals': 18
},
{
  'address': '0x1093F8a423e5F79E16968ae13C307572128d1fD5',
  'name': 'HEAVEN',
  #Name: ' Heaven Computer',
  'decimals': 18
},
{
  'address': '0xa76d4fc11346998cb8eD9a3839934555788E23f9',
  'name': 'BRS',
  #Name: 'Brenna Sparks',
  'decimals': 18
},
{
  'address': '0x244eBEb9Fe1eCE439a886fb1F1b143A8bC44De40',
  'name': 'CORGI',
  #Name: 'CryptoCorgis',
  'decimals': 18
},
{
  'address': '0x491D6b7D6822d5d4BC88a1264E1b47791Fd8E904',
  'name': 'LONDON',
  #Name: 'LONDON',
  'decimals': 18
},
{
  'address': '0xb232227680a517469660012E0E9aFeBCf34160ae',
  'name': 'ADMI',
  #Name: 'Admirers',
  'decimals': 18
},
{
  'address': '0x212Ceb1923F5ab3393Ba4d1B8f14761179D07FbA',
  'name': 'FDOGE',
  #Name: "Doge's father",
  'decimals': 18
},
{
  'address': '0x32a7C02e79c4ea1008dD6564b35F131428673c41',
  'name': 'CRU',
  #Name: 'CRUST',
  'decimals': 18
},
{
  'address': '0xfc10b3A8011B00489705EF1Fc00D0e501106cB1D',
  'name': 'uGAS-0921',
  #Name: 'uGAS September 21',
  'decimals': 18
},
{
  'address': '0x09759D67441fFDc8F470f368776368715D32a261',
  'name': 'DOPEST',
  #Name: 'DOPESHIBAS',
  'decimals': 18
},
{
  'address': '0x7198F1C380A6A4841bfEAa9C63991fbD1eCad6b6',
  'name': 'SAM',
  #Name: 'SBF Penguin',
  'decimals': 18
},
{
  'address': '0x54d339cFD8F308D32C2F07f5Dc9dD34AF7753e20',
  'name': 'PBONE',
  #Name: 'Party Bones',
  'decimals': 18
},
{
  'address': '0xf499b7d2C2dA27C023318DCE53050428071079c8',
  'name': 'JANK',
  #Name: 'Janky Heist',
  'decimals': 18
},
{
  'address': '0x68CFb82Eacb9f198d508B514d898a403c449533E',
  'name': 'CMK',
  #Name: 'Credmark',
  'decimals': 18
},
{
  'address': '0xf434Fc315977143c321A07406452a87eC62cB2D9',
  'name': 'CITIES',
  #Name: 'BlockCities',
  'decimals': 18
},
{
  'address': '0x7A98b6aEf8aC099E3deF72B5da3da102C0EbE1A0',
  'name': 'BTCDX',
  #Name: 'Bitcoin Dex',
  'decimals': 18
},
{
  'address': '0x75571a52dE30E2D7160AF134798acFb80CC9C0BE',
  'name': 'WNAV',
  #Name: 'Wrapped Navcoin',
  'decimals': 8
},
{
  'address': '0xEABE46c22A91C953D30606e0482da3f003e95d65',
  'name': 'LSS',
  #Name: 'Lost Souls Sanctuary 9292',
  'decimals': 18
},
{
  'address': '0x61107a409fFFe1965126aa456Af679719695C69C',
  'name': 'UMI',
  #Name: 'UmiToken',
  'decimals': 18
},
{
  'address': '0x313037b0Ec16079347113614A80a2b8224b748fF',
  'name': 'RIVER',
  #Name: 'rivermen-5',
  'decimals': 18
},
{
  'address': '0x3d491407CaE2ab78688E12e961F2eff8B46410f3',
  'name': 'PUNKR',
  #Name: 'CryptoPunk Rekt',
  'decimals': 18
},
{
  'address': '0x9a09EEc78998924C24B287f0576253Ffa9e87C21',
  'name': 'POGGER',
  #Name: 'Space Poggers',
  'decimals': 18
},
{
  'address': '0x616fe98349783f1975361d5EB827ef31f90B47B6',
  'name': 'CUZ',
  #Name: 'COUSIN CRYPTO NFT',
  'decimals': 18
},
{
  'address': '0x0171AbeF8c250195D2C062f60764E95298f2d5cC',
  'name': 'MLB',
  #Name: 'MLB Champions',
  'decimals': 18
},
{
  'address': '0x30e430c030B44c1d7C59E497F5CeE1487CBc9b3C',
  'name': 'BABE',
  #Name: 'MLB Champions',
  'decimals': 18
},
{
  'address': '0x232AFcE9f1b3AAE7cb408e482E847250843DB931',
  'name': 'SHARK',
  #Name: 'Shark DAO',
  'decimals': 18
},
{
  'address': '0xb9E3Fc4a2b30671F4492B426C6c20C29225d91eE',
  'name': 'DUMB',
  #Name: 'RIP "nfts r dumb"',
  'decimals': 18
},
{
  'address': '0x34c4b174C282Ac98e3e849F8dB102e5f413e7fA8',
  'name': 'HEAVEN',
  #Name: 'Heavens Computer',
  'decimals': 18
},
{
  'address': '0x698Ad151125deb394E62154245D6129e9068C483',
  'name': 'SINZ',
  #Name: 'Sinister Gainzy by Ratwell',
  'decimals': 18
},
{
  'address': '0x8689D850CdF3b74A1F6A5eB60302c785B71c2fc7',
  'name': '$CPHX',
  #Name: 'CRYPTO PHOENIX',
  'decimals': 18
},
{
  'address': '0xadd5E881984783dD432F80381Fb52F45B53f3e70',
  'name': 'VITE',
  #Name: 'Vite',
  'decimals': 18
},
{
  'address': '0x2b28e6a90782F970937e17668c6385c32eC3f773',
  'name': 'FAP',
  #Name: 'Fragmented Angry Peach Man',
  'decimals': 18
},
{
  'address': '0x7094b71F08f3Ab06b6592be00599C7F47922A51E',
  'name': 'MLBC',
  #Name: 'MLB Champions',
  'decimals': 18
},
{
  'address': '0x797975416716544795511A93DBB990Ee3Be5F392',
  'name': 'BGAN',
  #Name: 'Suffering Bastard',
  'decimals': 18
},
{
  'address': '0x1a3AAcC4FCEb968de9219691d7B1a63CC6da65E0',
  'name': '911',
  #Name: 'Project Freedom Inc 911',
  'decimals': 18
},
{
  'address': '0x00C2999c8B2AdF4ABC835cc63209533973718eB1',
  'name': 'STATE',
  #Name: 'New World Order',
  'decimals': 18
},
{
  'address': '0x863AD391091aE0e87B850c2BB7bFc7597c79C93f',
  'name': 'CANVAS',
  #Name: 'CanvasToken',
  'decimals': 18
},
{
  'address': '0xe356025459d8222b068C474d50d93933F7316610',
  'name': 'PACEF',
  #Name: 'Playing Arts 52 Card Deck',
  'decimals': 18
},
{
  'address': '0x0f2D719407FdBeFF09D87557AbB7232601FD9F29',
  'name': 'SYN',
  #Name: 'Synapse',
  'decimals': 18
},
{
  'address': '0xBbC3a290C7D2755B48681c87f25F9d7F480aD42f',
  'name': 'REMCO',
  #Name: 'Remittance Token',
  'decimals': 8
},
{
  'address': '0x150b0b96933B75Ce27af8b92441F8fB683bF9739',
  'name': 'GOLD',
  #Name: 'Dragonereum Gold',
  'decimals': 18
},
{
  'address': '0xeb61393503691c6E20EAfD82655B7a94450C3124',
  'name': 'LADY',
  #Name: 'ladypunk',
  'decimals': 18
},
{
  'address': '0xF67F7C4a7E0eC3DeDEc55315b521aa116c1c6D8F',
  'name': 'END#Name',
  #Name: 'Endless #Nameless #171',
  'decimals': 18
},
{
  'address': '0x2cc4E25A51Bba5f406ade5dd3dd01B1590aE9A88',
  'name': 'MUTANT',
  #Name: 'Five Rare 4-Trait Mutants',
  'decimals': 18
},
{
  'address': '0xE2311ae37502105b442bBef831E9b53c5d2e9B3b',
  'name': 'BANANA',
  #Name: 'Banana',
  'decimals': 18
},
{
  'address': '0x1a3414f3242Ebdc3e9Ee94222198a8d5F0C2900D',
  'name': 'DANKPEPE',
  #Name: 'DANKPEPE',
  'decimals': 18
},
{
  'address': '0x898BAD2774EB97cF6b94605677F43b41871410B1',
  'name': 'vETH2',
  #Name: 'validator-Eth2',
  'decimals': 18
},
{
  'address': '0xaF9700FcA16276Cd69c4e35FEecC66D1116826cC',
  'name': 'UPCO2',
  #Name: 'Universal Carbon',
  'decimals': 18
},
{
  'address': '0xA2120b9e674d3fC3875f415A7DF52e382F141225',
  'name': 'ATA',
  #Name: 'Automata',
  'decimals': 18
},
{
  'address': '0x24C19F7101c1731b85F1127EaA0407732E36EcDD',
  'name': 'SGT',
  #Name: 'Sharedstake.finance',
  'decimals': 18
},
{
  'address': '0x06c30962591720e1200b239fa70601381bA301D3',
  'name': 'ORANGE',
  #Name: 'Orange Side Punk #7973',
  'decimals': 18
},
{
  'address': '0x50100005a59A916627481B5443512B8015bCe41E',
  'name': '89SA',
  #Name: '89 seconds Atomized',
  'decimals': 18
},
{
  'address': '0x2847c48b4FD2e7dCAcC00Cb04f555fE8dD10D504',
  'name': 'WXCH',
  #Name: 'Wrapped XCH',
  'decimals': 12
},
{
  'address': '0xE7eaec9Bca79d537539C00C58Ae93117fB7280b9',
  'name': 'dogep',
  #Name: 'Doge Protocol',
  'decimals': 18
},
{
  'address': '0x9F9913853f749b3fE6D6D4e16a1Cc3C1656B6D51',
  'name': 'BITT',
  #Name: 'BITTOKEN',
  'decimals': 18
},
{
  'address': '0xea7Cc765eBC94C4805e3BFf28D7E4aE48D06468A',
  'name': 'PAD',
  #Name: 'NearPad Token',
  'decimals': 18
},
{
  'address': '0x2610F0bFC21EF389fe4D03CFB7De9ac1E6C99D6E',
  'name': 'SKYRIM',
  #Name: 'Skyrim Finance',
  'decimals': 18
},
{
  'address': '0xbaac39eD1f57aDdb6a02f6ca57F478c4fdAa8899',
  'name': 'DOG',
  #Name: 'The Doge NFT',
  'decimals': 18
},
{
  'address': '0xBaAC72D52B0793e3F75f661dDE547D09B6D88899',
  'name': 'DOG',
  #Name: 'The Doge NFT',
  'decimals': 18
},
{
  'address': '0x4B7ee45f30767F36f06F79B32BF1FCa6f726DEda',
  'name': 'eFIL',
  #Name: 'Ethereum Wrapped Filecoin',
  'decimals': 18
},
{
  'address': '0xBAac2B4491727D78D2b78815144570b9f2Fe8899',
  'name': 'DOG',
  #Name: 'The Doge NFT',
  'decimals': 18
},
{
  'address': '0x8e7D2DdE3f1E81d097Cb5EC29d21eA7588833Fe4',
  'name': 'SSS',
  #Name: 'Star Sailor Siblings',
  'decimals': 18
},
{
  'address': '0x32353A6C91143bfd6C7d363B546e62a9A2489A20',
  'name': 'AGLD',
  #Name: 'Adventure Gold',
  'decimals': 18
},
{
  'address': '0xcB84d72e61e383767C4DFEb2d8ff7f4FB89abc6e',
  'name': 'VEGA',
  #Name: 'VEGA',
  'decimals': 18
},
{
  'address': '0x95aA5d2DbD3c16ee3fdea82D5C6EC3E38CE3314f',
  'name': 'PXP',
  #Name: ' PointPay Crypto Banking Token V2 ',
  'decimals': 18
},
{
  'address': '0x1CFb084740B525069E2E074B9b2993248Bb30A7F',
  'name': 'mAGLD',
  #Name: 'MoreAdventureGold',
  'decimals': 18
},
{
  'address': '0xe71946B31Bda22526b2dE702BCA8B457ef85C4F1',
  'name': 'NEURO',
  #Name: 'Neuro Credits',
  'decimals': 18
},
{
  'address': '0xBA05A7ca74610631a1CF4967CD7358f61EBd37e9',
  'name': 'LOVE',
  #Name: 'Love',
  'decimals': 18
},
{
  'address': '0xbA7970f10D9f0531941DcEd1dda7ef3016B24e5b',
  'name': 'BGLD',
  #Name: 'Based Gold',
  'decimals': 18
},
{
  'address': '0x05224BD64eD68082F142F535e8b5c83e751fC956',
  'name': 'NOTHING',
  #Name: 'INVISIBLPEPE Rare Pepe OWN NOTHING',
  'decimals': 18
},
{
  'address': '0x5cE188B44266c7B4bbC67Afa3D16b2eB24eD1065',
  'name': 'UWU',
  #Name: 'uwucrew',
  'decimals': 18
},
{
  'address': '0x350758E4A1256561Fd0EE142dc7e0545F561fADc',
  'name': 'B2U',
  #Name: 'B2U Coin',
  'decimals': 18
},
{
  'address': '0xA15F6e2b82050728d27A2C66223140282C623Ca8',
  'name': 'HIPPO',
  #Name: 'HypeHippos',
  'decimals': 18
},
{
  'address': '0x92D6C1e31e14520e676a687F0a93788B716BEff5',
  'name': 'DYDX',
  #Name: 'dYdX',
  'decimals': 18
},
{
  'address': '0x991266869Bb7ba6F0b9Dc9564b6792264D46FCA9',
  'name': 'AXO',
  #Name: 'Axolittles',
  'decimals': 18
},
{
  'address': '0xA6a5DEEa66550772d4A2D77ecBE0187451A4f19E',
  'name': 'FRAK',
  #Name: 'Fraktal',
  'decimals': 18
},
{
  'address': '0x394Cb37e9E7C5ab5906F3440C53d5DC37d6d7348',
  'name': 'SEC',
  #Name: 'Security',
  'decimals': 18
},
{
  'address': '0xA00055e6EE4D1f4169096EcB682F70cAa8c29987',
  'name': 'WIVA',
  #Name: 'WIVA',
  'decimals': 18
},
{
  'address': '0xbA6B0dbb2bA8dAA8F5D6817946393Aef8D3A4487',
  'name': 'HSF',
  #Name: 'Hillstone.Finance',
  'decimals': 18
},
{
  'address': '0xeBD9dC65C723cAdc0EE4ee5A8013dDd3db98f250',
  'name': 'FANG',
  #Name: 'Fang Gang',
  'decimals': 18
},
{
  'address': '0x8D983cb9388EaC77af0474fA441C4815500Cb7BB',
  'name': 'ATOM',
  #Name: 'Cosmos',
  'decimals': 6
},
{
  'address': '0xae837EacBAE2a6bA166ce0DEd5C72340f212835c',
  'name': 'XPRT',
  #Name: 'Persistence',
  'decimals': 6
},
{
  'address': '0x76C4A2B59523eaE19594c630aAb43288dBB1463f',
  'name': 'IRIS',
  #Name: 'IRISnet',
  'decimals': 6
},
{
  'address': '0xdb85f6685950E285b1E611037BEBe5B34e2B7d78',
  'name': 'WZANO',
  #Name: 'Wrapped Zano',
  'decimals': 18
},
{
  'address': '0xeEE10b3736d5978924f392ED67497cfAE795128B',
  'name': 'REGEN',
  #Name: 'Regen Network',
  'decimals': 6
},
{
  'address': '0x6A55B1105497CE7939349f83cFE8b966845b1eB8',
  'name': 'DGLD',
  #Name: 'Doge Gold',
  'decimals': 18
},
{
  'address': '0xB3A824707E146FcFA583738BBE49D061Fe0d1294',
  'name': 'UNIV',
  #Name: 'Universal Token',
  'decimals': 9
},
{
  'address': '0x8642A849D0dcb7a15a974794668ADcfbe4794B56',
  'name': 'PROS',
  #Name: 'Prosper',
  'decimals': 18
},
{
  'address': '0x4542301FC134Dcb92d8464b050d830415214335E',
  'name': 'RMAFIA',
  #Name: 'Raccoon Mafia',
  'decimals': 18
},
{
  'address': '0xB435EEffE949182AeBe85506EB88D4a0fFeA8f9E',
  'name': 'MGG',
  #Name: 'MUD Guild Game',
  'decimals': 18
},
{
  'address': '0xF4617C7019434Bb103C457286f0494BD9fB9A9af',
  'name': 'WAGML',
  #Name: 'WagmipetLoveMaker',
  'decimals': 18
},
{
  'address': '0x7DD14dD66FF3f7A5FAda8B1AEb950521a455C818',
  'name': 'WATR',
  #Name: 'Water Settlements Token',
  'decimals': 18
},
{
  'address': '0xC727f87871ee12Bbcedd2973746D1Deb7529aaD6',
  'name': 'AKT',
  #Name: 'Akash Network',
  'decimals': 6
},
{
  'address': '0xa16001DD47f505B7B7c5639c710A52209E4e8904',
  'name': 'AVA',
  #Name: 'Alpha Fund',
  'decimals': 18
},
{
  'address': '0x1da4858ad385cc377165A298CC2CE3fce0C5fD31',
  'name': 'CCS',
  #Name: 'Clout address s',
  'decimals': 0
},
{
  'address': '0xDC6A0c32F4AEFC1cbf55c3f2a59adf97edD80F86',
  'name': '1\\0',
  #Name: '1nformation T0ken',
  'decimals': 18
},
{
  'address': '0xC64500DD7B0f1794807e67802F8Abbf5F8Ffb054',
  'name': 'LOCUS',
  #Name: 'Locus Chain',
  'decimals': 18
},
{
  'address': '0xe44fa1E8C1d66DD1aACC28C5a08629998d1a8439',
  'name': 'TOV',
  #Name: 'Tov',
  'decimals': 18
},
{
  'address': '0xaC156a935D8A829D7005B8e1D73540806D7B303F',
  'name': 'GRAVEL',
  #Name: 'GRAVEL',
  'decimals': 18
},
{
  'address': '0x3405A1bd46B85c5C029483FbECf2F3E611026e45',
  'name': 'WOW',
  #Name: 'WOWswap',
  'decimals': 18
},
{
  'address': '0xB14b87790643D2dAB44b06692D37Dd95B4b30E56',
  'name': 'WGK',
  #Name: 'Wrapped Genesis Kongz',
  'decimals': 18
},
{
  'address': '0x13f98F4cC80B32d328cB9802CdF0570aA925BC27',
  'name': 'ETHS',
  #Name: 'Ethereans Official',
  'decimals': 18
},
{
  'address': '0xf3110b27f481F9aC3c1Ba3C54dE542AcCB2D913C',
  'name': 'R64X',
  #Name: 'R64X.com',
  'decimals': 18
},
{
  'address': '0xd1b624f07a4D9B3e3746E33cb58f42dF079b5444',
  'name': 'NKCLC',
  #Name: 'NKCL Classic',
  'decimals': 18
},
{
  'address': '0x9C4A4204B79dd291D6b6571C5BE8BbcD0622F050',
  'name': 'TCR',
  #Name: 'Tracer',
  'decimals': 18
},
{
  'address': '0x1999A92711cF8815B7F6b07bd34B4287d853cFbA',
  'name': 'TOADZ',
  #Name: 'CrypToadz by GREMPLIN',
  'decimals': 18
},
{
  'address': '0xe8e611D56297adBE1c1C0683261bE58e6e4880A2',
  'name': 'BUTT',
  #Name: 'CryptoDickbutts',
  'decimals': 18
},
{
  'address': '0x058bC8Ef040bD3971418E36aA88b64899378CcF4',
  'name': 'DONA',
  #Name: 'DONA',
  'decimals': 18
},
{
  'address': '0x92425a88C18ceD9Cf3a1b9f686e4CeB36E35c7A4',
  'name': 'BMBWU',
  #Name: 'Bored Mummy Baby Waking Up',
  'decimals': 18
},
{
  'address': '0x8f693ca8D21b157107184d29D398A8D082b38b76',
  'name': 'DATA',
  #Name: 'Streamr',
  'decimals': 18
},
{
  'address': '0x60e46a4Dd91D10506D8eFA2caA266E7191fe7Ea8',
  'name': 'FEWGO',
  #Name: 'Fewmans Gold',
  'decimals': 18
},
{
  'address': '0x62550C9c4d5FBa8343752b4c0A37ed6915DA05f0',
  'name': 'CARTEL20',
  #Name: 'CanineCartel',
  'decimals': 18
},
{
  'address': '0xD8C1232FcD219286E341271385bd70601503B3D7',
  'name': 'DOGIRA',
  #Name: 'Dogira',
  'decimals': 9
},
{
  'address': '0x850aAB69f0e0171A9a49dB8BE3E71351c8247Df4',
  'name': 'KONO',
  #Name: 'Konomi',
  'decimals': 18
},
{
  'address': '0x219CAb58Ff00399154410364e8f36cdD38227721',
  'name': 'ROO',
  #Name: 'ROO CREW',
  'decimals': 18
},
{
  'address': '0x55aF5865807b196bD0197e0902746F31FBcCFa58',
  'name': 'BOO',
  #Name: 'SpookyToken',
  'decimals': 18
},
{
  'address': '0x34B6F5Aa05d2Bf9e524D5f0F5fa8ceA6dBef2bCd',
  'name': 'WCKD',
  #Name: 'Wicked',
  'decimals': 18
},
{
  'address': '0x76306F029f8F99EFFE509534037Ba7030999E3CF',
  'name': 'ACR',
  #Name: 'Acreage',
  'decimals': 18
},
{
  'address': '0x6b4d5e9ec2aceA23D4110F4803Da99E25443c5Df',
  'name': 'aKLIMA',
  #Name: 'AlphaKlima',
  'decimals': 18
},
{
  'address': '0x9D16187D7D8A6ADB39D7f373b7e24EA49F97e869',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0x25b539B1C179fbe2af92ABDFDc7E152Cbc97aDdC',
  'name': 'COOOM',
  #Name: 'INCOOOM GENESIS',
  'decimals': 18
},
{
  'address': '0xc016E4b42f80050bbF1D6244C6AdBd0B10fe93C5',
  'name': 'MONSTR',
  #Name: 'Monster Blocks',
  'decimals': 18
},
{
  'address': '0x6DC02164d75651758aC74435806093E421b64605',
  'name': 'WCHI',
  #Name: 'Wrapped CHI',
  'decimals': 8
},
{
  'address': '0xD453D48acA428Fd718bc0E1AD238BFc009EFf1D0',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xbdab72602e9AD40FC6a6852CAf43258113B8F7a5',
  'name': 'eSOV',
  #Name: 'eSOV',
  'decimals': 18
},
{
  'address': '0x9E797872f9b4B520530e59FAFf0fe7f610c44120',
  'name': 'LEM',
  #Name: 'Lockdown Lemmings',
  'decimals': 18
},
{
  'address': '0x84d821F7FbDD595c4C4A50842913e6b1E07d7a53',
  'name': 'BNPL',
  #Name: 'BNPL Pay',
  'decimals': 18
},
{
  'address': '0xbcd2D1F4369eee45E86eb76EBb6ef2D555D9A002',
  'name': 'SKITS',
  #Name: 'Skits',
  'decimals': 0
},
{
  'address': '0xe328d8DAa44B766F8A2e04E0479F6b316C0bf290',
  'name': 'L1',
  #Name: 'GENESIS',
  'decimals': 18
},
{
  'address': '0xB6F9044b544C8b86fcFA410D612336E340945ee9',
  'name': 'FAKE',
  #Name: 'FIM Internet Money',
  'decimals': 18
},
{
  'address': '0x33d63Ba1E57E54779F7dDAeaA7109349344cf5F1',
  'name': 'DATA',
  #Name: 'DATA Economy Index',
  'decimals': 18
},
{
  'address': '0xD5147bc8e386d91Cc5DBE72099DAC6C9b99276F5',
  'name': 'renFIL',
  #Name: 'renFIL',
  'decimals': 18
},
{
  'address': '0x6bE0CC3FA8D72846c6a4Ab15B298a03d295AAdfA',
  'name': 'MAGI',
  #Name: 'Magi Gold',
  'decimals': 18
},
{
  'address': '0xcF9601B2117B6971c75d3c8C7B3E68a876047D9a',
  'name': 'EMT',
  #Name: 'Emanate',
  'decimals': 18
},
{
  'address': '0x9f0f1Be08591AB7d990faf910B38ed5D60e4D5Bf',
  'name': 'MNC',
  #Name: 'MainCoin',
  'decimals': 18
},
{
  'address': '0x7BCe962AAa72d561D71B1a89168d07041249755D',
  'name': 'GLITCH',
  #Name: 'The Glitches',
  'decimals': 18
},
{
  'address': '0xaAe62DAeBf70d4fcF5797b1f93d2BaB90341b7b2',
  'name': 'CHIBI',
  #Name: 'Chibi Apes',
  'decimals': 18
},
{
  'address': '0xf88E8BAD7ee587e8B574EcB5cE2Ce9Ab0A7e6295',
  'name': 'PIL',
  #Name: 'PILL',
  'decimals': 18
},
{
  'address': '0x1e23Fb8Bd851cC2a341428C0B10E65d49987D744',
  'name': 'GCOOOM',
  #Name: 'INCOOOM GENESIS GOLD',
  'decimals': 18
},
{
  'address': '0xe07332FdCf3A8489B752CD86f3FdCD79eE9C373A',
  'name': 'QINDO',
  #Name: 'Qindo Token',
  'decimals': 18
},
{
  'address': '0x4884190C0e2D99AFC1A5fE4D61faAb955d7a4cdf',
  'name': 'DROID',
  #Name: 'AfroDroids',
  'decimals': 18
},
{
  'address': '0x9042195C2D28b0331dfE1e2d75c4AAaF810d2106',
  'name': 'PSS',
  #Name: 'Primate Social Society',
  'decimals': 18
},
{
  'address': '0x2D77f5b3EFA51821aD6483ADAf38EA4cb1824cC5',
  'name': 'MANA',
  #Name: 'Genesis Mana',
  'decimals': 18
},
{
  'address': '0x7c8155909cd385F120A56eF90728dD50F9CcbE52',
  'name': 'NII',
  #Name: 'Nahmii',
  'decimals': 15
},
{
  'address': '0x91dFbEE3965baAEE32784c2d546B7a0C62F268c9',
  'name': 'BONDLY',
  #Name: 'Bondly',
  'decimals': 18
},
{
  'address': '0xc41797d0e9299053d6f5cEBD7CbA48DE97096383',
  'name': 'FINE',
  #Name: 'FineToken',
  'decimals': 18
},
{
  'address': '0x10B47177E92Ef9D5C6059055d92DdF6290848991',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xFE3E6a25e6b192A42a44ecDDCd13796471735ACf',
  'name': 'REEF',
  #Name: 'Reef.finance',
  'decimals': 18
},
{
  'address': '0xF4bdeE03dbE9B0E154d6EB6ec5571E0ec5e2679b',
  'name': 'BRTCV',
  #Name: 'Crypto Venetians',
  'decimals': 18
},
{
  'address': '0x1deA15E1dE3abB5639603738c6edFA7191428CE8',
  'name': 'CAT',
  #Name: 'COOL CAT YELLOW BACKGROUNDS',
  'decimals': 18
},
{
  'address': '0x67d65DA2a678791152d33cDcf92cE3B2Bb2beccd',
  'name': 'RPC',
  #Name: 'Ready Player Cat',
  'decimals': 18
},
{
  'address': '0x67C5870b4A41D4Ebef24d2456547A03F1f3e094B',
  'name': 'G$',
  #Name: 'GoodDollar',
  'decimals': 2
},
{
  'address': '0x0aFeD7d7B0234310c8A22bDc8417701654154c2b',
  'name': 'VOID',
  #Name: 'VOID - Visitors of Imma Degen',
  'decimals': 18
},
{
  'address': '0x65Def5029A0e7591e46B38742bFEdd1Fb7b24436',
  'name': 'KAE',
  #Name: 'Kanpeki',
  'decimals': 18
},
{
  'address': '0x349D15D9AE4b42661BF18d28bbec86995099b8f9',
  'name': 'WATER',
  #Name: 'Water',
  'decimals': 18
},
{
  'address': '0x5d9c1B6F2c865b02bD8f57978CD79Fa7585f0E9b',
  'name': 'ICON',
  #Name: 'Incognito',
  'decimals': 18
},
{
  'address': '0x8e45115181F8a01aCCA317A9af83707649CebfE0',
  'name': 'PCOOOM',
  #Name: 'INCOOOM GENESIS PSYCHEDELIC',
  'decimals': 18
},
{
  'address': '0xE73121298c9b67687F83E07e4426928d1F39bffF',
  'name': '1XRPMRDN',
  #Name: '1x RPEPEARMANDO Sports NFT History',
  'decimals': 18
},
{
  'address': '0x725C263e32c72dDC3A19bEa12C5a0479a81eE688',
  'name': 'BMI',
  #Name: 'Bridge Mutual',
  'decimals': 18
},
{
  'address': '0x2781246fe707bB15CeE3e5ea354e2154a2877B16',
  'name': 'EL',
  #Name: 'ELYSIA',
  'decimals': 18
},
{
  'address': '0xA089eE09941C4459b936980d33796a9Fee31212A',
  'name': 'DIVER',
  #Name: 'DivergenceProtocol',
  'decimals': 18
},
{
  'address': '0xFb782396c9b20E564A64896181c7AC8d8979d5F4',
  'name': 'DIVER',
  #Name: 'DivergenceProtocol',
  'decimals': 18
},
{
  'address': '0x4CF488387F035FF08c371515562CBa712f9015d4',
  'name': 'WPR',
  #Name: 'WePower Token',
  'decimals': 18
},
{
  'address': '0x7F6B4d98789d283622D6B85d0efa3a7928C59B89',
  'name': 'DAOMSTR',
  #Name: 'DAO Masters',
  'decimals': 18
},
{
  'address': '0x44017598f2AF1bD733F9D87b5017b4E7c1B28DDE',
  'name': 'stkATOM',
  #Name: 'pSTAKE Staked ATOM',
  'decimals': 6
},
{
  'address': '0x16CDA4028e9E872a38AcB903176719299beAed87',
  'name': 'MARS4',
  #Name: 'MARS4',
  'decimals': 18
},
{
  'address': '0xB3E17c329ab2F5d32a9d7A0B7356af4EfcD75a5b',
  'name': 'NFB',
  #Name: 'NAH FUNGIBLE BONES',
  'decimals': 18
},
{
  'address': '0xd779eEA9936B4e323cDdff2529eb6F13d0A4d66e',
  'name': 'ENTR',
  #Name: 'ENTER Governance Token',
  'decimals': 18
},
{
  'address': '0xE339ad623217C69Bf00C4D2efD71babA428a863b',
  'name': 'QYU',
  #Name: 'QYUtility',
  'decimals': 18
},
{
  'address': '0x6D13c736BB4F69578E75CcC8E6a6232Fadea668d',
  'name': 'ECO',
  #Name: 'EcosystemNetwork',
  'decimals': 18
},
{
  'address': '0x84e7AE4897B3847B67f212Aff78BFbC5f700aa40',
  'name': 'VBTC',
  #Name: 'Virtual Bitcoin',
  'decimals': 8
},
{
  'address': '0x893700A1a86EE68B92536bf6fd4d3200d7369F7d',
  'name': 'EMT',
  #Name: 'Emanate',
  'decimals': 18
},
{
  'address': '0x6cc6Ba001dbBE18861737467e6C7c71B4992CF42',
  'name': 'TESTDAO',
  #Name: 'testdaoszn42069',
  'decimals': 18
},
{
  'address': '0x85E1927A1424fFB99Eb5e92845f0662372190A09',
  'name': '..',
  #Name: '.',
  'decimals': 18
},
{
  'address': '0xEec2bE5c91ae7f8a338e1e5f3b5DE49d07AfdC81',
  'name': 'DPX',
  #Name: 'Dopex Governance Token',
  'decimals': 18
},
{
  'address': '0x0115bd305885999562D593C94328fE25190dBc90',
  'name': 'ETHGAL',
  #Name: 'EtherGals',
  'decimals': 18
},
{
  'address': '0x71291f53683ECB6908c28d0632f9e211779Ea82E',
  'name': 'FATAL',
  #Name: 'Fatales',
  'decimals': 18
},
{
  'address': '0x332E824e46FcEeB9E59ba9491B80d3e6d42B0B59',
  'name': 'CHEESE',
  #Name: 'CheeseFry',
  'decimals': 18
},
{
  'address': '0xfa62a53D12aFdf618159123E5aD899fdB1574BB4',
  'name': 'FINE',
  #Name: 'FineToken',
  'decimals': 18
},
{
  'address': '0xE3Df5e08b72704C23229cB92fe847B23BfDe9dBd',
  'name': 'uGAS-1221',
  #Name: 'uGAS December 21',
  'decimals': 18
},
{
  'address': '0x37a572b95d3FB5007a3519e73D4e9D6e0fc9De50',
  'name': 'uPUNKS-1221',
  #Name: 'uPUNKS Index Token December 2021',
  'decimals': 18
},
{
  'address': '0xD96e84DDBc7CbE1D73c55B6fe8c64f3a6550deea',
  'name': 'GMAC',
  #Name: 'Gemach',
  'decimals': 18
},
{
  'address': '0xbabB543D300220458f1D5e9a8153cf7f62583D60',
  'name': 'BUN',
  #Name: 'Bad Bunnies',
  'decimals': 18
},
{
  'address': '0x6C16119B20fa52600230F074b349dA3cb861a7e3',
  'name': 'ALK',
  #Name: 'Alkemi_Network_DAO_Token',
  'decimals': 18
},
{
  'address': '0x805a96e740AEDABE738d08de78746C9A801f0f89',
  'name': 'HOOTS',
  #Name: 'CryptoHoots',
  'decimals': 18
},
{
  'address': '0x9C4Cb6b87443cD8D273002257D3e13D1713DF2b7',
  'name': 'DINOS',
  #Name: 'Chibi Dinos',
  'decimals': 18
},
{
  'address': '0xFb91AD82F883Dd912a0d41156e936c01C549cfc2',
  'name': 'LCD',
  #Name: 'Loot Creative Domain',
  'decimals': 18
},
{
  'address': '0x8B202f32762dc8A55b0cE3d1C357AF8BB3173aDa',
  'name': 'GOOB',
  #Name: 'Goobers',
  'decimals': 18
},
{
  'address': '0x81EfA5503C9e71CB0FE938268E266F5bDB028689',
  'name': 'WEOWNS',
  #Name: 'Weownomy',
  'decimals': 8
},
{
  'address': '0x3ebb4A4e91Ad83BE51F8d596533818b246F4bEe1',
  'name': 'SATA',
  #Name: 'Signata',
  'decimals': 18
},
{
  'address': '0x2a7C58e7677c42bf129504eB1B6A931f598AFd55',
  'name': 'SOCKZ',
  #Name: 'Sockz',
  'decimals': 18
},
{
  'address': '0x67979e64584b0E1De0182526BE995260D680ad31',
  'name': 'DAOT',
  #Name: 'DAO Turtles',
  'decimals': 18
},
{
  'address': '0x5c484894fe1AaaE696662943Abc6Cd7Dd50807d3',
  'name': 'GOOP',
  #Name: 'GOOP TROOP',
  'decimals': 18
},
{
  'address': '0x611bc3BE2e96913f2aF7ea97B2746Ba673F44d14',
  'name': 'Pronto',
  #Name: 'Prontotoken',
  'decimals': 18
},
{
  'address': '0x6123B0049F904d730dB3C36a31167D9d4121fA6B',
  'name': 'RBN',
  #Name: 'Ribbon',
  'decimals': 18
},
{
  'address': '0x7560b8B6841294c7a849C8FEEe8bE5164799af72',
  'name': 'NFTRZ',
  #Name: 'NFT RedZone',
  'decimals': 18
},
{
  'address': '0xF708DbE00198D97E083fF77B8F506Be38423Ec99',
  'name': 'ETHI',
  #Name: 'Ethical',
  'decimals': 18
},
{
  'address': '0x0b3B9dCc99F64e6D66C88D053fAe44009b032b3e',
  'name': 'GCG',
  #Name: 'Gutter Cat Gang',
  'decimals': 18
},
{
  'address': '0x73Fa6886E5B641eb4944E44F124bBb41f85Da2Df',
  'name': 'GBIRDS',
  #Name: 'Gutter Pigeons',
  'decimals': 18
},
{
  'address': '0xa79B1dB8907FD89AAf17Cb54fab919BecCfB5254',
  'name': 'GRATS',
  #Name: 'Gutter Rats',
  'decimals': 18
},
{
  'address': '0xbbb95FE8945dcF0886b688417Df2680a22B99Dce',
  'name': 'GDOGS',
  #Name: 'Gutter Dogs',
  'decimals': 18
},
{
  'address': '0xFD2087Bf08Ac28749a605BB3A9b8BCDA3a3151b6',
  'name': 'BEAR',
  #Name: 'Winter Bears',
  'decimals': 18
},
{
  'address': '0x0ba858ACD03bec498d1a99b434E29cE4e0381234',
  'name': 'GAL',
  #Name: 'Outlaw Gals MC',
  'decimals': 18
},
{
  'address': '0xd424fAd6012D473c9bE358471Bf48E345e2F602B',
  'name': 'FAKEREDEEM',
  #Name: 'Fake Redeem Token',
  'decimals': 18
},
{
  'address': '0xE97e496E8494232ee128c1a8cAe0b2B7936f3CaA',
  'name': 'CURIO',
  #Name: 'Curio Cards',
  'decimals': 18
},
{
  'address': '0x0Cf0Ee63788A0849fE5297F3407f701E122cC023',
  'name': 'XDATA',
  #Name: 'Streamr (old)',
  'decimals': 18
},
{
  'address': '0x2604e9f68259e609e8744fB67Cc410D50Fc9AA0F',
  'name': 'FISH',
  #Name: 'FISH Tank',
  'decimals': 18
},
{
  'address': '0x0763fdCCF1aE541A5961815C0872A8c5Bc6DE4d7',
  'name': 'SUKU',
  #Name: 'SUKU',
  'decimals': 18
},
{
  'address': '0x756eC31B40bF9C073f42A304dA244Fc5F9A83522',
  'name': 'BMNT',
  #Name: 'Bitcoin Moon Token',
  'decimals': 18
},
{
  'address': '0xdddD22674a285A58125A4579D2B7FeD1eD4EF8E0',
  'name': 'BMB',
  #Name: 'Bear Market Bears',
  'decimals': 18
},
{
  'address': '0x42C88F19edBd56d7F2b9014163491fDA7B25051d',
  'name': 'AGOS',
  #Name: 'AmeegosOfficialNFT',
  'decimals': 18
},
{
  'address': '0x377e54f25459A3E53D7174A6fC1A0AD4D0090d63',
  'name': 'DRAGON',
  #Name: 'Mighty baby Dragons',
  'decimals': 18
},
{
  'address': '0x1098269bFc70b26DeA43f18F812D2b9854E874bA',
  'name': 'OH-GEEZ',
  #Name: 'Oh..Geez',
  'decimals': 18
},
{
  'address': '0x45e007750Cc74B1D2b4DD7072230278d9602C499',
  'name': 'stkXPRT',
  #Name: 'Persistence Staked XPRT',
  'decimals': 6
},
{
  'address': '0x7A6EdCF89f9b543158bBCa5c8983Cae6CdBB5053',
  'name': 'SEEDS',
  #Name: 'Seeds',
  'decimals': 18
},
{
  'address': '0x76C47b2FB6a73c23c2252Cf7b901e6Be50946DD2',
  'name': 'SSC',
  #Name: 'Super Shiba Club',
  'decimals': 18
},
{
  'address': '0x97872EAfd79940C7b24f7BCc1EADb1457347ADc9',
  'name': 'STRP',
  #Name: 'Strips Token',
  'decimals': 18
},
{
  'address': '0x4C2e59D098DF7b6cBaE0848d66DE2f8A4889b9C3',
  'name': 'FODL',
  #Name: 'Fodl',
  'decimals': 18
},
{
  'address': '0x2BA8349123de45E931a8C8264c332E6e9CF593F9',
  'name': 'BCMC',
  #Name: 'Blockchain Monster Coin',
  'decimals': 18
},
{
  'address': '0xB5e09e6Bf6a5E96934B3fd99a40F7EDACa1173Ed',
  'name': 'DIVINE',
  #Name: 'divinedao',
  'decimals': 18
},
{
  'address': '0x1e33dBA7cd47e79C4385Ba39442A693B910a0A8a',
  'name': 'CELO',
  #Name: 'Celo native asset',
  'decimals': 18
},
{
  'address': '0xf0Ec9df5F03306c19a48Ec4EAa953210536420Df',
  'name': 'TT1',
  #Name: 'TitledTest1',
  'decimals': 18
},
{
  'address': '0x5cd2FAc9702D68dde5a94B1af95962bCFb80fC7d',
  'name': 'RWASTE',
  #Name: 'RadioactiveWaste',
  'decimals': 18
},
{
  'address': '0x31da07eef287E2644Fdb149A9214d4ADA4CfC776',
  'name': 'MHONEY',
  #Name: 'Bear Market Bears',
  'decimals': 18
},
{
  'address': '0x9F042cccE032E22221dFF3Fbc2A470dBea8e2b16',
  'name': 'FLYZ',
  #Name: 'CryptoFlyz',
  'decimals': 18
},
{
  'address': '0xbeBE03D890A535fd2427358EB030996CFe456ED7',
  'name': 'BTPP',
  #Name: 'BUTTPOOP',
  'decimals': 18
},
{
  'address': '0xc13F4F0F865bAc08F62654B57E38669EbC4747a3',
  'name': 'CREDS',
  #Name: 'Creds',
  'decimals': 18
},
{
  'address': '0x53F14f7a32CC0bb3A6ea858881EC2896Ee467BA3',
  'name': 'VERSE',
  #Name: 'Verse Lex',
  'decimals': 18
},
{
  'address': '0xD6a2a6D2F88E29938bb6C8D7146cC7a4306647C1',
  'name': 'SHOOTS',
  #Name: 'Bamboo Shoots',
  'decimals': 18
},
{
  'address': '0xfEE5F54e1070e7eD31Be341e0A5b1E847f6a84Ab',
  'name': 'ZUG',
  #Name: 'ZUG',
  'decimals': 18
},
{
  'address': '0x6418fc669De24cA50a25F7d86Db51569b4F114e7',
  'name': 'JOKER',
  #Name: 'JOKER',
  'decimals': 18
},
{
  'address': '0x7b39917f9562C8Bc83c7a6c2950FF571375D505D',
  'name': 'LEAG',
  #Name: 'LeagueDAO Governance Token',
  'decimals': 18
},
{
  'address': '0xAA2d6A4605aCfA6E0246F04a7BE3293DcC8c44bb',
  'name': 'STRBRY',
  #Name: 'Strawberries',
  'decimals': 18
},
{
  'address': '0x810F86eb43CcAacd401EF50DFab87945A514F9CF',
  'name': 'ATIME',
  #Name: 'Adventure Time',
  'decimals': 18
},
{
  'address': '0xFf5768A0054Eb456140270D0480290A67ec7Ff28',
  'name': 'NTOADZ',
  #Name: 'NinjaToadz',
  'decimals': 18
},
{
  'address': '0xCC72961E7ba4a8F7982594B0B661d3f02dcF239f',
  'name': 'SIMBA',
  #Name: 'Simba Coin',
  'decimals': 18
},
{
  'address': '0x2F131C4DAd4Be81683ABb966b4DE05a549144443',
  'name': 'DOODLE',
  #Name: 'Doodles',
  'decimals': 18
},
{
  'address': '0x7CF1FE11c0F800FF202eB16f973E722879DedF7e',
  'name': 'HORIZON',
  #Name: 'Dark Horizon',
  'decimals': 18
},
{
  'address': '0xC56e2a2455fFb19906ee6BA0CC7d4B9a4cE2c38C',
  'name': 'eCOMP',
  #Name: 'COMP eToken',
  'decimals': 18
},
{
  'address': '0xD7ff7290C83a4B82AcCDf68247e47cF8a1589e51',
  'name': 'dCOMP',
  #Name: 'COMP dToken',
  'decimals': 18
},
{
  'address': '0xdb846f1cD31aCC9a6Db72a1C58dC1760485505f4',
  'name': 'ZCAT',
  #Name: 'ZombieCats Fractional Vault',
  'decimals': 18
},
{
  'address': '0x26D0Ee7d0FAD46b0DEb495Fa09e283151438c102',
  'name': 'STAND',
  #Name: 'TokenStand',
  'decimals': 18
},
{
  'address': '0x9B935A387A6d5D1E153d6caa427cEe7226839ee2',
  'name': 'FMFH',
  #Name: 'Funky Monkey Frat House',
  'decimals': 18
},
{
  'address': '0x3c8D2FCE49906e11e71cB16Fa0fFeB2B16C29638',
  'name': 'NFTL',
  #Name: 'Nifty League',
  'decimals': 18
},
{
  'address': '0x9d3EE6B64e69Ebe12a4bF0b01D031CB80F556eE4',
  'name': 'PECO',
  #Name: 'Wrapped PECO',
  'decimals': 18
},
{
  'address': '0xeBF56B58Be8339A827F9E9Bed5FeAE3A6C63A562',
  'name': 'PIKACHU',
  #Name: 'Pikachu Inu',
  'decimals': 9
},
{
  'address': '0x1900E8B5619a3596745F715d0427Fe617c729BA9',
  'name': 'CBG',
  #Name: 'Chainbing',
  'decimals': 18
},
{
  'address': '0xc3B7dEfDB971999D56588F108ae2590c56e88475',
  'name': 'INVDR',
  #Name: 'Invader',
  'decimals': 18
},
{
  'address': '0x1A84CB84603D045eFC7c09c03C4a179145094927',
  'name': 'XPUNK',
  #Name: 'ExpansionPunks',
  'decimals': 18
},
{
  'address': '0x38bd56aa8125de3da3F0fcc2CAC9bb08597D93db',
  'name': 'THOR',
  #Name: 'THORSwap Token',
  'decimals': 18
},
{
  'address': '0x5A046140d8594369076feec4eE08bD6FEa1Bfe80',
  'name': 'YUM',
  #Name: 'Yum Yums',
  'decimals': 18
},
{
  'address': '0x544c42fBB96B39B21DF61cf322b5EDC285EE7429',
  'name': 'INSUR',
  #Name: 'InsurAce',
  'decimals': 18
},
{
  'address': '0xE7B7Db56482722f641ff05B8eaA5443Da63b4e98',
  'name': 'HYPE',
  #Name: 'HypeBlocks',
  'decimals': 18
},
{
  'address': '0x211bA03e3d6AF08cB0a021Aa695cD9c380f21884',
  'name': 'TENTEN',
  #Name: 'Ten Meta Token',
  'decimals': 9
},
{
  'address': '0x0AfFa06e7Fbe5bC9a764C979aA66E8256A631f02',
  'name': 'PLBT',
  #Name: 'Polybius Token',
  'decimals': 6
},
{
  'address': '0x4fa25D252D442D5949466736D4a634978F61d482',
  'name': 'PACA',
  #Name: 'ALPACADABRAZ',
  'decimals': 18
},
{
  'address': '0x761D38e5ddf6ccf6Cf7c55759d5210750B5D60F3',
  'name': 'ELON',
  #Name: 'Dogelon',
  'decimals': 18
},
{
  'address': '0x19980646f562F052ceAcCC1A26C8d547D9444534',
  'name': 'LOST',
  #Name: 'LOSTBOY',
  'decimals': 18
},
{
  'address': '0x7d647b1A0dcD5525e9C6B3D14BE58f27674f8c95',
  'name': 'BYTES',
  #Name: 'BYTES',
  'decimals': 18
},
{
  'address': '0x210f4A59097c5E10eC67DB9b03cF35332A9aa0Cf',
  'name': 'BOMB',
  #Name: 'Adam Bomb Squad',
  'decimals': 18
},
{
  'address': '0x6725363E565BAA1dda45d492810298ae0b25c4ac',
  'name': 'HEAD',
  #Name: 'Head DAO',
  'decimals': 18
},
{
  'address': '0x9DB9C3C9b729Da52340183B75031Ed6B9b0b535e',
  'name': 'ISLAND',
  #Name: 'Ape Only Island',
  'decimals': 18
},
{
  'address': '0x06A00715E6F92210Af9d7680B584931FAF71A833',
  'name': 'XNL',
  #Name: 'Chronicle',
  'decimals': 18
},
{
  'address': '0x18255f76a9eFd79f39E13C9Da84922946F37e3Ce',
  'name': 'BLOCK',
  #Name: 'Tiles Blocks',
  'decimals': 18
},
{
  'address': '0xD74C61bb1B61Db2459a40126095DEc210346ef90',
  'name': 'PYROINU',
  #Name: 'Pyro Inu',
  'decimals': 18
},
{
  'address': '0x9783B81438C24848f85848f8df31845097341771',
  'name': 'COLLAR',
  #Name: 'DOG COLLAR',
  'decimals': 18
},
{
  'address': '0xbA8A621b4a54e61C442F5Ec623687e2a942225ef',
  'name': 'QUARTZ',
  #Name: 'Sandclock',
  'decimals': 18
},
{
  'address': '0x3f409DA529cc9A1376934F14C5e36cd02c9135A6',
  'name': 'OGC',
  #Name: 'OG:Crystals',
  'decimals': 18
},
{
  'address': '0xB4Ef27a6f63Ffe1e7730af8DCbAB6FEdcF1d12c7',
  'name': 'DTO',
  #Name: 'DotOracle',
  'decimals': 18
},
{
  'address': '0xB57420FaD6731B004309D5a0ec7C6C906Adb8df7',
  'name': 'DTO',
  #Name: 'DotOracle',
  'decimals': 18
},
{
  'address': '0x16ba8Efe847EBDFef99d399902ec29397D403C30',
  'name': 'OH',
  #Name: 'Oh! Finance',
  'decimals': 18
},
{
  'address': '0x8b5728669F1fF5Bd14047d097CCDf0aac1Cb25F7',
  'name': 'ETHOLV',
  #Name: 'Etholvants',
  'decimals': 18
},
{
  'address': '0xDA0c94c73D127eE191955FB46bACd7FF999b2bcd',
  'name': 'STANDARD',
  #Name: 'Stakeborg Standard',
  'decimals': 18
},
{
  'address': '0xAe61EBE4b70f0740C53482413C56B8C924e1A9c3',
  'name': 'dBORING',
  #Name: 'BORING dToken',
  'decimals': 18
},
{
  'address': '0xBC19712FEB3a26080eBf6f2F7849b417FdD792CA',
  'name': 'BORING',
  #Name: 'BoringDAO',
  'decimals': 18
},
{
  'address': '0x06B884e60794Ce02AafAb13791B59A2e6A07442f',
  'name': 'UNBNK',
  #Name: 'Unbanked',
  'decimals': 18
},
{
  'address': '0x04F2694C8fcee23e8Fd0dfEA1d4f5Bb8c352111F',
  'name': 'sOHM',
  #Name: 'Staked Olympus',
  'decimals': 9
},
{
  'address': '0x50326f349787128102852645432AF908C4b34691',
  'name': 'SKELLIE',
  #Name: 'Spectral Skellies',
  'decimals': 18
},
{
  'address': '0xC949204Faf59C8CB7EAfFee2A5b540EA333F6123',
  'name': 'MEGAFLOKIDINGER',
  #Name: 'MEGAFLOKIDINGERDOGE',
  'decimals': 9
},
{
  'address': '0x24DF929F3b8947aCA48622410224129bF25ff844',
  'name': 'SUPERSHIBA',
  #Name: 'SuperShibaFlokiDoge',
  'decimals': 9
},
{
  'address': '0xccC8cb5229B0ac8069C51fd58367Fd1e622aFD97',
  'name': 'GODS',
  #Name: 'Gods Unchained',
  'decimals': 18
},
{
  'address': '0x21ad647b8F4Fe333212e735bfC1F36B4941E6Ad2',
  'name': 'SQUID',
  #Name: 'Squid',
  'decimals': 9
},
{
  'address': '0x47252A63C723889814AeBcAC0683E615624ceC64',
  'name': 'NIL',
  #Name: 'nil',
  'decimals': 18
},
{
  'address': '0x4a9D8B8FCe0B6ec033932B13c4e24d24Dc4113cd',
  'name': 'UDOG',
  #Name: 'United Doge Finance ',
  'decimals': 9
},
{
  'address': '0xca7b3ba66556C4Da2E2A9AFeF9C64F909A59430a',
  'name': 'WOLVERINU',
  #Name: 'WOLVERINU',
  'decimals': 9
},
{
  'address': '0x0dC7d0192c148d7d2D6fa32DC280f953c0AD6A34',
  'name': 'MetaCat',
  #Name: 'MetaCat',
  'decimals': 18
},
{
  'address': '0x6De91d2ebBb2D06EE569f82DC7e27e5088897A03',
  'name': 'MetaFrog',
  #Name: 'MetaFrog',
  'decimals': 9
},
{
  'address': '0x8a6D4C8735371EBAF8874fBd518b56Edd66024eB',
  'name': 'BLOCKS',
  #Name: 'BLOCKS',
  'decimals': 18
},
{
  'address': '0xc276a3d9c5443DE32Fde5b5719763C6Ff7790A10',
  'name': 'FREN',
  #Name: 'DogeFren',
  'decimals': 18
},
{
  'address': '0xE9a950121d839212B6Ab145BB1a819a693ceeFa5',
  'name': 'META by FB',
  #Name: 'META',
  'decimals': 18
},
{
  'address': '0x6226caA1857AFBc6DFB6ca66071Eb241228031A1',
  'name': 'LAR',
  #Name: 'Linkart',
  'decimals': 18
},
{
  'address': '0x0E5F6E67099529557F335be9E2333D90DCE0861b',
  'name': 'RBC',
  #Name: 'RareBunniClub',
  'decimals': 18
},
{
  'address': '0x8d71a64e8c8270116315709f08660360B1BEacf7',
  'name': 'MORPH',
  #Name: 'Morphys',
  'decimals': 18
},
{
  'address': '0xEE35D255120F4BF1D18b3c7eE2e679892A7Fc171',
  'name': 'CCCO',
  #Name: 'CANNABISCASHCOIN',
  'decimals': 18
},
{
  'address': '0x8ab893e33B2CFfF425fF9C67B958036C938A2649',
  'name': 'LLTH',
  #Name: 'Lilith',
  'decimals': 18
},
{
  'address': '0x2C0da41C89AdB5a1d4430E5761b9B400911426B0',
  'name': 'DAMA',
  #Name: 'DAMA Token',
  'decimals': 18
},
{
  'address': '0xc133529e57681b2999708F9458Be5634e293995E',
  'name': 'NAAL',
  #Name: 'Ethernaal',
  'decimals': 18
},
{
  'address': '0x066CdF088C17fF05432A48b08f701f5EB8c3CDF3',
  'name': 'eBORING',
  #Name: 'BORING eToken',
  'decimals': 18
},
{
  'address': '0x034B848caE7639bB93038C6A751C21a7bCF0Ece3',
  'name': 'BABEL',
  #Name: 'BabelFish',
  'decimals': 9
},
{
  'address': '0x0095151377296198241a25A0F36C805b03dE2F12',
  'name': 'FUM',
  #Name: 'The Fumetzu Koin',
  'decimals': 8
},
{
  'address': '0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72',
  'name': 'ENS',
  #Name: 'Ethereum #Name Service',
  'decimals': 18
},
{
  'address': '0x25d4BFeeaE3360E68C466c65A5E8f8D5CEBc5093',
  'name': 'FLESH',
  #Name: 'The Crypt',
  'decimals': 18
},
{
  'address': '0x1Fd154B4d0E3753B714B511a53Fe1fb72dc7AE1C',
  'name': 'SWD',
  #Name: 'SW DAO',
  'decimals': 18
},
{
  'address': '0xC00213E8b450a4CE7AF8892404efBe506f22Ef9F',
  'name': 'CARROTZ',
  #Name: 'Carrotz',
  'decimals': 18
},
{
  'address': '0xF036Ee5A0f68e928BB794730DFc8481a581d9c59',
  'name': 'THI',
  #Name: 'ThibzEC20',
  'decimals': 18
},
{
  'address': '0x47d9E3f2Ddae87ABe831521Cf5A9Eb7b71cCf3Ef',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0x31429d1856aD1377A8A0079410B297e1a9e214c2',
  'name': 'ANGLE',
  #Name: 'ANGLE',
  'decimals': 18
},
{
  'address': '0x72aa40952217bB1AE7b27Ea567207cb10af756E8',
  'name': 'OHMEOW',
  #Name: 'Ohmeow Token',
  'decimals': 9
},
{
  'address': '0xa5f2211B9b8170F694421f2046281775E8468044',
  'name': 'THOR',
  #Name: 'THORSwap Token',
  'decimals': 18
},
{
  'address': '0xF21a813B7847B6e912FB1ee6b4196d6aD4f7350F',
  'name': 'DUST',
  #Name: 'Urbit ID',
  'decimals': 18
},
{
  'address': '0xA4251eA8a5e71d3F10E3Dc224F073bc8a61b4BCd',
  'name': 'FLMTS',
  #Name: 'Filaments',
  'decimals': 18
},
{
  'address': '0xcbbA83a4d3F35D294A26012AC54e9ab6627da018',
  'name': 'ROAR',
  #Name: 'Roar Token',
  'decimals': 18
},
{
  'address': '0xEB3C1F8afF47C5Fb08f4eb813aD04A651Fbf7543',
  'name': 'KINGS',
  #Name: "KING'S GALA",
  'decimals': 18
},
{
  'address': '0x2b5C21578594F7988C7c80D258d0C927C756a848',
  'name': 'NGN',
  #Name: 'Crypto Nijigen',
  'decimals': 10
},
{
  'address': '0x9d1233cc46795E94029fDA81aAaDc1455D510f15',
  'name': 'ZAI',
  #Name: 'Zero Collateral Dai',
  'decimals': 18
},
{
  'address': '0x74d84D49b3b2F5170A82ECAB06cF8629e5239efb',
  'name': 'GENMINT',
  #Name: 'Gen.Art Membership',
  'decimals': 18
},
{
  'address': '0xF57e7e7C23978C3cAEC3C3548E3D615c346e79fF',
  'name': 'IMX',
  #Name: 'Immutable X',
  'decimals': 18
},
{
  'address': '0x9A584ca70FF5fa46c511B7Bd1A953d5a4BFFC3B8',
  'name': 'BUX',
  #Name: 'BuxToken',
  'decimals': 18
},
{
  'address': '0xcA2b663391684A57fb69f4Be1aA8D0DdE927b685',
  'name': 'DEMOHM',
  #Name: 'DemOHMSlayer',
  'decimals': 18
},
{
  'address': '0x23C0024e9D91B45420C94d2c4dc9c1e96EE8Be0D',
  'name': 'PANDA',
  #Name: 'Bamboozlers',
  'decimals': 18
},
{
  'address': '0x0a776842783488E2b4E1277e98C05923874bfA7d',
  'name': 'MEKA',
  #Name: 'MekaVerse',
  'decimals': 18
},
{
  'address': '0x5876ef1e155b8b28935965672cd185849332b77c',
  'name': 'ORCA',
  #Name: 'Orca DeFi Index',
  'decimals': 18
},
{
  'address': '0x438e69A90FEe446b1E4c7fb5B0A3B267D3d3a56A',
  'name': 'KLAYME',
  #Name: 'KLAYME',
  'decimals': 18
},
{
  'address': '0x8503a7b00B4b52692cC6c14e5b96F142E30547b7',
  'name': 'MEED',
  #Name: 'Meeds Token',
  'decimals': 18
},
{
  'address': '0x0De05F6447ab4D22c8827449EE4bA2D5C288379B',
  'name': 'OOKI',
  #Name: 'Ooki Token',
  'decimals': 18
},
{
  'address': '0x22B6C31c2bEB8f2d0d5373146Eed41Ab9eDe3caf',
  'name': 'COC',
  #Name: 'CocktailBar',
  'decimals': 8
},
{
  'address': '0x0110aD3Cf10A6d04993BeC37BDCCBA6EE2C48A27',
  'name': 'TETHERDOOM',
  #Name: 'Tether 3x Short',
  'decimals': 18
},
{
  'address': '0x030ed557a0775e110394C1a543f3eB181AeEa05F',
  'name': 'MKRETHDOOM',
  #Name: 'MKRETH 1x Short',
  'decimals': 18
},
{
  'address': '0xe2D8F9557fD46AD134C8fb5Eabf6f4DA3E0d3f68',
  'name': 'RATIOMOON',
  #Name: 'ETHBTC 2x Long',
  'decimals': 18
},
{
  'address': '0x70cDD88638cB569f1Ae1d4bD3529cc7FB331cbab',
  'name': 'LINKETHMOON',
  #Name: 'LINKETH 2x Long',
  'decimals': 18
},
{
  'address': '0xf9abaeEC0334FD30804446DB7423aBE0c02EF47D',
  'name': 'SHO',
  #Name: 'SHO Token',
  'decimals': 18
},
{
  'address': '0xC03096605F00855A241EB2e746f0b988f9bcBcCF',
  'name': 'PP',
  #Name: 'Peeny',
  'decimals': 18
},
{
  'address': '0x427A03Fb96D9A94A6727fbcfbBA143444090dd64',
  'name': 'PIXL',
  #Name: 'PIXL',
  'decimals': 18
},
{
  'address': '0xC19B6A4Ac7C7Cc24459F08984Bbd09664af17bD1',
  'name': 'SENSO',
  #Name: 'Sensorium',
  'decimals': 0
},
{
  'address': '0x1696d007C0719BF02E37184F2fA2D37BcCD11757',
  'name': 'dSunder',
  #Name: 'Sunder dToken',
  'decimals': 18
},
{
  'address': '0xe9807566F0db49706C392ac2fB195443575dC776',
  'name': 'eSunder',
  #Name: 'Sunder eToken',
  'decimals': 18
},
{
  'address': '0x136209a516D1C2660F045e70634c9d95D64325F9',
  'name': 'SHOW',
  #Name: 'Show Biz',
  'decimals': 18
},
{
  'address': '0x26AB7c9ec873633D03C8f3a828F657878245A2dd',
  'name': 'RATIODOOM',
  #Name: 'ETHBTC 1x Short',
  'decimals': 18
},
{
  'address': '0x9E976F211daea0D652912AB99b0Dc21a7fD728e4',
  'name': 'MAP',
  #Name: 'MAP Protocol',
  'decimals': 18
},
{
  'address': '0x1dB42cEBA6BdEBF86D287e11b159FF97B083b8Af',
  'name': 'GRMTK',
  #Name: 'Gramatik',
  'decimals': 18
},
{
  'address': '0x1a7e4e63778B4f12a199C062f3eFdD288afCBce8',
  'name': 'agEUR',
  #Name: 'agEUR',
  'decimals': 18
},
{
  'address': '0xe45d47ca65982Dd43A8d29Fe35cD67de4629493c',
  'name': 'SUSHIB',
  #Name: 'Sushib Token',
  'decimals': 0
},
{
  'address': '0xb499B5A97bDbC3E117d15B448DAACc9305025689',
  'name': 'YOKAI',
  #Name: 'Yokai Network',
  'decimals': 18
},
{
  'address': '0x24Eb24647786135352cbB14f888B23277F0014e7',
  'name': 'STAR',
  #Name: 'Star',
  'decimals': 18
},
{
  'address': '0xb31eF9e52d94D4120eb44Fe1ddfDe5B4654A6515',
  'name': 'DOSE',
  #Name: 'DOSE',
  'decimals': 18
},
{
  'address': '0x20eC84C46392cB3AE6A7925be92F597FCC7d88F9',
  'name': 'SUPER',
  #Name: 'SuperRare',
  'decimals': 18
},
{
  'address': '0x21585BBcD5bDC3f5737620cf0Db2E51978cf60ac',
  'name': 'MNFST',
  #Name: 'Manifest',
  'decimals': 9
},
{
  'address': '0x68c751ae64E9C786b5b576bCEC63D82755d52143',
  'name': 'WP',
  #Name: 'Well Played',
  'decimals': 9
},
{
  'address': '0x89C259DebB70befcAb1164e7d5f57b81DAd81133',
  'name': 'HAMZ',
  #Name: 'Hamzee',
  'decimals': 18
},
{
  'address': '0x7aC2EE38011E91d68C07Bfd717Cd015F30bB73da',
  'name': 'NPA',
  #Name: 'NPA disposal',
  'decimals': 18
},
{
  'address': '0x00813E3421E1367353BfE7615c7f7f133C89df74',
  'name': 'SPS',
  #Name: 'Splintershards',
  'decimals': 18
},
{
  'address': '0x7F0693074F8064cFbCf9fA6E5A3Fa0e4F58CcCCF',
  'name': 'gm',
  #Name: 'we love gm',
  'decimals': 18
},
{
  'address': '0xA09C0E98a252965a2b6bf2994E2D2c020af0F89a',
  'name': 'SHIBOHM',
  #Name: 'ShibOHM',
  'decimals': 9
},
{
  'address': '0xEe9801669C6138E84bD50dEB500827b776777d28',
  'name': 'O3',
  #Name: 'O3 Swap Token',
  'decimals': 18
},
{
  'address': '0xf474E526ADe9aD2CC2B66ffCE528B1A51B91FCdC',
  'name': 'LEVX',
  #Name: 'LevX DAŌh..Geez',
  'decimals': 18
},
{
  'address': '0xD7f6B167414593eF9D5a248CE6622dF9531f67dC',
  'name': 'FOOD',
  #Name: 'Delectables by Foodmasku',
  'decimals': 18
},
{
  'address': '0xc50EF449171a51FbeAFd7c562b064B6471C36caA',
  'name': 'ZINU',
  #Name: 'Zombie Inu',
  'decimals': 9
},
{
  'address': '0x55332170Cb7d36545B500f66a80291C83d40Bba7',
  'name': 'LFG',
  #Name: 'Lets Fucking GO!',
  'decimals': 9
},
{
  'address': '0xBA3DC9c2cF1C666Cf991BFBbeF77BB5f9C7F93B5',
  'name': 'CATOHM',
  #Name: 'Catohm - t.me/CatOhmEth',
  'decimals': 18
},
{
  'address': '0x9257fb8fab616867cEe67C3289547403617B1938',
  'name': 'DRINK',
  #Name: 'Beverage Token',
  'decimals': 18
},
{
  'address': '0x9E32b13ce7f2E80A01932B42553652E053D6ed8e',
  'name': 'Metis',
  #Name: 'Metis Token',
  'decimals': 18
},
{
  'address': '0x462d6F921C9CD59C0F77E63d5226e35eBf37949B',
  'name': 'WGMI',
  #Name: 'GM WGMI',
  'decimals': 6
},
{
  'address': '0xC793BD771d49B2dE823005F2B98bDD43d8765E9c',
  'name': 'DOMI',
  #Name: 'Domino',
  'decimals': 18
},
{
  'address': '0xCa76543Cf381ebBB277bE79574059e32108e3E65',
  'name': 'wsOHM',
  #Name: 'Wrapped sOHM',
  'decimals': 18
},
{
  'address': '0xEd1480d12bE41d92F36f5f7bDd88212E381A3677',
  'name': 'FDT',
  #Name: 'FIAT DAO Token',
  'decimals': 18
},
{
  'address': '0x46101FBe580940C7DD2D2879662bC98954B5edd1',
  'name': 'ROOT',
  #Name: 'ROOT',
  'decimals': 18
},
{
  'address': '0x7697B462A7c4Ff5F8b55BDBC2F4076c2aF9cF51A',
  'name': 'SARCO',
  #Name: 'Sarcophagus',
  'decimals': 18
},
{
  'address': '0xcAfE001067cDEF266AfB7Eb5A286dCFD277f3dE5',
  'name': 'PSP',
  #Name: 'ParaSwap',
  'decimals': 18
},
{
  'address': '0x4AA15e87aFa6740fE8E2472dA142584da5189bE4',
  'name': 'VITA',
  #Name: 'VitaFruits',
  'decimals': 18
},
{
  'address': '0xDd785d61AA140Afaa7c4c69166b4eC1C09D8f37c',
  'name': 'ALPIES',
  #Name: 'Dreamer Alpies',
  'decimals': 18
},
{
  'address': '0xFF7e285b87e7F9247f0953cf8CF5cB24eeDe4B9C',
  'name': 'STIMMY',
  #Name: 'STIMMY',
  'decimals': 18
},
{
  'address': '0x8a854288a5976036A725879164Ca3e91d30c6A1B',
  'name': 'GET',
  #Name: 'GET',
  'decimals': 18
},
{
  'address': '0xBcC776f9E50B766eD8cFE0b7698b798592c22F61',
  'name': 'PHZE',
  #Name: 'PHZE Coin',
  'decimals': 18
},
{
  'address': '0x52d87F22192131636F93c5AB18d0127Ea52CB641',
  'name': 'renLUNA',
  #Name: 'renLUNA',
  'decimals': 6
},
{
  'address': '0x72B886d09C117654aB7dA13A14d603001dE0B777',
  'name': 'XDEFI',
  #Name: 'XDEFI',
  'decimals': 18
},
{
  'address': '0x70a314daF0f23adc4a5166d77D14b4b0fe08caaB',
  'name': 'SKULL',
  #Name: 'Skullx',
  'decimals': 18
},
{
  'address': '0x92637DF9Cb3dFF55c3e193bC49073dB7D3e1d5aA',
  'name': 'BB',
  #Name: 'BitcoinBillionaires',
  'decimals': 18
},
{
  'address': '0xD96e64205C261eD36bB15b424BFeC58c2A5510d4',
  'name': 'SINS',
  #Name: 'SINS Token',
  'decimals': 18
},
{
  'address': '0x159C351745Fa9642B0785f2dDa15a785445eA935',
  'name': 'YCAT',
  #Name: 'SYNDICAT',
  'decimals': 18
},
{
  'address': '0x72B89605Ac528bb6037fD00dd2567b134355b777',
  'name': 'XDEFI',
  #Name: 'XDEFI',
  'decimals': 18
},
{
  'address': '0x72B819A6650880647E0F76335461Af9dBbE2B777',
  'name': 'XDEFI',
  #Name: 'XDEFI',
  'decimals': 18
},
{
  'address': '0x7162469321ae5880F077D250B626F3271b21b903',
  'name': 'KSW',
  #Name: 'KillSwitchToken',
  'decimals': 18
},
{
  'address': '0x4D71046Fe3B35d605c4FA9f109Da4BAd7771eF7A',
  'name': 'SUS',
  #Name: 'SUS Token',
  'decimals': 18
},
{
  'address': '0x7825e833D495F3d1c28872415a4aee339D26AC88',
  'name': 'TLOS',
  #Name: 'pTokens TLOS',
  'decimals': 18
},
{
  'address': '0x6330E5E49022D0B424a612bFb539F99A24f1c41D',
  'name': 'DAWG',
  #Name: 'Dawgsta',
  'decimals': 9
},
{
  'address': '0x17fddC43cCD46b9bb4ecaeEEc95A02fA8F7Dcffb',
  'name': 'MAIQ',
  #Name: 'MAIQCoin',
  'decimals': 8
},
{
  'address': '0x01597E397605Bf280674Bf292623460b4204C375',
  'name': 'BENT',
  #Name: 'Bent Token',
  'decimals': 18
},
{
  'address': '0x1E309227469ee1164a92232738DA9d24d48e7dAe',
  'name': 'TST',
  #Name: 'test',
  'decimals': 18
},
{
  'address': '0x6100dd79fCAA88420750DceE3F735d168aBcB771',
  'name': 'OS',
  #Name: 'Ethereans',
  'decimals': 18
},
{
  'address': '0xe3Cb486f3f5C639e98cCBaF57d95369375687F80',
  'name': 'renDGB',
  #Name: 'renDGB',
  'decimals': 8
},
{
  'address': '0xEeE972C4e7c425FB15DDCAf0f973B903446E74D7',
  'name': 'EARLY',
  #Name: 'Fractional Early Adopter',
  'decimals': 18
},
{
  'address': '0x64Bc251b0EB9200948C9155573Cd459C5E17C6a4',
  'name': 'SIPLEAN',
  #Name: 'Leancoin',
  'decimals': 18
},
{
  'address': '0x8355DBE8B0e275ABAd27eB843F3eaF3FC855e525',
  'name': 'WOOL',
  #Name: 'WOOL',
  'decimals': 18
},
{
  'address': '0x9cF77be84214beb066F26a4ea1c38ddcc2AFbcf7',
  'name': 'MSHIBA',
  #Name: 'Meta Shiba',
  'decimals': 18
},
{
  'address': '0x5b1D655C93185b06B00f7925791106132Cb3ad75',
  'name': 'DMT',
  #Name: 'DarkMatter',
  'decimals': 18
},
{
  'address': '0x86ed939B500E121C0C5f493F399084Db596dAd20',
  'name': 'SPC',
  #Name: 'SpaceChainV2',
  'decimals': 18
},
{
  'address': '0x48C3399719B582dD63eB5AADf12A40B4C3f52FA2',
  'name': 'SWISE',
  #Name: 'StakeWise',
  'decimals': 18
},
{
  'address': '0xFe2e637202056d30016725477c5da089Ab0A043A',
  'name': 'sETH2',
  #Name: 'StakeWise Staked ETH2',
  'decimals': 18
},
{
  'address': '0x382619212cFEc22E2320F1fC27905Fc54C8f8f23',
  'name': 'AAOR',
  #Name: 'Abu Alumni Oriole',
  'decimals': 18
},
{
  'address': '0x8715cA97c5B464C1957ceFBD18015b5567e52060',
  'name': 'SNOOP',
  #Name: 'Snoop DAO',
  'decimals': 9
},
{
  'address': '0xb5585AfEBBb9D955Da797845B3E0c41B3fF047ce',
  'name': 'Hi',
  #Name: 'Hi',
  'decimals': 18
},
{
  'address': '0xEDB171C18cE90B633DB442f2A6F72874093b49Ef',
  'name': 'WAMPL',
  #Name: 'Wrapped Ampleforth',
  'decimals': 18
},
{
  'address': '0x2Ca1803b5eB52c2AFf90cb2801DDA3CcAD49F64c',
  'name': 'BRAINZ',
  #Name: 'Brainz',
  'decimals': 18
},
{
  'address': '0x5f944B0c4315Cb7c3a846b025AB4045da44abf6c',
  'name': 'GCAKE',
  #Name: 'PANCAKE GAMES',
  'decimals': 18
},
{
  'address': '0x6BD599a8b945074a375bF6BdbB7AbE3126603Cb6',
  'name': 'COMMA',
  #Name: 'Incooom Index',
  'decimals': 18
},
{
  'address': '0xDEc41Db0c33F3F6f3cb615449C311ba22D418A8d',
  'name': 'LOBI',
  #Name: 'Lobi',
  'decimals': 9
},
{
  'address': '0xDA9FDAb21bC4A5811134A6E0Ba6CA06624e67c07',
  'name': 'QUIDD',
  #Name: 'QUIDD',
  'decimals': 18
},
{
  'address': '0x328E56AE02A7207a911d1c94748025202a2379a4',
  'name': 'WAGMINU',
  #Name: 'WAGMI INU',
  'decimals': 18
},
{
  'address': '0xDe5eA375FFBDc8b25a80fe13D631E8Ba0AB4BB02',
  'name': 'GERA',
  #Name: 'Gera',
  'decimals': 18
},
{
  'address': '0xE58Eb0Bb13a71d7B95c4C3cBE6Cb3DBb08f9cBFB',
  'name': 'GNOME',
  #Name: 'GenomesDAO Governance',
  'decimals': 18
},
{
  'address': '0x21413c119b0C11C5d96aE1bD328917bC5C8ED67E',
  'name': 'GENE',
  #Name: 'GenomesDAO',
  'decimals': 18
},
{
  'address': '0x4eE4f96838454E67Fce92B2c53b0f1a97D047179',
  'name': 'MBBT',
  #Name: 'meebitsdaopool',
  'decimals': 18
},
{
  'address': '0x13aa5c2A696a2803BD2879Df3942250A9D616e31',
  'name': 'META',
  #Name: 'meta.com',
  'decimals': 18
},
{
  'address': '0x410e731c2970Dce3AdD351064AcF5cE9E33FDBf0',
  'name': 'ONIT',
  #Name: 'Onbuff Token',
  'decimals': 18
},
{
  'address': '0xE594Fd3c8744b000D8F59d7b91E2C3D33D7E21DB',
  'name': 'ZARDOZ',
  #Name: 'ZARDOZ',
  'decimals': 18
},
{
  'address': '0x469861BDfd02E7ebCE7CdEb281e8EEC53069cf5f',
  'name': 'XFL',
  #Name: 'Flame',
  'decimals': 18
},
{
  'address': '0xAF92F11FAEc382a7949710DdC0D4cAAaa39Cb4F9',
  'name': 'A&B',
  #Name: 'A&BCoin',
  'decimals': 18
},
{
  'address': '0x226dE3151531AD8f6e4f6BEBb1Bd010bA25436fc',
  'name': 'FUR',
  #Name: 'Fur',
  'decimals': 0
},
{
  'address': '0x0405B21BC88aF1Fa4f7Ac9cC311Da0748CA8f31E',
  'name': 'XBMF',
  #Name: 'xBMF',
  'decimals': 18
},
{
  'address': '0xF422B6f41a14Fb74b21CB95a8d82971a3b527117',
  'name': 'SALMON',
  #Name: 'SALMON',
  'decimals': 18
},
{
  'address': '0xe2DA716381d7E0032CECaA5046b34223fC3f218D',
  'name': 'CUT',
  #Name: 'Carbon Utility Token',
  'decimals': 5
},
{
  'address': '0x9Da242c3fed08b643DC0D94d01B7aC200931749A',
  'name': 'TREASURE',
  #Name: 'TREASURE',
  'decimals': 18
},
{
  'address': '0x065A78026EBA5A3d32C033384246d5B49E531B18',
  'name': 'RGC',
  #Name: 'Rare Ghost Club',
  'decimals': 18
},
{
  'address': '0x056187e89d8A22cDa88698a75448Aa8ff8a5Bda4',
  'name': 'UNCOOL',
  #Name: 'Uncool Cats',
  'decimals': 18
},
{
  'address': '0x31c2415c946928e9FD1Af83cdFA38d3eDBD4326f',
  'name': 'UMAD',
  #Name: 'UMAD',
  'decimals': 8
},
{
  'address': '0x1BBf25e71EC48B84d773809B4bA55B6F4bE946Fb',
  'name': 'VOW',
  #Name: 'Vow',
  'decimals': 18
},
{
  'address': '0x40615B82999b8aa46803F11493BeDAB0314EB5E7',
  'name': 'HONEYD',
  #Name: 'Honey Deluxe Token',
  'decimals': 18
},
{
  'address': '0x0ab87046fBb341D058F17CBC4c1133F25a20a52f',
  'name': 'gOHM',
  #Name: 'Governance OHM',
  'decimals': 18
},
{
  'address': '0x501acE9c35E60f03A2af4d484f49F9B1EFde9f40',
  'name': 'SOLACE',
  #Name: 'solace',
  'decimals': 18
},
{
  'address': '0xa1fF4Ee88b53124b73eE16b315F61623CDacc987',
  'name': 'EL69',
  #Name: 'Element 69',
  'decimals': 18
},
{
  'address': '0xDb298285FE4C5410B05390cA80e8Fbe9DE1F259B',
  'name': 'FOREX',
  #Name: 'handleFOREX',
  'decimals': 18
},
{
  'address': '0x5F62c96FBe504244F69ec99c4638a507Fefc3ED7',
  'name': 'R360',
  #Name: 'Recycle 360',
  'decimals': 18
},
{
  'address': '0x5fE5E1d5D86BDD4a7D84B4cAfac1E599c180488f',
  'name': 'gBRC',
  #Name: 'BrincGovToken',
  'decimals': 18
},
{
  'address': '0x07B68e17D3253cBcFC1520f1B1E8ef75B0d1f6d2',
  'name': 'HOLD',
  #Name: 'HoldersDao',
  'decimals': 18
},
{
  'address': '0x6a091a3406E0073C3CD6340122143009aDac0EDa',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xC880fCB325A5D725404A35438583962dc4b5D610',
  'name': 'ACAB',
  #Name: 'George Floyd',
  'decimals': 18
},
{
  'address': '0x1117aC6Ad6Cdf1A3BC543baD3B133724620522d5',
  'name': 'MODA',
  #Name: 'moda',
  'decimals': 18
},
{
  'address': '0x69681f8fde45345C3870BCD5eaf4A05a60E7D227',
  'name': 'ibGBP',
  #Name: 'Iron Bank GBP',
  'decimals': 18
},
{
  'address': '0x5555f75e3d5278082200Fb451D1b6bA946D8e13b',
  'name': 'ibJPY',
  #Name: 'Iron Bank JPY',
  'decimals': 18
},
{
  'address': '0x1CC481cE2BD2EC7Bf67d1Be64d4878b16078F309',
  'name': 'ibCHF',
  #Name: 'Iron Bank CHF',
  'decimals': 18
},
{
  'address': '0x95dFDC8161832e4fF7816aC4B6367CE201538253',
  'name': 'ibKRW',
  #Name: 'Iron Bank KRW',
  'decimals': 18
},
{
  'address': '0xFAFdF0C4c1CB09d430Bf88c75D88BB46DAe09967',
  'name': 'ibAUD',
  #Name: 'Iron Bank AUD',
  'decimals': 18
},
{
  'address': '0xF17e65822b568B3903685a7c9F496CF7656Cc6C2',
  'name': 'BICO',
  #Name: 'Biconomy Token',
  'decimals': 18
},
{
  'address': '0x88536C9B2C4701b8dB824e6A16829D5B5Eb84440',
  'name': 'USV',
  #Name: 'Universal Store of Value',
  'decimals': 9
},
{
  'address': '0xe958598BFAFBeA2d7692b3Dc932498704E11D20a',
  'name': 'KIT',
  #Name: 'Caboodles',
  'decimals': 18
},
{
  'address': '0x20BC832ca081b91433ff6c17f85701B6e92486c5',
  'name': 'rETH2',
  #Name: 'StakeWise Reward ETH2',
  'decimals': 18
},
{
  'address': '0x03F80ed11125F72537B8ad25855F907f5eF53c65',
  'name': 'HONEYB',
  #Name: 'HoneyBadger by Robness 734 ttl',
  'decimals': 18
},
{
  'address': '0x0F83287FF768D1c1e17a42F44d644D7F22e8ee1d',
  'name': 'sCHF',
  #Name: 'Synth sCHF',
  'decimals': 18
},
{
  'address': '0xc36b4311B21Fc0c2eAd46f1eA6ce97c9C4D98D3d',
  'name': 'CRE8',
  #Name: 'Creaticles',
  'decimals': 18
},
{
  'address': '0x12D7B28a055621F4bA0C146d1728082eCF1B9390',
  'name': 'TREAT',
  #Name: 'TREAT',
  'decimals': 18
},
{
  'address': '0x3Dc7B06dD0B1f08ef9AcBbD2564f8605b4868EEA',
  'name': 'SPACE',
  #Name: 'Space Token',
  'decimals': 18
},
{
  'address': '0x4531D09C51922094cD140eE24Da59B060A0Ef795',
  'name': 'SPAM',
  #Name: 'SPAM by JayDelay 2019 108 ttl',
  'decimals': 18
},
{
  'address': '0x2ef52Ed7De8c5ce03a4eF0efbe9B7450F2D7Edc9',
  'name': 'REV',
  #Name: 'Revain',
  'decimals': 6
},
{
  'address': '0x6336D88238075052Eb79197c3283e579f0156e48',
  'name': 'FUR',
  #Name: 'Furballs',
  'decimals': 18
},
{
  'address': '0xCc6C340B722fB9f4551aD45939Fd1457F0e218c6',
  'name': 'SWEETS',
  #Name: 'Sweets',
  'decimals': 18
},
{
  'address': '0x7BEF710a5759d197EC0Bf621c3Df802C2D60D848',
  'name': 'SHOPX',
  #Name: 'SPLYT SHOPX',
  'decimals': 18
},
{
  'address': '0xBABA0d970e735c7E48bba07C1164c4e0449AE9b8',
  'name': 'BAGZ',
  #Name: 'Degen$ Farm Bags',
  'decimals': 0
},
{
  'address': '0xa9E64BD15DBA7Bd119dfdD7AC858a4DEAf674bFa',
  'name': 'DDS',
  #Name: 'Dead Devil Society',
  'decimals': 18
},
{
  'address': '0xD13c7342e1ef687C5ad21b27c2b65D772cAb5C8c',
  'name': 'UOS',
  #Name: 'Ultra Token',
  'decimals': 4
},
{
  'address': '0x55a23fB10506B2679d0C53b4468309c7105fB16f',
  'name': 'GLEAF',
  #Name: 'Gleaf',
  'decimals': 18
},
{
  'address': '0xBc6669E7914a2b327Ae428184086d8Ac88d74EfC',
  'name': 'CCM',
  #Name: 'Car Coin',
  'decimals': 18
},
{
  'address': '0x21E783bcf445B515957A10E992aD3c8E9FF51288',
  'name': 'LGB',
  #Name: "Let's Go Brandon",
  'decimals': 18
},
{
  'address': '0xb8a62D3df12755aC1722d934Bd70AaE82D842A43',
  'name': 'SWAP',
  #Name: 'SW DAO Alpha Portfolio',
  'decimals': 18
},
{
  'address': '0x0eDF9bc41Bbc1354c70e2107F80C42caE7FBBcA8',
  'name': 'STRM',
  #Name: 'Instrumental Finance',
  'decimals': 18
},
{
  'address': '0xe1590A6FA0CFf9C960181cb77d8a873601772f64',
  'name': 'WSB',
  #Name: 'pTokens WSB',
  'decimals': 18
},
{
  'address': '0x1b890fD37Cd50BeA59346fC2f8ddb7cd9F5Fabd5',
  'name': 'NEWO',
  #Name: 'New Order',
  'decimals': 18
},
{
  'address': '0x06e67903b6CbAD24C131a57Eff68b14512d933dE',
  'name': 'LYDF',
  #Name: 'Lyds Futures',
  'decimals': 18
},
{
  'address': '0xfa09DD10B4758e155202e3711b0624176A9d572E',
  'name': 'GOOSE',
  #Name: 'MongooseCoin',
  'decimals': 18
},
{
  'address': '0xe0b9BcD54bF8A730EA5d3f1fFCe0885E911a502c',
  'name': 'ZUM',
  #Name: 'Zum Token',
  'decimals': 8
},
{
  'address': '0x911b4fed45AB621cf1a8F567956DD218C3140bE7',
  'name': 'ZAP',
  #Name: 'ZAP',
  'decimals': 18
},
{
  'address': '0xAb55Ba6F172B74a7da7326F0a816d4e0b9ee16f2',
  'name': 'NOUNPUNK',
  #Name: 'NOUNPUNK',
  'decimals': 18
},
{
  'address': '0xCDeEeaaf2E96c25c679155e3854169c2f336b931',
  'name': 'MVRS',
  #Name: 'MetaverseAir',
  'decimals': 18
},
{
  'address': '0x3f5294DF68F871241c4B18fcF78ebD8Ac18aB654',
  'name': 'STZ',
  #Name: '99Starz',
  'decimals': 18
},
{
  'address': '0x04A3c9D70DF14de264E0B7a46d9fb09f573AAfd6',
  'name': 'BB',
  #Name: 'BallerBars',
  'decimals': 18
},
{
  'address': '0xA1a4E303e9C56962F201C5e834abC1E677A3C4F3',
  'name': 'CVNX',
  #Name: 'CVNX',
  'decimals': 18
},
{
  'address': '0x88a23C650e8C72960596Acad5901CAE56cE6EF35',
  'name': 'BRK',
  #Name: 'BRKToken',
  'decimals': 18
},
{
  'address': '0x56de8BC61346321D4F2211e3aC3c0A7F00dB9b76',
  'name': 'RENA',
  #Name: 'Rena',
  'decimals': 18
},
{
  'address': '0x64aa3364F17a4D01c6f1751Fd97C2BD3D7e7f1D5',
  'name': 'OHM',
  #Name: 'Olympus',
  'decimals': 9
},
{
  'address': '0x44709a920fCcF795fbC57BAA433cc3dd53C44DbE',
  'name': 'RADAR',
  #Name: 'DappRadar',
  'decimals': 18
},
{
  'address': '0xe29797910D413281d2821D5d9a989262c8121CC2',
  'name': 'ELIMU',
  #Name: 'elimu.ai',
  'decimals': 18
},
{
  'address': '0x5C173A51468694C0114aad0c14cbEA350f40C33e',
  'name': 'LORB',
  #Name: 'Leviathan Lobster Token',
  'decimals': 18
},
{
  'address': '0x39fBBABf11738317a448031930706cd3e612e1B9',
  'name': 'WXRP',
  #Name: 'Wrapped XRP',
  'decimals': 18
},
{
  'address': '0x53c4871322Bb47e7A24136fce291a6dcC832a294',
  'name': 'WLTC',
  #Name: 'Wrapped Litecoin',
  'decimals': 18
},
{
  'address': '0x85D7bdfc9c3426b33A684241eEEE70385Bc42820',
  'name': 'WKDA',
  #Name: 'Wrapped Kadena',
  'decimals': 18
},
{
  'address': '0xb2089A7069861C8D90c8dA3aaCAB8e9188C0C531',
  'name': 'GREEN',
  #Name: 'Green',
  'decimals': 8
},
{
  'address': '0x81d327cF395347Dd6CC0C427Bb9EA77ec120E304',
  'name': 'EGG',
  #Name: 'EGG',
  'decimals': 18
},
{
  'address': '0x0acC0FEE1D86D2cD5AF372615bf59b298D50cd69',
  'name': 'ILSI',
  #Name: 'Invest Like Stakeborg Index',
  'decimals': 18
},
{
  'address': '0x92Ec47DF1AA167806dFa4916D9Cfb99da6953b8F',
  'name': 'IDV',
  #Name: 'Idavoll Network',
  'decimals': 18
},
{
  'address': '0xcd7Ce5d63F7DC7b1076f64E6C1DD7cCfa31228c7',
  'name': 'INKz',
  #Name: 'INKzToken',
  'decimals': 18
},
{
  'address': '0x7f280daC515121DcdA3EaC69eB4C13a52392CACE',
  'name': 'FNC',
  #Name: 'Fancy Games',
  'decimals': 18
},
{
  'address': '0x811730013e801daDd5D1dE0542C57Aa110Af6643',
  'name': 'PXLMAP',
  #Name: 'PixelMap',
  'decimals': 18
},
{
  'address': '0x3E87D72F3455c56B739ffEF0Bfd75F3BA3c0F86b',
  'name': 'BTRFLY',
  #Name: 'Butterfly',
  'decimals': 18
},
{
  'address': '0xc0F4014A41C7511Bf22351a132A7282F84EaeC3a',
  'name': 'BTRFLY',
  #Name: 'BTRFLY',
  'decimals': 18
},
{
  'address': '0xC0d4Ceb216B3BA9C3701B291766fDCbA977ceC3A',
  'name': 'BTRFLY',
  #Name: 'BTRFLY',
  'decimals': 9
},
{
  'address': '0x00c4a73f10b05228c64e971cf81Ae84426a64780',
  'name': 'MPUNK',
  #Name: 'MineablePunks',
  'decimals': 18
},
{
  'address': '0xCC94Faf235cC5D3Bf4bEd3a30db5984306c86aBC',
  'name': 'xBTRFLY',
  #Name: 'xBTRFLY',
  'decimals': 9
},
{
  'address': '0xC735EfB4f32637bF3eA2F6956372D98DEb68F47d',
  'name': 'BCD',
  #Name: 'BlockChainDAO',
  'decimals': 18
},
{
  'address': '0xfEed6FEBED886cCF1735680a03182f6759dc512f',
  'name': 'EKTA v2',
  #Name: 'EKTA v2',
  'decimals': 18
},
{
  'address': '0x882e5b370D595E50c24b2a0e7a94e87Cc32ADdA1',
  'name': 'Game',
  #Name: 'Game',
  'decimals': 18
},
{
  'address': '0x75af3FD37d7CA74447e865F792f263b2b1159B58',
  'name': 'USDT',
  #Name: 'Tether USD',
  'decimals': 6
},
{
  'address': '0xeBC345e12c14449F2B63F077fd86F3345B0F0d14',
  'name': 'ESPL',
  #Name: 'ESplash',
  'decimals': 18
},
{
  'address': '0x0235a4Fa8374fd49BB2f01aC953f99748756f3Bd',
  'name': 'CHARGE',
  #Name: 'Charge',
  'decimals': 18
},
{
  'address': '0x108a850856Db3f85d0269a2693D896B394C80325',
  'name': 'TGT',
  #Name: 'THORWallet Governance Token',
  'decimals': 18
},
{
  'address': '0x5A35A6686db167B05E2Eb74e1ede9fb5D9Cdb3E0',
  'name': 'CIG',
  #Name: 'Cigarette Token',
  'decimals': 18
},
{
  'address': '0x65Ef703f5594D2573eb71Aaf55BC0CB548492df4',
  'name': 'MULTI',
  #Name: 'Multichain',
  'decimals': 18
},
{
  'address': '0x94c9cEb2F9741230FAD3a62781b27Cc79a9460d4',
  'name': 'MAYC',
  #Name: 'Mutant Ape Yacht Club',
  'decimals': 18
},
{
  'address': '0xF8964f9a4985749AbcA98114446F3adAcCE7CD92',
  'name': 'JON-M',
  #Name: 'Jonmang',
  'decimals': 18
},
{
  'address': '0x9AB7bb7FdC60f4357ECFef43986818A2A3569c62',
  'name': 'GOG',
  #Name: 'Guild of Guardians',
  'decimals': 18
},
{
  'address': '0x69fa8e7F6bf1ca1fB0de61e1366f7412b827CC51',
  'name': 'NRCH',
  #Name: 'EnreachDAO',
  'decimals': 9
},
{
  'address': '0xE2FB6529EF566a080e6d23dE0bd351311087D567',
  'name': 'COV',
  #Name: 'Covesting',
  'decimals': 18
},
{
  'address': '0xE57425F1598f9b0d6219706b77f4b3DA573a3695',
  'name': 'BTCBR',
  #Name: 'BitcoinBR',
  'decimals': 18
},
{
  'address': '0xFEEf77d3f69374f66429C91d732A244f074bdf74',
  'name': 'cvxFXS',
  #Name: 'Convex FXS',
  'decimals': 18
},
{
  'address': '0xF938424F7210f31dF2Aee3011291b658f872e91e',
  'name': 'VISR',
  #Name: 'VISOR',
  'decimals': 18
},
{
  'address': '0x47b9F01B16E9C9cb99191DCA68c9cc5bF6403957',
  'name': 'ONSTON',
  #Name: 'ONSTON',
  'decimals': 18
},
{
  'address': '0x4189C40ab775ae40169a3AE845FD6849aa4106a2',
  'name': 'CORGI',
  #Name: 'Corgi',
  'decimals': 18
},
{
  'address': '0x7269c9AAA5eD95f0CC9DC15ff19A4596308c889C',
  'name': 'MORIE',
  #Name: 'CryptoMories',
  'decimals': 18
},
{
  'address': '0x2a2550e0A75aCec6D811AE3930732F7f3ad67588',
  'name': 'PATH',
  #Name: 'PathDao',
  'decimals': 18
},
{
  'address': '0x3b484b82567a09e2588A13D54D032153f0c0aEe0',
  'name': 'SOS',
  #Name: 'SOS',
  'decimals': 18
},
{
  'address': '0xd0c37Cda48Fe5D6Ee7132181a90DC58206Db5404',
  'name': 'INKZ',
  #Name: 'INKz',
  'decimals': 18
},
{
  'address': '0x309627af60F0926daa6041B8279484312f2bf060',
  'name': 'USDB',
  #Name: 'Bancor USD Token',
  'decimals': 18
},
{
  'address': '0xb5f278Ee11811eFEC0692EC61b1e9f9984f2de11',
  'name': 'EMIT',
  #Name: 'SmartMint BondFiat StableToken',
  'decimals': 3
},
{
  'address': '0x490e3f4af13e1616EC97A8C6600c1061a8D0253e',
  'name': 'TRR',
  #Name: 'TERRAN',
  'decimals': 18
},
{
  'address': '0xdef1fac7Bf08f173D286BbBDcBeeADe695129840',
  'name': 'CERBY',
  #Name: 'Cerby Token',
  'decimals': 18
},
{
  'address': '0x24456F2786d975973a0905Fd53236c8311cc3006',
  'name': 'COSHIB',
  #Name: 'Shiba Inu VS COVID',
  'decimals': 8
},
{
  'address': '0x00F644CB516e53A09D02e5E2c49Fc7fC0cFC37A5',
  'name': 'CNDL',
  #Name: 'Candle',
  'decimals': 8
},
{
  'address': '0xC1B97bE3eD1b48e0dAca48606E34e13Fba2e3F82',
  'name': 'BIG',
  #Name: 'BIG DOG',
  'decimals': 18
},
{
  'address': '0x00000006e55A9364b657E3b91Cd0411B4fD11aC2',
  'name': 'ADIDAS',
  #Name: 'Adidas Originals Metaverse',
  'decimals': 18
},
{
  'address': '0x11a14CCEfb4344c0383ECf0a3F35514e6E2b6F72',
  'name': 'DHG',
  #Name: 'DaHuangGua',
  'decimals': 18
},
{
  'address': '0x731A04e1271D7E0Dd287eCd22c6f10bd76BEFb13',
  'name': 'RTG',
  #Name: 'Shortage',
  'decimals': 18
},
{
  'address': '0xF8Fe4dbE106AC2a1e6C96C3Ca77B344A1b1A49e1',
  'name': 'NFTism',
  #Name: 'NFTism',
  'decimals': 18
},
{
  'address': '0xe609Ea743130ADCe4A8Ae6Ec81A088A01E4C67fB',
  'name': 'XIMP',
  #Name: 'Imperial β',
  'decimals': 18
},
{
  'address': '0x12bcF29d1A5ee44c0872170facBC1D6f1b5A88d7',
  'name': 'IH8',
  #Name: 'IH8Money',
  'decimals': 18
},
{
  'address': '0xE9E73E1aE76D17A16cC53E3e87a9a7dA78834d37',
  'name': 'CAMP',
  #Name: 'Camp',
  'decimals': 18
},
{
  'address': '0xA548a7efE00371ded670cBdD9CAdcb383506C718',
  'name': 'Fire',
  #Name: 'Fire',
  'decimals': 18
},
{
  'address': '0x58CE85462a37Ca4CCFF93843eB8954Bc866a0c4C',
  'name': 'AMBER',
  #Name: 'Amber',
  'decimals': 18
},
{
  'address': '0x2DDbFb13677E8Df85F37Aa8E578424E99AF7Cb62',
  'name': 'WRAP',
  #Name: 'Wrapped',
  'decimals': 18
},
{
  'address': '0x144E3b02e08e644fFbB7fF652763F5B72eE22701',
  'name': 'DMND',
  #Name: 'DiamondDAO',
  'decimals': 9
},
{
  'address': '0x6Bba316c48b49BD1eAc44573c5c871ff02958469',
  'name': 'GAS',
  #Name: 'Gas DAO',
  'decimals': 18
},
{
  'address': '0x01012022D43a3f85196A6bEa96Dfdb7350fDAa3c',
  'name': '2022',
  #Name: 'Happy New Year',
  'decimals': 18
},
{
  'address': '0x4674672BcDdDA2ea5300F5207E1158185c944bc0',
  'name': 'GXT',
  #Name: 'Gem Exchange and Trading',
  'decimals': 18
},
{
  'address': '0xcD5CE26099Bd1F0eB9CD11AcCB7C1Bd0dE8247a7',
  'name': '$ZILLA',
  #Name: 'ZillaToken',
  'decimals': 18
},
{
  'address': '0xa4009D8Eda6F40f549Dfc10f33F56619b9754C90',
  'name': 'PAYC',
  #Name: 'Phunky Ape Yacht Club',
  'decimals': 18
},
{
  'address': '0x9010A15184Da16E3a7C5B4aA50094dfe3BB36989',
  'name': 'YEAR',
  #Name: 'EtherWrapped',
  'decimals': 18
},
{
  'address': '0x507586012a126421c3669A64B8393fffA9C44462',
  'name': 'ANKH',
  #Name: 'Anubis',
  'decimals': 9
},
{
  'address': '0x61DA4439aF79d6c567AFbc97421D9debfDfB96BE',
  'name': 'KISMET',
  #Name: 'KismetCoin',
  'decimals': 18
},
{
  'address': '0xDF7A2593A70fF1e69b5a20644Ae848558A2F7C86',
  'name': 'MFER',
  #Name: 'mfers',
  'decimals': 18
},
{
  'address': '0x70Bef3bB2f001dA2fDDb207dAe696cD9FAFf3f5d',
  'name': 'NST',
  #Name: 'Ninja Squad Token',
  'decimals': 18
},
{
  'address': '0x404E57E343556158F1BeF099069bC59fd35CC940',
  'name': 'XDT',
  #Name: 'xDai Tigers from Gnosis Chain',
  'decimals': 18
},
{
  'address': '0x7c5BbE30B5b1c1ABaA9e1Ee32e04a81a2B20a052',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0xB84C45174Bfc6b8F3EaeCBae11deE63114f5c1b2',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0x8545F42a5A4888f7A4D907Bf7ae11796c95F4cC2',
  'name': 'NEWY',
  #Name: 'NewYear',
  'decimals': 18
},
{
  'address': '0x0d34aaC34be3c1B4928e1574c1263Ada6603318D',
  'name': 'PHAYC',
  #Name: 'PHAYC',
  'decimals': 18
},
{
  'address': '0xb68B75C2256071bADDDFadD6f65F5079c44dF89b',
  'name': 'SOS99',
  #Name: 'SOSDAO',
  'decimals': 18
},
{
  'address': '0xae78736Cd615f374D3085123A210448E74Fc6393',
  'name': 'rETH',
  #Name: 'Rocket Pool ETH',
  'decimals': 18
},
{
  'address': '0x270B157A6bb0290484866383E14c1ef9375C6Fe8',
  'name': 'NOUN',
  #Name: 'Nouns',
  'decimals': 18
},
{
  'address': '0xf2Ef3551C1945A7218fc4eC0a75c9eCFDF012A4F',
  'name': 'C4G3',
  #Name: 'CAGE',
  'decimals': 18
},
{
  'address': '0x807a0774236A0fBE9e7f8E7Df49EDFED0e6777Ea',
  'name': 'BLOCK',
  #Name: 'Block',
  'decimals': 18
},
{
  'address': '0x7f3141c4D6b047fb930991b450f1eD996a51CB26',
  'name': 'X',
  #Name: 'X',
  'decimals': 18
},
{
  'address': '0xA31fDbaA772745D11843EFEDA9922dcbf5460672',
  'name': 'CTRL',
  #Name: 'Lift.Kitchen Control DAO',
  'decimals': 18
},
{
  'address': '0x62Ba3D7CceDedFc19117bDba63BF864b1829d5Ce',
  'name': 'WOKE',
  #Name: 'WokeDAO',
  'decimals': 18
},
{
  'address': '0x9db0dB8c4006A793df00caA6416b993a3ba90192',
  'name': 'CAC',
  #Name: 'Cool Ape Club',
  'decimals': 18
},
{
  'address': '0x5C4D2aA807d085b85D6B2b139d10F40455732b1D',
  'name': 'BUNGA',
  #Name: 'Lazy Lions Bungalows',
  'decimals': 18
},
{
  'address': '0xAfA004f6AF7866c201C64c935079aB22A50F6C13',
  'name': 'Wiki',
  #Name: 'Wikipedia DAO',
  'decimals': 18
},
{
  'address': '0x177905F9D89CFa183a9220c2f1a24ab233D9d35F',
  'name': 'DIAR',
  #Name: 'Diarrhoea Token',
  'decimals': 18
},
{
  'address': '0xDFB185B3C50191b5F598d6359074fdD765c4aD70',
  'name': 'CARROTZ',
  #Name: 'CARROTZ',
  'decimals': 18
},
{
  'address': '0xdCA02198656a70982Fa917CfaD1f95530c7fdbAf',
  'name': 'FLURK',
  #Name: 'Flurks by Stonetoss',
  'decimals': 18
},
{
  'address': '0xEe7527841A932d2912224E20a405e1a1FF747084',
  'name': 'SHX',
  #Name: 'Stronghold SHx',
  'decimals': 7
},
{
  'address': '0x4cec7ae83ABA671A59a40Ad2B170f46CA9A3614D',
  'name': 'CLONEX',
  #Name: 'CLONEX',
  'decimals': 18
},
{
  'address': '0xCE15cb5fe641E0C083bB3E12aA3bF70072D23C1E',
  'name': 'LP',
  #Name: 'LPDAO Token',
  'decimals': 18
},
{
  'address': '0xD12bD9c20bFaaD1F32a39856B2737146E9B18419',
  'name': 'FLU',
  #Name: 'Flurona',
  'decimals': 18
},
{
  'address': '0xeFe6Ba7E126197464aC88992751A59Fb81764268',
  'name': 'FLU',
  #Name: 'Flurona',
  'decimals': 18
},
{
  'address': '0xcB9f441FFAE898e7A2f32143Fd79ac899517a9Dc',
  'name': 'SHARPEI',
  #Name: 'Shar Pei',
  'decimals': 18
},
{
  'address': '0x79e43c44D5509D00D584000C0a6B1E9e62609f56',
  'name': 'REGULR',
  #Name: 'Regulars',
  'decimals': 18
},
{
  'address': '0xde1D324863dd2349850e6c8D685B8111AAbb7cD1',
  'name': 'JEWS',
  #Name: 'HOLOCAUST',
  'decimals': 18
},
{
  'address': '0x01BA67AAC7f75f647D94220Cc98FB30FCc5105Bf',
  'name': 'LYRA',
  #Name: 'Lyra Token',
  'decimals': 18
},
{
  'address': '0xb8B8FE22fa958b4b7B1279ca9aC11f9036586a3D',
  'name': 'STANDA',
  #Name: 'Standametti',
  'decimals': 18
},
{
  'address': '0x2AdCbeE886D23EFF5ADECC7767Bf102E4A1CE151',
  'name': 'VEDA',
  #Name: 'AyurVeda AG Shares',
  'decimals': 0
},
{
  'address': '0xB4272071eCAdd69d933AdcD19cA99fe80664fc08',
  'name': 'XCHF',
  #Name: 'CryptoFranc',
  'decimals': 18
},
{
  'address': '0x69570f3E84f51Ea70b7B68055c8d667e77735a25',
  'name': 'BSGG',
  #Name: 'Betswap.gg',
  'decimals': 18
},
{
  'address': '0x5dDAFa0856F883A634051dCb4dD710863d85a0c1',
  'name': 'JPEGS',
  #Name: 'IlliquidDAO',
  'decimals': 18
},
{
  'address': '0xE218ae707E7Aa0c138f7A44bcD89e79616E7430D',
  'name': 'Meta',
  #Name: 'Metaverse',
  'decimals': 18
},
{
  'address': '0x3b79a28264fC52c7b4CEA90558AA0B162f7Faf57',
  'name': 'wMEMO',
  #Name: 'Wrapped MEMO',
  'decimals': 18
},
{
  'address': '0x44dA528CdE933688Dffd4317774fd474298a356f',
  'name': 'FANG',
  #Name: 'Fangs',
  'decimals': 0
},
{
  'address': '0xD68b761597f07bcB2DEA7B56cc096b097F964cE2',
  'name': 'Jay',
  #Name: 'Phanta Bear NFT',
  'decimals': 18
},
{
  'address': '0xdEE7bd44f02189fB0A8Cc9BeBF95fad933A8CcD9',
  'name': 'KIA',
  #Name: 'Koala Intelligence Agency',
  'decimals': 18
},
{
  'address': '0xA68Dd8cB83097765263AdAD881Af6eeD479c4a33',
  'name': 'WTF',
  #Name: 'fees.wtf',
  'decimals': 18
},
{
  'address': '0x9B812C65529eC7d20ab630235ae20fde022c8aD3',
  'name': 'CBD',
  #Name: 'CybeeDAO',
  'decimals': 18
},
{
  'address': '0x5Bf34fa634b4EcCAAfA7609FCCfd6537CDC9f920',
  'name': 'DISD',
  #Name: 'DisDAO',
  'decimals': 18
},
{
  'address': '0xAd1da531e63D2b1203eD828c47780ea9900A7755',
  'name': 'ADIDAS',
  #Name: 'Adidas Originals Metaverse',
  'decimals': 18
},
{
  'address': '0xb97d3e98A1c607aae7784cc2dDEa3c77759e82C6',
  'name': 'KINGZ',
  #Name: 'KaijuKingz',
  'decimals': 18
},
{
  'address': '0x2034437801b62EDe275210f76E2D4e77d0198BfF',
  'name': 'ROO',
  #Name: 'Roo Troop',
  'decimals': 18
},
{
  'address': '0x1B3486487aC6eF1E9Cd126160dfDbC322A7CbA2b',
  'name': 'PXD',
  #Name: 'Pixel Doods',
  'decimals': 18
},
{
  'address': '0x0cd198a5F6cC84cA8499Dd97a6C1A1C4b4a12da1',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0x35F53755BA9bC9160D31FfE86bcAa9B1D187BA71',
  'name': 'QUBIT',
  #Name: 'Qubits',
  'decimals': 18
},
{
  'address': '0xBb9FD66c0632bC92a631721B094233379970cF2e',
  'name': 'SAFLE',
  #Name: 'Safle',
  'decimals': 18
},
{
  'address': '0x758B4684BE769E92eeFeA93f60DDA0181eA303Ec',
  'name': 'PHONON',
  #Name: 'Phonon DAO',
  'decimals': 18
},
{
  'address': '0x9Eb84f6c66870142309c247BF6D66680a931De86',
  'name': 'NEKO',
  #Name: 'ManekiNeko Japan',
  'decimals': 9
},
{
  'address': '0x3dBEBa7da4f4f0b061E260cEC71727616c75c0E1',
  'name': 'FEELS GOOD',
  #Name: 'FEELS GOOD',
  'decimals': 18
},
{
  'address': '0xCc173076D0f082651169fdf3F6D02fc0dAaB0976',
  'name': 'FOMO',
  #Name: 'FOMO MOFO',
  'decimals': 18
},
{
  'address': '0x045c335f9C408FE456611Db905dDe61a334980a7',
  'name': 'SBC',
  #Name: 'Shiba Cloud',
  'decimals': 0
},
{
  'address': '0xD47c30FfEf3d50a4FE764E34d755b057eB8755e6',
  'name': 'Walmart',
  #Name: 'Walmart Dao',
  'decimals': 18
},
{
  'address': '0x921F79aCcEEEe39f0F828C45cC7D30a0fD144560',
  'name': 'TWIST',
  #Name: 'Twisted Tweaks',
  'decimals': 18
},
{
  'address': '0xf34B1Db61ACa1a371fE97BAd2606c9f534fb9D7D',
  'name': 'RBIS',
  #Name: 'Arbismart Token',
  'decimals': 18
},
{
  'address': '0x591127253E40d4f63bF29CcF3D81FD062A149C8c',
  'name': 'XMETA',
  #Name: 'TTX METAVERSE',
  'decimals': 18
},
{
  'address': '0xa8bb2Ef88c9fD04952bF47041f9329D1e449C204',
  'name': '$Stardust',
  #Name: 'Stardust',
  'decimals': 18
},
{
  'address': '0x0ff5A8451A839f5F0BB3562689D9A44089738D11',
  'name': 'rDPX',
  #Name: 'Dopex Rebate Token',
  'decimals': 18
},
{
  'address': '0x4Dd981f0F2e7934B6B50c9d1bedA2B5456924DF6',
  'name': 'PICO',
  #Name: 'PicoGo',
  'decimals': 6
},
{
  'address': '0xd3ba270f82CadabD0596D3D30233448621d561BB',
  'name': 'BAE',
  #Name: 'Bay Area Excitement',
  'decimals': 18
},
{
  'address': '0x5Fe8C486B5f216B9AD83C12958d8A03eb3fD5060',
  'name': 'OIL',
  #Name: 'OIL',
  'decimals': 18
},
{
  'address': '0x002CdEbFCE2F5E3FD704DA0fa346Ad2621353B92',
  'name': 'KING',
  #Name: 'KING Token',
  'decimals': 18
},
{
  'address': '0x98D1Ee38fB137CCD42F46B52b44d5f2e36D4A66c',
  'name': 'CAP',
  #Name: 'Capsule House',
  'decimals': 18
},
{
  'address': '0x1A285E15A4d0F262ff61bA46B3cAc4E52dCFbF35',
  'name': 'LGN ',
  #Name: 'LOGAN',
  'decimals': 18
},
{
  'address': '0x6F87D756DAf0503d08Eb8993686c7Fc01Dc44fB1',
  'name': 'TRADE',
  #Name: 'UniTrade',
  'decimals': 18
},
{
  'address': '0xa6dD98031551C23bb4A2fBE2C4d524e8f737c6f7',
  'name': 'TKNFY',
  #Name: 'Tokenfy',
  'decimals': 18
},
{
  'address': '0xf0655287B6c34e221D3bba5BAF89CE1bB8d094B5',
  'name': 'HM',
  #Name: 'Half Moon co-op',
  'decimals': 18
},
{
  'address': '0x3579Fb82f7c22f19D62b170b482766d0d11dbD5E',
  'name': 'SUPERS',
  #Name: 'SemiSupers',
  'decimals': 18
},
{
  'address': '0xD89B16331f39AB3878dAf395052851D3aC8Cf3CD',
  'name': 'COVEN',
  #Name: 'Crypto Coven',
  'decimals': 18
},
{
  'address': '0x5058B77CBd029F56A11Bd56326519e3Ec0081cD0',
  'name': '$WATTS',
  #Name: 'WATTS',
  'decimals': 18
},
{
  'address': '0xE89C20096b636fFec9fd26d1a623F42A33eaD309',
  'name': 'OG',
  #Name: 'Oogear',
  'decimals': 18
},
{
  'address': '0xA66734D48d564e4e1c016c8d2Ea2E9131b41c1ad',
  'name': 'LOOT',
  #Name: 'Loot (for Adventurers)',
  'decimals': 18
},
{
  'address': '0x5b517Df31B3EDCD2CB569BeBB9bB817833CF746c',
  'name': 'GRQ',
  #Name: 'GRQ Token',
  'decimals': 0
},
{
  'address': '0x6bE6Fc85A0A7963909EF4572fae4df1ef100100D',
  'name': 'CHUBBI',
  #Name: 'Chubbiverse Frens',
  'decimals': 18
},
{
  'address': '0x7Cfea0DD176651E7B5a1CeD9c4fAf8Ee295315FD',
  'name': 'PRNT',
  #Name: 'PrimeNumbers',
  'decimals': 18
},
{
  'address': '0x0601f64B7ea089767D2fc6777a109A3372BF0742',
  'name': 'GCDA',
  #Name: 'GC Digital Assets',
  'decimals': 18
},
{
  'address': '0xB0c7a3Ba49C7a6EaBa6cD4a96C55a1391070Ac9A',
  'name': 'MAGIC',
  #Name: 'MAGIC',
  'decimals': 18
},
{
  'address': '0xCB56b52316041A62B6b5D0583DcE4A8AE7a3C629',
  'name': 'CIG',
  #Name: 'Cigarette Token',
  'decimals': 18
},
{
  'address': '0x2AD1219367DCBFF80D37Bb770dE008875ab58CD9',
  'name': 'BTED',
  #Name: 'BitEd',
  'decimals': 18
},
{
  'address': '0x3870Edfd239cbF769b87318D8791d74dD9e36E77',
  'name': 'FND',
  #Name: 'Foundation Collection [0x3B3]',
  'decimals': 18
},
{
  'address': '0xC669928185DbCE49d2230CC9B0979BE6DC797957',
  'name': 'BTT',
  #Name: 'BitTorrent',
  'decimals': 18
},
{
  'address': '0xc060443d763e7CE487595dB13700b2aa99b8Fc19',
  'name': 'EDOGE',
  #Name: 'EarnDoge',
  'decimals': 18
},
{
  'address': '0x48666Fe01d123D14B53EAcf21f36786F2a786c86',
  'name': 'EFI',
  #Name: 'EarnableFi',
  'decimals': 18
},
{
  'address': '0x3E828ac5C480069D4765654Fb4b8733b910b13b2',
  'name': 'CLNY',
  #Name: 'Colony Network Token',
  'decimals': 18
},
{
  'address': '0xD4e12B224C316664EbB647F69abC1fb8bB2697C7',
  'name': 'BRIBE',
  #Name: 'Bribe Token',
  'decimals': 18
},
{
  'address': '0xE8A1edB81B45b8FB8F5049F957faCCE779a45d22',
  'name': 'AZUKI',
  #Name: 'Azuki',
  'decimals': 18
},
{
  'address': '0xF43809d3CFE742d0830E14D3489B61cB6E30e0e9',
  'name': 'COMMON',
  #Name: 'LooksCommon Token',
  'decimals': 7
},
{
  'address': '0x88800092fF476844f74dC2FC427974BBee2794Ae',
  'name': 'WALLET',
  #Name: 'Ambire Wallet',
  'decimals': 18
},
{
  'address': '0x950F87e3561e56e961a00de273bBb376bC66D7Ba',
  'name': 'KODAV',
  #Name: 'KnownOrigin',
  'decimals': 18
},
{
  'address': '0xF373a10d21cc4a9f84421c69Ec2D9528B6162012',
  'name': 'KGF',
  #Name: 'Killer GF',
  'decimals': 18
},
{
  'address': '0xD18a0085989b67788e35Fc1f8A439707A7639D46',
  'name': 'AZZIP',
  #Name: 'Rare Pizzas',
  'decimals': 18
},
{
  'address': '0x4aF337126BF510179e7816A064a86B6aE3D449E0',
  'name': 'XPHUNK',
  #Name: 'ExpansionPhunks',
  'decimals': 18
},
{
  'address': '0x0C75dD36aF9a59BA1d248a98Fe91b2384cfea9be',
  'name': 'WHIRL',
  #Name: 'OmniWhirl',
  'decimals': 18
},
{
  'address': '0xD6c08040Db9d34932BA34c2cE10Ed37b4667A96a',
  'name': 'FNT',
  #Name: 'Fortnite Token',
  'decimals': 18
},
{
  'address': '0x5f4755BcD982984349Aa7893fB80Ff3ada808668',
  'name': 'BTP',
  #Name: 'Born To Pump Staging',
  'decimals': 18
},
{
  'address': '0x60bE1e1fE41c1370ADaF5d8e66f07Cf1C2Df2268',
  'name': 'PERC',
  #Name: 'Perion Credits',
  'decimals': 18
},
{
  'address': '0x2e6109B1Ac12ff120526AD1bF2Df707d22845019',
  'name': 'TOTER',
  #Name: 'ToterDAO: Historic Trashart Vault',
  'decimals': 18
},
{
  'address': '0x98585dFc8d9e7D48F0b1aE47ce33332CF4237D96',
  'name': 'NEWO',
  #Name: 'New Order',
  'decimals': 18
},
{
  'address': '0xd7f5CABdF696D7d1bf384D7688926A4bdB092c67',
  'name': 'DRC',
  #Name: 'Dream Car',
  'decimals': 18
},
{
  'address': '0x6D2665089D7030AC0D8abDD2d179e14df9A7cfb5',
  'name': 'PHANTS',
  #Name: 'Untamed Elephants',
  'decimals': 18
},
{
  'address': '0x3f95E5099CF3A125145212Afd53039B8d8C5656e',
  'name': 'SAFLE',
  #Name: 'Safle',
  'decimals': 18
},
{
  'address': '0x3D969C25d6FbAf26Dbb5e696D5031349af73e76c',
  'name': 'DAH',
  #Name: 'Dallah',
  'decimals': 18
},
{
  'address': '0xEDd27C961CE6f79afC16Fd287d934eE31a90D7D1',
  'name': 'veSOS',
  #Name: 'veSOS',
  'decimals': 18
},
{
  'address': '0xf66Cd2f8755a21d3c8683a10269F795c0532Dd58',
  'name': 'CoreDAO',
  #Name: 'CORE DAO',
  'decimals': 18
},
{
  'address': '0x0832De2Df6A4Cbd9Bb7962ddb2d0e87a325FC4B2',
  'name': 'FRENS',
  #Name: 'LittleFrens',
  'decimals': 18
},
{
  'address': '0xF48ddA868130ce65Ae38Cc8Fc7285b2F67AF49A5',
  'name': 'WHALETAMA',
  #Name: 'Whaletama',
  'decimals': 9
},
{
  'address': '0x903dFBC9bAC585feDaE3c2E327913abfd022E2E0',
  'name': 'XVX',
  #Name: 'MAINFINEX',
  'decimals': 18
},
{
  'address': '0xFE45A3d08a98F64230Fc103E4ea09536bc1DE3Ca',
  'name': 'TITS',
  #Name: 'CryptoTigVags',
  'decimals': 18
},
{
  'address': '0x6FF093DD03cb980115e27694B927435dCC71962f',
  'name': 'OMGK',
  #Name: 'omgkirby GENESIS',
  'decimals': 18
},
{
  'address': '0x37fE0f067FA808fFBDd12891C0858532CFE7361d',
  'name': 'CIV',
  #Name: 'Civilization',
  'decimals': 18
},
{
  'address': '0x59d1e836F7b7210A978b25a855085cc46fd090B5',
  'name': 'JUSTICE',
  #Name: 'AssangeDAO',
  'decimals': 18
},
{
  'address': '0xB4dFfa52fEe44BD493f12D85829D775EC8017691',
  'name': 'Gaas',
  #Name: 'Congruent DAO Token',
  'decimals': 9
},
{
  'address': '0x5c147e74D63B1D31AA3Fd78Eb229B65161983B2b',
  'name': 'WFLOW',
  #Name: 'Wrapped Flow',
  'decimals': 18
},
{
  'address': '0x24E79e946dEa5482212c38aaB2D0782F04cdB0E0',
  'name': 'palStkAAVE',
  #Name: 'Paladin stkAAVE',
  'decimals': 18
},
{
  'address': '0xc9bCA77c9FEd40710727948F6a934208918D316A',
  'name': 'BRUNO',
  #Name: 'Bruno Inu',
  'decimals': 9
},
{
  'address': '0xe2B9CCfed8c39AFEEe0450cB098D9D0f9A6a0299',
  'name': 'CDAD',
  #Name: 'CryptoDads',
  'decimals': 18
},
{
  'address': '0xD9a36081b641314a75cc030038428C41934F518C',
  'name': 'AIS',
  #Name: 'Apes In Space',
  'decimals': 18
},
{
  'address': '0x9300E4d9Aa61D0445EfA6C350cD804e044A1e63F',
  'name': 'TULIP',
  #Name: 'EtherTulips',
  'decimals': 18
},
{
  'address': '0xa54d2EBfD977ad836203c85F18db2F0a0cF88854',
  'name': 'BACON',
  #Name: 'BaconCoin',
  'decimals': 18
},
{
  'address': '0xEC3D5772471c7efcb59a4478d4ae09060Dad0591',
  'name': 'BPRINT',
  #Name: 'Async Art Blueprints',
  'decimals': 18
},
{
  'address': '0xA6586E19EF681b1AC0ED3D46413D199a555dBB95',
  'name': 'LETSGO',
  #Name: 'Lets Go Brandon',
  'decimals': 18
},
{
  'address': '0x0f97670b863dEfb863A6865FcCA3f345f5e6eb67',
  'name': 'MOSHI',
  #Name: 'MOSHI',
  'decimals': 18
},
{
  'address': '0xC57a51780f7c1aF20212BB9F8707152039F9630d',
  'name': 'FREEDOM',
  #Name: 'EMIT1USDB Freedom Act of 2022',
  'decimals': 18
},
{
  'address': '0x37Be876EF051eB8EDdD0745107c5222D8CA8EC60',
  'name': 'EMIT1USDB',
  #Name: 'SmartBuyerBot Smart Pool Token',
  'decimals': 18
},
{
  'address': '0xac59baDC3487bdC3C077a9061F4c9c9871390153',
  'name': 'SONG',
  #Name: 'Song A Day',
  'decimals': 18
},
{
  'address': '0x704f160CD2d67cCfB19A7FC7d70b41003c0F2a3d',
  'name': 'HADA',
  #Name: 'HADA Coin',
  'decimals': 8
},
{
  'address': '0x80293dB09050Af742838CC80B061FaF7d0c7Cfb3',
  'name': 'ONE',
  #Name: 'VIKIONE',
  'decimals': 18
},
{
  'address': '0xcf0BCf85082e3CFE591bd2451Bc4B46faa34c7De',
  'name': 'Froyo',
  #Name: 'Froyo',
  'decimals': 18
},
{
  'address': '0x00D0A61c5Cb78f236A715fE08a6bB4a72514f460',
  'name': 'RONI',
  #Name: 'R0N1 World',
  'decimals': 18
},
{
  'address': '0x0E050B2B7aDb2cAe5E8593e280ed5582953f9ad2',
  'name': 'TUBBY',
  #Name: 'Tubby Cats',
  'decimals': 18
},
{
  'address': '0x189564397643D9e6173A002f1BA98da7d40a0FA6',
  'name': 'OT-wxBTRFLY-21APR2022',
  #Name: 'OT wxBTRFLY 21APR2022',
  'decimals': 9
},
{
  'address': '0x1d292aFDcc5b8bA45D461AFcCdF53bC338Dd566e',
  'name': 'MPHER',
  #Name: 'mpher',
  'decimals': 18
},
{
  'address': '0x2543822ee83e4e8F646191b7761619988907Bf11',
  'name': 'SINU',
  #Name: 'SundaeInu',
  'decimals': 9
},
{
  'address': '0x329D75f6D8A95b23B021665Db5D63e93e0F1079a',
  'name': 'OPEN',
  #Name: 'OpenSea',
  'decimals': 18
},
{
  'address': '0x3335d6EEB523738E696F2AF01071Af1746E409e7',
  'name': 'EXO',
  #Name: 'EXODA',
  'decimals': 18
},
{
  'address': '0x4dAeb4a06F70f4b1A5C329115731fE4b89C0B227',
  'name': 'QUA',
  #Name: 'Quasacoin',
  'decimals': 18
},
{
  'address': '0x4Eb8b4C65D8430647586cf44af4Bf23dEd2Bb794',
  'name': 'FPIS',
  #Name: 'Frax Price Index Share',
  'decimals': 18
},
{
  'address': '0x578300CC8db63F871643307D553E485982E4f2C1',
  'name': 'KENKA',
  #Name: 'KENKA-DO METAVERSE',
  'decimals': 18
},
{
  'address': '0x58aC163ad6726249E655cb100F8bb7CE0357cc5B',
  'name': 'BOTB',
  #Name: 'Bears On The Block',
  'decimals': 18
},
{
  'address': '0x72bE818236864c3F76bDdB005EF51C72246045C7',
  'name': 'SEED',
  #Name: 'Birdez Gang Seed',
  'decimals': 18
},
{
  'address': '0xF1f6be5468638ce9503b4BD892948e10fA5c3CbD',
  'name': 'PUFA',
  #Name: 'Platform for Underpaid Female Athletes',
  'decimals': 9
},
{
  'address': '0x875bf9be244970B8572DD042053508bF758371Ee',
  'name': 'SOLID',
  #Name: 'Solidly',
  'decimals': 18
},
{
  'address': '0xF7168715217f60244ece4e461c592DF72b5173d0',
  'name': 'TUCKER',
  #Name: 'Tucker Inu',
  'decimals': 9
},
{
  'address': '0xfb5d1A0D4C728ab9Aa80F926bcE087a760B4CBcb',
  'name': 'PLANK',
  #Name: 'Planktoons',
  'decimals': 18
},
{
  'address': '0x98b69eBB4ce228145463d7C08Aa71FBB6791fE86',
  'name': 'RKTN',
  #Name: 'Rocket Token',
  'decimals': 18
},
{
  'address': '0xa10c97bF5629340A35c41a8AA308af0804750605',
  'name': 'SOLID',
  #Name: 'Solidly',
  'decimals': 18
},
{
  'address': '0xb1a2efe104e253CB36a7b26EeAF9C20cC2C56130',
  'name': 'LENS',
  #Name: 'Lens Protocol',
  'decimals': 18
},
{
  'address': '0xCE4a410B06fc6F6728994a43789cA1B5E288d21c',
  'name': 'PUFA',
  #Name: 'Platform for Underpaid Female Athletes',
  'decimals': 9
},
{
  'address': '0xe3a7DcCf2AcdBA6c54f3e18b43D3A434272778EF',
  'name': 'SHIBSAN',
  #Name: 'Shiba San',
  'decimals': 18
},
{
  'address': '0xeA1D9fF9cA23D72aC3e8E2de2B91a161B8B9F732',
  'name': 'THORG',
  #Name: 'ThorGuards',
  'decimals': 18
},
{
  'address': '0xeB8eec5a2dBf6e6f4Cc542ad31CCe706f8f80419',
  'name': 'MEMO',
  #Name: 'MetaMEMO',
  'decimals': 18
},
{
  'address': '0xEBAd12C59BCa1239f020F534F9C9dEfe69f8730c',
  'name': 'PUFA',
  #Name: 'Platform for Underpaid Female Athletes',
  'decimals': 9
},
{
  'address': '0xF1f6be5468638ce9503b4BD892948e10fA5c3CbD',
  'name': 'PUFA',
  #Name: 'Platform for Underpaid Female Athletes',
  'decimals': 9
},
{
  'address': '0xF7168715217f60244ece4e461c592DF72b5173d0',
  'name': 'TUCKER',
  #Name: 'Tucker Inu',
  'decimals': 9
},
{
  'address': '0xfb5d1A0D4C728ab9Aa80F926bcE087a760B4CBcb',
  'name': 'PLANK',
  #Name: 'Planktoons',
  'decimals': 18
},
{
  'address': '0xe3a7DcCf2AcdBA6c54f3e18b43D3A434272778EF',
  'name': 'SHIBSAN',
  #Name: 'Shiba San',
  'decimals': 18
},
{
  'address': '0xeA1D9fF9cA23D72aC3e8E2de2B91a161B8B9F732',
  'name': 'THORG',
  #Name: 'ThorGuards',
  'decimals': 18
},
{
  'address': '0xeB8eec5a2dBf6e6f4Cc542ad31CCe706f8f80419',
  'name': 'MEMO',
  #Name: 'MetaMEMO',
  'decimals': 18
},
{
  'address': '0xEBAd12C59BCa1239f020F534F9C9dEfe69f8730c',
  'name': 'PUFA',
  #Name: 'Platform for Underpaid Female Athletes',
  'decimals': 9
},
{
  'address': '0xF3863142d2eEe19d84Cf958b09fCd5B8c65121f6',
  'name': 'FRY',
  #Name: 'Fries',
  'decimals': 18
},
{
  'address': '0xFDb258ba11aE6C1a66a283ACa8b1b848dC3E6eAE',
  'name': 'TEC',
  #Name: 'Texas Coin',
  'decimals': 18
},
{
  'address': '0x704Ebb34c391621B4725b68f71D51Aa4d7aBDa16',
  'name': 'JABS',
  #Name: 'Jabs Token',
  'decimals': 18
},
{
  'address': '0xea8301F1df4b8e34650724EDc0dB9f39e91949A5',
  'name': 'BRBX',
  #Name: 'BrandonBucks',
  'decimals': 18
},
{
  'address': '0x75084627d60b3f3be97E3E19516f3Bb2Bb2BbEEc',
  'name': 'SUD',
  #Name: 'Save Ukraine DAO',
  'decimals': 18
},
{
  'address': '0x16121F4Cf3cb8d8060d7C1eb07997895E993FEA0',
  'name': 'TFB',
  #Name: 'TFB',
  'decimals': 18
},
{
  'address': '0xC88F0F45Bf1Fc9c77A54a81b8faF380D2456168e',
  'name': 'BBGST',
  #Name: 'Baby Ghosts',
  'decimals': 18
},
{
  'address': '0x3a3e29FFB06B516A1A85da7a5EFaD22FBc7C3cB9',
  'name': 'HZN',
  #Name: 'HZN',
  'decimals': 18
},
{
  'address': '0xE80C0cd204D654CEbe8dd64A4857cAb6Be8345a3',
  'name': 'JPEG',
  #Name: 'JPEG’d Governance Token',
  'decimals': 18
},
{
  'address': '0x9e6283dff4D0F1feb2bAFA030704fAA650d43Eda',
  'name': '$ZILLA',
  #Name: 'ZillaToken',
  'decimals': 18
},
{
  'address': '0xD4D92476B8B285597Cb1dA5572aEAd575d698E0b',
  'name': 'LUCHO',
  #Name: 'Lucho Poletti Vintage Cryptoart',
  'decimals': 18
},
{
  'address': '0xa45A801187C86eE3D99b4C476207F45579D42148',
  'name': 'LOVE',
  #Name: 'UkraineDAO',
  'decimals': 18
},
{
  'address': '0x45D74446748fB432F05E7a85bD974aBB7af5C285',
  'name': 'WRAB',
  #Name: 'White Rabbit',
  'decimals': 18
},
{
  'address': '0xa4E27ea37D18bb0f483779f9E75A6024EFa5E73e',
  'name': 'MONK',
  #Name: 'Monastery',
  'decimals': 9
},
{
  'address': '0x5380442d3C4EC4f5777f551f5EDD2FA0F691A27C',
  'name': 'LOVE',
  #Name: 'UkraineDAO Flag NFT',
  'decimals': 18
},
{
  'address': '0xD7D6e57892fe8dF9109E87d5ED62AE2337e1872A',
  'name': 'SHI',
  #Name: 'Shibuya',
  'decimals': 18
},
{
  'address': '0x710Aa623c2c881b0d7357bCf9aEedf660E606C22',
  'name': 'HEART',
  #Name: 'Hearts',
  'decimals': 18
},
{
  'address': '0x7841479c5976b8184DBcde9a7a5113901b233EfB',
  'name': 'GMT',
  #Name: 'STEPN Governance Token',
  'decimals': 18
},
{
  'address': '0xB22ecDFe16BeF29cE48A63cDE0aDd3E8b536d122',
  'name': 'THUG',
  #Name: 'THUG',
  'decimals': 18
},
{
  'address': '0x2B000332CD291eF558aF76298A4d6F6001E4e015',
  'name': 'XAR',
  #Name: 'Xar',
  'decimals': 18
},
{
  'address': '0x88303FeD02b31dB9C7a9eafB711dA9eF4A03e5D3',
  'name': 'ZIK',
  #Name: 'Ziktalk',
  'decimals': 18
},
{
  'address': '0x192422D3a1a199F9DcbD2781fc462757c97409f5',
  'name': 'ZADDY',
  #Name: 'ZaddyZelenskyy',
  'decimals': 18
},
{
  'address': '0x011671956844f31620bB8B9709F32230186a307A',
  'name': 'TRTL',
  #Name: 'Turtle Town',
  'decimals': 18
},
{
  'address': '0x169D79a5b69579C96008A908797F207Fd2021287',
  'name': 'MARS',
  #Name: 'Mars Protocol Token',
  'decimals': 18
},
{
  'address': '0x089808Ecc8B3be8C4E4d9724F2a43B69F249157F',
  'name': 'ESS',
  #Name: 'Rune Essence',
  'decimals': 0
},
{
  'address': '0x20d60c6eb195868d4643f2c9B0809e4De6Cc003d',
  'name': 'PLY',
  #Name: 'PlayNity token (Wormhole)',
  'decimals': 6
},
{
  'address': '0xe0a189C975e4928222978A74517442239a0b86ff',
  'name': 'KEYS',
  #Name: 'Keys',
  'decimals': 9
},
{
  'address': '0x3Ae962Fc1D3f2c4890237E4fE04dfe3a7EaB94e5',
  'name': 'MHTN',
  #Name: 'Manhattan ',
  'decimals': 18
},
{
  'address': '0x14C556a5E779574Eb26D4F72F2A43C8064f125e7',
  'name': 'FTSHIB',
  #Name: 'Fetus Shiba Inu',
  'decimals': 9
},
{
  'address': '0x6eC24985813a985E1B20041d30E209Db38cA1e1e',
  'name': 'MICE',
  #Name: 'Anonymice',
  'decimals': 18
},
{
  'address': '0xdF589Fc5d4fBc44EB437833d4E300b1DE4ae96a9',
  'name': 'BBMICE',
  #Name: 'Baby Anonymice',
  'decimals': 18
},
{
  'address': '0x1cF4033841BfB456EB7490b34df31EC23b04b88b',
  'name': 'VAP',
  #Name: 'v4apes',
  'decimals': 18
},
{
  'address': '0xfC4E558e2F96516e8E61c6c191aeD57d0cb5A4D7',
  'name': 'LUT',
  #Name: 'LUT',
  'decimals': 18
},
{
  'address': '0x171fB81f102066e1FF575B1310A9DbEE1B0754D5',
  'name': 'TES',
  #Name: 'ThirdEyeApesv2',
  'decimals': 18
},
{
  'address': '0xaF458348c43e864aecfaCd54cF371eC3142A1d4d',
  'name': 'IRON',
  #Name: 'IRON Stablecoin (Wormhole)',
  'decimals': 18
},
{
  'address': '0x518d6CE2D7A689A591Bf46433443C31615b206C5',
  'name': 'SLP',
  #Name: 'SushiSwap LP Token',
  'decimals': 18
},
{
  'address': '0x3D7462b447f5cf13B7A055A0F8Eaf7d231Da5CeF',
  'name': 'FANG',
  #Name: 'Fang',
  'decimals': 18
},
{
  'address': '0x162945A333CFc1048BBd7180BF50203588f48d7c',
  'name': 'ESSO',
  #Name: 'Espresso Systems',
  'decimals': 18
},
{
  'address': '0x0B9a59D28869e6E52aE86c1289bc39F63ba92D50',
  'name': 'GALAXY',
  #Name: 'Chibi Galaxy',
  'decimals': 18
},
{
  'address': '0xaC8477812146eb215fF9Ec4a0198973300Ac4BD2',
  'name': 'MANNYS',
  #Name: 'mannys.game',
  'decimals': 18
},
{
  'address': '0x30D20208d987713f46DFD34EF128Bb16C404D10f',
  'name': 'SD',
  #Name: 'Stader',
  'decimals': 18
},
{
  'address': '0x415282ac4420d3c3c2D4111f932bC71D6d385Fd0',
  'name': 'BEAR',
  #Name: 'PhantaBear',
  'decimals': 18
},
{
  'address': '0x8226b146C3f50594E7493f726F1bbAA446F15fD8',
  'name': 'SAGE',
  #Name: 'Sage Coin',
  'decimals': 4
},
{
  'address': '0x36AbFfa6255507618e9eb8d707E9fC6Bd5457d4C',
  'name': 'GOWSA',
  #Name: 'CryptoCelestials',
  'decimals': 18
},
{
  'address': '0x09F098B155D561Fc9F7BcCc97038b7e3d20bAF74',
  'name': 'ZOO',
  #Name: 'ZooDAO',
  'decimals': 18
},
{
  'address': '0x0B211CdE9e2420b97AbdF1eCD5B063be97543FE6',
  'name': 'TPGEN',
  #Name: 'ToastPunk Genesis',
  'decimals': 18
},
{
  'address': '0x227c7DF69D3ed1ae7574A1a7685fDEd90292EB48',
  'name': 'MILADY',
  #Name: 'Milady Maker',
  'decimals': 18
},
{
  'address': '0x7aBbC18ef3e01b8B93Cf236A6d68DFc35c5E48Aa',
  'name': 'TPC',
  #Name: 'TeamPizza',
  'decimals': 18
},
{
  'address': '0xAB2A7B5876D707e0126B3A75EF7781c77c8877EE',
  'name': 'QUAD',
  #Name: 'Quadency Token',
  'decimals': 18
},
{
  'address': '0x38D3c259cB5CBb8b5b4Bf263E3934f12a0128d7c',
  'name': 'PNFTC',
  #Name: 'PottersNFTCorporation (pottersnft.io)',
  'decimals': 18
},
{
  'address': '0x4d224452801ACEd8B2F0aebE155379bb5D594381',
  'name': 'APE',
  #Name: 'ApeCoin',
  'decimals': 18
},
{
  'address': '0x53A1E9912323B8016424D6287286E3b6de263F76',
  'name': 'PTT',
  #Name: 'PUTIN Token',
  'decimals': 18
},
{
  'address': '0xA75a25AEef83e643F716536B882BB633C4ED6E93',
  'name': 'ADD',
  #Name: 'Ape Dividend Distributoooor',
  'decimals': 18
},
{
  'address': '0x79F6828C1bD4A3b67f515d260E6f743d2ae28566',
  'name': 'PHPC',
  #Name: 'PHPC ERC20 STABLECOIN',
  'decimals': 18
},
{
  'address': '0x1738ACd3323f5Bd9b0c760b2871d0F0876116a87',
  'name': 'TOEKEN',
  #Name: 'Toeken',
  'decimals': 18
},
            {
                'name': 'mimatic',
                'address': '0xa3Fa99A148fA48D14Ed51d610c367C61876997F1',
                'decimals': 18,
            },
            {
                'name': 'FISH',
                'address': '0x3a3Df212b7AA91Aa0402B9035b098891d276572B',
                'decimals': 18,
            },
            {
                'name': 'bct',
                'address': '0x2F800Db0fdb5223b3C3f354886d907A671414A7F',
                'decimals': 18,
            },
            {
                'name': 'dpi',
                'address': '0x2F800Db0fdb5223b3C3f354886d907A671414A7F',
                'decimals': 18,
            },
           {
               'name': 'frax',
               'address': '0x45c32fA6DF82ead1e2EF74d17b76547EDdFaFF89',
               'decimals': 18,
           },
           {
               'name': 'ghst',
               'address': '0x385Eeac5cB85A38A9a07A70c73e0a3271CfB54A7',
               'decimals': 18,
           },
           {
               'name': 'grt',
               'address': '0x5fe2B58c013d7601147DcdD68C143A77499f5531',
               'decimals': 18,
            },
           {
               'name': 'iron',
               'address': '0xD86b5923F3AD7b585eD81B448170ae026c65ae9a',
               'decimals': 18,
           },
           {
               'name': 'klima',
               'address': '0xd50EC6360f560a59926216Eafb98395AC430C9fD',
               'decimals': 18,
           },
           {
               'name': 'nexo',
               'address': '0x41b3966B4FF7b427969ddf5da3627d6AEAE9a48E',
               'decimals': 18,
           },
           {
               'name': 'sand',
               'address': '0xBbba073C31bF03b8ACf7c28EF0738DeCF3695683',
               'decimals': 18,
           },
           {
               'name': 'WBtc',
               'address': '0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6',
               'decimals': 8,
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
            { 
                'name': 'USDT',
                'address': '0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
                'decimals': 6,
            },    
             
        ],
        'sides' : [
            {
                'name': 'WBTC',
                'address': '0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6',
                'decimals': 8,
                'minAmount':0.00000049 ,
            },
            {
                'name': 'QUICK',
                'address': '0x831753DD7087CaC61aB5644b308642cc1c33Dc13',
                'decimals': 18,
                'minAmount':0.00005385899714547316 ,
            },
            {
                'name': 'AAVE',
                'address': '0xD6DF932A45C0f255f85145f286eA0b292B21C90B',
                'decimals': 18,
                'minAmount':0.00005566069241901369 ,
            },
            {
                'name': 'SUSHI',
                'address': '0x0b3F868E0BE5597D5DB7fEB59E1CADBb0fdDa50a',
                'decimals': 18,
                'minAmount':0.002770083102493075 ,
            },
            {
                'name': 'DFYN',
                'address': '0xC168E40227E4ebD8C1caE80F7a55a4F0e6D66C97',
                'decimals': 18,
                'minAmount':0.1330795949057131 ,
            },
            {
                'name': 'BIFI',
                'address': '0xFbdd194376de19a88118e84E279b977f165d01b8',
                'decimals': 18,
                'minAmount':0.000006681678170289249 ,
            },
            {
                'name': 'AVAX',
                'address': '0x2C89bbc92BD86F8075d1DEcc58C7F4E0107f286b',
                'decimals': 18,
                'minAmount':0.00013005592404734037 ,
            },
            {
                'name': 'ADDY',
                'address': '0xc3FdbadC7c795EF1D6Ba111e06fF8F16A20Ea539',
                'decimals': 18,
                'minAmount':0.0175695049616282 ,
            },
            {
                'name': 'BAL',
                'address': '0x9a71012B13CA4d3D0Cdc72A177DF3ef03b0E76A3',
                'decimals': 18,
                'minAmount':0.0006321112515802782 ,
            },
            {
                'name': 'LINK',
                'address': '0x53E0bca35eC356BD5ddDFebbD1Fc0fD03FaBad39',
                'decimals': 18,
                'minAmount':0.000723589001447178 ,
            },
            {
                'name': 'UNI',
                'address': '0xb33EaAd8d922B1083446DC23f610c2567fB5180f',
                'decimals': 18,
                'minAmount':0.0011001100110011 ,
            },
            {
                'name': 'MANA',
                'address': '0xA1c57f48F0Deb89f569dFbE6E2B7f46D33606fD4',
                'decimals': 18,
                'minAmount':0.004830917874396136 ,
            },
            {
                'name': 'UST',
                'address': '0x692597b009d13C4049a947CAB2239b7d6517875F',
                'decimals': 18,
                'minAmount':0.01 ,
            },
            {
                'name': 'CRV',
                'address': '0x172370d5Cd63279eFa6d502DAB29171933a610AF',
                'decimals': 18,
                'minAmount':0.004405286343612335 ,
            },
            {
                'name': 'SAND',
                'address': '0xBbba073C31bF03b8ACf7c28EF0738DeCF3695683',
                'decimals': 18,
                'minAmount':0.0035714285714285718 ,
            },
            {
                'name': 'COMP',
                'address': '0x8505b9d2254A7Ae468c0E9dd10Ccea3A837aef5c',
                'decimals': 18,
                'minAmount':0.00007208246233691344 ,
            },
            {
                'name': 'SNX',
                'address': '0x50B728D8D964fd00C2d0AAD81718b71311feF68a',
                'decimals': 18,
                'minAmount':0.0016750418760469012 ,
            },
            {
                'name': '1INCH',
                'address': '0x9c2C5fd7b07E95EE044DDeba0E97a665F142394f',
                'decimals': 18,
                'minAmount':0.006329113924050633 ,
            },
            {
                'name': 'YFI',
                'address': '0xDA537104D6A5edd53c6fBba9A898708E465260b6',
                'decimals': 18,
                'minAmount':0.0000005250606182483769 ,
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
