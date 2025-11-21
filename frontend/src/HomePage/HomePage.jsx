import { useEffect, useState } from "react";

import styles from "./HomePage.module.css";

import renderBlogs from "../RenderBlogs/RenderBlogs";

export default function HomePage() {

    // state variables
    const [blogs, setBlogs] = useState(null); // used to store the blogs after fetching
    const [blogsRendered, setBlogsRendered] = useState(null); // use to store the blogs after theyve been rendered

    const api = import.meta.env.VITE_API;

    useEffect(() => {
        async function fetchBlogs() {
            // try to fetch blogs for page
            try {
                const response = await fetch(`${api}/get-home-blogs`, {
                    method: "GET",
                });
        
                // check and read response
                console.log(response);
                const data = await response.json();
                console.log(data);

                // update state with these newly fetched blogs
                setBlogs(data.blogs);
                console.log(data.blogs);
                const renderedBlogs = renderBlogs(data.blogs)
                setBlogsRendered(renderedBlogs);
        
            } catch (err) {
                throw new Error(err);
            };
        };
        fetchBlogs();

    }, [])

    

    // checks if the blogs have been fetched otherwise just shows a "loading" message
    if (!blogs || !blogsRendered) {
        return <h1>Loading...</h1>
    };



    return (
        <div className="universalWrapper">
            <div id={styles.homeBlogsWrapper}>

                {blogsRendered}
            </div>
        </div>
    )
};