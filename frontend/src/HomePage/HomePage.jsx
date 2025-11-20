import { useEffect, useState } from "react";

import styles from "./HomePage.module.css";

export default function HomePage() {

    // state variables
    const [blogs, setBlogs] = useState(null); // used to store the blogs after fetching

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
                console.log(data.blogs)
        
            } catch (err) {
                throw new Error(err);
            };
        };
        fetchBlogs();

    }, [])

    // checks if the blogs have been fetched otherwise just shows a "loading" message
    if (!blogs) {
        return <h1>Loading...</h1>
    };

    function renderBlogs() {
        const blogsArr = []; // create an array that will hold all the blogs
        for (let i = 0; i < blogs.length; i++) { // loop through the blogs and get each of their parts

            let blogId = blogs[i][0]; // get the blog id
            let title = blogs[i][1];// get the blog title
            let summary = blogs[i][2]; // get the blog content
            let username = blogs[i][3];// get the username of the user who created the blog
            let createdOn = blogs[i][4]; // get the creation time and date

            // push the div as one so that each blog will have its own div
            blogsArr.push(
            <div key={blogId} className={styles.blogContainer}>
                <p>{blogId}</p>
                <p>{title}</p>
                <p>{summary}</p>
                <p>{username}</p>
                <p>{createdOn}</p>
            </div>)
        }

        // return the newly made divs
        return blogsArr;
    };

    return (
        <div className="universalWrapper">
            <div id={styles.homeBlogsWrapper}>

                {renderBlogs()}
            </div>
        </div>
    )
};