const linkMemes = [
  "https://www.reddit.com/r/MAAU/new/",
  "https://www.reddit.com/r/DylanteroYT/new/",
  "https://www.reddit.com/r/MAAU/top/",
  "https://www.reddit.com/r/DylanteroYT/hot/",
  "https://www.reddit.com/r/MAAU/hot/",
  "https://www.reddit.com/r/DylanteroYT/top/",
  "https://www.reddit.com/r/linuxmemes/hot",
  "https://www.reddit.com/r/linuxmemes/new",
  "https://www.reddit.com/r/linuxmemes/top"
];

Object.defineProperty(Array.prototype, "flat", {
  value: function(depth = 1) {
    return this.reduce(function(flat, toFlatten) {
      return flat.concat(
        Array.isArray(toFlatten) && depth > 1
          ? toFlatten.flat(depth - 1)
          : toFlatten
      );
    }, []);
  }
});

var img = [];
const Discord = require("discord.js");
const axios = require("axios");
const cheerio = require("cheerio"); 

const client = new Discord.Client(),
  commands = {
    "*nm": async function(msg) {
      msg.channel.send("se busco un nuevo meme");
      linkMemes.map(i => {
        axios.get(i).then(r => {
          let $ = cheerio.load(r.data);
          $("._2_tDEnGMLxpM6uOa2kaDB3").each((i, e) => {
            img.push($(e).attr("src"));
          });
        });
      });
    },
    "*meme": async function(msg) {
      let exampleEmbed = new Discord.MessageEmbed()
        .setTitle(
          ":regional_indicator_b: :regional_indicator_r:  :regional_indicator_u: :regional_indicator_h:"
        )
        .setImage(img[Math.floor(Math.random() * img.length)]);
      msg.channel.send(exampleEmbed);
    },
    "*bruh": msg => {
      msg.channel.send(":flushed:");
      msg.channel.send("<:typescript:791822787689971772>")
      msg.channel.send("https://media.giphy.com/media/VIOkcgpsnA2Zy/200.gif");
    },
    "*cm": async function(msg) {
      msg.channel.send(`la cantidad de memes es :${img.length}`);
    },

    "*monda": async function(msg) {
      msg.channel.send("El pana brother jorge floyd todo un idolo  :bruh:");
      msg.channel.send("https://www.youtube.com/watch?v=IRZWiqBHYaY");
      msg.channel.send(
        "https://ichef.bbci.co.uk/news/640/cpsprodpb/8862/production/_112541943_whatsubject.jpg"
      );
    },
    
  };

client.on("ready", () => {
  console.log(`reddit ready! ${client.user.tag}!`);
});
client.on("message", msg => {
  if (commands.hasOwnProperty(msg.content)) {
    commands[msg.content](msg);
  }
});
client.login("");
