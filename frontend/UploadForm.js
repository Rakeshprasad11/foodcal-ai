import React, { useState } from "react";

export default function UploadForm() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // 🔽 ADD FUNCTION HERE
  const analyzeImage = async (imageData) => {
    setLoading(true);
    setResult(null);

    try {
      const formData = new FormData();
      const blob = await (await fetch(imageData)).blob();
      formData.append("image", blob, "food.jpg");

      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (data.error) throw new Error(data.error);

      setResult({
        food: data.food,
        confidence: data.confidence,
      });
    } catch (error) {
      console.error("Error analyzing image:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (image) analyzeImage(image); // <-- Call the function when form is submitted
  };

  return (
    <div>
      <h1>Upload Your Food</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept="image/*" />
        <button type="submit">Analyze</button>
      </form>

      {loading && <p>Analyzing...</p>}
      {result && (
        <div>
          <h3>Food: {result.food}</h3>
          <p>Confidence: {Math.round(result.confidence * 100)}%</p>
        </div>
      )}
    </div>
  );
}
