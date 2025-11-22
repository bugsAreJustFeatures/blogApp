import { useNavigate } from "react-router-dom";

import styles from "./CreateBlogPage.module.css";
import checkJwt from "../utils/checkJwt";
import { useEffect } from "react";

export default function CreateBlogPage() {

    const navigate = useNavigate(); // use hook to redirect user when needed

    const api = import.meta.env.VITE_API; // get api url from .env

    // use effect used on mount to check if jwt is there, if it is, user is logged in
    useEffect(() => {
        function checkJwtIsThere() {

            const token = localStorage.getItem("token"); // get bearer token from local storage

            const isJwtThere = checkJwt(token); // assign value

            // if no jwt redirect user to login page otherwise let them pass since they have a valid jwt, even if the contents are invalid, i have checks on backend that will redirect them after the try to make a blog
            if (!isJwtThere) {
                navigate("/login");
            };
        };
        checkJwtIsThere();

    }, [])

    // function for handling the form of creating a blog
    async function handleForm(e) {
        e.preventDefault(); // prevent default form behaviour

        // get form
        const form = e.target;

        // get elements from form
        const title = form.title.value;
        const content = form.content.value;
        const isPublished = form.isPublished.checked; 

        // try to send data to backend and create a blog
        try {
            const response = await fetch(`${api}/create-blog`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`, 
                },
                body: JSON.stringify({
                    title,
                    content,
                    isPublished,
                }),
            });

            // read and check response
            // check it was ok
            if (response.status == 201) { // blog was created
                navigate("/");

            } else if (response.status == 401) { // backend blocked the request to create it so send to log in again, this will only really happen if user has a invalid jwt
                navigate("/login");
            };

        } catch (err) {
            throw new Error(err);
        };

    };

    return (
        <div className="universalWrapper">
            <div id={styles.formWrapper}>
                <form onSubmit={(e) => handleForm(e)} method="post" id={styles.createBlogForm}>
                    <label htmlFor="title" id={styles.titleLabel}>What will your blog title be?</label>
                    <input type="text" name="title" id={styles.titleInput} placeholder="Hello, World!" required />

                    <label htmlFor="content" id={styles.contentLabel}>Write your blog:</label>
                    <textarea name="content" id={styles.contentTextarea} placeholder="This is my first blog!" required ></textarea>

                    <label htmlFor="isPublished" id={styles.isPublishedLabel}>Publish this blog?</label>
                    <input type="checkbox" name="isPublished" id={styles.isPublishedCheckBox} defaultChecked />

                    <button type="submit" id={styles.createButton}>Publish/Save Blog</button>
                </form>
            </div>
        </div>
    )
};