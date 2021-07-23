import React from 'react'
import Searchform from './Searchform'


const Header = ({onSearch}) => {

    return (
        
        <header className="header">
            <h1>Check out suggested Videos!</h1>
            <Searchform onSearch={onSearch}/>
        </header>

        
    )
}

export default Header
