import React from 'react'

const Vid = ({index,vid}) => {
    return (
        
        <div className = "video" key = {index}>
            <h3>{vid.title}</h3>
            <a href ={`https://www.youtube.com/watch?v=${vid.id}`}>https://www.youtube.com/watch?v={vid.id}</a>
        </div>
        
    )
}

export default Vid
