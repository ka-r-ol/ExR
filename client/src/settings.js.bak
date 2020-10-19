

import axios from "axios";
export const BASE_API_URL = "http://127.0.0.1:8000/api/v1/";


export var LoadCategories = function (username, password) {
    axios
        .get(BASE_API_URL + "categories", {
            auth: {
                username: username,
                password: password,
            },
        })
        .then((res) => {
            var categories = {}
            res.data.forEach((el) => (categories[el.id] = el.name));
            console.log("categories res.data", res.data);
            console.log("categories ", categories);
            return categories
        })
        .catch((error) => {
            console.log(error); //Logs a string: Error: Request failed with status code 404
        });
}