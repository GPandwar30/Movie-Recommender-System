# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **Python** and **machine learning** techniques.  
This system suggests the **top 5 movies** similar to a given movie based on their **content similarity** using features such as genres, cast, director, and plot keywords.

---

## 🚀 Features

- 🎥 Recommends top 5 similar movies  
- 🧠 Uses **content-based filtering**  
- 🔍 Utilizes **cosine similarity** for measuring similarity between movies  
- 💾 Data preprocessing and feature engineering using **pandas** and **scikit-learn**  
- 🌐 Web app built with **Flask** to provide a simple user interface  

---

## 🧰 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Language | Python |
| Data Handling | Pandas, NumPy |
| Machine Learning | scikit-learn |
| Text Processing | CountVectorizer / TF-IDF |
| Web Framework | Flask |

---

## 📂 Project Structure

```
movie-recommendation-system/
│
├── dataset/
│   └── movies.csv
│
├── static/
│   └── (CSS, images, JS files if web app)
│
├── templates/
│   └── index.html
│
├── app.py                # Flask app file
├── model.ipynb           # Jupyter Notebook for model building
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```
   Then open your browser and go to:  
   👉 `http://127.0.0.1:5000/`

---

## 💡 How It Works

1. The dataset is cleaned and preprocessed (removing nulls, combining features).  
2. A **feature vector** is created using **CountVectorizer** or **TF-IDF Vectorizer**.  
3. **Cosine similarity** is calculated between movie feature vectors.  
4. When a user inputs a movie name, the system retrieves and displays the **top 5 most similar movies**.

---

## 📊 Example Output

**Input:** `Avatar`  
**Recommendations:**
- Guardians of the Galaxy  
- Star Trek  
- The Fifth Element  
- Interstellar  
- The Matrix

---

## 🧪 Future Enhancements

- Integrate **collaborative filtering** for hybrid recommendations  
- Add **movie posters and ratings** via TMDB API  
- Deploy the app using **Render / Vercel / Heroku**  
- Improve UI using **Bootstrap / TailwindCSS**

---

## 👨‍💻 Author

**Gaurav Pandwar**  
📧 [Email](mailto:gp3084@gmail.com)  
🔗 [LinkedIn](#) | [GitHub](https://github.com/GPandwar30/Movie-Recommender-System/)

---

## 🪪 License

This project is licensed under the **MIT License** – feel free to use and modify it.
