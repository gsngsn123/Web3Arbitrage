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
      'name': "MEME",
      'address': "0xf2b5a8c37278bcdd50727d5ca879f8e5a4642e2e",
      'decimals': 8,
      
    },
    {
      'name': "SUPER",
      'address': "0xa1428174f516f527fafdd146b883bb4428682737",
      'decimals': 18,
      
    },
    {
    {
      'name': "mUSD",
      'address': "0xe840b73e5287865eec17d250bfb1536704b43b21",
      'decimals': 18,
      
    },
    {
      'name': "renBTC",
      'address': "0xDBf31dF14B66535aF65AaC99C32e9eA844e14501",
      'decimals': 18,
      
    },
    {
      'name': "DfynWMATIC",
      'address': "0x4c28f48448720e9000907BC2611F73022fdcE1fA",
      'decimals': 18,
      
    },
    {
      'name': "HAWK",
      'address': "0x69cbc7449ee102eb792f1656744bf1a7c1bacb7e",
      'decimals': 18,
      
    },
    {
      'name': "BPT",
      'address': "0x6863BD30C9e313B264657B107352bA246F8Af8e0",
      'decimals': 18,
      
    },
    {
      'name': "amAAVE",
      'address': "0x1d2a0E5EC8E5bBDCA5CB219e649B565d8e5c3360",
      'decimals': 18,
      
    },
    {
      'name': "amDAI",
      'address': "0x27F8D03b3a2196956ED754baDc28D73be8830A6e",
      'decimals': 18,
      
    },
    {
      'name': "amUSDC",
      'address': "0x1a13F4Ca1d028320A707D99520AbFefca3998b7F",
      'decimals': 6,
      
    },
    {
      'name': "amUSDT",
      'address': "0x60D55F02A771d515e077c9C2403a1ef324885CeC",
      'decimals': 6,
      
    },
    {
      'name': "amWBTC",
      'address': "0x5c2ed810328349100A66B82b78a1791B101C9D61",
      'decimals': 8,
      
    },
    {
      'name': "amWETH",
      'address': "0x28424507fefb6f7f8E9D3860F56504E4e5f5f390",
      'decimals': 18,
      
    },
    {
      'name': "amWMATIC",
      'address': "0x8dF3aad3a84da6b69A4DA8aeC3eA40d9091B2Ac4",
      'decimals': 18,
    
    },
    {
      'name': "BTU",
      'address': "0xfdc26cda2d2440d0e83cd1dee8e8be48405806dc",
      'decimals': 18,
    
    },
    {
      'name': "$DG",
      'address': "0x2a93172c8dccbfbc60a39d56183b7279a2f647b4",
      'decimals': 18,
    
    },
    {
      'name': "0xBTC",
      'address': "0x71b821aa52a49f32eed535fca6eb5aa130085978",
      'decimals': 8,
    
    },
    {
      'name': "AGA",
      'address': "0x033d942a6b495c4071083f4cde1f17e986fe856c",
      'decimals': 4,
    
    },
    {
      'name': "AGAr",
      'address': "0xf84bd51eab957c2e7b7d646a3427c5a50848281d",
      'decimals': 8,
    
    },
    {
      'name': "ARIA20",
      'address': "0x46f48fbdedaa6f5500993bede9539ef85f4bee8e",
      'decimals': 18,
    
    },
    {
      'name': "AZUKI",
      'address': "0x7cdc0421469398e0f3aa8890693d86c840ac8931",
      'decimals': 18,
    
    },
    {
      'name': "CC10",
      'address': "0x9c49ba0212bb5db371e66b59d1565b7c06e4894e",
      'decimals': 18,
    
    },
    {
      'name': "CEL",
      'address': "0xd85d1e945766fea5eda9103f918bd915fbca63e6",
      'decimals': 4,
    
    },
    {
      'name': "CFI",
      'address': "0xecf8f2fa183b1c4d2a269bf98a54fce86c812d3e",
      'decimals': 18,
    
    },
    {
      'name': "CTSI",
      'address': "0x2727ab1c2d22170abc9b595177b2d5c6e1ab7b7b",
      'decimals': 18,
    
    },
    {
      'name': "DB",
      'address': "0x0e59d50add2d90f5111aca875bae0a72d95b4762",
      'decimals': 18,
    
    },
    {
      'name': "DEFI5",
      'address': "0x42435f467d33e5c4146a4e8893976ef12bbce762",
      'decimals': 18,
    
    },
    {
      'name': "DEGEN",
      'address': "0x8a2870fb69a90000d6439b7adfb01d4ba383a415",
      'decimals': 18,
    
    },
    {
      'name': "DMT",
      'address': "0xd28449bb9bb659725accad52947677cce3719fd7",
      'decimals': 18,
    
    },
    {
      'name': "DRC",
      'address': "0xfed16c746cb5bfed009730f9e3e6a673006105c7",
      'decimals': 0,
    
    },
    {
      'name': "DSLA",
      'address': "0xa0e390e9cea0d0e8cd40048ced9fa9ea10d71639",
      'decimals': 18,
    
    },
    {
      'name': "EASY",
      'address': "0xdb3b3b147a030f032633f6c4bebf9a2fb5a882b5",
      'decimals': 18,
    
    },
    {
      'name': "ELET",
      'address': "0x07738eb4ce8932ca961c815cb12c9d4ab5bd0da4",
      'decimals': 18,
    
    },
    {
      'name': "ETH",
      'address': "0x7ceb23fd6bc0add59e62ac25578270cff1b9f619",
      'decimals': 18,
    
    },
    {
      'name': "GAME",
      'address': "0x8d1566569d5b695d44a9a234540f68d393cdc40d",
      'decimals': 18,
    
    },
    {
      'name': "HEX",
      'address': "0x23d29d30e35c5e8d321e1dc9a8a61bfd846d4c5c",
      'decimals': 8,
    
    },
    {
      'name': "HH",
      'address': "0x521cddc0cba84f14c69c1e99249f781aa73ee0bc",
      'decimals': 18,
    
    },
    {
      'name': "IGG",
      'address': "0xe6fc6c7cb6d2c31b359a49a33ef08ab87f4de7ce",
      'decimals': 6,

    },
    {
      'name': "JULIEN",
      'address': "0x268ad27c28601d28b79c792c14e95bd2b7a030f8",
      'decimals': 4,
    
    },
    {
      'name': "LEND",
      'address': "0x313d009888329c9d1cf4f75ca3f32566335bd604",
      'decimals': 18,
    
    },
    {
      'name': "MONA",
      'address': "0x6968105460f67c3bf751be7c15f92f5286fd0ce5",
      'decimals': 18,
    
    },
    {
      'name': "NDR",
      'address': "0xfb65ef42f7c8a70ff73f627db6e9ba2aff1f20fa",
      'decimals': 18,
    
    },
    {
      'name': "OM",
      'address': "0xc3ec80343d2bae2f8e680fdadde7c17e71e114ea",
      'decimals': 18,
    
    },
    {
      'name': "PICKLE",
      'address': "0x2b88ad57897a8b496595925f43048301c37615da",
      'decimals': 18,
    
    },
    {
      'name': "PPDEX",
      'address': "0x127984b5e6d5c59f81dacc9f1c8b3bdc8494572e",
      'decimals': 18,
    
    },
    {
      'name': "RBAL",
      'address': "0x03247a4368a280bec8133300cd930a3a61d604f6",
      'decimals': 18,
    
    },
    {
      'name': "SDT",
      'address': "0x361a5a4993493ce00f61c32d4ecca5512b82ce90",
      'decimals': 18,
    
    },
    {
      'name': "SENT",
      'address': "0x48e3883233461c2ef4cb3fcf419d6db07fb86cea",
      'decimals': 8,
    
    },
    {
      'name': "SUSHI",
      'address': "0x0b3f868e0be5597d5db7feb59e1cadbb0fdda50a",
      'decimals': 18,
    
    },
    {
      'name': "SWAP",
      'address': "0x3809dcdd5dde24b37abe64a5a339784c3323c44f",
      'decimals': 18,
    
    },
    {
      'name': "SWG",
      'address': "0x043a3aa319b563ac25d4e342d32bffb51298db7b",
      'decimals': 18,
    
    },
    {
      'name': "SX",
      'address': "0x840195888db4d6a99ed9f73fcd3b225bb3cb1a79",
      'decimals': 18,
    
    },
    {
      'name': "UBT",
      'address': "0x7fbc10850cae055b27039af31bd258430e714c62",
      'decimals': 8,
    },
    {
      'name': "WISE",
      'address': "0xb77e62709e39ad1cbeebe77cf493745aec0f453a",
      'decimals': 18,
     
    },
    {
      'name': "WOLF",
      'address': "0x8f18dc399594b451eda8c5da02d0563c0b2d0f16",
      'decimals': 9,
     
    },
    {
      'name': "WRX",
      'address': "0x72d6066f486bd0052eefb9114b66ae40e0a6031a",
      'decimals': 8,
     
    },
    {
      'name': "ZUT",
      'address': "0xe86e8beb7340659dddce61727e500e3a5ad75a90",
      'decimals': 18,
     
    },
    {
      'name': "ZUZ",
      'address': "0x232eab56c4fb3f84c6fb0a50c087c74b7b43c6ad",
      'decimals': 18,
     
    },
    {
      'name': "bBADGER",
      'address': "0x2628d301b161db70e3dbbac88d9d900ca426ff02",
      'decimals': 18,
     
    },
    {
      'name': "bDIGG",
      'address': "0xfdde616084427f0a231d0664a985e1f820e34693",
      'decimals': 18,
     
    },
    {
      'name': "eDAI",
      'address': "0xa1c09c8f4f5d03fcc27b456475d53d988e98d7c5",
      'decimals': 8,
     
    },
    {
      'name': "eUSDC",
      'address': "0x4ebde54ba404be158262ede801744b92b9878c61",
      'decimals': 8,
     
    },
    {
      'name': "eUSDT",
      'address': "0xfc39742fe9420a7af23757fc7e78d1c3ae4a9474",
      'decimals': 8,
     
    },
    {
      'name': "iFARM",
      'address': "0xab0b2ddb9c7e440fac8e140a89c0dbcbf2d7bbff",
      'decimals': 18,
     
    },
    {
      'name': "mDEF",
      'address': "0x82b6205002ecd05e97642d38d61e2cfeac0e18ce",
      'decimals': 9,
     
    },
    {
      'name': "mOCEAN",
      'address': "0x282d8efce846a88b159800bd4130ad77443fa1a1",
      'decimals': 18,
     
    },
    {
      'name': "mRBAL",
      'address': "0x66768ad00746ac4d68ded9f64886d55d5243f5ec",
      'decimals': 18,
     
    },
    {
      'name': "maAAVE",
      'address': "0x823cd4264c1b951c9209ad0deaea9988fe8429bf",
      'decimals': 18,
     
    },
    {
      'name': "maDAI",
      'address': "0xe0b22e0037b130a9f56bbb537684e6fa18192341",
      'decimals': 18,
     
    },
    {
      'name': "maLINK",
      'address': "0x98ea609569bd25119707451ef982b90e3eb719cd",
      'decimals': 18,
     
    },
    {
      'name': "maTUSD",
      'address': "0xf4b8888427b00d7caf21654408b7cba2ecf4ebd9",
      'decimals': 18,
     
    },
    {
      'name': "maUNI",
      'address': "0x8c8bdbe9cee455732525086264a4bf9cf821c498",
      'decimals': 18,
     
    },
    {
      'name': "maUSDC",
      'address': "0x9719d867a500ef117cc201206b8ab51e794d3f82",
      'decimals': 6,
     
    },
    {
      'name': "maUSDT",
      'address': "0xdae5f1590db13e3b40423b5b5c5fbf175515910b",
      'decimals': 6,
     
    },
    {
      'name': "maWETH",
      'address': "0x20d3922b4a1a8560e1ac99fba4fade0c849e2142",
      'decimals': 18,
     
    },
    {
      'name': "maYFI",
      'address': "0xe20f7d1f0ec39c4d5db01f53554f2ef54c71f613",
      'decimals': 18,
     
    },
    {
      'name': "sd3Crv",
      'address': "0x87f0bfee4435ce2b8643b221d0c1cad21f5328b4",
      'decimals': 18,
     
    },
    {
      'name': "sdcrvRenWSBTC",
      'address': "0xe212f92e5af85268b33d2aa587b51f49c3b945be",
      'decimals': 18,
     
    },
    {
      'name': "sdeursCRV",
      'address': "0xfbdb45075fb73ca4cc8b83fd6fdb4f9b696b1ba1",
      'decimals': 18,
     
    },
    {
      'name': "xMARK",
      'address': "0xf153eff70dc0bf3b085134928daeea248d9b30d0",
      'decimals': 9,
     
    },
    {
      'name': "xSDT",
      'address': "0xd921f8318cfd786bab1ea7492673f053c518ac04",
      'decimals': 18,
     
    },
  

            {
                'name': 'mimatic',
                'address': '0xa3Fa99A148fA48D14Ed51d610c367C61876997F1',
                'decimals: 18,
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
               'name': 'fxs',
               'address': 'fxs',
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
             {
                 'name': 'DAI'
                 'address': '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063',
                 'decimals': 18,
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
