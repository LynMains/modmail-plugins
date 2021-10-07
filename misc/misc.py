import logging
from enum import Enum
from random import randint, choice
import discord
from discord.ext import commands
from core import checks
import box
import json
import string
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)

logger = logging.getLogger("Modmail")


class Misc(Cog):
    """
    Commands that Sage has made for the server.
    """

    aki = [
        "https://cdn.discordapp.com/attachments/568778270598889472/817536212235059210/20210305_181639.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/816921765510905877/20190816_215610.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/810032934035783680/20210213_011915.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/807734340502945796/20210206_170708.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/801887714294104124/20210121_135448.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/800468163271720960/20210117_155417.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/799919355063959552/20210116_033340.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/799119003654029392/20210113_223313.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/797929645131038750/20210110_154722.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/797923846225002516/20210110_152409.jpg",
        "https://media.discordapp.net/attachments/568778270598889472/797329448395210772/20210109_000225.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/797328420001284116/20210108_235810.jpg",
        "https://cdn.discordapp.com/attachments/471874298798407680/797310792444674078/20210108_224807.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/796883070987927562/20210107_182839.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/796882797418905650/20210107_182654.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/796862459410776105/20210107_170637.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/795486163825590303/20210103_215720.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/794458323747078184/20210101_014711.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/794048993331380244/20201230_224700.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/793005512149041172/20201228_013952.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/788503792030973952/20201215_032139.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/782702630757466184/20201129_152023.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/782674350981120000/20201129_132815.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/782673641972039691/20201129_132511.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/781680555544150026/20201126_193344.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/781235504871899146/20201125_141019.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/781228128079970385/20201125_134046.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/780531729990811668/20201123_153407.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/780319624176205874/20201123_010850.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/780294163333775380/20201122_235009.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/779542321573396500/20201120_220232.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/776158264093442109/20201111_135539.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/776145378835562566/20201111_130345.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/774847366947274792/20201107_230634.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/773793388276875264/20201105_011742.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/773627568888741899/20201104_141926.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/773333851133050901/20201103_183404.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/772985584959619112/20201102_194810.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/772965422474592276/20201102_182523.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/769601795492020265/20201024_124231.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/769442331039891456/20201024_020850.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/769429653218918400/20201024_011813.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/768533676417876009/20201021_135811.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/765747533884424232/20201001_232409.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/765742795683004436/20200323_121231.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/765741904910090260/20200725_152738.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/765741569428422676/20200906_224623.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/765741420165988392/20200908_174703.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/765741208080744448/20200215_134007.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/765741117618126848/20200926_140850.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/763928007521468427/20201008_205446.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/762886727676723200/20201005_235846.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/762480773269815347/20201004_210549.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/761429864548401182/20201001_232929.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/761408463452110858/20201001_220507.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/760298107786231848/20200928_203221.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/760298106834255912/20200928_203243.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/758076991411978331/Snapchat-623970649.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/758076989872537690/Snapchat-761678842.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/756720926476861480/20200918_233645.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/756720330579378287/20200918_233545.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/754191741871063090/20200911_234844.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/751992544325402674/20200905_222926.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/750525696421527614/20200901_110146.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/749808075527028796/20200830_214607.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/749808074834837604/20200830_214838.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/744281138767331408/20200815_045357.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/730833968035004457/20200709_131259.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/568803722734338052/20190419_102235.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/568859099421343749/20190419_140243.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/568922036886306816/20190419_181237.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/569928461674610704/20190422_125051.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/569928492947603476/20190422_125014.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/569951641281757194/20190422_142401.jpg",
        "https://cdn.discordapp.com/attachments/471867421565779990/572489172355645460/20190429_142715.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/573296017903058964/20190501_195240.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/573296505088114689/20190501_195230.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/573688846861074442/20190502_215239.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/574984151313285120/20190506_114021.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/575373820316221442/20190507_132934.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/575374178522365964/20190507_133113.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/576810858642931722/20190511_124002.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/582396299081678858/20190526_223232.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/583172744431009813/20190529_015943.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/588031170231664650/20190611_114506.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/588923723604688896/20190613_225111.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/591444914403934230/20190620_215010.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/592119418465550336/20190622_182559.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/603654770162401305/20190724_142805.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/608462612115488769/20190806_205242.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/609873515037851648/20190810_181913.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/610194223236513798/20190811_153340.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/610192398240317460/20190811_152114.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/611005219379347456/20190813_211609.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/623187574034399246/20190916_115822.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/620697078519300136/20190909_150806.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/633708940680495124/20191015_125108.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/635227449960955905/20191019_172643.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/635240695413735424/20191019_181916.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/639505236641447936/20191031_124421.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/640978505995255810/20191104_131854.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/827398646756147200/20210402_002522.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/827304926119985182/IMG_1507.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/825581274324271134/20210328_000453.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/825581273325371433/20210328_000245.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/824153285137006662/20210324_012957.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/824153284432101396/20210324_012619.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/824013821118644224/20210323_161623.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/823620013582843904/20210322_141136.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/823619090026463292/20210322_140730.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/823619088545873930/20210322_140743.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/823339403962220594/20210321_193450.jpg",
        "https://cdn.discordapp.com/attachments/568778270598889472/817535487329566760/20210305_181342.jpg"
    ]
    
    gay = [
        "https://safebooru.org//samples/3489/sample_8e5e3458e6788ef916f4db8f5afbebf22c422b52.jpg?3629971",
        "https://safebooru.org//samples/3418/sample_e5861d6b0eba7070cdeffea52983ffe54a5a68c4.jpg?3555913",
        "https://safebooru.org//samples/3405/sample_8e14cfa2ec64d6b931d23bb4f3e2bca94e313f73.jpg?3541674",
        "https://safebooru.org//samples/3409/sample_f31afe3850d93d8dd28952631b6bcd32d35b0276.jpg?3546907",
        "https://safebooru.org//images/3458/90025cec9d8eb3c332f88c12172aa2b53f4d5aea.jpg?3600101",
        "https://safebooru.org//samples/3481/sample_006d9f7c47ef9004a9036fcb81d84fde9e9e1edd.jpg?3621759",
        "https://safebooru.org//samples/3480/sample_58f403f15c4af169280f255a637b910860730a10.jpg?3620207",
        "https://safebooru.org//samples/3484/sample_61f8149cf82a122038da55ebad055d4897ad1ded.jpg?3624822",
        "https://safebooru.org//samples/3468/sample_e702582f860ebf8d82bd3ec1dbea64487c045f77.jpg?3607650",
        "https://safebooru.org//images/3482/e96ccda93743bb7e2e747828fa9260e42d78178b.jpg?3622033",
        "https://safebooru.org//images/3489/8e5e3458e6788ef916f4db8f5afbebf22c422b52.jpg",
        "https://safebooru.org//images/3502/ec447ffd246cb6651a0eceb2c5d77846a9583c6c.jpg",
        "https://safebooru.org//images/3469/ac09de3729f400cebf891d74cd5a09dcb83087c3.png",
        "https://safebooru.org//images/3461/75d7faa91f4ebda49603be632798948fa0a3aac1.png?3600271",
        "https://safebooru.org//images/3461/6d244dd93278c5e4423909b8bae980e1d09ead98.png?3600229",
        "https://safebooru.org//images/3461/095871d0bb1e6a72be2f4c05949dde04450a7637.png?3600252",
        "https://safebooru.org//images/3451/dd9b0a0e672882be6c101cbe0253c0163d98c05c.png",
        "https://safebooru.org//images/3459/34e88ab68f0d399020e61b17192c61e9c9b07c2c.jpg",
        "https://safebooru.org//images/3459/dc412d95d1ad2c266176d6a2e1830d5c53f357cd.jpg",
        "https://safebooru.org//images/2677/6fd0c736910d54e45a54a08f81df9e17df2ab4df.jpg",
        "https://safebooru.org//images/2494/303cffc76bc3faf9ee0a65af0b62048160f0a679.jpg",
        "https://safebooru.org//images/2782/2305140b40bd9661657eee9d071fc2927c78015a.jpg",
        "https://safebooru.org//images/2777/0461f417db426c897f9cc3f81a47be261503ef50.jpg",
        "https://safebooru.org//images/2876/81103966389306059000b87e06910bfcde0e1fa2.jpg",
        "https://safebooru.org//images/2876/d9e6b4a611f9bea46ec92a0c0d7fa5d32d6ebbcd.png",
        "https://safebooru.org//images/3024/b820a529526c890d5da3786ff121c8fc30e61e97.jpg",
        "https://safebooru.org//images/3363/9d7cd66836ee2a76440141e94efac4e1c0f0c57c.jpg",
        "https://safebooru.org//images/3230/a5dcc5169c3da770646f92de21b08b32697669b7.jpg",
        "https://safebooru.org//images/3377/77e1d12948d99397b2955f0c2428e40c88024fde.png",
        "https://safebooru.org//images/3376/48d0ebfcfc9ef482ac620cffcc7b9ea3d4dc406f.jpg",
        "https://safebooru.org//images/3406/73816de021641a5c768466ef432236bce92e3ca0.jpg",
        "https://safebooru.org//images/3410/fef0d45f806af69e8a8648bec4b9b141e9ca1e43.png?3547775",
        "https://safebooru.org//images/3406/4999044d0e957b60f5736502b511cbbd1a75c930.jpg",
        "https://safebooru.org//images/3406/ce25e0a7e9fbfe08f545517c79128124577e72a9.png",
        "https://safebooru.org//images/3412/3c7547b31d6dbab55146d00ff3c798a34bb4f9aa.jpg",
        "https://safebooru.org//images/3426/3afd7cc860c7de6c9cf68ce761d14f5f80a18c96.jpg",
        "https://safebooru.org//images/3426/f2f00f137be1a6e0fb37a46a5a2526c69bcac442.jpg?3564218",
        "https://safebooru.org//images/3426/b314d3651fa8a095b597522e79bb1b2ce484b4fc.jpg?3564285",
        "https://safebooru.org//images/3427/0d69344252faebe64317a0b626b6498c30e90938.jpg",
        "https://safebooru.org//images/3427/27d250dbc4c18885b9be8823f58d2ecdcab86f96.jpg",
        "https://safebooru.org//images/3433/118f28098c591feba696e10d60fdf10d523039cd.jpg"
    ] 

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        # self.db = bot.plugin_db.get_partition(self)

    @commands.command(name="aki", aliases=["cat"])
    async def _aki(self, ctx):
        """
        Retrieves a random photo of Aki, Sage's cat.
        """
        embed = discord.Embed(
            title=":black_cat: Aki has come to see you!", color=3553599
        )
        embed.set_image(url=choice(self.aki))
        await ctx.send(embed=embed)
        
    @commands.command(name="gaytime", aliases=["gay"])
    async def _gaytime(self, ctx):
        """
        Retrieves a random photo of Yae being gay.
        """
        embed = discord.Embed(
            color=3553599
        )
        embed.set_image(url=choice(self.gay))
        embed.set_footer(
            text="Credit page coming...soon!"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
