import { useEffect, useState } from "react";

import styles from "./HomePage.module.css";

import renderBlogs from "../RenderBlogs/RenderBlogs";

export default function HomePage() {

    // state variables
    const [blogsRendered, setBlogsRendered] = useState(null); // use to store the blogs after theyve been rendered

    const api = import.meta.env.VITE_API; // get api url from .env

    // useEffect used on mount to fetch the blogs to display
    useEffect(() => {
        async function fetchBlogs() {
            // try to fetch blogs for page
            try {
                const response = await fetch(`${api}/get-home-blogs`, {
                    method: "GET",
                });
        
                // check and read response
                const data = await response.json();

                // parse through renderBlogs function to display them properly, then update state with these newly fetched blogs
                const renderedBlogs = renderBlogs(data.blogs)
                setBlogsRendered(renderedBlogs);
        
            } catch (err) {
                throw new Error(err);
            };
        };
        fetchBlogs();

    }, [])

    // checks if the blogs have been fetched otherwise just shows a "loading" message
    if (!blogsRendered) {
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