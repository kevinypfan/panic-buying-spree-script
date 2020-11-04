const mongoose = require("mongoose");
const { Schema } = mongoose;
const { v4: uuidv4 } = require("uuid");

const activateSchema = new Schema(
  {
    activate_code: { type: String, default: uuidv4() },
    serial_code: { type: String, default: null },
    revoked: { type: Boolean, default: false },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Activate", activateSchema);
