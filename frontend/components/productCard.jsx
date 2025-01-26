import { Card } from 'antd';

function productCard() {
    return(
        <div>
            <Card
            title="Default size card"
            extra={<a href="#">More</a>}
            style={{
                width: 300,
                }}
                >
            <p>Card content</p>
            <p>Card content</p>
            <p>Card content</p>
            </Card>
        </div>
    )
};

export default productCard;