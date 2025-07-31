import express from "express";
const app = express();

app.get("/", (req, res) => {
  res.json({
    success: true,
    message: "Product service. v1.0.2",
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
