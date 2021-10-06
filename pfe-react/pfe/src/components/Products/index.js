import React, {useRef} from 'react'
import Card from '../Card/index';
import { models } from '../../services/models'; 

// import './ProductsElements'

const Products = (props) => {
    const myRef = useRef(null)

    const scrollToRef = (ref) => window.scrollTo(0, ref.current.offsetTop)   

    const executeScroll = () => scrollToRef(myRef)

  return (
    <div>

        <div className="row">
            {
              models.filter(model => model.id !== parseInt(props.currentProductId) )
                    .map((model, i) =>
                    <div className="column" key={i}>
                        <Card
                            id= { model.id }
                            name= { model.name }
                            image= { model.image }
                            description= { model.description }
                            detailLink= { model.detailLink }
                            inputImageExempleLink= { model.inputImageExempleLink }
                            outputImageExempleLink= { model.outputImageExempleLink }
                            fileExtentions= { model.fileExtentions }
                        />
                    </div>
                )
            } 
                {/* <div ref={myRef}>Element to scroll to</div> 
                <button onClick={executeScroll}> Click to scroll </button>  */}
        </div>





            
        </div>
    )
}

export default Products
