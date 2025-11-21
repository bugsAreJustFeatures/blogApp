import styles from "./RenderBlogs.module.css"

export default function renderBlogs(blogs) {
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