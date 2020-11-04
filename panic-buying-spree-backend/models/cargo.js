class Cargo {
  constructor(returnCode = "000000", returnMessage = "SUCCESS", info = null) {
    this.returnCode = returnCode;
    this.returnMessage = returnMessage;
    this.info = info;
  }
}

module.exports = Cargo;
