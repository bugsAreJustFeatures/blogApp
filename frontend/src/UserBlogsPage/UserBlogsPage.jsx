import { useEffect, useState } from "react"
import styles from "./UserBlogsPage.module.css"
import { useParams } from "react-router-dom";
import renderBlogs from "../RenderBlogs/RenderBlogs";

export default function UserBlogsPage() {

    const [blogs, setBlogs] = useState(null);
    const [blogsRendered, setBlogsRendered] = useState(null);

    const api = import.meta.env.VITE_API;
    const params = useParams()

    useEffect(() => {

        async function fetchUserBlogs(){

            const response = await fetch(`${api}/get-user-blogs/${params.username}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                },
            });

            const data = await response.json()
            console.log(data)
            setBlogs(data.blogs)
            const renderedBlogs = renderBlogs(data.blogs);
            setBlogsRendered(renderedBlogs);

        };
        fetchUserBlogs();

    }, [])
    
    if (!blogs || !blogsRendered) {
        return <h1>Loading...</h1>
    }

    return (
        <div className="universalWrapper">
            <div id={styles.userBlogsWrapper}>
                {blogsRendered}
            </div>
        </div>
    )
};

