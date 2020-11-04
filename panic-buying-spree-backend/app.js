require("dotenv").config();

const Koa = require("koa");
const bodyParser = require("koa-bodyparser");
const mongoose = require("mongoose");
const activateRouter = require("./router/activate");

mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const app = new Koa();
app.use(bodyParser());

app.use(activateRouter.routes()).use(activateRouter.allowedMethods());

app.listen(process.env.PORT, () => {
  console.log("server start port: " + process.env.PORT);
});
