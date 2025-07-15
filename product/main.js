import express from "express";
const app = express();

app.get("/", (req, res) => {
  res.json({
    success: true,
    message: "Product service.",
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
