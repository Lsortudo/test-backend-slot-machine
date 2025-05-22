import { motion } from 'framer-motion';

interface SlotSymbolProps {
  symbol: string;
  isSpinning: boolean;
}

export const SlotSymbol = ({ symbol, isSpinning }: SlotSymbolProps) => {
  const getSymbolEmoji = (symbol: string) => {
    switch (symbol) {
      case 'ONE_BAR':
        return '💎';
      case 'BLANK':
        return '⭐';
      default:
        return '❓';
    }
  };

  return (
    <motion.div
      className="text-5xl"
      animate={{
        y: isSpinning ? [0, -100, 0] : 0,
        opacity: isSpinning ? [1, 0.5, 1] : 1,
      }}
      transition={{
        repeat: isSpinning ? Infinity : 0,
        duration: 0.5
      }}
    >
      {getSymbolEmoji(symbol)}
    </motion.div>
  );
};