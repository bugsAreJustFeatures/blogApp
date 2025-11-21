import { useEffect, useState } from "react"
import styles from "./UserBlogsPage.module.css"
import { useParams } from "react-router-dom";
import renderBlogs from "../RenderBlogs/RenderBlogs";

export default function UserBlogsPage() {

    // state variables
    const [blogsRendered, setBlogsRendered] = useState(null);

    // global func variables
    const api = import.meta.env.VITE_API; // api url
    const params = useParams(); // use params from url

    // useEffect on mount that fetches the blogs of that user
    useEffect(() => {
        async function fetchUserBlogs(){
            const response = await fetch(`${api}/get-user-blogs/${params.username}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                },
            });

            // read response and update state
            const data = await response.json()
            const renderedBlogs = renderBlogs(data.blogs);
            setBlogsRendered(renderedBlogs);

        };
        fetchUserBlogs();

    }, [])
    
    if (!blogsRendered) {
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

