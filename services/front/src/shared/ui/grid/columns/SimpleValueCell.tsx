type Props = {
  value: any
  className?: string
}

const SimpleValueCell = ({ value, className } : Props) => (<div className={className}>{value}</div>)

export { SimpleValueCell }
