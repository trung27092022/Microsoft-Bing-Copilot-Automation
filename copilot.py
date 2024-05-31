
import asyncio

import os

os.environ["BING_COOKIES"] = "input the cookie of my Bing Copilot account here!!!!>"

from sydney import SydneyClient

async def main() -> None:
    sydney = SydneyClient()

    await sydney.reset_conversation(style="creative")

    response = await sydney.ask("Input the message here!!!!")
    print(response)

    await sydney.close_conversation()


if __name__ == "__main__":
    asyncio.run(main())

# _fbp=fb.1.1705184031124.176453887; MC1=GUID=ad5b04d7cc214e74997fea523e327bd6&HASH=ad5b&LV=202401&V=4&LU=1705184035095; MUIDB=0674AD1EBB7163EB20D7B91BBA63625E; USRLOC=HS=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=8834812510A34BABB220D9D16571E0BA&dmnchg=1; ANON=A=B3EBE056930FF5F2A6CDF933FFFFFFFF; _tt_enable_cookie=1; _ttp=GNxglH8Tu_yNMRX2_V9P8zQj5XP; _cs_c=0; _cs_id=2b61f504-0817-ad3b-a127-6c48ba4cb16c.1708066164.1.1708066164.1708066164.1613561419.1742230164125.1; mbox=PC#4326cf8edd1045e49069d0bc82059d97.38_0#1742252873|session#b5715d4de6854e47950872a0195be5a5#1708068034; AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg=1585540135%7CMCIDTS%7C19770%7CMCMID%7C47386002280784609564283935031787676091%7CMCAAMLH-1708670973%7C3%7CMCAAMB-1708670973%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCCIDH%7C1033060618%7CMCOPTOUT-1708073373s%7CNONE%7CMCSYNCSOP%7C411-19777%7CMCAID%7CNONE%7CvVersion%7C4.4.0; _clck=jpnyzf%7C2%7Cfjn%7C1%7C1473; _EDGE_S=SID=257E8A5B191A696F05099ED7180868B1; WLS=C=b2189545ed05338c&N=Trung; _U=1B4-UfE7ajvW9Yk_xlK9Cs81JqK3giTYJ5C2v1B_kGu2NPEYXGqF6KADDjXzYvv-PnLIIfMXhRrA_-gWsA-19qJiZN5l64rbzjddCG9OeRJ-Y2aH7q5Z-kvnolCiRMNnHJf-lVhhUIYAoRYmy0DOS2HxiuhWMsdMwbQXnUf9te_0FRUXawcBkkCuigMGUgjKaj_faYwyhIn0RSMHaQNKFgWv-s9QbypesocwRsemiryc; ak_bmsc=6CBFFF274134B6BAD5842DCF17358520~000000000000000000000000000000~YAAQ2xBFdk48cKuPAQAAB86JuBflfufIrZaLzDfTR63C9GYTAqwnvtn94kLn3Kmoha27z68RdyEIvOwkkJs13SvnxBAEEvzPB4GPeXDq3/br3wnZSphy0llKI0khOaOmQiaBFVC9J76fHKwbdBg7gPUwm4FrsMj3Neb+by6SRUiSe0XiXRgSX0Woj8Jq5MWwKHiqH8e+kxQRnLTyaL6Z5xZDU+Cdr1rzEtfob0KKBIBHpOyU3aUbeMv6fce0gPYfGDWsHteXGeMbA3bNOf0U71mLigsA14fA5UZmdwedRbxxFnOCLVrEqSfzBVCUDjODi54N4lt8R0wIVRLDQZcXvfK0uP/M899zGTtRJLy+0EjwZBxOWjmW3Xu6Mdb5eqMLNN6BN7WRuCvG31duf6B3zJpRIeFyclCQ+gsXx1GMfhij/IKDRul8; _C_Auth=; MUID=0674AD1EBB7163EB20D7B91BBA63625E; _Rwho=u=d&ts=2024-05-27; SRCHUSR=DOB=20240206&T=1716788023000; MS0=7652b55da7634f7ca43dcc51ae6c4392; _RwBf=mta=0&rc=169&rb=169&gb=0&rg=0&pc=169&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=2&l=2024-05-26T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-01-25T03:44:26.6342179-08:00&rwflt=2024-01-28T12:29:25.8695305-08:00&o=0&p=MSAAUTOENROLL&c=MR000T&t=2825&s=2024-01-13T18:02:24.8833090+00:00&ts=2024-05-27T05:45:52.4639992+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&e=3wOONe3PqtkN1W-TX0JzFss3R3bS_04SBiMkk9KuYEvqOKD74o0gheGQqZLjFZQkOO6Nlfg_6CwIsVOSbr_XRPI_bTSsUl_easga9i43-XU; _SS=SID=257E8A5B191A696F05099ED7180868B1&R=169&RB=169&GB=0&RG=0&RP=169; SRCHHPGUSR=SRCHLANG=en&PV=11.3.1&BRW=S&BRH=M&CW=1077&CH=852&SCW=1204&SCH=796&DPR=2.0&UTC=420&DM=1&CIBV=1.1759.0&HV=1716788028&PRVCW=1077&PRVCH=852; _uetsid=b110e5901bea11efbe10339fe655a966; _uetvid=081ec8d0b26111ee8d71f78f81637e0f; ext_pgvwcount=-0.1; _C_ETH=1; bm_sv=617C8AB9C302778DC01071CD18043D30~YAAQyRBFdolTAJWPAQAAfp6VuBfFChwYi5fxRJZPqcBV1b6fHNDxpEz5t2OkEQ505rf49QYRgE2E01eKcuRx2omGpiAqMQ2ut3Tmdp3RS8RmQkbrYSseIt09yzPKXSnFaaPecnLeUjzniE6tBWGHi5x8KnG3xcBap3xGc5/9Pz5OyjRGtzzOHzioejeUqQlBlJnlUjQ2Dl9x7SNFU3SkR3f+VQ7/oRVUDM04WnVowFgjEOhieQQm4UbeMLLPFx4h6SG1Qg==~1; fptctx2=H3ihr9e92IdW6yd1ZgQ9SzatWryjyxVbTdQYFEUia0bd3U%252b7jzshaegBB1ExHLG4Nx84msm9tP81sPNBaJQaNpy47ASfAc0tNeJxxkMIQ%252bw9OFt5COy3QqvNcSwS%252fsU3BY22GFyHbB71ABQj7oobN%252bjDLP%252fnOixpkFgmlCf9XchSHm2BnAxYsTkQnbigv9vqkmghZe8E36qC0y14rOvtDYFPWiNfh8m6vPxpBegU4xTsu20m%252foUP5Of%252bzjLrJfAS1LuquQhYE64bdkvtBcfxGl%252bTZGaH6Zt2V7mv6QhnMsktI9JR62tT%252b3bQLnOhzClWtOd64qbjxGscij9fZ7THXg%253d%253d
# What I was doing: Can you put it all in a file like a .pdf one and send me the link to download it, please?