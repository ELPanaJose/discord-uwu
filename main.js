const linkMemes = [
  "https://www.reddit.com/r/MAAU/top/",
  "https://www.reddit.com/r/DylanteroYT/hot/",
  "https://www.reddit.com/r/linuxmemes/hot",
  "https://www.reddit.com/r/linuxmemes/new/",
  "https://www.reddit.com/r/linuxmemes/top/",
  "https://www.reddit.com/r/shitposting/top/",
  "https://www.reddit.com/r/shitposting/new/",
  "https://www.reddit.com/r/shitposting/hot/",
  "https://www.reddit.com/r/ProgrammerHumor/hot/",
  "https://www.reddit.com/r/ProgrammerHumor/new/",
  "https://www.reddit.com/r/ProgrammerHumor/top/",
  "https://www.reddit.com/r/MAAU/hot/",
  "https://www.reddit.com/r/MAAU/new/"
];

var ayuda =
  "```*nm = nuevo meme\n*meme = te da un meme\n*cm = cantidad de memes```";

var img = [];
const Discord = require("discord.js");
const axios = require("axios");
const cheerio = require("cheerio");

const client = new Discord.Client(),
  commands = {
    "*nm": async function (msg) {
      msg.channel.send("se busco un nuevo meme");
      linkMemes.map((i) => {
        axios.get(i).then((r) => {
          let $ = cheerio.load(r.data);
          $("._2_tDEnGMLxpM6uOa2kaDB3").each((i, e) => {
            img.push($(e).attr("src"));
          });
        });
      });
    },
    "*meme": async function (msg) {
      let exampleEmbed = new Discord.MessageEmbed()
        .setTitle(
          ":regional_indicator_b: :regional_indicator_r:  :regional_indicator_u: :regional_indicator_h:"
        )
        .setImage(img[Math.floor(Math.random() * img.length)]);
      msg.channel.send(exampleEmbed);
    },
    "*cm": async function (msg) {
      msg.channel.send(`la cantidad de memes es :${img.length}`);
    },
    "*help": async function (msg) {
      msg.channel.send(ayuda);
    },
  };

client.on("ready", () => {
  console.log(`bot ready! ${client.user.tag}!`);
});
client.on("message", (msg) => {
  if (commands.hasOwnProperty(msg.content)) {
    commands[msg.content](msg);
  }
});
client.login("");
