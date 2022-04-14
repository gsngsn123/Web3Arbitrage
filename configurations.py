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
                'name': 'DAI',
                'address': '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063',
                'decimals': 18,
                'minAmount':1,
            },    
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
