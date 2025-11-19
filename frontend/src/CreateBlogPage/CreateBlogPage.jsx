import { useNavigate } from "react-router-dom";

import styles from "./CreateBlogPage.module.css";

export default function CreateBlogPage() {

    const navigate = useNavigate();

    const api = import.meta.env.VITE_API;

    async function handleForm(e) {
        e.preventDefault(); // prevent default form behaviour

        const form = e.target;

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
            if (response.status == 201) {
                navigate("/")
            } else if (response.status == 401) {
                navigate("/login")
            };

        } catch (err) {
            throw new Error(err);
        };

    };

    return (
        <div className="universalWrapper">
            <form onSubmit={(e) => handleForm(e)} method="post">
                <input type="text" name="title" id={styles.titleInput} placeholder="Hello, World!" required />

                <textarea name="content" id={styles.contentTextarea} placeholder="This is my first blog!" required ></textarea>

                <label htmlFor="isPublished">Publish this blog?</label>
                <input type="checkbox" name="isPublished" id={styles.isPublishedCheckBox}/>

                <button type="submit">Finish Blog</button>
            </form>
        </div>
    )
};