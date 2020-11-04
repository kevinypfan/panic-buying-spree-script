const mongoose = require("mongoose");
const { Schema } = mongoose;

const activateSchema = new Schema(
  {
    activate_code: { type: String },
    serial_code: { type: String, default: null },
    revoked: { type: Boolean, default: false },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Activate", activateSchema);
