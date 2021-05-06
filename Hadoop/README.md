# Analysis Approach 

At its core the Ethereum blockchain is an immutable distributed ledger. However, creator Vitalik Buterin extended its set of capabilities by including a virtual machine that can execute arbitrary code stored on the blockchain as smart contracts. This makes the ethereum blockchain notably distinct from other blockchain datasets.

- The Ethereum blockchain’s primary crypto-economic unit of value is Ether. However, the majority of value transfer on the Ethereum blockchain is composed of so-called tokens. Tokens are created and managed by smart contracts.

- Ether value transfers are precise and direct, resembling accounting ledger debits and credits.

- Addresses can be not only be wallets that hold balances, but can also contain smart contract bytecode that allows the programmatic creation of agreements and automatic triggering of their execution. An aggregate of coordinated smart contracts could be used to build a decentralized autonomous organization.

Taking all of these points into consideration, we set out to find patterns in the dataset beginning from November 2019 which was a few months prior to the onset of COVID-19. 

## Limitations of the Dataset 

- The Ethereum dataset is huge in size with multiple tables having over 100gb in size. This makes it difficult to run in memory operations in PySpark or Hadoop.
- The Ethereum Dataset is mostly comprimised of data that is machine generated in the form of hashes and bytecode. This makes it difficult to intuitively make assumptions on the data but that also makes analysis of this type of data that much more important.

## Assumptions on the dataset

Some of the assumptions on the dataset prior to analysis:

- The number of transactions would increase with increase in the price of ethereum.
- The number of miners joining the network would increase with the price increase of ethereum, thereby increasing the hashing power of the network which will subsequently increase the difficulty of the network.
- Contract complexity should increase overtime with more indivisuals figuring out new ways to make more complex applications on ethereum.
- The Top tokens traded on the network will be some variation of the US dollar backed token. These are also called stable coins.

# Tools Used

The Ethereum dataset used for this analysis was
collected from the dumps uploaded to a repository on
Google’s BigQuery, now available as a public dataset. The
dataset was uploaded to a NYU Hadoop cluster and stored in
HDFS.

Due to its high speed and performance, Hadoop mapReduce was used to process the dataset (in order of 100 of GBs). 


# Time Analysis

In this section we did Time Analysis of the data on different metrics like Transactions, Amount Transferred, Gas Prices, Gas Used by contracts and the Complexity of contracts over time.

## Part A - Total Number of Transactions Per Day


<img align="center" width="100%" height="100%" src="https://i.ibb.co/jVV6vkZ/G1.png">

<br>
<br>

A general trend that has been observed is that the number of transaction increases with time. The same trend can be obeserved with the price. The price of the asset went to an all time low around March of 2020 this was in occardance with the stock market at the time. During this time Lockdown was enforced in most countries, and the stock market fell in reaction.

The price then continued to rise far surpassing its previous all time high.

