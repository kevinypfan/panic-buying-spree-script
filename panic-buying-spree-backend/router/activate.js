const Router = require("@koa/router");
const { v4: uuidv4 } = require("uuid");
const Activate = require("../entities/activate");
const Cargo = require("../models/cargo");

const router = new Router();

router.prefix(`/v${process.env.VERSION}/activate`);
// /activate/create-new-code
router.get("/create-new-code", async (ctx, next) => {
  const cargo = new Cargo();

  if (!ctx.headers["api-key"]) {
    cargo.returnCode = "100000";
    cargo.returnMessage = "required header not found";
    return (ctx.body = cargo);
  }

  if (ctx.headers["api-key"] !== process.env.API_KEY) {
    cargo.returnCode = "100001";
    cargo.returnMessage = "required header invalid";
    return (ctx.body = cargo);
  }

  const activate = await new Activate({ activate_code: uuidv4() }).save();

  cargo.info = activate;
  ctx.body = cargo;
});

router.post("/verify-code", async (ctx, next) => {
  const cargo = new Cargo();

  if (!ctx.request.body.serial_code) {
    cargo.returnCode = "100022";
    cargo.returnMessage = "required field not found";
    return (ctx.body = cargo);
  }

  const serial_code_find = await Activate.findOne({
    serial_code: ctx.request.body.serial_code,
  });

  if (serial_code_find) {
    cargo.returnCode = "000001";
    cargo.returnMessage = "already activate";
    cargo.info = serial_code_find;
    return (ctx.body = cargo);
  }

  const activate = await Activate.findOne({
    activate_code: ctx.request.body.activate_code,
  });

  if (!activate) {
    cargo.returnCode = "100004";
    cargo.returnMessage = "此啟動碼不存在！";
    return (ctx.body = cargo);
  }

  if (activate.revoked) {
    cargo.returnCode = "100003";
    cargo.returnMessage = "此啟動碼已無法使用！";
    return (ctx.body = cargo);
  }

  if (activate.serial_code === ctx.request.body.serial_code) {
    return (ctx.body = cargo);
  }

  if (activate.activate_code && activate.serial_code) {
    cargo.returnCode = "100002";
    cargo.returnMessage = "此啟動碼已被啟用！";
    return (ctx.body = cargo);
  }

  if (!activate.serial_code) {
    await activate.updateOne({ serial_code: ctx.request.body.serial_code });
    return (ctx.body = cargo);
  }
});

module.exports = router;
