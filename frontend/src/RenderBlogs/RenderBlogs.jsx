import { Link } from "react-router-dom";
import styles from "./RenderBlogs.module.css"

export default function renderBlogs(blogs) {
    const blogsArr = []; // create an array that will hold all the blogs
    const blogsWrapper = []; // this will act as a wrapper for the blogs
    for (let i = 0; i < blogs.length; i++) { // loop through the blogs and get each of their parts
        let blogId = blogs[i][0]; // get the blog id
        let title = blogs[i][1];// get the blog title
        let summary = blogs[i][2]; // get the blog summary
        let createdOn = blogs[i][3];// get the username of the user who created the blog
        let username = blogs[i][4]; // get the creation time and date
        // push the div as one so that each blog will have its own div
        blogsArr.push(
            <div key={blogId} className={styles.individualBlogWrapper}>
                <Link to={`/blogs/${blogId}`} >

                    <div id={styles.titleWrapper}>
                        <h1>Title: {title}</h1>
                    </div>

                    <div id={styles.summaryWrapper}>
                        <h2>Summary: {summary}</h2>
                    </div>

                    <div id={styles.usernameWrapper}>
                        <h3>Author: {username}</h3>
                    </div>

                    <div id={styles.createdOnWrapper}>
                        <h4>Created On: {createdOn}</h4>
                    </div>



                </Link>
                
            </div>
        )
    };

    blogsWrapper.push(
        <div id={styles.blogsWrapper}>
            {blogsArr}
        </div>
    );
    // return the newly made divs
    return blogsWrapper;
};