One of our intial assumptions was that the number of transactions would increase with price and while that trend did hold true in the beginnning the number of transactions then flatlined torwards the end while the price was still increasing exponentially. This could be potentially attributed to the fact that during this time period there was an ongoing [ethereum 2.0 staking program](https://ethereum.org/en/eth2/). Ethereum is planning on migratiting its infastructure from proof-of-work to proof-of-stake , this migration involves locking up ETH in a smart contract, which is also known as staking. Since a large portion of ETH is locked up in this contract the supply of ETH in the network reduces leading to decrease in the rate of transactions and increase in price.


## Part B - Average Transaction Amount Per Day

<img align="center" width="100%" height="100%" src="https://i.ibb.co/Zf9bSbp/G2.png">
<br>
<br>
The monthwise total transactions gives an intresting overview of the total amount of Ether that was transferred between addresses every month. We observe during the month of march in 2020 alot of transactions were taking place. This could be attributed to the fact that alot of Ether was moving to exchanges to be sold off causing the dip in price to all time low levels.
<br>
<br>
Later on in the year we observe a large amount of value transfered in the months of August,September and October. This is when alot of new protocols were developed on top of ethereum. These allowed peer-to-peer trading within smart contracts and even evolved to the extent that a new ecosystem of unique passive income-generating projects can be easily accessed by any address with ether in it. This period of time is known collectively as "DEFI SUMMER" by the crypto community. DEFI referes to Decentralized Finance .Decentralized finance is a system by which financial products become available on a public decentralized blockchain network, making them open to anyone to use, rather than going through middlemen like banks or brokerages. 
<br>
<br>
Torwards the end of the year we see another surge in total amount of ether transferred. The rapid increase in price and the beginning of the staking program probably lead to large amount of ether being transferred from exchange wallets to user wallets.
<br>
<br>

## Part C - Average Gas Price Per Day

<img align="center" width="100%" height="100%" src="https://i.ibb.co/JyNY7g6/G3.png">
<br>
<br>

On the Ethereum blockchain, gas refers to the cost necessary to perform a transaction on the network.
Miners set the price of gas based on supply and demand for the computational power of the network needed to process smart contracts and other transactions.       
      
In the chart above we outline the the change in gas price over the specified time period. Immediately we notice huge outliers, particularly the spike in june. When researching the cause for this, we came across a transaction that paid 10,668 Ether or 2.6 Million dollars at the time in gas fees due to a [mistake](https://decrypt.co/31830/someone-just-made-a-2-6-million-mistake-on-ethereum).

Then beginning from august to october we saw another rise in gas prices primarily due to increased user activity on newly created DEFI protocals. With More people interacting with contracts, users had to bid higher gas for their transaction to get completed. The term "front-running" was coined during this phase, it refers to act of getting a transaction first in line in the execution queue, right before a known future transaction occurs.This happens because bots are able to bid a slightly higher gas price on a transaction, incentivizing miners to place earlier in the order when constructing the block. The higher-paying transactions are executed first. Thus, if two transactions making a profit from the same contract call are placed in the same block, only the first takes the profit. During DEFI Summer alot of these front running transactions took place which is why we observe spikes in the data.

Torwards the end of the year the gas price continued to rise again because more users were using the network. With the price of ethereum constantly rising more people were getting intrested in ethereum and subsequently there was more user activity with contracts on the network.

## Part D - Contract Gas Per Day

The Gas used for contract creation tended to increased with time, pointing to the fact that contracts are becoming much more complex, in particular during "DEFI SUMMER" alot of the complex contracts were created which is why the gas requirments of these contracts was so high.

## Part E - Complexity Over Time

Ethereum Network difficulty is the difficulty of a problem that miners must solve to find a block. The more miners are mining Ethereum the more difficult it is to find the block to be rewarded.
Ethereum has the preset average block find time managed by a network(around 10mins). If the number of miners increases, the network hashrate goes up. The effective block find time becomes lower than the preset value. As a result, the network gradually increases its difficulty, that is, the difficulty of a problem that miners are solving. The network will keep increasing it until the block find time reaches the preset value.
Same thing when the number of miners decreases. When miners leave, the network hashrate goes down. Miners need more time to find a block. So the network lowers its difficulty, thus making a problem easier to solve.

What we observe with ethereum is that the network difficulty has continued to rise throughout the year, meaning more and more people are joining the network as miners.


# Contract Analysis

##  PART A - Top 20 Contracts with Most Value Transferred

```
| Address                                    | Total Amount Transferred   |
|--------------------------------------------|----------------------------|
| 0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f | 15272176801115294667690218 |
| 0x398ec7346dcd622edc5ae82352f02be94c62d119 | 6739837306218646155454747  |
| 0x111111125434b319222cdbf8c261674adb56f3ae | 4636875933761345329405440  |
| 0xd06527d5e56a3495252a528c4987003b712860ee | 3373044666886447787682595  |
| 0xc83e009c7794e8f6d1954dc13c23a35fc4d039f6 | 3343452240000000000000001  |
| 0x67b66c99d3eb37fa76aa3ed1ff33e8e39f0b9c7a | 2564559210392379429295341  |
| 0x00000000219ab540356cbb839cbe05303d7705fa | 2494123495428587780437332  |
| 0x2b591e99afe9f32eaa6214f7b7629768c40eeb39 | 2366998339242551619634563  |
| 0xc61b9bb3a7a0767e3179713f3a5c7a9aedce193c | 2360001000604813220000000  |
| 0xfa103c21ea2df71dfb92b0652f8b1d795e51cdef | 2161974576997272400000911  |
| 0x26aad4d82f6c9fa6e34d8c1067429c986a055872 | 1630749171748989118130898  |
| 0xd848f54280f8fe8661b796e3bb8d8922c87af452 | 1497010000000000000000000  |
| 0x91db9e27e750c43a96926b2e04d795c24f13f67b | 1161144975076891415819264  |
| 0x03f34be1bf910116595db1b11e9d1b2ca5d59659 | 1146247549340220000000000  |
| 0xdcd33426ba191383f1c9b431a342498fdac73488 | 1126619429158447351876951  |
| 0xdef1c0ded9bec7f1a1670819833240f027b25eff | 1115286839252554366157905  |
| 0x3e66b66fd1d0b02fda6c811da9e0547970db2f21 | 1000691537146885150012207  |
| 0x6a11f3e5a01d129e566d783a7b6e8862bfd66cca | 831475449811730739256272   |
| 0xf164fc0ec4e93095b804a4795bbe1e041497b92a | 823225555842111522886730   |
| 0x3ad412055f123f6b596deb290417e182ee192fb2 | 818463000000000000000000   |
```

The analysis of the top contracts reveal that most of the top contracts are DEFI protocals.  
 The first entry is the contact address of `Sushiswap` which is an automated market maker i.e peer-to-peer trading platform .    
  The second entry is the contact address of `AAVE` which is borrowing and lending platform on the blockchain.     
 The third entry is `1.inch` which is an aggregator of various automated market makers to find the best price for trading.

## PART B - Top 20 ERC-20 Token Transfers

```
| Address                                    | Total Transfers |
|--------------------------------------------|-----------------|
| 0xdac17f958d2ee523a2206206994597c13d831ec7 | 89495941        |
| 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2 | 39042226        |
| 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 | 14223564        |
| 0x6b175474e89094c44da98b954eedeac495271d0f | 8632879         |
| 0x0e3a2a1f2146d86a604adc220b4967a898d7fe07 | 7974877         |
| 0x514910771af9ca656af840dff83e8264ecf986ca | 7083902         |
| 0x629cdec6acc980ebeebea9e5003bcd44db9fc5ce | 6592487         |
| 0x8e870d67f660d95d5be530380d0ec0bd388289e1 | 2819625         |
| 0xe62e6e6c3b808faad3a54b226379466544d76ea4 | 2716504         |
| 0x1f9840a85d5af5bf1d1762f925bdaddc4201f984 | 2225559         |
| 0xac08809df1048b82959d6251fbc9538920bed1fa | 2113359         |
| 0x0000000000004946c0e9f43f4dee607b0ef1fa1c | 1932534         |
| 0x6b3595068778dd592e39a122f4f5a5cf09c90fe2 | 1835973         |
| 0x0d8775f648430679a709e98d2b0cb6250d2887ef | 1725755         |
| 0xa821f14fb6394e82839f5161f214cacc90372453 | 1586488         |
| 0x2b591e99afe9f32eaa6214f7b7629768c40eeb39 | 1529866         |
| 0x2260fac5e5542a773aa44fbcfedf7c193bc2c599 | 1506856         |
| 0xa3f440ef604a6380a030360f85bb0dedb6db5a85 | 1335390         |
| 0xc12d1c73ee7dc3615ba4e37e4abfdbddfa38907e | 1300357         |
| 0xc00e94cb662c3520282e6f5717214004a7f26888 | 1207822         |
```

One of the most significant Ethereum tokens is known as ERC-20. ERC-20 has emerged as the technical standard; it is used for all smart contracts on the Ethereum blockchain for token implementation and provides a list of rules that all Ethereum-based tokens must follow.

The first entry is the address of `USDT` or tether which is Dollar backed crypto currency, also know as a "stablecoin".      
The second entry is the address of `WETH` or Ether that has been wrapped to conform to the ERC-20 standard. WETH can be unwrapped to give back ETH.
The third entry is `USDC` which is another US Dollar backed stable coin.
The Fourth entry is `DAI` which is an algortihmically backed stable coin.

From this we begin to see that most of the transaction of tokens that take place are with respect to these stable coins and that makes sense because even on decentralized exchanges like sushiswap trading will be done with respect to dollar which is why the number of transactions for these tokens are so high.

## PART C - Top 20 ERC-721 Token Transfers

```
| Address                                    | Total Transfers |
|--------------------------------------------|-----------------|
| 0xf915bbfbb6c097dc327e64eec55e9ef4d110d627 | 78117           |
| 0x812b17908972e3db860247303dd041312b821e0e | 2037            |
| 0xdb7e971d39367b20bcf4df5ae2da0fa4261bf0e8 | 893             |
| 0x60f3680350f65beb2752788cb48abfce84a4759e | 861             |
| 0xac92356226e31fe91810e48c0706daccf9cfe467 | 665             |
| 0xc4aeb6cdfac2dc870bb8ac00cc9049319e5d0bf8 | 603             |
| 0x9c260150c240611e62fc9ba7693e4fe2be16ef61 | 543             |
| 0x31019a4b0b32bdd2a8c0e9a91c9b5e8067740685 | 508             |
| 0x69c1ca6a60fc703ea5f48d37f08cace6cb0a4a6f | 471             |
| 0x395e5461693e0bb5ec78302605030050f69e628d | 459             |
| 0x65a92c6d14f1fa251bf17be232ce43381f18a14a | 456             |
| 0x3ad503084f1bd8d15a7f5ebe7a038c064e1e3fa1 | 421             |
| 0x1073c94a9c54165a8b8de32a6ff0204bbf3fcf6c | 420             |
| 0x08ffa05e1f22e3081914af04e3c093385c7bbaa7 | 417             |
| 0x9048583bd410526ca16f0d270a5836dbdea92033 | 403             |
| 0x476eda02bf0c35603fd6e0306cf85381029f90f1 | 343             |
| 0x4c100f1e9178f209dc99575f315be1ef99330dd3 | 340             |
| 0x0ac4b59aa9c320e556a1e19176ef61eebdfacd25 | 334             |
| 0x4e5377b725fbb319c1e0ccd06b382772839ababa | 255             |
```

ERC721 is a token standard on Ethereum for Non-Fungible Tokens (NFT). Fungible means interchangeable and replaceable so something like Ethereum is fungible because any Ethereum can replace another Ethereum. Each NFT, on the other hand, is completely unique. One NFT cannot replace another.



# Other Analysis 


## Price Comparison With Gold

<img align="center" width="100%" height="100%" src="https://i.ibb.co/d54XMYD/G4.png">
<br>
<br>

Looking at the prices of both gold and Ethereum, it is apparent that Ethereum has been rising at a high pace compared to gold and even other assets like stocks. gold currently has a market cap of 11 trillion dollars, at its current price ethereum has a market cap of 400 billion dollars. If Ethereum as a currency reaches a market cap of atleast 1 trillion dollars which is 10% of gold. Its current price will go up 250% from here, which makes it a much more lucrative investment compared to gold.
