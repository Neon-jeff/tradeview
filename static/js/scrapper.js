   const url = `https://redstone.p.rapidapi.com/prices?provider=redstone&symbols=1INCH,AAVE,ALGO,ANC,APE,AURORA,AXS,BTG,ADA,XCN,LINK,CRO,DAI,DAO,DASH,MANA,DFL,ETC,EVMOS,GT,LN,XMR,NEXO,OKB,OP,OGN,ORN,DOT,XPR,RARI,SFP,SHIB,XLM,GMT,SUSHI,TLOS,XTZ,GRT,TRX,UNI,VET,WING,WXT,TIME,ZEC,ZIG,XRP,AVAX,BCH,BTC,DOGE,ETH,LTC,MATIC,SOL,USDT,ICP,LUNA,LUNC,RUNE,ATOM,BNB,KCS,FTM,ASTR,SAND,NEO,CAKE,XEC,FTT,NEXO,HT,GAS,USDP,MAGIC,DESO,FLOKI,BAND,DCR,RVN,YFI,WAVES,ICX,OCEAN,RAY,MX,HEX,PLS`;

    const config = {
      method: "get",
      headers: {
        "X-RapidAPI-Key": "396a8cb761mshc0459779f675ee6p18d42djsn4cd87cfd13f7",
        "X-RapidAPI-Host": "redstone.p.rapidapi.com",
      },
    };


async function fetchChfPairs() {
      const url = `https://exchangerate-api.p.rapidapi.com/rapid/latest/CHF`;

      const config = {
        method: "get",
        headers: {
          "X-RapidAPI-Host": "exchangerate-api.p.rapidapi.com",
          "X-RapidAPI-Key":
            "396a8cb761mshc0459779f675ee6p18d42djsn4cd87cfd13f7",
        },
      };
