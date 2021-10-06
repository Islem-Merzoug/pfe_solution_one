import React from 'react'
import './Header.css'

const Header = () => {
    return (
        <div className="main">
            <div id="wrapperHeader">
                <div id="header">
                    <img src="/images/—Pngtree—robot artificial intelligence robot blue_926814.jpg" alt="logo" />
                </div> 
            </div>

            <div className="centered">
                <div className="divone" >
                    <div>
                        IMED Bejaia MODEL GALLERY
                    </div>
                    <div>
                        Discover open source deep learning code and pretrained models.
                    </div>
                </div>

                <div className="divtwo" >
                    <div>
                        Pre- trained AI Models
                    </div>
                    <div>
                        to get you started 
                    </div>
                </div>

                <div className="divthree" >
                    <div>
                        Explore the IMED club pre-build,
                    </div>
                    <div>
                        ready-to-use AI models to suit your specific use cases
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Header
