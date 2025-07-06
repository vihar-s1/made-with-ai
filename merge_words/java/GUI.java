package merge_words.java;

import javax.sound.sampled.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUI extends JFrame {
    private final MergeWords game;
    private boolean isDarkTheme = false;
    private final JLabel scoreLabel, wordLabel;
    private final JPanel gridPanel, buttonPanel, wordListPanel;
    private final JDialog gameOverDialog;
    private Color bgColor, tileColor, tileSelectedColor, tileBorderColor, textColor, buttonColor, buttonHoverColor, rulesBgColor;

    public GUI() {
        game = new MergeWords();
        setTitle("Merge Words");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(350, 650);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));
        updateTheme();

        // Rules
        JPanel rulesPanel = new JPanel();
        rulesPanel.setBackground(rulesBgColor);
        rulesPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        rulesPanel.setLayout(new BoxLayout(rulesPanel, BoxLayout.Y_AXIS));
        String[] rules = {
            "Merge Words Rules:", "1. Click tiles to form a word", "2. Submit or Enter to check",
            "3. Score = word length", "4. Shuffle, backspace, or reset"
        };
        for (String rule : rules) {
            JLabel label = new JLabel(rule);
            label.setForeground(textColor);
            rulesPanel.add(label);
        }
        add(rulesPanel, BorderLayout.NORTH);

        // Top Buttons
        JPanel topPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        topPanel.setBackground(bgColor);
        JButton resetButton = createButton("Reset", _ -> { playSound(600); game.initializeGame(); updateUI(); });
        JButton themeButton = createButton("Theme", _ -> { playSound(350); isDarkTheme = !isDarkTheme; updateTheme(); updateUI(); });
        topPanel.add(resetButton);
        topPanel.add(themeButton);
        add(topPanel, BorderLayout.NORTH);
        rulesPanel.setBorder(BorderFactory.createEmptyBorder(0, 10, 10, 10));

        // Center Panel
        JPanel centerPanel = new JPanel();
        centerPanel.setBackground(bgColor);
        centerPanel.setLayout(new BoxLayout(centerPanel, BoxLayout.Y_AXIS));

        scoreLabel = new JLabel("Score: 0");
        scoreLabel.setForeground(textColor);
        scoreLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        centerPanel.add(scoreLabel);

        wordLabel = new JLabel("Word: ");
        wordLabel.setForeground(textColor);
        wordLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        centerPanel.add(wordLabel);

        gridPanel = new JPanel(new GridLayout(3, 3, 0, 0));
        gridPanel.setBackground(bgColor);
        gridPanel.setMaximumSize(new Dimension(240, 300));
        centerPanel.add(gridPanel);

        buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        buttonPanel.setBackground(bgColor);
        buttonPanel.add(createButton("Submit", _ -> { playSound(500); String msg = game.submitWord(); if (!msg.startsWith("Valid")) JOptionPane.showMessageDialog(this, msg); updateUI(); }));
        buttonPanel.add(createButton("Shuffle", _ -> { playSound(400); game.shuffleTiles(); updateUI(); }));
        buttonPanel.add(createButton("Backspace", _ -> { playSound(300); game.backspace(); updateUI(); }));
        centerPanel.add(buttonPanel);

        add(centerPanel, BorderLayout.CENTER);

        // Word List
        wordListPanel = new JPanel();
        wordListPanel.setBackground(rulesBgColor);
        wordListPanel.setLayout(new BoxLayout(wordListPanel, BoxLayout.Y_AXIS));
        wordListPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        updateWordList();
        add(wordListPanel, BorderLayout.SOUTH);

        // Keyboard Support
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    if (game.isGameOver()) {
                        playSound(600);
                        gameOverDialog.dispose();
                        game.initializeGame();
                        updateUI();
                    } else {
                        playSound(500);
                        String msg = game.submitWord();
                        if (!msg.startsWith("Valid")) JOptionPane.showMessageDialog(GUI.this, msg);
                        updateUI();
                    }
                } else if (e.getKeyCode() == KeyEvent.VK_BACK_SPACE) {
                    playSound(300);
                    game.backspace();
                    updateUI();
                }
            }
        });
        setFocusable(true);

        // Game Over Dialog
        gameOverDialog = new JDialog(this, "Game Over", true);
        gameOverDialog.setSize(200, 150);
        gameOverDialog.setLocationRelativeTo(this);
        gameOverDialog.setLayout(new BorderLayout());
        JLabel gameOverLabel = new JLabel("", SwingConstants.CENTER);
        gameOverLabel.setForeground(textColor);
        gameOverDialog.add(gameOverLabel, BorderLayout.CENTER);
        JButton playAgainButton = createButton("Play Again", _ -> { playSound(600); gameOverDialog.dispose(); game.initializeGame(); updateUI(); });
        gameOverDialog.add(playAgainButton, BorderLayout.SOUTH);

        updateUI();
    }

    private JButton createButton(String text, ActionListener action) {
        JButton button = new JButton(text);
        button.setBackground(buttonColor);
        button.setForeground(textColor);
        button.setFocusPainted(false);
        button.setBorder(BorderFactory.createLineBorder(textColor, 1));
        button.addActionListener(action);
        button.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                button.setBackground(buttonHoverColor);
            }
            @Override
            public void mouseExited(MouseEvent e) {
                button.setBackground(buttonColor);
            }
        });
        return button;
    }

    private void updateTheme() {
        if (isDarkTheme) {
            bgColor = new Color(26, 32, 44);
            tileColor = new Color(45, 55, 72);
            tileSelectedColor = new Color(56, 161, 105);
            tileBorderColor = new Color(74, 85, 104);
            textColor = new Color(226, 232, 240);
            buttonColor = new Color(52, 211, 153);
            buttonHoverColor = new Color(44, 181, 130);
            rulesBgColor = new Color(45, 55, 72);
        } else {
            bgColor = new Color(237, 242, 247);
            tileColor = new Color(255, 255, 255);
            tileSelectedColor = new Color(104, 211, 145);
            tileBorderColor = new Color(160, 174, 192);
            textColor = new Color(45, 55, 72);
            buttonColor = new Color(34, 197, 94);
            buttonHoverColor = new Color(22, 163, 74);
            rulesBgColor = new Color(226, 232, 240);
        }
    }

    private void updateUI() {
        scoreLabel.setText("Score: " + game.getScore());
        scoreLabel.setForeground(textColor);
        wordLabel.setText("Word: " + game.getCurrentWord());
        wordLabel.setForeground(textColor);
        gridPanel.removeAll();
        for (int i = 0; i < 9; i++) {
            JPanel tile = new JPanel();
            tile.setBackground(game.getSelectedTiles().contains(i) ? tileSelectedColor : tileColor);
            tile.setBorder(BorderFactory.createLineBorder(tileBorderColor, 2));
            tile.setPreferredSize(new Dimension(80, 100));
            JLabel label = new JLabel(String.join("", game.getTiles().get(i)), SwingConstants.CENTER);
            label.setForeground(textColor);
            tile.add(label);
            int index = i;
            tile.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    if (!game.isGameOver()) {
                        game.selectTile(index);
                        updateUI();
                    }
                }
            });
            gridPanel.add(tile);
        }
        updateWordList();
        if (game.isGameOver()) {
            gameOverDialog.getContentPane().setBackground(rulesBgColor);
            ((JLabel)gameOverDialog.getContentPane().getComponent(0)).setText("<html><center>Game Over!<br>Score: " + game.getScore() + "</center></html>");
            gameOverDialog.getContentPane().getComponent(0).setForeground(textColor);
            gameOverDialog.setVisible(true);
        }
        getContentPane().setBackground(bgColor);
        gridPanel.setBackground(bgColor);
        buttonPanel.setBackground(bgColor);
        revalidate();
        repaint();
    }

    private void updateWordList() {
        wordListPanel.removeAll();
        JLabel title = new JLabel("Found Words:");
        title.setForeground(textColor);
        wordListPanel.add(title);
        for (String word : game.getFoundWords()) {
            JLabel label = new JLabel(word);
            label.setForeground(textColor);
            wordListPanel.add(label);
        }
        wordListPanel.revalidate();
        wordListPanel.repaint();
    }

    private void playSound(int frequency) {
        try {
            AudioFormat format = new AudioFormat(44100, 16, 1, true, false);
            SourceDataLine line = AudioSystem.getSourceDataLine(format);
            line.open(format);
            line.start();
            byte[] buffer = new byte[4410]; // 0.1 seconds
            for (int i = 0; i < buffer.length; i += 2) {
                double angle = i / 44100.0 * frequency * 2.0 * Math.PI;
                short sample = (short)(Math.sin(angle) * 32767 * 0.5);
                buffer[i] = (byte)(sample & 0xFF);
                buffer[i + 1] = (byte)((sample >> 8) & 0xFF);
            }
            line.write(buffer, 0, buffer.length);
            line.drain();
            line.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new GUI().setVisible(true));
    }
}