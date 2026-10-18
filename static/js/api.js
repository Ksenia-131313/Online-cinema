// import axios from "axios";

// // --- Создание экземпляра axios ---
// const api = axios.create({
//     baseURL: "http://127.0.0.1:8000/", // адрес Django-сервера
//     headers: {
//         "Content-Type": "application/json",
//     },
//     withCredentials: true
// });

// // --- Интерсепторы запросов ---
// api.interceptors.request.use(
//     (config) => {
//         // Например, добавить токен авторизации
//         const token = localStorage.getItem("token");
//         if (token) {
//             config.headers["Authorization"] = `Bearer ${token}`;
//         }
//         return config;
//     },
//     (error) => Promise.reject(error)
// );

// // --- Интерсептор ответов ---
// api.interceptors.response.use(
//     (response) => response,
//     (error) => {
//         if (error.response) {
//             console.error("Ошибка API:", error.response.status, error.response.data);
//         } else {
//             console.error("Ошибка сети или CORS:", error);
//         }
//         return Promise.reject(error);
//     }
// );

// // --- Функции для работы с API ---

// // Получение списка фильмов с фильтрацией
// export const getMovies = async (genre = "", year = "") => {
//     const response = await api.get("/json-filter/", {
//         params: { genre, year }
//     });
//     return response.data.movies;
// };

// // Поиск фильмов по названию
// export const searchMovies = async (query) => {
//     const response = await api.get("/search/", {
//         params: { q: query }
//     });
//     return response.data;
// };

// // Добавление рейтинга фильму
// export const addRating = async (movieId, star) => {
//     const response = await api.post("/add-rating/", {
//         movie: movieId,
//         star: star
//     });
//     return response.status === 201;
// };

// // Добавление отзыва
// export const addReview = async (movieId, reviewText, parentId = null) => {
//     const response = await api.post(`/review/${movieId}/`, {
//         text: reviewText,
//         parent: parentId
//     });
//     return response.data;
// };

// // Экспорт экземпляра для других запросов
// export default api;
