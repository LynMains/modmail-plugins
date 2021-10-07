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
        "https://cdn.discordapp.com/attachments/568778270598889472/817535487329566760/20210305_181342.jpg",
    ]
    
    gay = [
        "https://cdn.discordapp.com/attachments/799069920402341893/833069759120801842/maxresdefault-2.png",
        "https://img3.gelbooru.com//samples/01/f6/sample_01f6d4f8538db12cba435f84f5f35bea.jpg",
        "https://cdn.discordapp.com/attachments/799069920402341893/833967051433312306/yae_sakura_kallen_kaslana_yae_sakura_kallen_kaslana_and_yae_kasumi_honkai_and_1_more__8e3f2dc73ee909.png",
        "https://img3.gelbooru.com//samples/ab/fc/sample_abfc6631bf22bb6c50eb253b6199abdf.jpg",
        "https://img3.gelbooru.com//samples/2f/b9/sample_2fb9ad159221fb7171d469e08a607856.jpg",
        "https://img3.gelbooru.com//samples/96/5f/sample_965fb7297114b36af690cb67f3bbc4b1.jpg",
        "https://64.media.tumblr.com/c38c0f2ebb7b887062be31170f41bce3/tumblr_ph9fwsnQYF1qey13zo1_1280.png",
        "https://64.media.tumblr.com/227d5caeb3ab546838cdea43f3e2da1f/tumblr_pks5xn0JSD1tkxb7uo2_r2_1280.png",
        "https://64.media.tumblr.com/5b5cc8c05f94de0c1f440ee76d74bae2/tumblr_pks5xn0JSD1tkxb7uo1_r2_1280.png",
        "https://64.media.tumblr.com/47ef3db2c483cecd2e3f8db32552df02/8d549bf6c4c0b29e-40/s1280x1920/774013fc276e7ff276f9744ef024ceaabdd67244.png",
        "https://64.media.tumblr.com/f692d1c84dcd0438522df65beee25428/8d549bf6c4c0b29e-e1/s1280x1920/966082fd3f043ef5d93ca33163be171a769da452.png",
        "https://cdn.discordapp.com/attachments/799009843452313640/833501542778667038/EdHbNRKXkAAs6nA.jpg",
        "https://64.media.tumblr.com/3454a7fcd5289110d6f049eaeae873ae/1833996a65d53586-0c/s1280x1920/0b3f54cb9cd15acdde68305b495ef37e8c76c48b.jpg",
        "https://64.media.tumblr.com/24240d8213608eb4c540ea2f5eb8c8dd/tumblr_phnk164ob41trpsq8_1280.png",
        "https://64.media.tumblr.com/c4798b8373780457068297c0ec9e2313/392d268c3e6fa066-6e/s1280x1920/9308136aa1c215391c91784f6d2df6e255e370cf.png",
        "https://64.media.tumblr.com/2d2fc05a4d1723f40af7671d8fc83a69/tumblr_per9lkHwj91rwcs8fo6_1280.jpg",
        "https://64.media.tumblr.com/aa2fe7e50f1e3fc150f9adf46174ad14/tumblr_per9lkHwj91rwcs8fo5_1280.jpg",
        "https://64.media.tumblr.com/ad50c9aa4e42e66c0ef61e30b787ed74/ee70362d6603625b-35/s1280x1920/79e0db2e48cd11d5c5a195631173571e8dc63514.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_kallen_kaslana_and_kallen_kaslana_honkai_and_1_more_drawn_by_jiaming_liu__sample-d00bec3dc082f2bc705889df58048f9b.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_kallen_kaslana_and_yae_sakura_honkai_and_1_more_drawn_by_senseofexistenc__sample-83be79afd99977c58e9c3f907d65178f.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_and_kallen_kaslana_honkai_and_1_more_drawn_by_dokun7__sample-cb80d9b720205b45455536be100ad891.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_theresa_apocalypse_seele_vollerei_yae_sakura_and_otto_apocalypse_honkai_and_1_more_drawn_by_tsubasa_tsubasa__sample-38f6f7b6b14d4673e131dab1e662ba42.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_kallen_kaslana_and_yae_sakura_honkai_and_1_more_drawn_by_791_meiyuewudi__sample-ccdc08bc9c6d103c9d249714b931d081.jpg",
        "https://danbooru.me/data/sample/__yae_sakura_and_kallen_kaslana_honkai_and_2_more_drawn_by_shibanme_tekikumo__sample-a521bdadc742caeb1bf8f60315143011.jpg",
        "https://safebooru.org//samples/3024/sample_b820a529526c890d5da3786ff121c8fc30e61e97.jpg?3148813",
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
    async def _aki(self, ctx):
        """
        Retrieves a random photo of Yae being gay.
        """
        embed = discord.Embed(
            color=3553599
        )
        embed.set_image(url=choice(self.gay))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
