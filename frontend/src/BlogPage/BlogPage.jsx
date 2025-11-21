import { useParams } from "react-router-dom";
import styles from "./BlogPage.module.css";
import { useEffect, useState } from "react";

export default function BlogPage() {
    
    // state variables
    const [blog, setBlog] = useState(null); // used to store the blog and its data

    const params = useParams(); // use params in url

    const api = import.meta.env.VITE_API; // get .env variable for api

    const blogId = params.blogId; // get the blog id from url which i pass when it gets clicked

    // useEffect used to get the blog data from backend api
    useEffect(() => {

        async function getBlog() {
            // try to get blog 
            try {
                const response = await fetch(`${api}/get-blog/${blogId}`, {
                    method: "GET",
                    headers: {
                        "Authorization": `Bearer ${localStorage.getItem("token")}`,
                    },
                });

                // reads response
                const data = await response.json();

                // update state with blog details
                setBlog(data);
                
            } catch (err) {
                throw new Error(err);
            };
        };

        getBlog();
    }, [blog])

    // checks if blog has been found otherwise show loading message
    if (!blog) {
        return <h1>Loading...</h1>
    };

    return (
        <div className="universalWrapper">
            <div id={styles.blogWrapper}>
                {blog.username}
                {blog.date}
                {blog.title}
                {blog.content}
            </div>
        </div>
    )
};